---
type: lesson
title: "Define the abstract language once and treat every concrete surface as a replaceable projection of it"
figure: backus
works: [syntax-and-semantics-of-the-proposed-international-algebraic-language]
axes: [expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Define the abstract language once and treat every concrete surface as a replaceable projection of it

**Lesson:** A language definition faces a conflict of audiences. Machines of the era had small, arbitrary character repertoires; mathematicians writing for publication wanted superscripts, subscripts, and Greek letters; and the definition itself needs a fixed set of marks to be unambiguous about. Trying to satisfy all three at once produces a compromise that serves none of them well, and the compromise gets baked into the definition where it cannot be revised. The resolution is to designate one form whose only purpose is to state the rules of construction and meaning, and to treat every other form — the restricted character set a particular machine can read, the typographically rich form used in print — as a transliteration of it that shares its grammar and its semantics exactly.

The important part is which way the dependency points. The definitional form is not the true language with the others as approximations; it is the place where the rules live, chosen for definiteness rather than for convenience, and it claims no authority over how anyone writes in practice. Surface constraints that come from hardware, keyboards, printing, or habit then belong to the projection, where they can differ per site and change over time without touching the definition. Anything that would otherwise be a permanent limitation of the language becomes a local property of one rendering.

The transferable practice is to notice, whenever a representational constraint is about to influence a design, whether the constraint belongs to the thing or to one of its renderings — and to push it outward if it belongs to a rendering. Encoding, punctuation, available symbols, display width, and file format are usually properties of a projection. Keeping them out of the definition is what allows several audiences with incompatible requirements to be served by fitted surfaces over one shared object, instead of all being served badly by one negotiated middle.

**Source:** [The Syntax and Semantics of the Proposed International Algebraic Language](../works/syntax-and-semantics-of-the-proposed-international-algebraic-language.md) — the preliminary remarks distinguishing the form used for stating the rules from the machine-oriented and publication-oriented renderings, which are described as direct transliterations sharing the same syntax and semantics, together with the recorded discussion about a symbol-set compromise satisfying neither machines nor people.
