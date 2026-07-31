---
type: lesson
title: "When the general completeness question is closed, find the narrow one you actually need"
figure: scott
works: [a-type-theoretical-alternative-to-iswim-cuch-owhy]
axes: [verifiability, expressiveness]
subdomains: [foundations-of-computation, formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# When the general completeness question is closed, find the narrow one you actually need

**Lesson:** Having built a set of rules and a semantics for them, the natural question is whether the rules can derive everything true. For any system strong enough to be interesting the answer is no, and the reason is worth internalizing rather than lamenting: derivable statements are enumerable by construction, true ones are not, and a system becomes strong precisely by pinning down a structure rich enough to make its truths inaccessible to enumeration. Incompleteness is thus a symptom of having succeeded at something else. The mistake is to treat the negative answer as a verdict on the system, when what it actually establishes is that "complete" was the wrong thing to have asked for.

The productive move is to replace the closed question with the strongest open one. Notice first which direction was never in doubt: rules that were each checked against the semantics cannot produce a false conclusion, so soundness is already in hand and no diagonal argument threatens it. What remains is the converse restricted to the cases you care about — not "is every truth derivable" but "whenever the semantics says a concrete computation has an answer, do the rules always find it?" That version is not obviously impossible, it is what an implementer actually needs, and it converts an abstract foundational worry into a question about whether reduction terminates on the inputs where a value exists.

Underneath this is a structural point about why the narrow question can be asked at all. A system given only by rewriting rules has no standard external to itself, so there is nothing for its rules to be adequate *to*; you take the rules on faith and inadequacy is not even expressible. The independent semantics is what creates the gap between "what the rules derive" and "what holds," and that gap is what makes both soundness and any form of completeness into claims with content. So the payoff of doing the semantic work is not only that you can trust the rules — it is that when the maximal question turns out to be unanswerable you still have a well-posed hierarchy of weaker ones to fall back through, instead of nothing.

**Source:** [A Type-Theoretical Alternative to ISWIM, CUCH, OWHY](../works/a-type-theoretical-alternative-to-iswim-cuch-owhy.md) — Section 4, which proves valid assertions non-enumerable via equations between primitive recursive functions, refuses to treat that as cause for despair on the grounds that the system's strength is what produced it, and then poses the restricted question of completeness for numerical equations, observing that the reduction rules can never give a wrong answer and that this question cannot even be asked of a calculus with no semantics to be adequate to.
