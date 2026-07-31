---
type: lesson
title: "Repeating a test buys confidence only if you have proved the failures are independent"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [verifiability]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Repeating a test buys confidence only if you have proved the failures are independent

**Lesson:** A test with one-sided error is a genuinely useful thing: failure is conclusive, success is suggestive. The natural next move is to run it repeatedly and treat accumulating successes as accumulating confidence. That move is valid or worthless depending on a property most people never check, and the difference between the two cases is instructive precisely because the tests look identical from outside.

For one such primality test, repetition does not work, and the reason is not that the probabilities are unfavourable — it is that a rare class of composite numbers passes *for every possible choice of witness*. For those inputs the trials are not independent samples at all; they are the same trial performed repeatedly, and a thousand successes carry exactly the information of one. Confidence appears to grow while nothing is being learned, which is worse than a test known to be weak.

The repair is not a better test but a *proof about* the test. Variants exist for which one can show that, unless the number is prime, the condition fails for at least half of the possible witnesses. That theorem is what makes each trial an independent sample and therefore what makes repetition multiply confidence — halving the error each time, so that arbitrary certainty is purchasable with a linear number of trials. Note where the work sits: not in the algorithm, which is barely different, but in the guarantee attached to it.

The general discipline: whenever you plan to buy confidence through repetition — retries, resampling, multiple reviewers, redundant checks — ask what rules out the case where every repetition fails the same way. Without an argument for independence you have bought nothing, and you have bought it while feeling increasingly sure. The cases where this bites hardest are the ones where the correlated failure is a property of the *input* rather than of the test, because then it is invisible in every trial you run and shows up only on the inputs you never sampled.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) — chapter 1 section 1.2.6's treatment of the Fermat test and probabilistic methods: failing the test proves compositeness while passing does not prove primality; Carmichael numbers are composites for which the congruence holds for all values less than n, so no amount of retrying detects them; and the contrast with variants such as Miller-Rabin, for which one can prove the condition fails for at least half the candidate witnesses unless n is prime, so that repeated trials make the probability of error as small as desired.
