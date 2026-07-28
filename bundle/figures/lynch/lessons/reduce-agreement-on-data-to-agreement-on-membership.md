---
type: lesson
title: "When you cannot agree on an answer, try agreeing on who counts and derive the answer"
figure: lynch
works: [impossibility-of-distributed-consensus-with-one-faulty-process]
axes: [primitive-count, verifiability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity]
tags: [lesson]
---
# When you cannot agree on an answer, try agreeing on who counts and derive the answer

**Lesson:** The positive protocol tucked into the back of the asynchronous-consensus impossibility paper does something structurally interesting: it never tries to agree on the answer at all. Participants exchange who-heard-from-whom, build a picture of that communication relation, and identify a distinguished subgroup that the relation itself singles out. Everyone who finishes identifies the same subgroup, and everyone knows that subgroup's inputs, so the answer follows from applying any fixed rule to a set all parties already share. Agreement on a value has been replaced by agreement on a membership, and the value is then a local computation.

The move generalizes far past this one protocol, and it is worth naming as a design reflex. Deciding a value is hard because the space of values is unconstrained and the decision has to be reached, not derived. Deciding a set of participants is easier because the candidates are known in advance, the structure that picks them out is something the communication pattern already generates, and — crucially — the set is stable in a way a value is not. Once the membership is common knowledge, everything downstream becomes a pure function that each node evaluates alone, with no further coordination required. You have traded a coordination problem for a naming problem, and naming problems have smaller state spaces.

This is why so much real machinery in this area is about views, epochs, configurations, and quorums rather than about values. Those are all the same substitution: fix who is participating, and correctness of the payload becomes a local matter. It also explains why membership changes are the part of these systems that keeps being subtly wrong — the substitution only pays off while the membership is agreed, so the seam where membership itself changes is where the original hard problem resurfaces, undiluted.

The practical discipline is to look, whenever a design calls for agreement on some computed result, for a smaller thing that the result is a function of, and to try to agree on that instead. Often the smaller thing is a set of identities, a version number, or a term index. If you can pin that down, the expensive coordination collapses into arithmetic that every node can do independently.

**Source:** [Impossibility of Distributed Consensus with One Faulty Process](../works/impossibility-of-distributed-consensus-with-one-faulty-process.md) — the constructive section following the main theorem, where a distinguished subgroup is extracted from the transitive closure of the heard-from relation and used as the common basis for a locally computed decision.
