---
type: lesson
title: "State the perspective you need before you name the person, and let missing knowledge be a qualification"
figure: parnas
works: [active-design-reviews-principles-and-practices]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# State the perspective you need before you name the person, and let missing knowledge be a qualification

**Lesson:** The usual order is backwards. You look around at who is available, hand them the design, and hope their combined attention happens to cover it. That yields whatever coverage the org chart produces — which is why the same blind spots survive review after review. Reverse it: work out from the design itself which distinct viewpoints could possibly detect its distinct failure modes, write each viewpoint down as a set of required characteristics, and only then go find a human who has them. The written characteristic is the artifact that matters; it turns "we reviewed it" into a claim you can audit, because you can now ask which named perspective was never staffed.

The counterintuitive consequence is that ignorance can be a hiring criterion. A reviewer checking whether a component's stated assumptions are sufficient to implement its stated operations should be someone who cannot silently supply the missing assumption from their own head. Domain expertise is exactly what corrupts that check: an expert fills gaps unconsciously and reports no problem, because for them there was none. So the person who knows the application but not this particular device is the right one to ask "which stated assumption tells you this is implementable?" Their unfamiliarity is what makes the answer informative. Meanwhile the deep specialist is the only one who can judge whether an assumption will still hold for the thing that replaces the current hardware next year — a question no amount of logical rigor answers.

A designer who takes this seriously stops thinking of review as a quantity of eyeballs and starts thinking of it as a set of independent detectors, each with a documented sensitivity and blind spot. Coverage becomes a property you can reason about before the review happens rather than a hope you evaluate after. It also protects reviewers: someone asked to assess an entire system will default to the aspects they feel safe on and stay quiet elsewhere, whereas someone handed one question inside their competence has nowhere to hide and no reason to feel exposed.

**Source:** [Active Design Reviews: Principles and Practices](../works/active-design-reviews-principles-and-practices.md) — lives in the sections on identifying review types and classifying reviewers, including the tabulated match between each review's purpose and the expertise it demands, and the remark that a reviewer's lack of device-specific knowledge can be an advantage for consistency checking.
