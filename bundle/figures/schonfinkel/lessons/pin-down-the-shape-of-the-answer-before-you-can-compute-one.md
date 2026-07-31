---
type: lesson
title: "Pin down the shape of the answer before you can compute one"
figure: schonfinkel
works: [entscheidungsproblem-der-mathematischen-logik]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# Pin down the shape of the answer before you can compute one

Before any procedure appears, the authors settle what an answer is permitted to look like, and they do it with two arguments that cost almost nothing. First, if two domains can be put in one-to-one correspondence, then every interpretation over one transfers to an interpretation over the other with the same truth values, so nothing about a domain except how many things are in it can influence the verdict. Any condition on the domain is therefore a condition on a number. Second, if a formula is satisfiable over some domain it stays satisfiable over any larger one — the argument maps the extra elements onto a chosen existing element and rebuilds the interpretations to agree — and dually, validity carries downward to smaller domains. So the numerical condition is monotone, which means it can only ever read "at least this many" for satisfiability and "at most this many" for validity.

Two cheap structural facts have now eliminated every other conceivable form of answer. Not "which particular domains" but "how many things"; not an arbitrary set of sizes but a threshold. The remaining work has a target with a known shape, and the eventual results slot into it: the finite bound found later is exactly a threshold, and the closing observation that some formulas hold on every finite domain but fail on an infinite one is exactly the case where the threshold does not exist. Even the failure mode was pre-described by the framing.

This ordering is the opposite of the reflex to start computing. Establishing the invariances of a problem — what transformations of the input leave the answer alone — and the monotonicity — which direction of change can only help or only hurt — takes a fraction of the effort of solving it and constrains the solution space enormously. Anything invariant under a symmetry can only depend on the quotient by that symmetry, which usually turns a rich structure into a scalar. Anything monotone in a parameter has a threshold as its answer, so the search for the answer becomes a search for one number. Both facts also give you free tests: a candidate answer that is not invariant under the symmetry, or not monotone, is wrong before you check anything else.

The engineering version turns up wherever tuning happens. If throughput is monotone in a pool size up to saturation, the answer is a threshold and bisection finds it, so you do not sweep. If a scheduler's behavior is invariant under renaming of workers, then per-worker identity cannot appear in the answer and a policy that mentions it is suspect. If a cache's correctness is invariant under reordering of independent writes, the ordering constraints you thought you needed are not real constraints. Working out these properties first is not preliminary throat-clearing; it is the step that tells you which of the answers you might otherwise chase are impossible.

**Source:** [Zum Entscheidungsproblem der mathematischen Logik](../works/entscheidungsproblem-der-mathematischen-logik.md) — section 1, the argument that equinumerous domains behave identically so only a cardinality condition is possible, together with the theorem that satisfiability passes to larger domains and validity to smaller ones, forcing every condition into a minimum or maximum count.
