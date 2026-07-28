---
type: lesson
title: "A rule that forbids without replacing will be broken"
figure: pike
works: [hello-world]
axes: [expressiveness, primitive-count, verifiability]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# A rule that forbids without replacing will be broken

The sharpest criticism in this work is aimed not at a competing encoding but at a
standard library. Once a character can span several storage units, the standard's
own rules make the classic byte-search routine unusable for portable code — and
the standard offers nothing that does the job instead. It also declines to say
how wide characters reach the output system at all. The result is a specification
that tells you what you may not do while leaving the task itself undone, which
means every real program either becomes non-portable or does not get written.
Prohibition without provision does not change behavior; it just relocates the
violation somewhere the rulemaker cannot see it.

The diagnosis offered is about process, and it is unkind but precise: the wide
character facility was designed by committee, late, and without being used. An
interface for a problem nobody has lived through will be incomplete in ways that
are invisible from the outside, because the missing pieces are exactly the ones
you only discover by finishing a real program. The authors' alternative was to
design while building and to change the interface repeatedly as the problems
became clear — and to state honestly that once they had to invent part of it,
they chose to invent the whole thing rather than inherit a partial design's shape.
Some of what they ended up with corresponds closely to the standard's routines;
the difference is that theirs covers enough ground to write applications with.

The constructive form of this is worth holding onto: when you deprecate,
restrict, or forbid a practice, you own the replacement. Shipping the ban without
the substitute pushes the cost onto every caller and guarantees inconsistent
workarounds, which is a worse outcome than the practice you banned. And the way
to know your replacement is adequate is not review, it is use — convert real
programs with it until the interface stops changing under you.

**Source:** [Hello World or Καλημέρα κόσμε or こんにちは 世界](../works/hello-world.md) — the Libraries section's enumerated reasons for not following ANSI C's wide and multi-byte character design, particularly the observation that the standard invalidates the byte-search routine while providing no equivalent.
