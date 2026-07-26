---
type: figure
title: Jack Edmonds
description: b. 1934, Waterloo/NBS. First to formally articulate polynomial time as the tractability boundary; gave the first polynomial-time matching algorithm.
status: accepted
layer: implementation-mapping
subdomains: [algorithms-and-complexity]
tags: [figure, accepted]
---

# Jack Edmonds

**Dates:** b. 1934. American-born mathematician/computer scientist; University of Waterloo, earlier National Bureau of Standards.

## Why a candidate
First to formally articulate polynomial time as the boundary between tractable and intractable ("Cobham-Edmonds thesis") and gave the first polynomial-time matching algorithm with a rigorous complexity bound — the founding gesture of "efficient algorithm" as a formal category.

## Top 10 most influential works
1. "Paths, Trees, and Flowers" (1965, Canadian J. Math.) — `public` (NIST/math.nist.gov mirror)
2. "Maximum Matching and a Polyhedron with 0,1-Vertices" (1965, J. Res. Nat. Bur. Standards) — `public` (US govt technical report)
3. "Optimum Branchings" (1967, J. Res. Nat. Bur. Standards) — `public` (US govt technical report)
4. "Theoretical Improvements in Algorithmic Efficiency for Network Flow Problems" (1972, with Karp) — `paywalled`
5. "Matroids and the Greedy Algorithm" (1971, Math. Programming) — `paywalled`
6. "Matroid Partition" (1968) — `uncertain`
7. "Submodular Functions, Matroids, and Certain Polyhedra" (1970) — `uncertain`

## Phase 3 access flag
Three of the seven listed works — "Matroids and the Greedy Algorithm" (1971,
Math. Programming), "Matroid Partition" (1968, in *Mathematics of the Decision
Sciences, Part I*, AMS), and "Submodular Functions, Matroids, and Certain
Polyhedra" (1970, in *Combinatorial Structures and their Applications*, Gordon
and Breach) — are genuinely unavailable from any public source checked.
"Matroids and the Greedy Algorithm" is paywalled at Springer with no
self-archived, institutional, or third-party-rehost copy found anywhere
(ResearchGate/Academia.edu block anonymous access; no author or course-mirror
copy surfaced). The other two are out-of-print conference/AMS proceedings
volumes; the only digitized copies found are on the Internet Archive
(`combinatorialstr0000calg` and `mathematicsofdec0000summ`), both flagged
`access-restricted-item: true` — Internet Archive's controlled digital
lending, which requires a borrow/login and does not count as public under
this pass's rules. The Springer reprints of these three in *Jack Edmonds:
Selected Papers* (the "Combinatorial Optimization — Eureka, You Shrink!"
volume) were also checked directly and are paywalled (HTML paywall page
returned instead of PDF).

These three are not central to the "why a candidate" case above (which rests
on the polynomial-time thesis and the matching algorithm, both covered by the
four works that *were* confirmed public), but they represent a real gap in
Edmonds's matroid-theory legacy — the greedy-algorithm characterization paper
in particular is one of his most-cited results. No work file was created for
any of the three; they remain excluded pending a future pass (e.g. a
library-access check, or contacting a rights holder) if that legacy needs
fuller documentation later.

## Lessons

Edmonds's contribution to how programmers think is the insistence that cost is
a mathematical property of a problem, statable as a proposition and provable or
refutable before any code exists — which forces two disciplines his papers then
carry out in detail: choose a cost measure that cannot be gamed and that counts
the input by what it takes to write down, precision included, and never let a
performance claim rest on a step whose resolution the specification left free.
Around that spine sits a repertoire of design moves that all share one shape,
replacing enforcement with structure. Where a recurring configuration defeats a
uniform search, he collapses it into an opaque element and works where it cannot
arise, paying for the move with correspondence theorems rather than with special
cases. Where a discreteness condition must otherwise be policed, he hunts for a
continuous description whose corners are exactly the discrete objects, so the
condition becomes geometry and the existing machinery for continuous
optimization applies. Where a method might merely assert its answer, he arranges
for the stuck state to hand over an independently checkable witness of
optimality, maintained alongside the answer throughout rather than reconstructed
afterwards. His work also models an unusual rigour about what transfers between
similar-looking problems: a shortcut's validity belongs to a structural property,
not to family resemblance, and an invariance that holds for one formulation can
fail for its near neighbour for reasons visible only in the proof. Two further
habits round it out — separating the choices a run makes arbitrarily from the
object the input actually determines, which is where both parallel freedom and a
usable test oracle come from; and reshaping data to keep a component inside its
cheap regime, licensed by working out what the component's answers are invariant
under. Read together, the lessons describe a way of working in which efficiency
is never a matter of making operations faster but of finding the representation
in which the expensive thing has nothing left to do.
