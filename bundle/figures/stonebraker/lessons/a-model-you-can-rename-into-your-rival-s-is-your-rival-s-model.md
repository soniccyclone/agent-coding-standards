---
type: lesson
title: "A model you can rename into your rival's is your rival's model"
figure: stonebraker
works: [the-implementation-of-postgres]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [databases-and-data-management, programming-environments-and-object-systems]
tags: [lesson]
---
# A model you can rename into your rival's is your rival's model

There is a cheap and decisive test for whether a debate about which paradigm a system belongs to is worth having. Take the system's description and substitute the rival camp's vocabulary throughout — collection for class, member for instance, procedure for method — and see whether anything breaks. If the document still reads correctly, the disagreement was never about capability. It was about which words the parser accepts, and the camps are arguing over a dictionary while believing they are arguing over semantics. A system can satisfy several mutually hostile definitional checklists at once, which tells you the checklists are testing vocabulary rather than power.

The useful reframing is that a model is defined by what you can express and what the machinery can do with what you expressed — which operations compose, what the system can infer about them, what it can optimize, what it refuses. Those are checkable properties with observable consequences. Membership in a named family is not; it is a social fact about which conference accepted the paper. Once you notice this, most paradigm arguments dissolve into either a real question nobody was asking (can this system express a value that is one of several unrelated types, and can it index one?) or nothing at all.

The practical effect is to change what you ask when someone offers you a new model or a new framework. Not what it is called and which tradition it belongs to, but what became expressible that was not, and what became decidable or optimizable that was not. If the answer to both is nothing, the offer is a vocabulary migration priced as an architecture change. The corollary applies to your own work: if you find yourself defending your system's membership in a category, you have stopped talking about the system, and the energy is better spent on the capability questions the categorization was standing in for.

**Source:** [The Implementation of Postgres](../works/the-implementation-of-postgres.md) — the section asking whether the system is object-oriented, which shows it satisfying the object-oriented, extended-relational, and nested-relational descriptions simultaneously and concludes the difference is a handful of tokens.
