---
type: lesson
title: "Build the machinery for inventing vocabulary, not a guess at the vocabulary itself"
figure: liskov
works: [programming-with-abstract-data-types]
axes: [primitive-count, expressiveness]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Build the machinery for inventing vocabulary, not a guess at the vocabulary itself

**Lesson:** There are two ways to give a programmer powerful notation. You can
try to anticipate what concepts the problem domain needs and install them as
built-ins, or you can install one mechanism that lets any concept be added
later with the same standing as a built-in. The first strategy fails for a
reason that has nothing to do with how clever the designer is: a notation that
gets used at all gets used on problems its author never imagined, so the
anticipated set will always be missing the piece the current problem actually
needs. Betting on foresight is betting against the future usefulness of your
own work.

The move this reframes is subtle. Rather than climbing higher — more
domain-specific constructs, richer built-in structures — you go sideways and
make the level itself open. A design whose extension mechanism is strong enough
has no ceiling on how domain-fitted its notation can become, because the
ceiling is now set by the programmer at the point of use rather than by the
designer years earlier. That makes a small, sharply-chosen primitive set more
powerful than a large, guessed one, which inverts the usual intuition that more
built-in features means more expressive power.

A programmer who has internalized this stops treating "we need a feature for
X" as a request for a feature. The question becomes whether the existing
mechanisms let a user construct X with the same first-class status as anything
shipped in the core — same declaration syntax, same type discipline, same
compilation treatment. If user-built concepts are visibly second-class,
that is the real defect, and no quantity of added built-ins repairs it. The
same discipline applies to library and framework design: the abstraction
you were asked for is less valuable than the ability to build the one nobody
asked for yet.

**Source:** [Programming with Abstract Data Types](../works/programming-with-abstract-data-types.md) — the opening argument contrasting very-high-level languages (fixed, pre-selected abstractions) against a structured-programming language that supplies an extension mechanism instead, and the notion of an indefinitely-high-level language that follows from it.
