---
type: lesson
title: "Specify what must remain possible, or a generator will hand you the least capable thing that qualifies"
figure: emerson
works: [using-branching-time-temporal-logic-to-synthesize-synchronization-skeletons, model-checking-algorithmic-verification-and-debugging]
axes: [expressiveness, parallelizability, verifiability]
subdomains: [formal-methods-and-verification, distributed-systems-and-concurrency]
tags: [lesson]
---
# Specify what must remain possible, or a generator will hand you the least capable thing that qualifies

**Lesson:** Requirements written entirely as obligations are satisfiable by degenerate artifacts. If every clause says something must always hold or must eventually happen, then a system with exactly one behavior can meet the whole set, and it will meet it more easily than a system with many behaviors, since fewer behaviors means fewer chances to violate anything. Anything that constructs an artifact from your requirements, whether that is a synthesis procedure, an optimizer, an over-eager refactoring, or a scheduler, is under pressure to collapse alternatives, because collapsing alternatives is the cheapest route to compliance. Nothing in an obligation-only specification objects.

Emerson makes this the reason for preferring a notation with an explicit existential quantifier over futures. Once you can assert that some continuation reaching a given condition exists, you can require that the built system retain genuine choice: this branch must remain reachable, that alternative must not be pruned away. Without it you can write a disjunctive obligation and be handed a system that satisfies one disjunct and has no run at all where the other occurs, which is compliant and useless. The concrete consequence in his setting is parallelism. A concurrent program whose specification only constrains what must happen can be realized as something with a single interleaving, technically correct and with the concurrency squeezed out of it. Preserving independent execution turns out to require saying that independent execution remains available, which is a possibility claim, not an obligation.

The same asymmetry appears whenever a system is generated or reduced rather than written by hand. A cache that always returns a correct value can return one value forever. A retry policy constrained only by "eventually succeeds or reports failure" is satisfied by never trying. A state machine that must never enter an illegal state is satisfied by never leaving the start state. Restartability, availability of a fallback path, and reachability of every branch of a feature flag are all claims about what remains possible, and none of them survive translation into a language of obligations alone. Emerson notes the restartability case specifically as one of the properties the obligation-only vocabulary cannot state.

A programmer who has internalized this writes reachability requirements alongside safety requirements. For every important state, an assertion that the state is still attainable. For every branch that must not be dead, a test that reaches it. When shrinking a system, whether by simplifying, removing a feature, or serializing a concurrent path, they check the possibility claims first, since those are the ones a shrink silently breaks while every obligation still passes.

**Source:** [Using Branching Time Temporal Logic to Synthesize Synchronization Skeletons](../works/using-branching-time-temporal-logic-to-synthesize-synchronization-skeletons.md) — the related-work comparison against linear-time synthesis, which argues that asserting the existence of paths is what keeps a synthesized concurrent program from being a degenerate single-path solution. The Turing lecture's expressiveness discussion supplies the restartability example as a property the universally quantified vocabulary cannot express.
