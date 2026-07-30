---
type: lesson
title: "Ask which parts of a famous decomposition were forced by the language rather than by the problem"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [primitive-count, expressiveness]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Ask which parts of a famous decomposition were forced by the language rather than by the problem

**Lesson:** A widely-copied structure gets treated as a single insight, when it is usually several decisions of unequal quality bundled under one name. The instructive case here is Model-View-Controller, described by the person who created it, who separates his own three-way split into parts he still defends and a part he does not.

Splitting the information from its presentation he argues for on two grounds, one technical and one about people. Technically, presentations turn out to be reusable across quite different information — text, list and tree presentations especially. But the argument he leans on is the user's: he routinely wants several simultaneous presentations of the same thing, and says he misses the capability sorely in systems that lack it. Splitting the presentation from the *input handling* gets a markedly cooler assessment: the value "is not as evident," much of the same benefit "could have been achieved by suitable configuration facilities," and the real reason given is that the implementation language had single inheritance, so the two needed separate ancestries. He adds that he has not revisited it only because there is no reason to rewrite working editors — and that he would reconsider if designing a library from scratch.

That is worth generalizing into a habit. When adopting an established decomposition, ask of each seam whether it tracks a distinction in the problem or a limitation of the tooling where it was born, because the second kind does not transfer and often has no justification left once the constraint is gone. A related observation from the same discussion: the long argument about whether MVC needs three objects or two dissolves once you separate the *roles* from the objects carrying them, because then three roles can be borne by three objects or two or one as the situation warrants, and the question stops being architectural and becomes local. Much apparently deep disagreement about structure is really disagreement about a mapping that nobody had named as a separate choice.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 9's account of Model-View-Controller, which the author states he created while working with Adele Goldberg at Xerox PARC in 1978-79, together with the boxed assessment that the model/view separation is justified by view reuse and above all by user convenience, that the view/controller separation is not as evident and is attributable to Smalltalk's single inheritance, and that role modeling dissolves the three-or-two-objects debate by permitting any mapping of roles onto objects.
