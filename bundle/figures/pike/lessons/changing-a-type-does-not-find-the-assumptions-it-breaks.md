---
type: lesson
title: "Changing a type does not find the assumptions it breaks"
figure: pike
works: [hello-world]
axes: [verifiability, cognitive-load, hardware-affinity]
subdomains: [programming-languages-and-semantics, operating-systems-and-systems-programming]
tags: [lesson]
---
# Changing a type does not find the assumptions it breaks

A representation change of the kind described here breaks two equations that
almost no program ever wrote down: that a character occupies one storage unit,
and that the form a character has in memory is the form it has in a stream. Code
that relied on those equations does not fail to compile. It compiles and does
something wrong. Clearing a buffer with a byte-count fill is correct until the
buffer's elements grow. A table indexed directly by character value is correct
until the index space becomes a million entries wide. A fixed array holding one
flag per possible option character is correct until options can be any character
at all. In each case the old code is type-correct and semantically dead.

This is the general hazard with invariants that are true, load-bearing, and
unstated. The compiler cannot help, because nothing was ever declared; the
assumption lives in arithmetic, in array sizes, in loop bounds. What the authors
had instead was a proxy: search for calls to the library routines that treat
storage units as characters, since those calls mark most of the places where the
equation was being used, and replacing them fixes many programs outright. That is
the transferable technique — when a hidden invariant breaks, find a *syntactic
shadow* of it that you can grep for, and accept that the shadow is incomplete.
The remainder gets found by knowing which programs are genuinely about the thing
that changed.

The second half of the lesson is that the fix is rarely mechanical even where you
find it, because the naive translation is often absurd. A lookup table does not
want to become a million-entry array; it wants to become a compressed run
representation. A byte-oriented matching automaton does not want its alphabet
widened by four orders of magnitude; it wants character classes represented as
ranges, and a deliberate decision about whether to convert its input at the
boundary or work in the encoded form directly. Widening a type is the trivial
part. The real work is that the data structures downstream were designed against
the old size, and their designs — not their declarations — are what must change.

**Source:** [Hello World or Καλημέρα κόσμε or こんにちは 世界](../works/hello-world.md) — the Ramifications section naming the two broken symmetries, and the tools-conversion section's examples of the buffer-clearing hazard, the character-indexed translation table, and the redesign of the regular expression matcher's alphabet.
