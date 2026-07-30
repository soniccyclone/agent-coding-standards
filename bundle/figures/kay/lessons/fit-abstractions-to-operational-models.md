---
type: lesson
title: "People hold knowledge as ad hoc procedures, not consistent axioms, so build on the models they already have"
figure: kay
works: [a-personal-computer-for-children-of-all-ages]
axes: [cognitive-load, expressiveness]
subdomains: [programming-environments-and-object-systems, programming-languages-and-semantics]
tags: [lesson]
---
# People hold knowledge as ad hoc procedures, not consistent axioms, so build on the models they already have

**Lesson:** What someone understands about a domain is not a coherent axiom system but a collection of situated procedures — ways of getting particular results — which are frequently incompatible with each other and are held anyway, because each one works in the situation that produced it. Formal consistency arrives late if at all, and it arrives on top of the procedures rather than replacing them. Two things follow. First, teaching or documenting by presenting the clean formal structure first fights how the knowledge is actually stored, which is why a formalization can be simultaneously correct and useless. Second, executable description is an unusually good fit for how people already think, since a procedure that mostly works and needs debugging is exactly the shape of the knowledge in their heads.

The design consequence is that abstractions must be chosen against the models a user already operates, not against the elegance ranking a specialist would produce. When a formally superior framing depends on a concept the user does not yet hold, it will be memorized rather than understood, and every use will require rebuilding it from scratch. The productive move is to find what they do hold — often relational, local, comparative notions rather than global absolute ones — and express the target ideas in those terms, so that the new capability arrives as an extension of existing competence instead of a replacement for it. Powerful ideas expressed relative to the user's own position are learnable in a way that the same ideas expressed against a global frame are not.

This also argues for preferring semantic framings over syntactic ones. Distinctions that exist only to keep a notation tidy — labels for the difference between a thing and its written form, categories that carve the domain by how it is written rather than by what it does — impose real cost and teach nothing, and they tend to collapse under the first case that does not fit the notation. Ask of every concept you require someone to hold: does it correspond to something that happens, or only to something in the way we write it down? The second kind is where gratuitous difficulty lives.

**Source:** [A Personal Computer for Children of All Ages](../works/a-personal-computer-for-children-of-all-ages.md) — the discussion of developmental research in which knowledge is characterized as ad hoc operational models resembling algorithms and strategies rather than logical axioms and theorems, the argument that this makes computers a natural medium for expressing what a person knows, the account of teaching geometry through relative rather than global coordinate framings, and the criticism of the syntax-first number/numeral distinction as nonsemantic.
