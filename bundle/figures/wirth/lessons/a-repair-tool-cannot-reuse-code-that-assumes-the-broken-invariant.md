---
type: lesson
title: "A repair tool cannot reuse code that assumes the broken invariant"
figure: wirth
works: [project-oberon]
axes: [verifiability, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# A repair tool cannot reuse code that assumes the broken invariant

**Lesson:** The normal-path implementation of a subsystem is fast and short precisely because it trusts things: that an index is within its declared range, that a record has the layout its type says, that a reference points at something of the kind it claims, that a read returns what was written. Those assumptions are legitimate — they are the invariants the subsystem maintains, and re-checking them everywhere would be waste. But a tool built to repair that subsystem runs in the one situation where the invariants are known to be false. Reusing the normal implementation there is not code reuse; it is importing, into the only program that must not fail, the entire set of assumptions whose violation is the reason the program exists.

So the repair tool re-implements what it needs from beneath, with every assumption converted into a test and every test into a diagnostic. This looks like duplication and should be recognised as something else: the two versions have genuinely different specifications, one optimised for a system in a good state and one that must terminate sensibly on arbitrary bytes. Judge them separately. The repair version is allowed to be slower, longer, and uglier, and it is not allowed to have a path on which it faults, loops, or writes something it did not confirm — because there is no layer above it to catch it and nothing left to fall back to.

The design consequence, made at the time the repair tool is planned rather than when it is written, is that its dependency set must be as small as the loading mechanism permits. Every component it imports is a component whose assumptions it has inherited and whose correctness it now requires, and the failure it is meant to survive may be in any of them. Choosing the dependency set is therefore the main decision, and the right instinct is to take only what physically cannot be avoided and reprogram the rest. The general principle: when a component's job is to operate on a structure in an unknown state, the reasonable amount of shared code between it and the component that maintains that structure in a known state is close to none.

**Source:** [Project Oberon](../works/project-oberon.md) — section 14.3's account of DiskCheck, which imports only the kernel and the minimal input/output module, and of which the text states that no data read may be assumed correct, no index assumed within its declared bounds, no sector number assumed valid and no directory or header page assumed to have the expected format, so that guards and error diagnostics take a prominent place and the kernel's own disk procedures are deliberately not used but reprogrammed with additional guards and status reporting.
