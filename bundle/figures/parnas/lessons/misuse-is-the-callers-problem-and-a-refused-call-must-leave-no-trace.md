---
type: lesson
title: "Misuse is the caller's problem, and a refused operation must leave no trace"
figure: parnas
works: [a-technique-for-software-module-specification-with-examples]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Misuse is the caller's problem, and a refused operation must leave no trace

**Lesson:** Decide who owns a violated precondition and much else follows. Put ownership with the callee and you get a component that must invent a policy for every way it can be misused, encode that policy in a return convention, and force every ordinary call site to interleave normal logic with checks for situations that mostly cannot happen there. Put ownership with the caller and the component's job shrinks to detecting the violation and diverting control to a handler the caller supplied. The main path then contains only the main case, which is both shorter and far easier to reason about, and the classification of what counts as misuse becomes part of the published boundary instead of buried folklore.

This only works if the refusal is genuinely nothing but a refusal. Two properties make that true. Divert control on the first violated condition and no other, so which handler runs is determined rather than a matter of internal order. And leave no observable residue: a refused call must be indistinguishable from a call never made, so that if the caller repairs its mistake and comes back, the component behaves as if this were the first attempt. There is no memory of the bad call. That is a heavy obligation on an implementer, and it is worth spelling out what it demands — no irreversible change may be started unless the implementer knows the remaining changes can all complete without any further refusal. Effectively you have imposed all-or-nothing behavior on every operation, which is exactly the property that makes retry safe and makes a partial failure not a lasting corruption.

The layering rule falls out of the same reasoning. Every component receives the refusals of what it uses, and has exactly two honest options: absorb the refusal so its own client never learns anything happened, or report a condition phrased entirely in its own vocabulary — terms a client who knows only this component's boundary can act on. What it may never do is pass along a condition that only makes sense to someone who knows what it is built out of, because that is the interface leaking its internals through the failure channel, which is the channel people forget to hide. Also worth noting: distinguish the cases finely in the specification even if they will be handled identically. Merging them is the caller's option to exercise later; pre-merging them destroys information the caller might need and cannot recover.

**Source:** [A Technique for Software Module Specification with Examples](../works/a-technique-for-software-module-specification-with-examples.md) — the discussion of trap-style error conditions in the effect section: that response is the caller's responsibility, that only the first applicable condition fires, that no record of an erroneous call survives, the resulting constraint on irreversible changes, and the two permitted options for a component receiving a lower-level trap.
