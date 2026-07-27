---
type: lesson
title: "A barrier to your technique is not a property of the problem"
figure: hartmanis
works: [relativization-a-revisionistic-retrospective]
axes: [verifiability]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# A barrier to your technique is not a property of the problem

**Lesson:** A result showing that a family of methods cannot settle a question is a statement about the methods. It gets silently upgraded, over years of repetition, into a statement about the question — and then into a reason not to try. That is what happened to a whole generation of open problems in complexity theory: once someone showed that the standard machinery could be made to give either answer depending on what extra power you handed the machines, the profession concluded that any problem with that signature was out of reach, and demonstrating the signature became a routine way to declare a line of attack closed. The conclusion was overdrawn. Results falling outside the supposed barrier had existed since two years after the barrier was announced, proved with nothing more exotic than simulation and diagonalization, sitting in a well-known journal, confirming an intuition everybody already had. They were not hidden. They were simply not looked at, because the framing made looking unnecessary.

The failure mode has a recognizable structure. First, an honest negative result about a technique. Second, a plausible generalization from that technique to "all known techniques." Third, the generalization becomes a screening rule that decides which problems get attention. Fourth, evidence against the rule accumulates in plain sight and is filed as artificial, contrived, or model-dependent — the vocabulary a paradigm uses to metabolize counterexamples without changing. What finally broke the pattern was not new evidence but evidence too spectacular to file away, at which point the older counterexamples were suddenly visible and had been all along.

For a programmer the transferable habit is to keep two questions separate: what has been proven impossible, and what the team has decided is impossible. The second set is always larger, drifts, and is maintained by nobody. When you hear that some property cannot be checked, some class of bug cannot be prevented, or some architecture cannot be made to work, the useful next question is what exactly was shown and under which assumptions — and whether the counterexample has been waiting in the codebase, dismissed as a special case. Beliefs of this kind are load-bearing in a way that beliefs about what *is* possible are not, because nobody stress-tests them: a wrong optimistic belief gets refuted by the first attempt, while a wrong pessimistic one prevents the attempt that would refute it.

Worth copying too is the move this work actually makes. Rather than adding another result on top of the paradigm, it goes back and audits whether the standard telling of the story was ever accurate. Periodically re-deriving why you believe a foundational constraint, instead of citing the person who cited the person who proved something adjacent, is cheap and occasionally recovers years.

**Source:** [Relativization: A Revisionistic Retrospective](../works/relativization-a-revisionistic-retrospective.md) — the retrospective's central argument, particularly the revisionist section observing that a well-known 1977 separation of time-bounded from space-bounded computation already failed to relativize, was proved by ordinary techniques, and was never treated as a challenge to the prevailing principle.
