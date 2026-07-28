---
type: lesson
title: "Write the form you can prove, then transform it into the form that runs — they are different artifacts of one algorithm"
figure: knuth
works: [fast-pattern-matching-in-strings]
axes: [verifiability, hardware-affinity]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Write the form you can prove, then transform it into the form that runs — they are different artifacts of one algorithm

**Lesson:** The paper presents the matcher twice. The first version is short, and the authors state its loop invariant and argue its correctness from that invariant in a couple of paragraphs — including the part that is easy to get wrong, namely why the shift table is defined the way it is and why applying it preserves the invariant. Then the next section opens by admitting that this provable version is not the version you would ship, and that it might not even beat the naive approach on realistic input. What follows is a sequence of changes: peel the first pattern position out as a special case, since with a large alphabet the overwhelmingly common event is failing immediately and the general machinery handles that clumsily; then eliminate the end-of-input and end-of-pattern tests by planting impossible characters just past both ends, so the conditions that used to be checked every iteration are now enforced by the data itself; and finally, for the short patterns a text editor actually sees, abandon the table entirely and emit straight-line code with the shift decisions baked into its jump targets.

Two things make this a methodological lesson rather than a list of micro-optimizations. First, the ordering is deliberate and Knuth points at the literature on mechanical program transformation while making it: you establish correctness on the representation where the argument is short, and you reach the fast representation by steps that are individually small enough to be checked or automated, so the proof is not re-litigated at the end. The alternative — writing the optimized version first and then trying to verify it — means proving something about code whose invariants have been deliberately smeared into sentinels, special cases and jump tables. Nobody does that successfully.

Second, look at what the transformations actually are. Every one of them moves a decision from run time to some earlier time or to a different representation. A test on every character becomes a property of the data layout. A table lookup in a loop becomes a position in the instruction stream. The shift logic, which began as arithmetic on an index, ends up as the control-flow graph of a compiled routine. That is the same idea applied at successive levels, and it is the general shape of making something fast on real hardware: not doing less work in the abstract, but arranging for the work to have already been done by the structure the program is written in.

The habit this recommends is to treat the readable, verifiable version as a permanent artifact rather than a draft that gets overwritten. You keep it, you prove things about it, and the optimized version is understood as its image under a chain of transformations you can name. When the optimized version misbehaves, the question is which transformation was invalid — a much smaller question than what is wrong with this code.

**Source:** [Fast Pattern Matching in Strings](../works/fast-pattern-matching-in-strings.md) — the transition from the programming section, where the invariant-based correctness argument is given, to the efficiency section, which concedes the provable form is not competitive and then derives faster forms via special-casing, sentinel characters, and compiling the pattern into machine code with the shift table implicit in the control flow.
