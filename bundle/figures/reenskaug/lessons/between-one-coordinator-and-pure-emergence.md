---
type: lesson
title: "Between one omniscient coordinator and pure emergence sits declared topology"
figure: reenskaug
works: [the-common-sense-of-object-oriented-programming]
axes: [cognitive-load, expressiveness, primitive-count]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Between one omniscient coordinator and pure emergence sits declared topology

Faced with logic that spans many parts, the usual debate offers two positions. Hoist all the coordination into one component that knows every participant and issues every instruction, leaving the participants as inert holders of data. Or push every decision down into the participants and let the system-level behavior be whatever their local decisions add up to. Reenskaug rejects both with a symmetrical diagnosis: total centralization becomes unmanageably intricate the moment the interaction pattern is itself intricate, since one component now encodes every path through it; total decentralization is unanalyzable, since no component knows the plan and the plan therefore exists nowhere.

The third position is to keep the logic distributed across the participants while making the arrangement they sit in an explicit, written thing. Each participant still holds the part of the procedure that belongs to its position, so no single component swells into a controller. But the set of positions and the permitted paths between them are declared where a reader can see them, and code in one position can only address positions the declaration says it is connected to. Distribution stops being chaos because the shape it happens inside is stated rather than inferred.

Reenskaug also blocks the obvious objection, that this is procedural programming smuggled back in. His answer is that both state and behavior remain spread across the participants; what has been added is the ability to talk about more than one of them at once. The complaint conflates two different things — writing a procedure down in one readable place, and running it in one place. Only the second is centralization, and only the first is what this buys.

A programmer working this way treats "who orchestrates this?" as a false question with two bad answers, and asks instead where the arrangement is written down. Any design argument that oscillates between a god object and hoping the pieces work it out is missing the artifact that makes the middle position available.

**Source:** [The Common Sense of Object Oriented Programming](../works/the-common-sense-of-object-oriented-programming.md) — the conclusion's contrast between the fully centralized mediator treatment of the animation example and unconstrained peer-to-peer collaboration, and the answer to the charge that the resulting scheme is procedural programming in disguise.
