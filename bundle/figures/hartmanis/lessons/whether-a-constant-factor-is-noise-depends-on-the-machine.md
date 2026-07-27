---
type: lesson
title: "Whether a constant factor is noise is a fact about your machine model, not about computation"
figure: hartmanis
works: [computational-complexity-of-random-access-stored-program-machines, on-the-computational-complexity-of-algorithms]
axes: [hardware-affinity, primitive-count]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# Whether a constant factor is noise is a fact about your machine model, not about computation

**Lesson:** The comfortable habit of discarding constant factors rests on a theorem, and theorems have hypotheses. On a tape machine you can always fold pairs of steps into single richer steps, so any constant speedup is available for free and a cost measure that noticed constants would be measuring your choice of alphabet. Move to a model organized like an actual computer — registers holding unbounded values, addressing through those values, a program living in the same memory it operates on — and the folding trick dies. Each instruction can enlarge the value in the accumulator by only so much, so a function whose answer is enormous relative to its input has a floor on its step count that no re-encoding lowers. In that model there are computations, at every level of difficulty, whose best program cannot be beaten by even a hair's worth of constant factor. The classical constant-factor freedom was never a truth about computation; it was a truth about a formalism that lets you buy width for time.

That is the general shape worth carrying: every "this doesn't matter asymptotically" claim is really "in this model, this can be simulated away with bounded overhead," and the moment you change the model you owe the argument again. Modern practice quietly relies on the tape-machine intuition — treat the constant as slack to be recovered by tuning, batching, wider words, a faster machine — while running on hardware with unbounded-magnitude arithmetic, indirect addressing, and code that can be generated at runtime. Sometimes the slack really is there. Sometimes there is a genuine floor, and the effort spent hunting for a constant-factor win is spent hunting for something the model provably does not contain.

A programmer who takes this seriously asks, before conceding a factor as unimportant, what mechanism would recover it. If the answer is a concrete transformation with bounded per-step cost, the factor is genuinely noise. If the answer is a vague appeal to optimization, the honest position is that the constant may be structural. This also reverses a common instinct: the model that looks more realistic is not automatically the more forgiving one to reason in. It has fewer symmetries, so fewer things are free, and its bounds are correspondingly tighter and more informative — sharper statements than the tape-machine setting could supply, precisely because you cannot cheat by re-encoding.

**Source:** [Computational Complexity of Random Access Stored Program Machines](../works/computational-complexity-of-random-access-stored-program-machines.md) — the section building programs whose running time admits no multiplicative improvement, explicitly contrasted there with the constant-factor speedup available for time-, tape-, and reversal-bounded Turing machine computations established in [On the Computational Complexity of Algorithms](../works/on-the-computational-complexity-of-algorithms.md).
