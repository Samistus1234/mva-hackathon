#!/usr/bin/env python3
"""
mechanism-hop drug repurposing for undruggable rare-disease genes.

The problem this solves
-----------------------
Ask a drug-gene interaction database about BUB1B - the gene causing this child's
Mosaic Variegated Aneuploidy - and you get nothing. Zero drugs. That is the normal
result for a rare-disease gene: the causal protein is a structural/regulatory
component nobody has ever built a drug against, so a naive "look up the gene, get a
drug" pipeline terminates immediately.

This tool takes the next step. Instead of stopping at the undruggable gene, it hops
outward through the gene's physical interaction neighbourhood and asks which
*neighbours* are druggable, then scores each candidate by how tightly it is coupled
to the disease gene and how mature its pharmacology is.

    stage 0  direct druggability of the disease gene            (expected: empty)
    stage 1  mechanism neighbourhood from Open Targets/IntAct   (scored interactors)
    stage 2  druggability of every neighbour via DGIdb          (+ approved-drug flag)
    stage 3  rank: interaction confidence x pharmacological maturity

Everything is public data over public APIs; no patient data is read or written.

    python3 repurpose.py --gene BUB1B
    python3 repurpose.py --gene CEP57 --out outputs/cep57.tsv
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.request

OPEN_TARGETS = "https://api.platform.opentargets.org/api/v4/graphql"
DGIDB = "https://dgidb.org/api/graphql"

# Interactors below this IntAct-derived confidence are noise for our purposes.
MIN_INTERACTION_SCORE = 0.40


def graphql(url: str, query: str, retries: int = 3) -> dict:
    """POST a GraphQL query, returning the `data` block. Retries transient failures."""
    payload = json.dumps({"query": query}).encode()
    request = urllib.request.Request(
        url, data=payload, headers={"Content-Type": "application/json"}
    )
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                body = json.loads(response.read())
            if "errors" in body and not body.get("data"):
                raise RuntimeError(body["errors"])
            return body["data"]
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            if attempt == retries - 1:
                raise RuntimeError(f"{url} failed after {retries} attempts: {exc}")
            time.sleep(2 ** attempt)
    raise AssertionError("unreachable")


def resolve_ensembl_id(symbol: str) -> str:
    data = graphql(
        OPEN_TARGETS,
        f'{{ search(queryString: "{symbol}", entityNames: ["target"]) '
        f"{{ hits {{ id name }} }} }}",
    )
    for hit in data["search"]["hits"]:
        if hit["name"].upper() == symbol.upper():
            return hit["id"]
    raise SystemExit(f"No Open Targets target found for {symbol!r}")


def mechanism_neighbourhood(ensembl_id: str, size: int) -> list[dict]:
    """Physical interactors of the disease gene, best-scoring first, deduplicated."""
    data = graphql(
        OPEN_TARGETS,
        f'{{ target(ensemblId: "{ensembl_id}") {{ approvedSymbol '
        f"interactions(sourceDatabase: intact, page: {{index: 0, size: {size}}}) "
        f"{{ count rows {{ score targetB {{ approvedSymbol id }} }} }} }} }}",
    )
    target = data["target"]
    best: dict[str, dict] = {}
    for row in target["interactions"]["rows"]:
        partner = row.get("targetB") or {}
        symbol = partner.get("approvedSymbol")
        score = row.get("score") or 0.0
        if not symbol or score < MIN_INTERACTION_SCORE:
            continue
        if symbol not in best or score > best[symbol]["interaction_score"]:
            best[symbol] = {
                "symbol": symbol,
                "ensembl_id": partner.get("id"),
                "interaction_score": score,
            }
    return sorted(best.values(), key=lambda n: -n["interaction_score"])


def druggability(symbols: list[str]) -> dict[str, dict]:
    """DGIdb drug-gene interactions, batched. Returns per-symbol drug evidence."""
    if not symbols:
        return {}
    names = ", ".join(f'"{s}"' for s in symbols)
    data = graphql(
        DGIDB,
        f"{{ genes(names: [{names}]) {{ nodes {{ name interactions "
        f"{{ interactionScore drug {{ name approved }} }} }} }} }}",
    )
    out: dict[str, dict] = {}
    for node in data["genes"]["nodes"]:
        interactions = node.get("interactions") or []
        approved = [
            i["drug"]["name"] for i in interactions if i["drug"].get("approved")
        ]
        ranked = sorted(
            interactions, key=lambda i: -(i.get("interactionScore") or 0.0)
        )
        out[node["name"]] = {
            "n_drugs": len(interactions),
            "n_approved": len(approved),
            "approved_drugs": approved,
            "top_drugs": [i["drug"]["name"] for i in ranked[:5]],
        }
    return out


def maturity(evidence: dict) -> float:
    """
    Pharmacological maturity, 0-1.

    An approved drug is worth far more to a repurposing effort than a tool compound,
    so approvals dominate; the raw count of known binders contributes a smaller,
    saturating term.
    """
    if not evidence or evidence["n_drugs"] == 0:
        return 0.0
    approved_term = min(evidence["n_approved"], 5) / 5.0
    breadth_term = min(evidence["n_drugs"], 40) / 40.0
    return 0.75 * approved_term + 0.25 * breadth_term


def rank(genes: list[str], size: int) -> tuple[dict, list[dict]]:
    """
    Rank the druggable neighbourhood of one or more seed genes.

    Multiple seeds let one run cover a whole mechanism axis rather than a single
    protein - e.g. the senescence consequence of aneuploidy is seeded by CDKN2A and
    TP53 together. A neighbour reachable from several seeds keeps its best score and
    records every seed that reached it.
    """
    direct = druggability(genes)

    merged: dict[str, dict] = {}
    for gene in genes:
        for neighbour in mechanism_neighbourhood(resolve_ensembl_id(gene), size):
            symbol = neighbour["symbol"]
            if symbol in genes:  # a seed is not its own candidate
                continue
            existing = merged.get(symbol)
            if existing is None:
                neighbour["via"] = [gene]
                merged[symbol] = neighbour
            else:
                existing["via"].append(gene)
                existing["interaction_score"] = max(
                    existing["interaction_score"], neighbour["interaction_score"]
                )

    neighbours = sorted(merged.values(), key=lambda n: -n["interaction_score"])
    evidence = druggability([n["symbol"] for n in neighbours])

    # Stage 3 - couple interaction confidence to pharmacological maturity.
    for neighbour in neighbours:
        found = evidence.get(neighbour["symbol"], {})
        neighbour["n_drugs"] = found.get("n_drugs", 0)
        neighbour["n_approved"] = found.get("n_approved", 0)
        neighbour["approved_drugs"] = found.get("approved_drugs", [])
        neighbour["top_drugs"] = found.get("top_drugs", [])
        neighbour["maturity"] = round(maturity(found), 3)
        neighbour["priority"] = round(
            neighbour["interaction_score"] * neighbour["maturity"], 4
        )

    ranked = sorted(neighbours, key=lambda n: -n["priority"])
    header = {"genes": genes, "direct": direct, "n_neighbours": len(neighbours)}
    return header, ranked


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--gene", required=True, nargs="+",
                        help="one or more seed gene symbols, e.g. BUB1B, or CDKN2A TP53")
    parser.add_argument("--size", type=int, default=100,
                        help="interactors to pull per seed from Open Targets (default 100)")
    parser.add_argument("--top", type=int, default=20, help="rows to print (default 20)")
    parser.add_argument("--out", help="write the full ranking to this TSV path")
    args = parser.parse_args()

    genes = [g.upper() for g in args.gene]
    header, ranked = rank(genes, args.size)

    print(f"\n=== stage 0: are the seed genes themselves druggable? ===")
    for gene in genes:
        found = header["direct"].get(gene, {"n_drugs": 0, "n_approved": 0, "top_drugs": []})
        if found["n_drugs"] == 0:
            print(f"  {gene}: DGIdb knows 0 drugs. A direct-lookup pipeline stops here "
                  f"— this is why we hop.")
        else:
            print(f"  {gene}: {found['n_drugs']} drugs ({found['n_approved']} approved) "
                  f"— {', '.join(found['top_drugs'][:4])}")

    print(f"\n=== stage 1-3: druggable mechanism neighbourhood of {', '.join(genes)} ===")
    print(f"  {header['n_neighbours']} interactors scoring >= {MIN_INTERACTION_SCORE}\n")
    print(f"{'gene':10} {'intact':>7} {'drugs':>6} {'appr':>5} {'prio':>7}  approved / top compounds")
    print("-" * 100)
    for row in ranked[: args.top]:
        drugs = row["approved_drugs"] or row["top_drugs"]
        print(f"{row['symbol']:10} {row['interaction_score']:>7.2f} {row['n_drugs']:>6} "
              f"{row['n_approved']:>5} {row['priority']:>7.3f}  "
              f"{', '.join(drugs[:4]) if drugs else '-'}")

    if args.out:
        with open(args.out, "w") as handle:
            handle.write("gene\tvia_seed\tinteraction_score\tn_drugs\tn_approved\tmaturity"
                         "\tpriority\tapproved_drugs\ttop_drugs\n")
            for row in ranked:
                handle.write(
                    f"{row['symbol']}\t{'|'.join(row['via'])}\t{row['interaction_score']}\t"
                    f"{row['n_drugs']}\t{row['n_approved']}\t{row['maturity']}\t"
                    f"{row['priority']}\t{'|'.join(row['approved_drugs'])}\t"
                    f"{'|'.join(row['top_drugs'])}\n"
                )
        print(f"\nwrote {len(ranked)} rows to {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
