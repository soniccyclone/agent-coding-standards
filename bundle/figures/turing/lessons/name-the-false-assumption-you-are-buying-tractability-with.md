---
type: lesson
title: "Name the false assumption you are buying tractability with, and say where it fails"
figure: turing
works: [paper-on-the-statistics-of-repetitions]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Name the false assumption you are buying tractability with, and say where it fails

**Lesson:** Every tractable model of a messy system rests on assumptions that are not true. The difference between a usable model and a dishonest one is not whether such assumptions are present but whether they are written down as separate, inspectable claims with their known failure points attached. In this paper the whole derivation depends on treating repetitions at different positions as independent events, and Turing does not smuggle that in as a modelling convenience. He states it as its own proposition, immediately concedes it is false for adjacent letters, argues that the failure is local and does not propagate across the span he cares about, and only then builds on it. The assumption becomes a labelled joint in the argument rather than an invisible weld.

This matters because the failure mode of an approximate model is never "slightly wrong everywhere." It is "badly wrong in exactly the region where the assumption breaks." If the assumption is explicit and its breaking region is named, a later reader can check whether their case falls inside that region, and a later maintainer can replace that one joint without re-deriving everything downstream. If it is implicit, the model appears to be a theorem, and the eventual wrong answer arrives with no diagnostic trail. The cost of being explicit is a few sentences; the cost of being implicit is that nobody can tell a modelling limitation from a bug.

For a programmer this is the discipline of separating "this is exact" from "this is close enough, here, for this reason." It means the smoothing constant, the assumed-uncorrelated failure domains, the assumed-uniform hash, the assumed-monotonic clock each get stated as their own named premise near the code that depends on them, with the case that violates them written down alongside. It also changes how you argue for a simplification: not "it works in practice," but "here is precisely where it stops being true, and here is why the region I operate in stays clear of that."

**Source:** [Paper on Statistics of Repetitions](../works/paper-on-the-statistics-of-repetitions.md) — the early section where the independence of repetitions at separated positions is set out as an explicit assumption, with the adjacent-letter counterexample acknowledged rather than hidden, before any of the distribution work rests on it.
