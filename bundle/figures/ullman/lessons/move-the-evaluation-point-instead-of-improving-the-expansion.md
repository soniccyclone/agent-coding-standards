---
type: lesson
title: "Move the evaluation point instead of improving the expansion"
figure: ullman
works: [mining-of-massive-datasets]
axes: [cognitive-load, verifiability]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Move the evaluation point instead of improving the expansion

**Lesson:** Convergence is a yes-or-no property of a series and it tells you almost nothing about whether you can use one. What you actually need is a rate: how many terms buy you the accuracy you want. And the rate is not a fixed attribute of the expansion — it is a function of where in the parameter space you evaluate it. The same series can need three terms at one argument and thousands at another while being perfectly convergent at both. So the question "does this converge" is the wrong gate. The question is "how many terms at the arguments I will actually pass it," and that question has a different and much better answer available than truncating harder.

The better answer is to move the argument. Before expanding anything, look for an algebraic identity that transports the evaluation from wherever the caller put it into the region where the expansion is short, evaluate there, and transform the result back. This is the standard structure behind range reduction in every serious numerical routine, and it is worth recognizing as a general tactic rather than a numerical-analysis specialty: when a method's cost depends on where you apply it, relocating the application is usually cheaper than strengthening the method. The reflex most people have — accept the argument as given and go looking for a better-converging series — attacks the term that was never the problem.

The rewrite frequently pays a second time. Massaging an expression until it exhibits a limit form you already know does not just put you in the fast regime; it often hands you a closed-form approximation outright, so the expansion becomes unnecessary. Reparameterizing a quantity raised to a large power until the base has the shape of a known limiting sequence collapses it to a single exponential, and now you have a formula you can reason about symbolically — take its derivative, see how it responds to each parameter, use it inside a proof — rather than a numerical procedure you can only run. That is a substantial upgrade in what you can do with the result, obtained from the same manipulation that was supposed to be about convergence speed.

The habit generalizes past mathematics to anything whose cost varies over its input domain: iterative solvers that converge quickly near a good starting point, compressors that do well on data with the right local structure, caches that behave differently under different access orders, search procedures that are fast in one coordinate system and hopeless in another. In each case there are two knobs, the method and the point at which it is applied, and the second is systematically underused because the input arrives looking like a fact rather than a choice. Ask whether an exact transformation exists that lands you somewhere the existing method is already good. That is usually less work than a new method and it does not cost you accuracy, because the transformation is an identity.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 1's section on the base of natural logarithms, which observes that the Taylor expansion of the exponential converges slowly for large arguments despite converging for all of them and rapidly for small ones where only a few terms are needed, and which rewrites a quantity of the form one-plus-a-small-number raised to a large power by substituting until the expression contains the classic limit definition of e, thereby producing a closed-form approximation valid for small positive and negative perturbations alike.
