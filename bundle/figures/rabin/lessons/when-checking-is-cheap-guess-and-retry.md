---
type: lesson
title: "When checking is cheap, guess and retry instead of constructing"
figure: rabin
works: [digitalized-signatures-and-public-key-functions-as-intractable-as-factorization]
axes: [primitive-count, cognitive-load, verifiability]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# When checking is cheap, guess and retry instead of constructing

**Lesson:** Several steps in this work face the same situation: a value is wanted, constructing it directly is intricate or unknown, and recognizing a correct one is easy. The response every time is the same and it is not a construction. Draw a candidate at random, do the cheap check, and go again if it fails. What makes this a technique rather than a shrug is the accompanying argument that a random draw succeeds with a fixed probability — often one in two — independent of which instance you are on. A constant success probability with cheap verification means the expected number of attempts is a small constant, and the loop is finished before it has to be clever.

The intellectual move is to stop treating randomness as a source of unpredictability to be eliminated and start treating it as a way to buy an unconditional-looking bound cheaply. The bound is over your own coin flips, not over the input, which is what makes it robust: there is no adversarial instance, because the hard part of the instance has been replaced by a fair sample. Notice this appears at both scales in the same document — inside the root-extraction step, where a random shift splits the roots apart half the time; and at the level of the whole reduction, where a random starting value lands in a useful configuration half the time. One idea, applied at whatever granularity is stuck.

The design consequence is that "can I recognize the answer?" is a more important question than "can I compute the answer?", and it should be asked first. Where verification is cheap and the space of candidates is not absurdly sparse, a five-line loop with a proven per-attempt probability replaces a page of case analysis, and it is the loop that is easier to trust: there are fewer branches to get wrong, and the correctness of what it returns is enforced by the check rather than argued from the construction. The cost of being wrong is a wasted iteration instead of a silent bad answer.

This also flips how you handle a case analysis you cannot complete. When a construction works for most situations and one awkward situation resists, the reflex is to grind out the special case. The alternative on offer here is to randomize until you are out of the awkward situation, provided you can bound how often it comes up and confirm cheaply that you have left it. That trades an unbounded amount of human reasoning for a bounded amount of machine time, which is nearly always the right side of the trade.

**Source:** [Digitalized Signatures and Public-Key Functions as Intractable as Factorization](../works/digitalized-signatures-and-public-key-functions-as-intractable-as-factorization.md) — the root-finding section where a randomly chosen shift separates roots with probability one half, giving a small expected number of attempts, and the factoring reduction where a randomly chosen starting value yields a nontrivial common factor with the same probability per attempt.
