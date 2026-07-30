---
type: lesson
title: "Before accepting a restriction, find out whether it is forced by the mathematics or inherited as caution"
figure: scott
works: [logic-and-programming-languages]
axes: [expressiveness, primitive-count]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# Before accepting a restriction, find out whether it is forced by the mathematics or inherited as caution

**Lesson:** Some prohibitions in a formal system are theorems and some are folklore, and the two are hard to tell apart from inside. The specific case worth internalizing: a discipline of types that forbids an object from being applied to itself looks like a hard requirement, because the historical reason for introducing types was to block self-reference paradoxes. Arguing from that history, one can talk a practitioner out of using an untyped calculus on the grounds that it has no mathematical basis — and be technically persuasive while being wrong about the conclusion. The restriction is not what rules out self-application; the restriction is one sufficient way to rule out the *bad* self-application, and mistaking one sufficient fix for a necessary law forecloses everything else that fix happens to exclude.

The productive move was to keep pulling the thread instead of banking the win. If computable functions can be sensibly defined over many different spaces, then function spaces themselves might be perfectly good spaces; and if function spaces are good spaces, nothing obviously prevents one from being isomorphic to its own space of functions on itself — which is exactly the model that legitimizes the untyped calculus the type discipline had seemed to condemn. Notice the shape of the reasoning: the doubt was aimed at the author's own successful argument, and the target was the assumption doing the most work, not the weakest link. Peers with excellent judgment believed the required construction had no constructive description, which is worth remembering as calibration — an expert's confident impossibility claim about a construction nobody has attempted is a hypothesis, not a result.

The working practice this suggests has two halves. First, whenever a design rule is defended by the class of disasters it prevents, ask separately whether it is the *minimum* thing that prevents them; the gap between "this suffices" and "this is necessary" is where lost expressiveness accumulates. Second, run the interrogation hardest on the restrictions you yourself argued for most successfully, because a proof that a restriction is safe is not a proof that its absence is unsafe, and the satisfaction of having won the argument is what usually stops the inquiry a step too early.

**Source:** [Logic and Programming Languages](../works/logic-and-programming-languages.md) — the account of the 1969 Oxford visit, where an initially successful case against the type-free calculus led instead to doubting the enforced rigidity of logical types, to treating function spaces as first-class spaces, and to a space isomorphic to its own function space, against a contemporary's disbelief that such spaces admitted a constructive description.
