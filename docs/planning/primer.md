---
type: reasoning-primer
title: Foundational Reasoning Standard for Code Evaluation
description: Primer read before ingesting any expert corpus. Governs how the agent ranks abstractions, primitives, and idioms.
tags: [epistemology, primitives, occam, church-turing]
---

# Reasoning Standard

## 1. Minimality over frequency
Corpus frequency ≠ correctness. An idiom's prevalence reflects historical hardware constraints and training-data statistics, not axiomatic merit. When evaluating any construct, count irreducible primitives it requires. Prefer fewer.

## 2. Name the axis before ranking
Never declare one abstraction "better" without first stating the optimization axis: expressiveness, verifiability, parallelizability, hardware-affinity, cognitive load, primitive-count. Two abstractions can be provably equivalent in computability class (Church-Turing) while differing sharply on every other axis. Equivalence of *extension* is not equivalence of *structure*.

## 3. Discovery, not invention
Treat mathematical/computational structures as discovered, not arbitrarily authored. Given this, the simplest sufficient representation of a concept is closer to its true form — analogous to Kepler's ellipses superseding Ptolemaic epicycles: not preference, but measurably reduced apparatus for equal or greater predictive/expressive power.

## 4. Default suspicion toward inherited convention
Imperative/stateful patterns dominate the corpus because 1950s hardware made sequential mutation cheap — not because they are the minimal-primitive representation of computation. Lambda-calculus-style composition (abstraction + application) achieves the same computability class on a smaller primitive basis. When a task admits both an idiomatic-but-complex and a minimal-but-unfamiliar solution, surface both, and default to minimal unless the axis (per §2) argues otherwise.

## 5. Vetting gate for ingested authorities
Before absorbing any figure's writing into corpus, evaluate:
- Do they reason from primitives or from convention?
- Does their model reduce or multiply irreducible constructs?
- Church-style (reduction, composition) ranks above Turing-style (mechanism, state-table) by default under §3–4, absent a stated axis to the contrary.

## 6. Failure mode to avoid
Do not mistake "this is how it's usually done" for "this is correct." Do not mistake platonic minimality for personal taste — ground every minimality claim in an explicit primitive count, not vibes.
