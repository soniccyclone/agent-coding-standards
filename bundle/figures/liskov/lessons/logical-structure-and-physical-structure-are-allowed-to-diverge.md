---
type: lesson
title: "Let logical structure and physical structure diverge, and make the compiler own the gap"
figure: liskov
works: [programming-with-abstract-data-types]
axes: [hardware-affinity, expressiveness]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Let logical structure and physical structure diverge, and make the compiler own the gap

**Lesson:** The standard objection to fine-grained abstraction is that it costs
runtime: every access through an operation is a call, every layer is overhead,
so the structure that makes a program comprehensible is the structure that makes
it slow. The resolution is to stop treating these as the same structure. A
program has a logical shape, chosen for whoever has to understand and change
it, and a physical shape, chosen for the machine. They are allowed to differ.
Reconciling them is a translation job, and translation is what compilers are
for.

This only works if two things are arranged deliberately. The notation for
invoking an operation must be identical whether it compiles to a real call or
to inlined code, so the compiler can switch strategies without any source
edit — the decision is not visible in the program text and therefore is not the
programmer's decision to make prematurely. And the code implementing the
operations must be kept structurally separate from the per-object state, so
that the code is substitutable at the call site at all. Discipline elsewhere in
the design pays here too: with no free variables and only structured control
flow, the compiler can actually complete the flow analysis that lets it delete
redundant work — including checks inside an operation that the calling context
makes provably unnecessary. Good logical structure is what makes the machine
mapping tractable, not what obstructs it.

The gap does have a price, and the price is named rather than waved away.
Inlining across a module boundary means changing that module can force
recompiling its users, so speed is bought with modification cost. But that
trade is deferrable: pick it after measurement tells you which parts of the
system are hot, and pay it only there. A programmer holding this view does not
accept the efficiency argument against abstraction as a fact about abstraction —
they treat it as a claim about a particular compiler, and check whether the
tooling could close the gap before contorting the design. They also insist the
debugger and other tools present the logical structure, because a divergence
the tools do not hide is a divergence the programmer ends up paying for anyway.

**Source:** [Programming with Abstract Data Types](../works/programming-with-abstract-data-types.md) — the implementation-considerations discussion of efficiency, distinguishing a program's logical from its physical structure and assigning the mapping between them to an optimizing compiler, together with the two language properties that make cross-boundary inlining possible.
