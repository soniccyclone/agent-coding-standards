---
type: lesson
title: "Narrowing a specification to well-behaved inputs buys nothing until you show the hard inputs cannot be smuggled in"
figure: valiant
works: [np-is-as-easy-as-detecting-unique-solutions]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Narrowing a specification to well-behaved inputs buys nothing until you show the hard inputs cannot be smuggled in

**Lesson:** A standard move when a component looks too hard to build is to shrink its contract: promise correct behavior only on inputs of a restricted, well-behaved shape, and let the answer be anything at all on the rest — while still requiring the thing to terminate. This feels like a large concession extracted from the problem, and sometimes it is. But it is only a real concession if the restricted shape actually excludes the instances that made the problem hard. The trap is that the restriction is stated in terms of a property of the input, and a caller can often manufacture inputs with that property out of arbitrary ones. When that manufacturing step is cheap, the narrowed component is a full solution to the general problem wearing a disguise, and the difficulty you thought you had dodged reappears intact behind the caller.

The instructive case is a promise that the input has exactly one witness. Instances with many witnesses look like the source of the trouble; a procedure that need only work when the answer is unique looks dramatically weaker. It is not, because from an arbitrary instance one can cheaply produce a family of derived instances in which uniqueness is likely, hand those to the restricted procedure, and check its output against the original. The check is the crucial ingredient: the caller cannot tell whether the promise held, but it can verify the answer, so wrong answers on off-promise inputs are harmless noise rather than corruption. What kills the concession is the conjunction of cheap manufacture and cheap verification.

So the discipline is to state the narrowing as a claim about the *closure* of your input class under things callers can do, not as a claim about the class itself. Two questions settle it. Can a general input be pushed into the promised class by work you consider cheap? And can the caller check the result without trusting the promise? If both are yes, the narrowing is cosmetic and you should look for a different weakening — one that gives up accuracy, or coverage, or a resource bound, rather than domain. The same test applies to the everyday version of this move: a function that documents preconditions its callers can trivially satisfy from arbitrary data has not simplified anything; it has only relocated the difficulty into every call site, or hidden it behind an assumption nobody is enforcing.

**Source:** [NP Is as Easy as Detecting Unique Solutions](../works/np-is-as-easy-as-detecting-unique-solutions.md) — the introduction's formulation of the promise problem, where a procedure need only answer correctly when the instance has a single solution and may output anything otherwise provided it halts, together with the corollary showing that solving that relaxed problem is as hard as the unrestricted one because the caller can verify a returned candidate itself.
