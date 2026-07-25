---
type: lesson
title: "A part that can consult the whole is no longer a part you may vary independently"
figure: cardelli
works: [a-theory-of-primitive-objects-untyped-and-first-order-systems, an-imperative-object-calculus]
axes: [verifiability, cognitive-load]
subdomains: [programming-environments-and-object-systems, formal-methods-and-verification]
tags: [lesson]
---
# A part that can consult the whole is no longer a part you may vary independently

**Lesson:** Aggregates whose components are inert behave in a friendly way: refine any component and you have refined the aggregate, since nothing inside it can be surprised. That reasoning is so natural it gets applied by reflex to aggregates whose components are not inert. The moment a component can reach back to the container it lives in, its meaning depends on what all its siblings are, and refining one component changes the assumptions of the others. A refinement is then no longer a local act. The consequence is stark and provable: the friendly rule becomes unsound, and the only safe general rule for such aggregates is that the shape may be extended with new components while the existing ones stay exactly as they were.

This is the sharpest available answer to a question people usually settle by analogy. A structure holding functions looks like a structure holding data, and gets treated the same way, but the presence of self-reference makes them different kinds of thing, and the difference shows up only once substitutability is in play. Untyped, they are interchangeable. Under a substitution discipline, one supports free refinement of its parts and the other does not, because in the second case each part's obligations are stated in terms of the whole and therefore point the wrong way for refinement to travel.

Two operational habits fall out. First, when you find yourself wanting to relax an invariance restriction, look for the back-reference that makes it necessary; there is almost always exactly one, and finding it is more useful than winning the argument. Second, do not detach a component that had access to the whole from the whole it had access to. A component pulled out and offered as a standalone operation carries an implicit premise about its context, and once that premise is unstated anyone may violate it. Reuse of such a component has to keep it attached, which is a stronger constraint than reuse of an ordinary value and worth designing for explicitly.

**Source:** [A Theory of Primitive Objects: Untyped and First-Order Systems](../works/a-theory-of-primitive-objects-untyped-and-first-order-systems.md) — the section on objects versus records, which establishes invariance of components as necessary, derives contradictions from both a covariant rule and a component-extraction operation, and identifies the dependency of each component on the type of the whole as the cause. Also [An Imperative Object Calculus](../works/an-imperative-object-calculus.md) — the object type formation rules, where the type of the whole may occur in component types only in the permitted direction, and the worked examples showing where a component returning the whole blocks the refinements one would expect.
