---
type: lesson
title: "Price a feature by which closure property it breaks, and read your limits off the ones that remain"
figure: vardi
works: [on-the-expressive-power-of-datalog]
axes: [expressiveness, primitive-count, verifiability]
subdomains: [databases-and-data-management, programming-languages-and-semantics]
tags: [lesson]
---
# Price a feature by which closure property it breaks, and read your limits off the ones that remain

**Lesson:** Every restricted formalism preserves certain transformations of its input for free, as a structural consequence of what it is allowed to say. A positive recursive rule language, for instance, can only ever compute answers that survive growing the data, growing the universe, and merging two elements into one — because none of its constructs can notice anything disappearing or anything being distinguished. The moment you know that list, you have a test that costs nothing: take any task, ask whether it survives those transformations, and if it does not, no program in that language can ever compute it. No search, no lower-bound argument, no complexity assumption. Kolaitis and Vardi use this to dispose of whole families of tasks in a sentence.

The same list prices new features precisely. Adding the ability to state that two things differ removes exactly one item — invariance under merging elements — and leaves the others intact. So the gain in power is not a vague "more expressive"; it is the specific set of tasks that are sensitive to distinctness and insensitive to growth, and the loss is that you can no longer rely on merge-invariance when reasoning about programs. That is what a feature actually costs and buys, stated in terms you can check. Contrast the usual way features get argued about — convenience, familiarity, one motivating example — and the difference in rigour is stark.

The transferable habit has two halves. When you constrain a language, a DSL, a configuration format, or an API, write down the transformations of the input under which its results are invariant, because that list is simultaneously your optimization licence and your expressiveness ceiling. And when someone proposes an extension, ask which invariant it destroys before asking what it enables. Features that break no invariant are usually sugar; features that break one are the real decisions, and the invariant they break tells you which reasoning you are giving up in exchange.

**Source:** [On the Expressive Power of Datalog: Tools and a Case Study](../works/on-the-expressive-power-of-datalog.md) — the introduction's account of Datalog computing strongly monotone queries, preserved by adding tuples, adding universe elements, and identifying elements, so that any query lacking those preservations is immediately inexpressible; and the observation that permitting equalities and inequalities weakens strong monotonicity to plain monotonicity, which both explains the extension's added power and immediately rules out the complement of transitive closure. Also the closing note in the positive-results section that the homeomorphism programs depend crucially on inequalities, since those queries are not preserved under homomorphisms.
