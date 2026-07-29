---
type: lesson
title: "Three features that rewrite the same tree are one feature"
figure: stonebraker
works: [the-design-and-implementation-of-ingres]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [databases-and-data-management, programming-languages-and-semantics]
tags: [lesson]
---
# Three features that rewrite the same tree are one feature

Restricting what a user is allowed to see, refusing updates that would violate a stated invariant, and letting someone name a derived subset of the data as if it were real all arrive on a requirements list as three separate subsystems. They are not three subsystems. Each one, expressed correctly, is a predicate that must hold in addition to whatever the user asked for, and each is implemented by taking the parsed form of the request and conjoining that predicate onto it before execution. Once you see them that way, none of them needs runtime machinery of its own: the enforcement point is a single stage that consults stored predicates and grafts them onto the request tree, and the whole execution path downstream is untouched because what reaches it is just another ordinary request.

The move that unlocks this is choosing a representation in which the features become the same operation, and it depends on two prior commitments. The request has to exist as a manipulable structure between parsing and execution rather than being interpreted directly, and the extra predicates have to be stored in the same form so that attaching one is structural surgery rather than string splicing and re-parsing. Neither commitment is free, but both are paid for once and then amortized across every feature that turns out to be expressible as an additional restriction — which is a startling number of them, because most policy is a restriction wearing a domain-specific costume.

What a programmer does differently is delay the decision about mechanism until after asking what each requested feature does to the meaning of a request. Features whose effect is to narrow a result set collapse together; features that genuinely change the shape of the answer do not, and that distinction is worth more than the feature list itself. The failure mode this avoids is the one where authorization checks live in the API layer, invariants live in triggers, and derived views live in a materialization service — three implementations of conjunction, three places to be inconsistent, and no single point where you can read off what a given user is actually permitted to compute.

**Source:** [The Design and Implementation of INGRES](../works/the-design-and-implementation-of-ingres.md) — the query modification stage described in the discussion of the parser process, where view resolution, integrity assertions, and access control are applied in sequence to one request as successive conjunctions on its tree.
