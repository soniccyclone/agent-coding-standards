---
type: lesson
title: "Some things belong in the core because everyone must agree on them, not because they cannot be built out of something smaller"
figure: steele
works: [common-lisp-the-language-2nd-edition]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Some things belong in the core because everyone must agree on them, not because they cannot be built out of something smaller

**Lesson:** The opening of this specification draws a line that most discussions of minimality never notice is there. It distinguishes the set of things the language must contain conceptually from the set of things that could not be derived from anything else, and states plainly that the former is not the latter and is not meant to be. Arbitrary-precision integers and exact rationals are the worked example: both are perfectly constructible in the language itself out of machine-sized arithmetic, and some implementations do exactly that internally — yet they are specified as though primitive, because the point of putting them in the core is not that they resist derivation, it is that every user should be able to write code assuming them without negotiating.

The reasoning behind this is about what happens when a capability is left out of a shared definition. It does not stay absent. It gets built, repeatedly, by every group that needs it, in mutually incompatible ways, and the incompatibility then propagates into every program that touches the capability. A derivable feature omitted from a specification is therefore not a saving; it is a decision to relocate the same complexity into user code and multiply it by the number of independent users. Whether that trade is worth making depends entirely on how many people need the feature and how much they need to agree, which is an empirical question about the community rather than a structural question about the formalism. The same document is candid that this measure has a price: it also declines to close several of its type partitions, deliberately leaving room for implementors to add kinds of number nobody had thought of, and the resulting taxonomy is admittedly tangled rather than clean.

What makes this more than an excuse for a large language is that the criterion is stated as a criterion and applied selectively. Constructs that exist only for convenience are documented with their reductions shown, so that a reader can see they are furniture. Constructs promoted into the core against derivability are argued for individually, on grounds of how badly the community needs a common answer. The specification also reserves the opposite move: where implementations disagreed and no agreement could be forced, the document leaves the behaviour unspecified rather than inventing a compromise nobody would honour.

A designer who holds both halves of this stops treating "can it be defined in terms of the others?" as decisive. They ask two questions instead: can it be derived, and does it matter that everyone derive it the same way? A yes to the first and a yes to the second argues for putting it in the core anyway and paying the cost in surface area. A yes to the first and a no to the second argues for shipping it as a library with its derivation visible. The distinction is what separates a small language from a merely incomplete one, and it is why a specification's size is not by itself evidence of anything.

**Source:** [Common Lisp the Language, 2nd Edition](../works/common-lisp-the-language-2nd-edition.md) — the introductory statement of purpose distinguishing the conceptually necessary core from an implementationally minimal one, with the arbitrary-precision-integer example, read against the repeated refusals elsewhere in the type chapter to declare partitions exhaustive.
