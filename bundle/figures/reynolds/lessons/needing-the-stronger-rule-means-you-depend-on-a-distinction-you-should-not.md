---
type: lesson
title: "A rule sound for several readings proves only what they agree on, and needing the stronger one is a warning"
figure: reynolds
works: [the-craft-of-programming]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# A rule sound for several readings proves only what they agree on, and needing the stronger one is a warning

**Lesson:** A reasoning principle that stays valid under more than one possible interpretation of a construct is, by that very fact, incapable of proving anything the interpretations disagree about. This is not a defect to be patched but a property to be exploited. If your rule is sound for both readings of some under-specified feature, then every program you can verify with it behaves the same way under both — which means the verification is portable across implementations, across compiler versions, across whichever reading the next maintainer assumes. You have bought insensitivity to a question you would rather not have to answer.

The corollary is the useful part. When a program cannot be handled by the shared rule and demands a stronger one tied to a single interpretation, that failure is a signal about the program. It is telling you that the program's behaviour actually depends on the disputed point — that it distinguishes the readings — and therefore that anyone reading it has to know which reading is in force before they can say what it does. The rule was not too weak; the program was too clever. And the stronger rule needed to cope is invariably more complicated, with more parameters and more conditions, which is not a coincidence: the extra complexity of the reasoning is a direct measure of the extra difficulty a human reader faces.

So run the two-rule setup deliberately. Keep the weak, interpretation-independent principle as the default and use it wherever it suffices. Keep the strong one available, because occasionally the distinguishing behaviour is genuinely wanted. But treat every appeal to the strong one as a code review finding rather than a proof step, and let the size of the gap between the two rules be your estimate of how much comprehension the construct in question is costing. A pattern that only the complicated rule can justify — a loop whose body moves its own bounds, say — is one you should be looking for an excuse to rewrite.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 4.1.3, which exhibits a for statement whose body changes its own upper bound and behaves completely differently under the call-by-name and call-by-value variants, shows that the specification which is universal for the call-by-value variant cannot be proved by the earlier rule because an unsatisfiable non-interference assumption would appear in the conclusion, explains that this is because the earlier rule is valid for both variants and therefore cannot be used to reason about programs whose behaviour differs between them, gives the stronger variant-specific rule, notes that the earlier rule is derivable from it, and observes that the stronger rule's greater complexity directly mirrors the fact that for statements which alter their bounds are unnecessarily difficult to understand.
