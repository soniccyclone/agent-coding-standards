---
type: index
title: Tensions
description: The 21 genuine cross-figure contradictions found in Phase 5, each resolved. Every resolution is an agent decision marked resolved-by-llm and open to being overturned.
---

# Tensions

Phase 5 examined 51 apparent contradictions across six thematic slices of the
corpus and judged 21 to be real. The other 30 dissolved on close reading, and are
recorded with their reasoning in `docs/planning/phase5-dissolved.md` — knowing
that an apparent conflict is not one is a result worth keeping.

Every resolution here carries `status: resolved-by-llm`. That marker is load
bearing: these are agent judgements, not Nathan's, and each file states the
decision, the reasoning, and the strongest argument against itself so it can be
picked up and overturned. Resolutions were held to naming something — a layer
split, or a switching condition stated precisely enough that a reader can tell
which side of it they are on, or a winner plus what the losing side did not know.
An unfalsifiable "it depends" was not accepted.

| tension | figures | status |
|---|---|---|
| [Handing off a system: fund the written design or fund the overlap with the people who hold it](can-a-written-record-carry-the-theory.md) | naur, parnas | resolved-by-llm |
| [What establishes that a system too large to hold in one head is correct](confidence-in-a-large-system.md) | dijkstra, chaitin | resolved-by-llm |
| [Whether one facility may have two costs: cost models against uniform generality](cost-model-vs-uniform-generality.md) | wirth, kay, ingalls | resolved-by-llm |
| [Should the notation you design in be made to run](executable-design-notation.md) | hoare, kay | resolved-by-llm |
| [Whether the first artifact of a project is allowed to run](first-artifact-runnable-or-not.md) | brooks, abrial, chaitin | resolved-by-llm |
| [Whether expected access is a legitimate input to the structure of stored data](invariants-or-access-paths-shape-stored-structure.md) | codd, bachman, ullman | resolved-by-llm |
| [When a subsystem runs to tens of thousands of lines, is that a measurement of the problem or of the attempt](is-current-size-evidence-of-intrinsic-difficulty.md) | brooks, kay | resolved-by-llm |
| [Does every operation in a replicated service pass through one agreed order, or does each operation declare the order it needs](one-agreed-log-vs-per-operation-ordering.md) | lamport, liskov | resolved-by-llm |
| [One name over two realizations: proof of a good abstraction or a false claim of equivalence](one-interface-over-two-cost-profiles.md) | hoare, wirth | resolved-by-llm |
| [Whether a type can be a part of one universal domain, or must be a rule about what may be said](one-universal-domain-vs-type-as-a-restriction-on-what-may-be-said.md) | scott, reynolds | resolved-by-llm |
| [Whether to buy a construct by weakening a reasoning principle or to decline the construct](pay-the-reasoning-principle-vs-refuse-the-feature.md) | reynolds | resolved-by-llm |
| [Where in the workflow the correctness argument attaches](proof-that-leads-construction-vs-analysis-that-consumes-the-artifact.md) | sifakis, dijkstra, milner | resolved-by-llm |
| [A question with no principled answer: delete the vocabulary or publish a menu of answers](remove-the-question-vs-answer-it-from-a-menu.md) | hoare | resolved-by-llm |
| [When a construct is provably redundant, is that a reason to reject it or a reason to ship it?](simulability-kills-a-construct-vs-simulability-proves-nothing.md) | stonebraker, abiteboul | resolved-by-llm |
| [When a partition makes an invariant uncheckable, does the node withhold the answer or emit it and repair afterwards](stall-or-compensate-under-partition.md) | brewer, lamport, lynch | resolved-by-llm |
| [When a program commits to what a thing is: enforced declaration against deferred binding](static-declaration-vs-late-binding.md) | wirth, kay | resolved-by-llm |
| [Whether the substrate's cost is a specification or a temporary obstacle](substrate-cost-as-given-or-as-revisable.md) | kay, wirth, lampson, hoare | resolved-by-llm |
| [What standard of acceptance a component boundary is entitled to demand](tolerance-vs-demonstrated-correctness-at-a-boundary.md) | cox, abrial, dijkstra | resolved-by-llm |
| [Whether to delete a distinction today's operations cannot observe](unobservable-distinctions-banned-vs-deliberately-kept.md) | jones | resolved-by-llm |
| [What evidence promotes a slow composition into a fast primitive](what-evidence-promotes-a-slow-composition-into-a-fast-primitive.md) | ritchie, lampson | resolved-by-llm |
| [Who owns the efficiency budget an abstraction spends](who-owns-the-efficiency-budget.md) | wilkes, hoare | resolved-by-llm |

## What each one decided

**[Handing off a system: fund the written design or fund the overlap with the people who hold it](can-a-written-record-carry-the-theory.md)** — naur, parnas
They are not funding the same thing, and the line between them is whether   the incoming change lies on an axis of variation the design anticipated.

**[What establishes that a system too large to hold in one head is correct](confidence-in-a-large-system.md)** — dijkstra, chaitin
The two absolutes are about different propositions, and once the   propositions are separated both survive intact.

**[Whether one facility may have two costs: cost models against uniform generality](cost-model-vs-uniform-generality.md)** — wirth, kay, ingalls
Both are right, and the line between them is whether the discriminator that   selects the cheap or the expensive realization can be written down and   stays written down.

**[Should the notation you design in be made to run](executable-design-notation.md)** — hoare, kay
Run the design notation, keep the executor deliberately naive, and refuse to   let anything it produces be the deliverable.

**[Whether the first artifact of a project is allowed to run](first-artifact-runnable-or-not.md)** — brooks, abrial, chaitin
Run both, because they answer different questions, and when only one can be   funded the deciding question is where the properties that would kill you   come from.

**[Whether expected access is a legitimate input to the structure of stored data](invariants-or-access-paths-shape-stored-structure.md)** — codd, bachman, ullman
The two govern different objects and the mapping between them is a   maintainability test: an access-shaped structure is legitimate exactly   when it is a derived function of the invariant-shaped one, recomputable   from it, discardable without loss, and maintained by the system rather   than by the application.

**[When a subsystem runs to tens of thousands of lines, is that a measurement of the problem or of the attempt](is-current-size-evidence-of-intrinsic-difficulty.md)** — brooks, kay
The disagreement dissolves once you notice that Brooks's inherent category   is holding two different things, and that only one of them is a property   of the problem.

**[Does every operation in a replicated service pass through one agreed order, or does each operation declare the order it needs](one-agreed-log-vs-per-operation-ordering.md)** — lamport, liskov
These are consecutive steps in one design, not rival architectures, and the   seam between them is the question of whether an operation's postcondition   mentions anybody else.

**[One name over two realizations: proof of a good abstraction or a false claim of equivalence](one-interface-over-two-cost-profiles.md)** — hoare, wirth
The line is how many realizations are live inside one running program, and   both lessons state their own side of it clearly enough that this is not a   reconciliation imposed from outside.

**[Whether a type can be a part of one universal domain, or must be a rule about what may be said](one-universal-domain-vs-type-as-a-restriction-on-what-may-be-said.md)** — scott, reynolds
Both claims are true because they are about different things, and the seam   is that an abstraction boundary is not a value and therefore cannot   survive or fail to survive an embedding of values.

**[Whether to buy a construct by weakening a reasoning principle or to decline the construct](pay-the-reasoning-principle-vs-refuse-the-feature.md)** — reynolds
The line is the shape of the repair, not the size of the loss.

**[Where in the workflow the correctness argument attaches](proof-that-leads-construction-vs-analysis-that-consumes-the-artifact.md)** — sifakis, dijkstra, milner
Sifakis is not objecting to the argument leading the construction; he is   objecting to the argument being made per program.

**[A question with no principled answer: delete the vocabulary or publish a menu of answers](remove-the-question-vs-answer-it-from-a-menu.md)** — hoare
The two rules are selected by whether the arbitrariness goes all the way   down, and the test is whether any implementation has a definite answer   that a client could sensibly rely on.

**[When a construct is provably redundant, is that a reason to reject it or a reason to ship it?](simulability-kills-a-construct-vs-simulability-proves-nothing.md)** — stonebraker, abiteboul
The seam is whether the construct adds a semantic rule or eliminates itself   by translation, and on the first side Stonebraker is right and on the   second Abiteboul is.

**[When a partition makes an invariant uncheckable, does the node withhold the answer or emit it and repair afterwards](stall-or-compensate-under-partition.md)** — brewer, lamport, lynch
The two rules govern different sides of a boundary, and the boundary is   repairability without a second party's consent.

**[When a program commits to what a thing is: enforced declaration against deferred binding](static-declaration-vs-late-binding.md)** — wirth, kay
Most of this conflict dissolves once you separate two things that both sides   call binding, and the residue that survives has a sharp condition attached   to it.

**[Whether the substrate's cost is a specification or a temporary obstacle](substrate-cost-as-given-or-as-revisable.md)** — kay, wirth, lampson, hoare
The line is whether you can name the party who would revise the substrate   and the evidence that would move them.

**[What standard of acceptance a component boundary is entitled to demand](tolerance-vs-demonstrated-correctness-at-a-boundary.md)** — cox, abrial, dijkstra
Apply Abrial's own rule and it produces Cox's answer at Cox's boundary,   because the rule is conditional on something Cox's situation lacks.

**[Whether to delete a distinction today's operations cannot observe](unobservable-distinctions-banned-vs-deliberately-kept.md)** — jones
The ban stands, but the three lessons that state it quantify it over the   wrong set: run the test against the operations the subject matter admits,   not against the operations the interface currently lists.

**[What evidence promotes a slow composition into a fast primitive](what-evidence-promotes-a-slow-composition-into-a-fast-primitive.md)** — ritchie, lampson
These are two different decisions wearing one word.

**[Who owns the efficiency budget an abstraction spends](who-owns-the-efficiency-budget.md)** — wilkes, hoare
The deciding property is not the size of the multiple but whether the cost   is opt-out-able at the granularity where a program actually needs the   performance.

