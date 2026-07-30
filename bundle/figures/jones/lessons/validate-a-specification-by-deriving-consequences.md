---
type: lesson
title: "You cannot prove a specification right, so probe it by deriving consequences and checking them against intent"
figure: jones
works: [systematic-software-development-using-vdm]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# You cannot prove a specification right, so probe it by deriving consequences and checking them against intent

**Lesson:** Every artifact below the top of a development can be judged against the one above it. The topmost description has nothing above it, so correctness is not a property it can have — there is only the question of whether it says what was meant, and that question is not settled by any proof. This is where precise description is most often oversold and where its critics have a real point. But it does not follow that nothing can be done. You can interrogate the description: state a property you believe ought to hold, derive whether it follows, and compare the answer with your expectation. Agreement raises confidence; disagreement means either your expectation or your description is wrong, and either way you have learned something you did not know.

The properties worth probing are usually the ones that span several operations, because that is where a description of each operation in isolation can be individually plausible and collectively wrong. Does the thing you just added come back when you ask for what it belongs to? Does something you never added stay absent from every answer? Is a quantity you believe can only grow actually incapable of shrinking? Each of these is a small claim about the interaction of two or three operations, each is checkable against the description alone with no implementation in existence, and each corresponds directly to something a user would assume without being told. Assumptions users make without being told are exactly the failure surface of an interface.

Two things make this practical rather than aspirational. First, it is much easier when the description is phrased in terms of objects with an established body of properties, because then a derivation is a few steps of algebra instead of a struggle with representation detail — which is a further payoff of investing in the vocabulary you describe things in. Second, the probing questions are cheap to invent and cheap to answer, so the activity fits in the same slot that testing occupies later, and finds the same class of defect vastly earlier. Treat it as the top-level analogue of testing: not a proof of correctness, which is unavailable, but a systematic attempt to be surprised while surprise is still free.

**Source:** [Systematic Software Development Using VDM](../works/systematic-software-development-using-vdm.md) — the specifications section of the set-notation chapter, where the equivalence-relation specification is probed by stating and proving two cross-operation properties — that an element passed to the group query is a member of the returned set, and that a freshly added element does not appear in the group of a pre-existing one — with the accompanying remark that collecting and verifying such properties goes some way towards validating the formal specification against the informal understanding of the requirements, and that this is easier because the algebra of the underlying objects has been established.
