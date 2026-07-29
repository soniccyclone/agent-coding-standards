---
type: lesson
title: "Whatever dimension your metric leaves out is the dimension your design will quietly spend"
figure: ungar
works: [design-and-evaluation-of-a-high-performance-smalltalk-system]
axes: [hardware-affinity, verifiability]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Whatever dimension your metric leaves out is the dimension your design will quietly spend

**Lesson:** Every measurement scheme fixes some quantities and ignores others, and design decisions flow toward whatever the scheme ignores. Count only the steps a computation takes and you will accumulate features that reduce steps while lengthening the interval each step requires, until the product gets worse while your numbers get better. Model only the component you are building and you will happily push work across its boundary into the parts you did not model, where it becomes someone else's measurement problem and, eventually, the user's. Neither failure requires anyone to be careless. Both follow mechanically from optimizing against an incomplete accounting, and both are invisible from inside the accounting that caused them.

The failure mode is worth recognizing by its signature: a feature that looks free in the model and is expensive in reality. The most painful version is a component-level win whose cost lands entirely in an interface — the piece performs beautifully in isolation, and the surrounding system cannot keep up with what it now demands, so the effective speed is set by a boundary nobody simulated. That kind of defect is found late, after fabrication or deployment, because the model that would have shown it was never built. The correction is not more precision inside the component model; it is extending the model outward until it closes over the thing you actually care about, even at the cost of much cruder detail.

Practically: name, in writing, the dimensions your evaluation does not capture, and treat every result as conditional on them. When a proposal trades into an unmeasured dimension, that is the moment to extend the measurement rather than accept the result. Prefer an end-to-end model that includes the interfaces over a detailed model of one part, because the crude whole-system number is the one that can be wrong in the direction that matters. And when you do report incomplete results, say so plainly — an evaluation that states which effects it ignores is far more useful than one that quietly presents a partial figure as the answer.

**Source:** [The Design and Evaluation of a High-Performance Smalltalk System](../works/design-and-evaluation-of-a-high-performance-smalltalk-system.md) — the repeated caveat that the feature evaluations count cycles while ignoring their effect on cycle duration, together with the fast-call mechanism whose interaction with the surrounding memory system degraded the delivered speed and which the text says would have been caught by simulating the whole system rather than the processor alone.
