---
type: lesson
title: "A constraint does not have to determine a unique implementation, only the properties the argument downstream actually consumes"
figure: church
works: [introduction-to-mathematical-logic]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# A constraint does not have to determine a unique implementation, only the properties the argument downstream actually consumes

In one of his reduction proofs Church needs some auxiliary machinery to behave like an enumeration of pairs, and he arranges it the way one arranges such things: he writes a formula whose antecedent constrains the auxiliary predicates, so that anything satisfying the antecedent behaves the way the rest of the argument needs. He then exhibits one particular interpretation that satisfies it, and immediately admits the obvious objection — for a given starting point there are in general *other* interpretations satisfying the same antecedent, not just the one he built. His response is not to strengthen the antecedent until the interpretation is unique. It is to observe that all the satisfying interpretations must share certain properties, and that those shared properties are sufficient to make the rest of the proof go through.

That is a small moment and a large habit. The instinct, when a specification admits more models than you intended, is to add clauses until only the intended one survives. Church instead asks what the consumer of the specification actually needs, checks that every model supplies it, and stops. Uniqueness was never the requirement; the requirement was whatever the downstream argument reads. Extra models are only a problem if one of them can break something, and determining that is a different question from determining whether they are all the same.

The cost of the other approach is worth stating, because it is usually invisible. Every clause added to force uniqueness is a commitment that everything satisfying the spec must honor forever, including things nobody has consumed and nobody will. Those clauses are the ones that make a spec impossible to satisfy with a better implementation later, that turn a permissible optimization into a violation, and that fail in review with no one able to say what actually depends on them. A specification tightened past the point of use has not become more correct; it has become more expensive to satisfy while proving exactly as much.

Programmers meet this constantly under different names. An interface is a constraint that admits many implementations, and the discipline that makes it useful is exactly Church's: enumerate the properties callers rely on and require those, rather than describing one implementation and calling it the contract. A test that asserts on the full serialized output is a spec forcing uniqueness; a test that asserts the two fields the caller reads is a spec of the consumed properties, and it survives a formatting change that the first one turns into a false failure. The same distinction separates a schema that pins field order and a schema that pins field meaning, or an API doc that describes a response and one that describes the guarantees over responses.

The practical procedure follows directly and is uncomfortable in a productive way: for each constraint you are about to impose, name the argument or the caller that consumes it. If you cannot name one, the constraint is not specifying, it is describing — and description masquerading as specification is where the accidental commitments accumulate. And when someone reports that the spec admits an unintended case, the first question is not how to exclude it, but whether the properties everything shares are still enough.

**Source:** [Introduction to Mathematical Logic](../works/introduction-to-mathematical-logic.md) — the closing remark of the proof of the reduction theorem in the section on reductions of the decision problem, where Church concedes that for a given value of the original variable other systems of values of the auxiliary variables may also satisfy the antecedent, and argues that these must nevertheless share properties with the exhibited system sufficient to ensure that the consequent holds exactly when the original formula does.
