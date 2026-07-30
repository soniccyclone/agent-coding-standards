---
type: lesson
title: "A closed claim admits no degrees: an invariant with a known exception is false, and the exception belongs inside the statement"
figure: church
works: [introduction-to-mathematical-logic]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# A closed claim admits no degrees: an invariant with a known exception is false, and the exception belongs inside the statement

Church works through a universally quantified arithmetic statement that fails for exactly one value, notes that a single counterexample suffices to make it false, and then adds a warning aimed squarely at the reader's instinct to soften the verdict. Do not say the statement is nearly always true, or true with one exception, or anything of that shape. Those descriptions are appropriate to the open form — the expression with a free variable, which genuinely has a value that varies and is true for most assignments and false for one. They are not appropriate to the closed statement, which has no free variable left to vary and about which there is exactly one thing to say. Once you quantify, you have committed to a claim with two possible values, and the fact that the underlying form was mostly true is no longer part of what you said.

The precision here is about which object carries the qualification. The open form and the closed statement are different things, and each supports a different vocabulary. Degrees, exceptions, frequencies, and typical cases are properties of the form — that is, of the family of instances. Truth is a property of the statement. Speaking as if a statement could be almost true is silently substituting the form's profile for the statement's value, and the substitution hides precisely the case that matters: the one where it fails.

The engineering translation is unforgiving and worth stating flatly. An invariant that holds except in one situation is not an invariant. A postcondition that holds unless the cache is cold does not hold. A function documented as returning a sorted list, which returns an unsorted one on empty input or on ties or under concurrent modification, does not return a sorted list. In every case the honest repair is one of two moves, and neither is to describe the claim as mostly holding. Either narrow the claim until it is true — state the precondition that excludes the failing case, so that the exception is inside the statement rather than in a footnote about it — or weaken what is claimed until the failing case satisfies it too. Both produce something a caller can rely on. The softened description produces something a caller will rely on and be wrong to.

The reason this matters more than it sounds is compositional. Callers do not consume your prose; they consume the claim, and they chain it with other claims. A statement that is true carries through composition; a statement that is nearly true carries nothing, because the composed argument breaks wherever the exception lives and there is no way to see from the outside where that is. Which is why the sentence "this always holds, apart from the case where" should be read as an admission that a precondition has been discovered and not yet written down. The work is not to hedge it. The work is to move it inside.

**Source:** [Introduction to Mathematical Logic](../works/introduction-to-mathematical-logic.md) — the section on operators and quantifiers, and its warning against describing a universally quantified statement falsified by a single value as nearly always true or true with one exception, on the ground that such descriptions apply to the open form rather than to the closed statement.
