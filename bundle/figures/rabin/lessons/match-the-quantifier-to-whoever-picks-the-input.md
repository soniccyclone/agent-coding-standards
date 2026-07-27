---
type: lesson
title: "Match the quantifier in your guarantee to whoever gets to pick the input"
figure: rabin
works: [digitalized-signatures-and-public-key-functions-as-intractable-as-factorization]
axes: [verifiability]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Match the quantifier in your guarantee to whoever gets to pick the input

**Lesson:** A cost claim is meaningless until you say who chooses the input it is measured over. This work makes the point sharply: a construct can be expensive to break in the worst case, expensive to break on average, and still be worthless, because a small minority of easy cases is enough. An opponent is not obliged to accept the inputs you hand him. He can search for the ones that suit him, and if one input in a thousand yields, he simply keeps searching until he lands on it and then uses that one for something that matters. Averaging over inputs assumes a sampler with no stake in the outcome. The moment something with a stake picks, the average describes a situation nobody is in.

So the guarantee is restated in the only form that survives adversarial selection: succeeding on even a tiny fraction of cases must be enough to break the underlying hard problem. The proof structure that gets there is instructive on its own — an attacker who works only on a thousandth of inputs is simply invoked repeatedly with fresh random inputs, aborting each attempt that runs long, and the expected number of attempts before landing in his good fraction is a constant multiplier on the cost. Any island of easiness becomes reachable by retrying, which is exactly why an island of easiness cannot be tolerated.

The generalization outside cryptography is direct and mostly ignored. Average latency is the wrong statistic whenever the request mix is chosen by users, competitors, or an unlucky correlation, because the case you would have called rare is the case that gets requested repeatedly once something upstream starts retrying. A cache hit rate measured on yesterday's traffic says nothing about traffic shaped by someone probing for misses. A validation routine that rejects almost all bad inputs is not a validation routine. Wherever a bound is quoted, name the population it is over, and ask whether anyone can steer inputs out of that population.

Concretely this changes what you measure and what you promise. Prefer bounds that hold for all inputs, or for all but a provably negligible set, over bounds on the mean; when only a mean is available, treat it as a capacity-planning number and never as a safety property. And when a design has a small pocket of cheap-for-the-attacker or expensive-for-us behavior, do not discount it by its frequency in normal traffic, because the frequency in normal traffic is not the frequency you will face.

**Source:** [Digitalized Signatures and Public-Key Functions as Intractable as Factorization](../works/digitalized-signatures-and-public-key-functions-as-intractable-as-factorization.md) — the introduction's argument that high worst-case or average cost is commercially useless if a small percentage of cases is easy, and the strengthened theorem showing that success on a small fraction still yields a factoring procedure with only a constant-factor penalty.
