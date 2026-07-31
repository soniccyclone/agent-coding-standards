---
type: lesson
title: "If safety demands a check at every use, redesign the notation so the fact is established once and carried by scope"
figure: hoare
works: [notes-on-data-structuring]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# If safety demands a check at every use, redesign the notation so the fact is established once and carried by scope

**Lesson:** When an operation is only meaningful under a condition that cannot be settled from the text, the reflexive fix is to test the condition at every point of use. That fix is bad on both counts that matter. It is expensive, since the same question gets re-asked at each access even though the answer cannot have changed. And it fails late: the check that fires is at the deepest point of a computation, far from anywhere the mistake could be repaired, which is why a diagnostic of this kind arrives at the least convenient possible moment. The better response treats the repeated check as evidence that the notation is wrong rather than as a cost of doing business.

The repair is to invent a construct that binds the discrimination to the region where its outcome is used. Ask the question once, and let the answer hold over a delimited body of text in which the corresponding operations are simply available, unqualified, with no further testing. Inside that region the fact is not rechecked because it cannot fail; outside it, the operations are not offered at all. What was a runtime property becomes a scoping property, so a reader — and equally a compiler — establishes it by looking at where the code sits rather than by tracing values. The condition of validity is worth stating explicitly: this works only while the thing being discriminated does not change under you, which is why the construct has to name what it is holding fixed rather than leaving that implicit.

The move generalizes well past type discrimination. Any time you find guards multiplying — a null test before each dereference, a permission check on each call, a state assertion at the top of every method of an object — the shape is the same, and the same remedy applies: find the point where the fact is first established, and make that point introduce a scope in which the fact is a standing assumption. What you gain is not merely fewer instructions. You gain the ability to say where a property comes from and how far it reaches, which is exactly the information that repeated defensive checks destroy by making every site look independently suspicious.

**Source:** [Notes on Data Structuring](../works/notes-on-data-structuring.md) — the manipulation section of the chapter on discriminated unions, which observes that converting a value back to the wrong constituent type can only be caught by a costly and badly-timed runtime test on the tag, and therefore proposes a combined discrimination-and-scope construct in which each limb may use the selectors of its own alternative directly, guaranteed safe by textual inspection alone provided the discriminated value is not altered within the limb.
