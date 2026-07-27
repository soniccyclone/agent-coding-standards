---
type: lesson
title: "If you cannot explain a feature without inventing a machine to run it, the feature is costing more than it looks"
figure: floyd
works: [assigning-meanings-to-programs]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# If you cannot explain a feature without inventing a machine to run it, the feature is costing more than it looks

**Lesson:** Some constructs can be given a rule of reasoning directly, in terms of the claims they carry from input to output. Others resist, and the only way to pin them down is to postulate an execution mechanism, an evaluation stack say, expand the construct into a sequence of primitive operations on that mechanism, and reason about the expansion. When that happens, something has been revealed rather than merely solved. The construct's behavior was never expressible in terms of the values of program variables alone; it depended on machinery the language pretends not to have, and the expansion is the bill arriving.

The constructs that force this are recognizable. Expressions that assign as a side effect of being evaluated are the clean example: their result depends on when each subexpression was evaluated relative to the others, so no rule phrased purely over variable values can be adequate, and the expansion has to make evaluation order explicit by naming an intermediate store. Scoping constructs and procedure mechanisms with several parameter conventions push in the same direction, which is why an honest account of them turns into a description of an implementation rather than a rule of inference. The apparent economy of such features is an illusion: they add no expressive reach that a couple of explicit statements do not already have, and in exchange they inject a hidden mechanism into every argument anyone will ever make about code that uses them.

This gives a usable design test that costs nothing to apply. Before adding a construct, try to state what a reader is entitled to conclude after it, using only names the language already exposes. If you cannot do it without introducing apparatus that programmers are supposed to be shielded from, you are not adding a convenience, you are adding a state variable to every reader's working memory. The test cuts across eras and paradigms: implicit context, ambient mutable state, evaluation-order-sensitive operators, and inheritance chains that resolve at runtime all fail it the same way.

The practical corollary is that desugaring is diagnostic, not just an implementation technique. Being able to mechanically rewrite a fancy construct into explicit primitive steps proves the construct adds no power, and the size and awkwardness of the rewrite measures what it costs in reasoning. A programmer who applies this reaches for the explicit version by default and pays for sugar only when the rewrite is small.

**Source:** [Assigning Meanings to Programs](../works/assigning-meanings-to-programs.md) — the treatment of extended assignment statements with embedded assignments, where a stack-equipped processor has to be introduced reluctantly and the statement expanded into explicit stack operations before its rule can be given, alongside the admission that block structure and procedure statements are only sketched because their real complexities exceed the method as presented.
