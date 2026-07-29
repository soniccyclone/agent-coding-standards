---
type: lesson
title: "Isolate the part of a problem that is irreducibly a guess, then keep the rest strictly mechanical"
figure: turing
works: [the-applications-of-probability-to-cryptography]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Isolate the part of a problem that is irreducibly a guess, then keep the rest strictly mechanical

**Lesson:** Most real problems contain a component nobody can derive: a prior belief, a tuning constant, an estimate of how often the world behaves a certain way. The instinct is either to pretend it is derivable and bury it inside the machinery, or to declare the whole problem unrigorous because one input is soft. Both are wrong. The correct move is to cut the problem at the seam: name the guess, put it at a single identified input point, and let every step after it be pure derivation that would survive replacing the guess with a better one. The soft number becomes a parameter of the system rather than a defect in it.

Doing this buys two things that are hard to get any other way. First, the mechanical part becomes auditable independently — you can check it for correctness without arguing about the estimate, and you can rerun it when the estimate improves. Second, the guess itself becomes criticizable, because a guess stated as a single number sitting at a known place invites someone to attack that number, whereas the same guess smeared through a derivation is invisible and therefore permanent. And a guess can be given internal structure: rather than asserting one implausibly precise figure, decompose it into a product of smaller judgements, each of which is separately arguable and separately wrong in a bounded way. The decomposition does not make the estimate correct. It makes the estimate discussable, which is the property that matters when someone later disagrees with it.

A programmer who takes this seriously stops hiding constants. Heuristic thresholds, retry counts, cost-model weights, expected-frequency tables — each one gets pulled to a declared boundary of the system with its provenance recorded next to it, distinguishing "measured from data" from "somebody's calibrated feel for it." Code written this way splits cleanly into a layer that is defensible on its own terms and a small set of dials that are honestly labelled as dials. The failure mode it prevents is the system whose behaviour hinges on a number that nobody remembers choosing, embedded so deep that the only way to question it is to reverse-engineer the whole computation.

**Source:** [The Applications of Probability to Cryptography](../works/the-applications-of-probability-to-cryptography.md) — the introductory chapter's treatment of a priori probabilities, where the evidence is deliberately split into a part supported by statistics and a part left to judgement, with the worked example that breaks a single vague estimate into a chain of separately-defended smaller estimates.
