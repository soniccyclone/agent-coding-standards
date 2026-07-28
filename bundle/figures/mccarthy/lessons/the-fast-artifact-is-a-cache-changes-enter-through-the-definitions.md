---
type: lesson
title: "In a self-hosted system the fast artifact is a cache, so name the high-level definitions as the only place a change may enter"
figure: mccarthy
works: [lisp-1.5-programmers-manual]
axes: [hardware-affinity, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# In a self-hosted system the fast artifact is a cache, so name the high-level definitions as the only place a change may enter

**Lesson:** The compiler in this system is written in the language it compiles, and the manual walks through the resulting situation in order rather than leaving it implicit. The compiler exists first as ordinary definitions, debugged interpretively. It is then turned on itself, which is slow because most of it is still being interpreted while it runs. Because repeating that step on every system build is wasteful, the machine-language result is dumped out and reloaded thereafter. And then the sentence that makes the whole arrangement safe: any future correction has to begin from the definitions, which is why they are kept and shipped.

Without that rule the arrangement is a trap rather than a convenience. Two representations of the same program now exist, one readable and one fast, and they were equal only at the instant of the dump. The fast one is what actually runs, so it is the one a person under pressure will be tempted to patch — and the assembler is right there, documented, capable of inserting exactly that kind of fix. Every such patch silently promotes the derived artifact to a second source of truth, and the next regeneration from the definitions quietly reverts it. The single declared entry point for change is what keeps the pair from diverging, and it costs nothing except the discipline of paying the slow rebuild when you change something.

The right way to see the machine-language form, then, is as a cache: valuable, legitimately shipped, reproducible on demand from something more authoritative, and never to be edited. That framing also explains why the readable form must remain distributed rather than being discarded once the fast one exists. A cache you cannot regenerate is not a cache, it is the artifact, and the moment the definitions are lost the system's fast form becomes its only form — untouchable at the level anyone can actually reason at, which is how systems end up with a compiler nobody can change.

A programmer who holds this distinction asks of every build product, generated client, vendored bundle, or checked-in lockfile: which file is the input, and is the derived thing reachable from it by a command anyone can run? Where the answer is yes, the derived thing can be committed freely and treated as disposable. Where it is no — where the generator has been lost, or the output has been hand-edited even once — the derived artifact has silently become the source, and the honest move is either to reconstruct the generating path or to stop pretending the file is generated.

**Source:** [LISP 1.5 Programmer's Manual](../works/lisp-1.5-programmers-manual.md) — the compiler appendix, which narrates the four development steps from interpreted definitions through self-compilation to the punched assembly-language form reloaded at system-build time, and states that corrections must start from the retained definitions.
