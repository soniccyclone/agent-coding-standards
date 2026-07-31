---
type: lesson
title: "Impose a known invariance as shared parameters, don't hope the fit rediscovers it"
figure: ullman
works: [mining-of-massive-datasets]
axes: [primitive-count, verifiability]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Impose a known invariance as shared parameters, don't hope the fit rediscovers it

**Lesson:** When you already know that a rule should behave identically no matter where in the input it is applied, you have two options: let each position carry its own independently adjustable copy of the rule and trust the fitting process to make them all come out the same, or force them to be literally the same parameters and let the fitting process adjust one shared copy. The second is almost always right, and the reason is not elegance. Independent copies mean the number of things to be determined grows with the size of the input, so the evidence per parameter shrinks as the problem gets bigger — exactly backwards. Tying them means the number of things to be determined is fixed by the size of the local rule, and every position in every example contributes evidence about the same shared quantity.

The knowledge that licenses the tie is domain knowledge, not statistics, and it has to be stated explicitly before any fitting begins. It takes the form of a claim about what the problem is indifferent to: the meaning of a local pattern does not depend on where it occurs, or on when, or on which member of a group produced it. That claim is falsifiable and worth arguing about, because tying parameters under a false invariance is a real error — it forbids the system from ever expressing a difference that genuinely exists. The discipline is to name the invariance out loud, decide whether you believe it, and only then encode it.

Once encoded, the invariance is not something the system can drift away from. This is the difference between a property that holds because it was built in and a property that holds because the data happened to support it. The first survives retraining on new evidence, unusual inputs, and the parts of the space you never sampled. The second is a coincidence that you will discover has ended only after it has caused something to break. Anywhere a system is expected to treat equivalent situations equivalently, the structural version of that guarantee is worth far more than the empirical one.

The general habit is to look at any parameterised system and ask which of its knobs ought to move together. Configuration that is duplicated per region, per tenant, per shard, per input position is a place where independent copies were created for something that has one true value. Collapsing those into a single shared setting shrinks what has to be determined, concentrates the evidence you have, and makes an assumption visible that was previously only implicit in the fact that all the copies happened to agree.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the convolutional-network section of the neural-nets chapter, which requires every node in a convolutional layer to use the same weight for the input at a given relative offset, argues that this makes training far more efficient because there are many fewer parameters per layer and therefore fewer training examples needed, and justifies the constraint by the observation that recognising a feature such as an edge is the same computation wherever in the field of vision it appears.
