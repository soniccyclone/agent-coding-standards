---
type: lesson
title: "Compare your algorithm's error rate against the machine's, not against zero"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [verifiability, hardware-affinity]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Compare your algorithm's error rate against the machine's, not against zero

**Lesson:** A probabilistic primality test can be fooled by a rare class of composite numbers, which sounds like a disqualifying flaw for anything that must be correct. The authors answer it with a comparison rather than a reassurance: for large numbers chosen at random, the chance of hitting one of those adversarial values is smaller than the chance that cosmic radiation flips a bit and makes the computer execute a provably correct algorithm incorrectly. They then name what the comparison exposes — treating an algorithm as inadequate for the first reason while accepting the second is the difference between mathematics and engineering.

The transferable idea is that "correct" is not a property an executed program can have absolutely, because the execution rests on hardware with its own failure rate. Once that is admitted, the meaningful question is never whether your method can fail but whether its failure probability is small relative to everything else in the stack it depends on. An algorithm whose error rate sits well below the substrate's contributes nothing measurable to the observed failure rate of the system; demanding zero from it while tolerating the substrate is not rigour, it is inconsistency with a comforting shape.

Applying this requires knowing the substrate's number, which is the part usually skipped. Memory error rates, disk error rates, network corruption that slips past a checksum, and the residual defect density of the correct-by-construction code around your component are all measurable or at least boundable, and any of them may dominate. Where your method's failure probability is orders of magnitude below the largest of those, further reducing it buys nothing observable and any effort spent doing so was misallocated.

The judgement has a boundary worth respecting. This is an argument about *comparable* magnitudes under *random* inputs, and it collapses when an adversary chooses the input — the rare fooling values stop being rare when someone selects them deliberately. So the rule is to compare against the substrate for accidental failure, and never to use that comparison where the input is chosen by someone who benefits from your error.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) — chapter 1 section 1.2.6's discussion of probabilistic methods and its footnote on Carmichael numbers, which reports there are 255 below 100,000,000, observes that when testing large randomly chosen numbers the chance of stumbling on one is less than the chance that cosmic radiation causes the computer to err while carrying out a correct algorithm, and concludes that considering an algorithm inadequate for the first reason but not the second illustrates the difference between mathematics and engineering.
