---
type: lesson
title: "A correctness method that hands back a failing trace gets adopted; one that only ever says yes does not"
figure: emerson
works: [model-checking-algorithmic-verification-and-debugging]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# A correctness method that hands back a failing trace gets adopted; one that only ever says yes does not

**Lesson:** Verification is sold on the promise of proving systems correct, and that framing mispredicts which techniques get used. Almost every system under development is wrong, so the overwhelmingly common outcome of any check is failure. What determines whether engineers keep running the check is therefore not the quality of its affirmative answer but the quality of its negative one. A method that returns a concrete execution leading to the violation has produced something immediately actionable; a method that returns only a stuck proof attempt has produced work. Some teams adopt exhaustive state-space checking purely for the traces and never care about the verification claim at all, which is a fact about incentives that any tool builder should take seriously.

The second adoption factor is organizational rather than technical. A methodology where correctness argument and construction advance together is intellectually attractive, and it couples the two activities so tightly that neither can be automated or staffed independently. Checking a finished artifact against a separately written specification decouples them: implementation proceeds, verification proceeds alongside, defects come back as traces, and when the deadline arrives the system ships at whatever level of assurance has accumulated. That is not as satisfying as correctness by construction, and it is the property that let the technique into industry. Graceful partial adoption beats an all-or-nothing discipline, because partial adoption is the only kind that survives contact with a schedule.

The transferable rule is to judge a verification or analysis tool by its behavior on the failing case, and to design for it. Whatever you build that checks a property — a type system, a linter, a property-based test harness, a runtime assertion, a schema validator — the interface that matters is the one presented when the property does not hold. Producing a minimal reproducing input beats producing a category label; a trace beats a location; a location beats a boolean. And the deployment story matters as much as the analysis: a check that can be adopted incrementally by one team while the rest of the organization ignores it will spread, and one that requires everyone to change how they work will not.

**Source:** [Model Checking: Algorithmic Verification and Debugging](../works/model-checking-algorithmic-verification-and-debugging.md) — Emerson's account of what made the method succeed where deductive verification adopted slowly, and Clarke's opening section on model checker components, where the counterexample-producing feature is called out as the one whose importance cannot be overstated and is dated to a specific later addition to an early tool that lacked it.
