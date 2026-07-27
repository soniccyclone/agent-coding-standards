---
type: figure
title: Richard M. Karp
description: b. 1935, Berkeley. Extended Cook's NP-completeness result to 21 concrete combinatorial problems.
status: accepted
layer: implementation-mapping
subdomains: [algorithms-and-complexity]
tags: [figure, accepted]
---

# Richard M. Karp

**Dates:** b. 1935. American computer scientist, UC Berkeley; founding director of the Simons Institute for the Theory of Computing.

## Why a candidate
Extended Cook's NP-completeness result to 21 concrete combinatorial/graph problems, demonstrating intractability as a formal, provable property across a huge swath of practical computing problems.

## Top 10 most influential works
1. "Reducibility Among Combinatorial Problems" (1972) — `uncertain` (original is paywalled Springer chapter, PDF copies self-archived on multiple university course pages)
2. "A n^5/2 Algorithm for Maximum Matchings in Bipartite Graphs" (1973, with Hopcroft) — `paywalled`
3. "Theoretical Improvements in Algorithmic Efficiency for Network Flow Problems" (1972, with Edmonds, Edmonds-Karp algorithm) — `paywalled`
4. "An Optimal Algorithm for On-line Bipartite Matching" (1990, with U./V. Vazirani) — `uncertain`
5. "Combinatorics, Complexity, and Randomness" (1985 Turing lecture) — `uncertain`

## Lessons
Karp teaches a single discipline applied over and over: before you try to make
something faster, establish what kind of thing its cost is, and make every
claim about it name the conditions under which it holds. That starts with
knowing when effort is futile — translate an unfamiliar problem into one whose
difficulty is already settled, ask how hard an answer is to *check* before
asking how hard it is to *find*, route everything through one universal target
rather than building translators pairwise, and trust only the distinctions that
survive a change of machine or representation. When a problem does turn out to
be hard, the response is never to refine harder, because refinement cannot
repair a growth rate; it is to change the specification deliberately — drop
exactness, drop generality, drop the assumption that inputs are adversarial —
and then prove something exact about whatever remains. Where his own algorithms
are concerned the recurring moves are structural rather than clever: an
unspecified "choose any" is the seam where pathology enters, so pin the choice
down; cost that tracks the magnitude of numbers rather than the size of data is
exponential wearing a disguise; solve a coarse version and pay for a bounded
repair; reshape the data to fit a cheap tool instead of reaching for a general
one; stop optimizing the single step and find the batch of steps that do not
interfere, then bound how many batches there can be; and make every step retire
part of the input permanently so the cost bound becomes a census rather than a
trace of the control flow. Running underneath all of it is a preoccupation with
what a guarantee is actually a guarantee against. Every performance claim
assumes an adversary, and knowing which one you assumed decides whether a local
stopping condition certifies global optimality or merely means you ran out of
moves you allowed yourself. That preoccupation is what makes randomness a tool
rather than a hedge — become unpredictable yourself instead of hoping inputs
are kind, but recognize that *where* the randomness sits governs its value, one
hidden commitment held consistently being worth far more than a fresh coin flip
per decision. And when the future is genuinely unavailable, define quality as a
ratio against an oracle you can never build, prove the ceiling so you know when
to stop trying, analyze a crippled variant you have proved you dominate rather
than a simplification of unknown bias, and hunt for the symmetry that relocates
the uncertainty to wherever you can reason about it.
