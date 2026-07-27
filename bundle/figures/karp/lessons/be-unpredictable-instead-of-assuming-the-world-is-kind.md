---
type: lesson
title: "Make your own behavior unpredictable instead of assuming the inputs will be kind"
figure: karp
works: [combinatorics-complexity-and-randomness, an-optimal-algorithm-for-on-line-bipartite-matching]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Make your own behavior unpredictable instead of assuming the inputs will be kind

**Lesson:** If a procedure is fully determined, then its bad case is a fixed target and anyone who can read it can aim at it. The usual responses are to assume nobody will aim, or to patch each bad case as it is discovered. There is a third response that is structurally better than both: move the randomness out of the environment and into the procedure itself. Choose among a large family of equally valid strategies by coin flip at the moment of execution. Now the bad case is not a property of the input alone, because the input no longer determines what you do. An opponent who knows your entire source code, and who picks the input after reading it, still cannot pick one that is likely to hurt you, because the choice that matters has not been made yet.

The classic illustration is comparing a short summary value rather than a long string, where any single fixed summarizing function admits an input that collides everywhere and destroys the whole benefit, so a fallback path is needed and the advantage is lost. Draw the summarizing function at random from a large family per run, and the collision probability becomes small for every input, with no assumption about where inputs come from. That last clause is the whole point and the reason this beats reasoning about input distributions: the guarantee is per-instance and unconditional, purchased with a small, quantified probability of being wrong rather than with an unverifiable claim about the world.

What a programmer does differently is to notice the shape of the problem whenever a fixed choice creates a systematic worst case, and reach for randomization as a first-class fix rather than a curiosity. Hash seeds chosen per process, randomized backoff, random probe order, randomized load assignment, sampled rather than scheduled checks. The reasoning cost is real and worth naming honestly: you trade a deterministic system you can reproduce for a probabilistic one you must reason about in terms of failure odds, and you need the error probability driven low enough that it stops being an engineering concern. Karp is also clear about the limit of the technique. Randomization defeats adversarial inputs; it does not defeat a problem whose difficulty is intrinsic, so both this approach and distributional reasoning kept their separate uses.

**Source:** [Combinatorics, Complexity, and Randomness](../works/combinatorics-complexity-and-randomness.md) — the section on randomized algorithms, its analogy to varying play calls so a defense cannot commit, and the fingerprinting pattern-matcher where drawing the fingerprint function at random restores a guarantee that any single fixed choice loses. [An Optimal Algorithm for On-line Bipartite Matching](../works/an-optimal-algorithm-for-on-line-bipartite-matching.md) supplies the sharpest instance: a proved separation showing every deterministic policy is held to half of what foresight would achieve, while a randomized one provably does better.
