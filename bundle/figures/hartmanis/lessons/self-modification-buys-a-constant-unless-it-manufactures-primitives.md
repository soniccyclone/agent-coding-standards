---
type: lesson
title: "Code that writes code buys a constant — unless it can manufacture primitives you did not have"
figure: hartmanis
works: [computational-complexity-of-random-access-stored-program-machines]
axes: [expressiveness, primitive-count, verifiability]
subdomains: [algorithms-and-complexity, programming-languages-and-semantics]
tags: [lesson]
---
# Code that writes code buys a constant — unless it can manufacture primitives you did not have

**Lesson:** A program that rewrites itself is genuinely faster than any program that cannot, and the size of that advantage is knowable rather than mystical. The mechanism is simple: a fixed program of bounded length has to keep coming back to a test or a branch, because a finite body of instructions can only run straight for so long, whereas a program that emits a fresh, longer straight-line body for each input pays the control-flow tax once instead of continually. That is the honest performance case for generated code, and it is real. But it is also capped. If the language can inspect and dissect its own instruction encodings at bounded cost, a fixed interpreter can drive a copy of any self-modifying program step by step, losing only a constant factor that depends on the instruction set and nothing else. Metaprogramming, in a language rich enough to interpret itself cheaply, is worth exactly one constant.

The exception is the interesting part. Remove the ability to operate on the contents of registers and leave only operations on literal constants, and now a program that assembles instructions is doing something no fixed program can approach: it is synthesizing operations that were not in its original vocabulary, and the gap between generated and fixed code becomes unbounded — worse than any growth rate you care to name. The unbounded win comes not from generating code but from generating *capability*. Framed that way it is less an achievement than a symptom that the base instruction set was impoverished, which is how the result is characterized in the work itself: a pathology rather than a technique.

This gives a sharp test for anything in the code-generation family — macros, JIT compilation, template expansion, runtime eval, dynamically built query plans. Ask whether the generation is producing something the ordinary machinery could have produced given a bounded interpretive overhead. If yes, you are buying a constant, and you should decide whether that constant is worth the price paid elsewhere. If the generated form does something the base language cannot express at all, you have discovered a missing primitive, and the right response is usually to add the primitive rather than to institutionalize the generator.

The price paid elsewhere is not small, and it is worth naming precisely. Whether a given program in such a system ever modifies itself is not decidable, so the property that most reasoning tools depend on — that the instructions you are looking at are the instructions that will execute — becomes an assumption rather than a fact. You can design the system so that the well-behaved programs form a recognizable set and still compute everything, but that has to be a deliberate restriction built in up front. Self-modification's constant-factor win is therefore paid for in analyzability, which is nearly always the worse end of the trade.

**Source:** [Computational Complexity of Random Access Stored Program Machines](../works/computational-complexity-of-random-access-stored-program-machines.md) — the section on self-modifying programs: the argument that a bounded-length fixed program must execute a conditional at bounded intervals, the simulation result capping the advantage at a constant once prefix-manipulation instructions exist, the unbounded-gap construction for a machine whose only additive operation takes a literal, and the remark that being a non-self-modifying program is an undecidable property.
