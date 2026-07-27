---
type: lesson
title: "Settle performance by measurement, using an instrument built out of the system rather than bolted onto it"
figure: goldberg
works: [smalltalk-80-the-interactive-programming-environment]
axes: [hardware-affinity, cognitive-load]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Settle performance by measurement, using an instrument built out of the system rather than bolted onto it

**Lesson:** This book puts performance work in a strict order and a strict register. The order: first establish that the thing computes the right answer, by looking at the state of the objects involved, and only then ask a separate question — of the total time, what fraction went where. The register: that second question is answered by measurement, never by reasoning about which code looks expensive. In a system with uniform dispatch and layers of derived definitions, intuition about cost is close to worthless, because the operation you wrote may bottom out in something several levels down that you never named. The measurement offered is a sampling one: execution is interrupted repeatedly and the currently-executing operation noted, so the result is a distribution over what was actually running rather than a count of what was called.

What makes the design instructive is the shape of the answer, not just its existence. The result is presented as a nesting of operations with a share of total time attached at each level, which lets you follow the cost down from the expression you invoked to the specific operation that consumed it — and this book's worked example lands exactly where nobody would have guessed from the source, in a string comparison and its machine-level part, reached through a sorted-collection construction. Alongside the tree, the same data is presented flattened, gathering the many scattered appearances of one operation into a single figure; the reason given is that an operation spread thinly across a call structure looks negligible everywhere and can be dominant in total. Those are two genuinely different views of the same measurement, and needing both is a general fact about profiling rather than a quirk of this system.

The other half of the lesson is that the instrument is an ordinary part of the system. You hand a piece of deferred computation to an object and ask it to be watched; the result appears in an ordinary editable text area. There is no separate build, no instrumented variant of the program, no external tool with its own model of what your program is. That matters beyond convenience: an instrument made of the same material measures the thing you actually run, and it can be extended, redirected, or specialized by the same means as anything else. Also worth noting is the epistemic caution attached — the book says plainly that repeating the measurement gives somewhat different numbers, because sampling is statistical. An instrument that reports its own imprecision is teaching you not to over-read small differences.

A programmer who works this way refuses to accept a performance claim without a measurement, and refuses to accept a measurement without knowing whether it is a sample or a count. Practically: get it right, measure it, follow the nesting down to the leaf, check the flattened view for the cost hiding in a hundred places, then change exactly that.

**Source:** [Smalltalk-80: The Interactive Programming Environment](../works/smalltalk-80-the-interactive-programming-environment.md) — the performance chapter, which separates verifying correctness by inspecting object state from asking where time is spent, introduces the sampling analyzer applied to a deferred piece of code, explains the nested percentage tree and the separate flattened summary of low-level operations, and warns that repeated runs will differ because the sampling is statistical.
