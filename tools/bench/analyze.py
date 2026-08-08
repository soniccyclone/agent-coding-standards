#!/usr/bin/env python3
"""Score benchmark arms on how much of each round's code survived later rounds.

The claim under test is whether a design absorbs new requirements or fights
them. That is measurable: of the lines a round wrote, how many are still
standing at the end? Low survival for round 1 means the initial representation
was wrong for requirements that had not arrived yet, and rounds 2-4 paid for it.

Usage: analyze.py <BENCH_ROOT> [arm ...]
"""
import json
import os
import subprocess
import sys
from collections import defaultdict

ROUNDS = [1, 2, 3, 4]
# The treatment itself and generated noise are not part of the work product.
SKIP_SUFFIX = (".md",)
SKIP_NAMES = {"CLAUDE.md", "RTK.md", "tropes.md"}


def git(work, *args):
    return subprocess.run(["git", "-C", work, *args],
                          capture_output=True, text=True).stdout


def tracked_sources(work, ref):
    out = git(work, "ls-tree", "-r", "--name-only", ref).splitlines()
    return [f for f in out
            if os.path.basename(f) not in SKIP_NAMES
            and not f.endswith(SKIP_SUFFIX)
            and not f.startswith(".git")]


def introduced(work, r):
    """Lines added in round r, excluding docs and the treatment file."""
    n = 0
    for line in git(work, "diff", "--numstat", f"round{r-1}", f"round{r}").splitlines():
        parts = line.split("\t")
        if len(parts) != 3 or parts[0] == "-":
            continue
        added, _, path = parts
        if os.path.basename(path) in SKIP_NAMES or path.endswith(SKIP_SUFFIX):
            continue
        n += int(added)
    return n


def surviving(work):
    """Lines in the final tree, bucketed by the round commit that last wrote them."""
    sha = {r: git(work, "rev-parse", f"round{r}").strip() for r in ROUNDS}
    by_sha = {v: k for k, v in sha.items()}
    counts = defaultdict(int)
    for path in tracked_sources(work, "round4"):
        blame = git(work, "blame", "--line-porcelain", "round4", "--", path)
        for line in blame.splitlines():
            if line and line[0].isalnum() and len(line.split()[0]) == 40:
                counts[by_sha.get(line.split()[0])] += 1
    return counts


def cost(root, arm):
    tok = usd = 0.0
    for r in ROUNDS:
        p = os.path.join(root, "logs", arm, f"r{r}.json")
        if not os.path.exists(p):
            continue
        try:
            d = json.load(open(p))
        except (json.JSONDecodeError, ValueError):
            continue
        usd += d.get("total_cost_usd") or 0
        u = d.get("usage") or {}
        tok += sum(v for k, v in u.items()
                   if isinstance(v, (int, float)) and "token" in k)
    return tok, usd


def main():
    root = sys.argv[1]
    arms = sys.argv[2:] or ["control", "incumbent", "general", "flavored"]

    print(f"{'ARM':<11}{'r1 kept':>9}{'r2 kept':>9}{'r3 kept':>9}"
          f"{'final':>8}{'churn':>8}{'$':>8}")
    print("-" * 62)

    for arm in arms:
        work = os.path.join(root, arm)
        if not os.path.isdir(os.path.join(work, ".git")):
            print(f"{arm:<11}  (not run)")
            continue
        intro = {r: introduced(work, r) for r in ROUNDS}
        surv = surviving(work)
        final = sum(surv.values())
        total_written = sum(intro.values())
        churn = 1 - (final / total_written) if total_written else 0

        def pct(r):
            return f"{100*surv.get(r,0)/intro[r]:.0f}%" if intro[r] else "n/a"

        _, usd = cost(root, arm)
        print(f"{arm:<11}{pct(1):>9}{pct(2):>9}{pct(3):>9}"
              f"{final:>8}{100*churn:>7.0f}%{usd:>8.2f}")

    print("\nr1 kept = share of round-1 lines still standing after rounds 2-4.")
    print("Higher means the initial design absorbed the new requirements.")
    print("churn  = share of all lines ever written that are gone by the end.")


if __name__ == "__main__":
    main()
