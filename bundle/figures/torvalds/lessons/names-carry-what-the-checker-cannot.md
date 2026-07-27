---
type: lesson
title: "Let names carry exactly what the checker cannot, scaled to how far the reader is from the definition"
figure: torvalds
works: [linux-kernel-coding-style]
axes: [cognitive-load, verifiability, expressiveness]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Let names carry exactly what the checker cannot, scaled to how far the reader is from the definition

**Lesson:** This document takes what looks like two contradictory positions on naming — terse single letters are correct for loop counters and scratch values, while a vague name on anything globally visible is treated as a serious offense — and the contradiction dissolves once you see the underlying rule. A name's job is to supply the context a reader is missing, and how much context a reader is missing is a function of distance from the declaration. Inside a five-line body the declaration is visible; a longer name adds typing and reading cost while supplying nothing. At the other end of the program, where the definition is thousands of files away, the name is the entire interface and must say what the thing does. If you cannot keep your locals straight, the diagnosis is not that the names are too short but that the function is too long.

The complementary half is a rule about what names must *not* carry: anything a mechanical checker already knows. Encoding a value's type into its identifier is rejected on the grounds that the compiler knows the type, checks it, and will never let it drift — whereas the hand-written encoding can drift and will silently lie. This generalizes into a discipline for allocating information between the type system and human convention: every fact that a checker can verify should live where the checker can see it, and naming convention should be spent only on invariants the checker is blind to. The clearest demonstration is the rule that ties a function's grammatical form to the meaning of its return value — an imperative name promises an error code, a predicate name promises a success flag — precisely because the language cannot distinguish those two integer conventions and mixing them produces bugs no compiler will catch. Convention is deployed exactly where verification runs out.

There is a structural version of the same principle in the treatment of type aliases. Hiding a structure behind a bare alias is rejected because it removes information the reader needs and gives nothing back; the alias earns its place only when the thing genuinely has no accessible interior worth naming, or when the underlying width really does vary by configuration so that the alias is carrying a fact rather than concealing one. The test proposed is not stylistic but informational: does this indirection remove something a caller could have used, or does it remove something a caller must not depend on?

A programmer who believes this stops arguing about name length in the abstract and starts asking two questions per identifier: how far away is the nearest reader, and is any part of this name duplicating a fact the toolchain already enforces? Answers follow immediately, and the naming debate mostly evaporates.

**Source:** [Linux Kernel Coding Style](../works/linux-kernel-coding-style.md) — the naming chapter's split between short local names and mandatory descriptive names for anything global, and its dismissal of type-encoding notation; the typedef chapter's enumeration of the narrow cases where an alias carries information instead of hiding it; and the chapter tying return-value representation to the grammatical form of the function name.
