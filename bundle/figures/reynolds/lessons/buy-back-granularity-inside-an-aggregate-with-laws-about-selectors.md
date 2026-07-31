---
type: lesson
title: "Independence analysis works at the granularity of names, so buy finer granularity with laws about selectors"
figure: reynolds
works: [the-craft-of-programming]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# Independence analysis works at the granularity of names, so buy finer granularity with laws about selectors

**Lesson:** Any argument that "this cannot disturb that" ultimately decomposes into facts about identifiers, because identifiers are the only handles the text offers. That default granularity is fine until you meet an aggregate: an array, a record, a table — one name covering many independently updatable parts. At that grain the analysis can only say that touching the aggregate might disturb anything reached through the aggregate, which is true and useless. Everything interesting about working with such structures depends on saying that writing one part leaves another part alone, and no reasoning framed in terms of names alone can say it.

The recovery is a small family of laws relating independence of parts to a condition on the *selectors* rather than on the names. Writing at one index does not affect reading at another, given that the indices differ; writing at one index does not affect a whole region, given that the index lies outside the region. What makes these usable is that their hypotheses are ordinary mathematical facts about the index domain, holding in every state of the computation rather than at one moment, so they can be discharged by arithmetic and then relied on throughout. That is the trade being made: you accept an obligation in a completely different currency — a fact about numbers or about set membership — and in exchange you get to treat two parts of one structure as if they had been two separate names all along.

The warning attached is where the effort actually goes. Passing a *part* of an aggregate to a component, rather than the whole thing, is the case that makes this reasoning expensive, because the component's own independence conditions now have to be re-established for every other part that the surrounding code cares about, one law application at a time. It is worth knowing this before designing an interface: handing over the aggregate and an index keeps the independence facts where they can be stated once, while handing over a designator for one element scatters them across the call. And notice that the same move — express independence between parts as a state-independent condition on how the parts are selected — is what any such structure needs, whatever the selector happens to be.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 3.3.13's axioms for array element and array segment non-interference, with the remark that these go significantly beyond the previously given rules since they specify non-interference between parts of an entity named by a single identifier, and the accompanying note on the use of static assertions to ensure the independence holds in any state; the introduction of an integer-set data type absent from the executable language so that a region may be denoted; the axiom giving conditions under which an array designator is a good variable, derived from the abstract assignment axiom; and the worked factorial-table example, prefaced by the observation that the rather complicated reasoning used there is typical of programs in which array designators are used as actual parameters.
