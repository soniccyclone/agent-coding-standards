---
type: lesson
title: "Write the program for the machine you wish you had, and make the gap down to the real one mechanical"
figure: floyd
works: [nondeterministic-algorithms, the-syntax-of-programming-languages-a-survey]
axes: [expressiveness, cognitive-load, hardware-affinity, parallelizability]
subdomains: [algorithms-and-complexity, programming-languages-and-semantics]
tags: [lesson]
---
# Write the program for the machine you wish you had, and make the gap down to the real one mechanical

**Lesson:** A large fraction of the difficulty in a hard program is not the problem but the bookkeeping the real machine imposes: saving values so they can be restored, recording which branch was taken so it can be unwound, deferring output until it is known to be wanted. None of that is insight. The productive move is to invent a machine on which the bookkeeping does not exist, write the algorithm for that machine where it is short enough to read, and then supply a translation down to the machine you actually have. The translation is where the tedium goes, and because it is uniform it can be written once and applied forever.

What makes this more than wishful thinking is the demand that the translation be local: each construct of the idealized program expands independently into a small group of real instructions, one group carrying out the original effect while recording what it would take to reverse it, another doing the reversing. Locality is the property that makes the scheme mechanizable and therefore trustworthy, since a compiler, a macro processor, or a preprocessor can do it and nobody has to audit the result. It also means the two programs stay in correspondence construct by construct, so a change to the readable version has a predictable effect on the generated one. The choice of what to record is where the cost lives, and it is informed by structure rather than guessed: an operation that destroys information must save it, an operation that has an inverse needs no storage at all, and a branch, which loses nothing, needs no support on the way out but does need a record of which way it came in.

The idealized machine is deliberately uncommitted about how it is realized, and that neutrality is worth as much as the readability. The same abstract program can be executed by inline expansion with an undo stack, by snapshotting state at each decision point, or by a machine that forks at each decision and pursues every possibility at once. Those have wildly different performance profiles, including a genuinely parallel one, and choosing among them is a decision that arrives after the algorithm is written and correct, not before. Committing early to the mechanism is what usually forecloses the parallel option.

A programmer who works this way separates the question "what is the computation" from "what does this hardware make me track," and treats any code where the second question has infiltrated the first as unfinished. The same instinct explains why complicated control structures are best expressed as programs for a fictional interpreter and then compiled, rather than hand-woven at the level the target machine understands.

**Source:** [Nondeterministic Algorithms](../works/nondeterministic-algorithms.md) — the construct-by-construct conversion scheme and the closing observation that a complicated control structure is best written as a simpler algorithm for an imagined processor and then converted, plus the survey of alternative realizations including a self-replicating parallel one. Also [The Syntax of Programming Languages — A Survey](../works/the-syntax-of-programming-languages-a-survey.md) — the analyzer introduced as a hierarchy of imaginary subordinates who hire and dismiss each other, explicitly acknowledged to be hiding bookkeeping, then reduced to an explicit stack machine.
