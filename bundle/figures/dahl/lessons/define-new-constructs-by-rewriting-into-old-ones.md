---
type: lesson
title: "Specify a derived construct as a rewriting into constructs whose meaning is already settled"
figure: dahl
works: [class-and-subclass-declarations, simula-67-common-base-language]
axes: [cognitive-load, verifiability, primitive-count]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
tags: [lesson]
---
# Specify a derived construct as a rewriting into constructs whose meaning is already settled

**Lesson:** There are two ways to give meaning to a mechanism that builds one description on top of another. You can describe a runtime process — a search that starts here, fails, and continues there — or you can describe a source-to-source transformation that produces a single description in the language you already understand, and then say that the meaning of the composite is the meaning of that result. The second way is enormously cheaper for everyone downstream. Inheritance defined by textual composition means the parameter lists join, the declarations land in one shared scope, the statement sequences interleave in a stated order, and name collisions are exactly the collisions of an ordinary declaration list. Nothing new has been added to the semantics; a new way of writing has been added to the syntax.

This choice pays in three places at once. A reader reasons about a composite by reasoning about one flat construct, so the working set stays the size of a single block rather than a chain of frames. A compiler resolves almost everything statically, because the transformation is stipulated to happen before execution. And the awkward cases surface as concrete questions about the rewriting rather than as mysteries: what happens when an inner definition shadows an outer name is answered by a stated renaming discipline for uncommitted name occurrences, which is the same problem substitution has always had and has a known answer.

The general habit: when you introduce a layering, sharing, or reuse mechanism, write down the reduction. If you cannot say what single artifact the composite is equivalent to, you have not defined the mechanism, you have described an implementation of it, and every later question about interaction with scoping, initialization order, or redefinition will have to be settled by experiment. Choosing the reduction also forces the honest ordering decisions early: which side's statements run first, which side can see which names, which side owns the frame. Those answers, written into the rewriting, become properties a reader can rely on instead of folklore.

**Source:** [Class and Subclass Declarations](../works/class-and-subclass-declarations.md) — the semantics of prefixed declarations, given as a recursive concatenation of parameter lists, specifications, block heads and statement sequences, plus the later extension that lets a prefix body be split around a placeholder. Also [SIMULA 67 Common Base Language](../works/simula-67-common-base-language.md) — the concatenation section, which states the transformation as taking place before execution and spells out the systematic identifier substitution that keeps it sound.
