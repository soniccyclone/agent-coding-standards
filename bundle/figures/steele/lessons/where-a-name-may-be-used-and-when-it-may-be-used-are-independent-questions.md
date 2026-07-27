---
type: lesson
title: "Where a name may be used and when it may be used are independent questions, and most confusion comes from treating them as one"
figure: steele
works: [common-lisp-the-language-2nd-edition]
axes: [cognitive-load, verifiability, expressiveness]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Where a name may be used and when it may be used are independent questions, and most confusion comes from treating them as one

**Lesson:** Before this specification describes a single binding construct, it factors the notion of "visibility" into two orthogonal dimensions and gives them separate names: the region of program text from which a reference may be written, and the interval of execution time during which a reference may succeed. Once the two are separated, they can be varied independently, and the four resulting combinations turn out to describe things that are genuinely different rather than variants of one idea. A local variable is restricted in text but unrestricted in time — its binding outlives the construct that made it, which is exactly what a closure is. A dynamically bound variable is the mirror image: writable from anywhere, but only meaningful while the binding is live. An escape point out of a block is restricted in *both*, which is why it can be captured lexically and still be dead by the time you invoke it. Most data objects are restricted in neither.

The payoff of the factoring is diagnostic power. The specification works through two examples that look nearly identical and behave completely differently, and shows that the difference is entirely attributable to one construct having textual restriction with unlimited lifetime while the other has textual restriction with bounded lifetime. Reasoning about either example without the two-axis vocabulary requires holding a great deal of operational detail in your head at once; with it, each case reduces to reading off two independent properties. The specification also uses the factoring to explain why textual scoping is what makes reasoning about interleaved recursive calls tractable at all: because a textually scoped construct effectively mints a fresh entity per execution, a name captured in one activation cannot be accidentally shadowed by a later one — the reference is fixed by where it was written, not by which activation happens to be innermost when it fires. It is honest about the limits of its own vocabulary too, noting that the traditional composite term for the anywhere-but-briefly combination is a misnomer that it keeps only because everyone uses it.

Why the split holds generally is that the two axes are answering questions with different kinds of answer. Textual reach is decidable by reading the program; temporal reach is a fact about an execution. Any mechanism that conflates them will be correct only where the two happen to coincide, and will fail silently where they diverge — which is precisely at closures, at resources with cleanup, and at non-local exits.

A programmer who thinks in these two axes stops asking "is this in scope?" and starts asking two questions: can this text legally mention the name, and is the thing the name denotes still alive. Applied outside language semantics, the same split cleanly separates the shape of a module's public surface from the lifetime of the resources it hands out — and makes it obvious that an API which is visible everywhere but whose handles are only valid inside one call is a completely different animal from one whose handles outlive the call that made them, even though both are usually described as "public".

**Source:** [Common Lisp the Language, 2nd Edition](../works/common-lisp-the-language-2nd-edition.md) — the chapter that introduces scope and extent as separate notions and enumerates their useful combinations, together with its two paired examples of a captured escape point used inside and outside its lifetime.
