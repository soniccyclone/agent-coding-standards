---
type: lesson
title: "Any operation whose misuse escapes into implementation-dependent behavior destroys reasoning everywhere, not just at the fault"
figure: dahl
works: [class-and-subclass-declarations, simula-67-common-base-language]
axes: [verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Any operation whose misuse escapes into implementation-dependent behavior destroys reasoning everywhere, not just at the fault

**Lesson:** A meaningless data reference is not just an error; it is an error whose consequences cannot be described in the language in which the program was written. Once a mistaken access can produce whatever the underlying machine happens to do, no argument conducted in the language's own terms is sound any more, because the argument's premises were about the language and the behavior came from somewhere else. This is the reason such faults are so expensive to chase: the evidence is in a vocabulary the program does not have, and the search for a cause has no principled place to start. The property to demand of a design, then, is closure — every reachable behavior of every construct must be explicable within the system's own semantics.

Achieving closure is a whole-design commitment, not a check bolted on at the end. Storage has to be reclaimed automatically, because manual deallocation is precisely the operation that manufactures references to things that no longer exist. The operations on references have to be restricted to storing and fetching, with new reference values arising only from allocation, so no arithmetic can synthesize a pointer to nothing in particular. What remains is the interpretation problem: naming an attribute through a reference is meaningful only if the referenced thing actually has that attribute. So references carry a declared class, most of the checking lands at compile time, and where static knowledge genuinely runs out the programmer is compelled by the syntax to discriminate on the actual class before any access is legal. Each piece exists to close off a different route by which behavior could leak outside the language.

A programmer who takes this seriously stops treating undefined behavior as a performance concession and starts treating it as a hole in the specification through which all confidence drains. The practical form of the belief is that unsafe constructs must be either eliminated or made syntactically impossible to use without a check, that the check should be pushed to compile time wherever the type structure permits it, and that the residue should trap loudly at run time rather than continue into a state nobody can characterize. The debugging cost of a system is largely set by how much of its behavior it can explain about itself.

**Source:** [Class and Subclass Declarations](../works/class-and-subclass-declarations.md) — the opening argument that the effects of meaningless references cannot be determined by reasoning inside the programming language, and the requirements it derives for automatic deallocation, restricted pointer operations, and checked attribute access. Also [SIMULA 67 Common Base Language](../works/simula-67-common-base-language.md) — the introduction's third requirement on a language for complex programs, stating reference security as a means of reducing debugging cost, and the qualification rules that implement it.
