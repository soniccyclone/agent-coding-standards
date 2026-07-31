---
type: lesson
title: "A property names a thing only when it pins the thing down, so find out which parts of the structure it leaves free"
figure: jones
works: [software-development-a-rigorous-approach]
axes: [expressiveness, verifiability]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# A property names a thing only when it pins the thing down, so find out which parts of the structure it leaves free

**Lesson:** Describing something by the property it must satisfy, rather than by a recipe for building it, is the most useful move available when writing down what you want. It has a limit that is easy to walk into unnoticed. A property picks out a single object only when the object is determined by exactly the information the property talks about. Where the thing you are describing carries structure the property says nothing about, the description names a family and you have quietly stopped saying which member you meant.

The clean illustration is the difference between an unordered collection and an ordered one. You can define a collection by "all the values satisfying this condition", and that is a complete definition, because a collection of that kind is fully determined by what belongs to it. Attempt the same for a sequence and the definition fails — not because the notation is missing but because the condition never mentioned order, so it cannot fix one. Sequences therefore have to be described by construction, or by a property that explicitly speaks about positions. The lesson generalizes past sequences to anything whose identity depends on more than the predicate can see: which of two identical-looking records this is, which of several arrangements was intended, which duplicate was kept.

So the working question when writing a property-style description is not "is this true of what I want" but "what does this leave free, and did I mean to leave it free". Both answers are legitimate and they lead to different work. If the slack is deliberate, you have deferred a decision to whoever implements, which is often exactly right and should be said out loud. If the slack is an oversight, you have a description that several distinct behaviours satisfy, and the disagreement will surface much later as an argument in which everyone can point at the specification.

The disciplined form of this is a rule about a piece of vocabulary. The phrase "the thing such that" is only legitimate once you have established that exactly one thing satisfies the condition — existence alone is not enough, and two objects satisfying it must be shown to be the same object. Treat that as an obligation you owe every time you write a definite description, and the ambiguity gets caught at the moment it is introduced rather than at integration.

**Source:** [Software Development: A Rigorous Approach](../works/software-development-a-rigorous-approach.md) — chapter 9's "Use in Specifications" remark that there is no analogue for lists of the implicit set definition, with the stated reason that such a definition would not fix the order of the elements in the generated list, and the consequent reliance on generating functions instead; together with the chapter's earlier introduction of the unique-existence quantifier and the description operator, defined so that the definite description is only meaningful under a prior assertion that exactly one object satisfies the property — spelled out there as existence conjoined with the requirement that any two satisfying objects be equal — and applied to the concatenation definition and to the alternative formulation of the equivalence-relation invariant.
