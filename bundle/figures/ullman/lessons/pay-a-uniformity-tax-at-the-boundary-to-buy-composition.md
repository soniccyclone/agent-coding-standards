---
type: lesson
title: "Pay a uniformity tax at the boundary to buy composition"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Pay a uniformity tax at the boundary to buy composition

**Lesson:** When a framework insists that every stage consume and produce the same shape, the insistence looks like bureaucracy from inside any single stage. The first stage's inputs carry a field that is meaningless for it and gets ignored. Some stages need only half the machinery and fill the other half with the identity function. The final result is not quite the type the user wanted and has to be projected down by dropping a component. Each of these is a small, visible cost paid by every stage, and each is an argument for letting stages have the shapes that suit them.

The compensation is not visible from inside a stage at all, which is why the trade is easy to get wrong. A uniform boundary type means any output can be any input, so multi-stage jobs are built by juxtaposition instead of by adapters, the system can insert operations of its own between stages without asking, and the number of interfaces the runtime must support is one rather than quadratic in the number of stage kinds. That last point is the real prize: the machinery for partitioning, transporting, restarting, and grouping data is written once against one shape, and adding a new stage kind costs nothing in that machinery. The tax is per-stage and constant; the benefit is per-pair and grows with the system.

The judgement is therefore about where you sit on that curve, and the rule of thumb is to ask how many things will meet each other. A pipeline of three fixed steps does not repay a uniform boundary type, and imposing one is genuinely the bureaucracy it appears to be. An open-ended family of steps written by people you will never meet, composed in orders you did not anticipate, repays it many times over — and the tell that you are in that regime is the appearance of adapter code, shims that unwrap one stage's result to feed the next. That code is the tax being paid anyway, in a worse currency: distributed across pairs, written by hand, and re-derived every time someone adds a stage.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 2's statement that inputs and outputs are held to key-value form specifically to allow composition of several MapReduce processes even though input keys are usually irrelevant, together with the relational-operator implementations where selection needs only the Map side and uses an identity Reduce, and where the result must be read as a relation by taking only one component of each output pair.
