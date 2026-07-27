---
type: lesson
title: "Push every check to where it costs nothing, and never promote your own suspicion into someone else's outage"
figure: torvalds
works: [linux-kernel-coding-style]
axes: [verifiability, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Push every check to where it costs nothing, and never promote your own suspicion into someone else's outage

**Lesson:** Two positions in this document look unrelated and turn out to be one idea about who does the checking and when. The first is an unreserved endorsement of assertions evaluated during compilation, justified purely by their price: they catch a whole class of mistake and cost nothing at execution time, so there is no trade-off to weigh. The second, developed at more length, is a deep suspicion of assertions that fire at execution time by killing the system. The reasoning is jurisdictional rather than technical. A component that sits at the bottom of the world has nobody to escalate to; when it aborts, it takes down whatever the machine was actually doing, and the person who cares about that loss is not the person who wrote the check. Whether a suspicious internal condition warrants losing the running workload is a judgment about stakes the author cannot see, so it belongs to the operator, who is given a switch to make warnings fatal if that is their preference. Having offered them that switch, the author owes them accuracy: a condition ordinary use can trigger must never be reported as impossible, and repeated noise about the same condition is itself a failure mode, since a flooded log destroys the evidence you were trying to preserve.

Between those poles sits the document's treatment of build-time configuration, which is the same principle applied to whether the compiler gets to look at your code at all. Textual exclusion by the preprocessor removes disabled code from the compiler's view entirely, so it rots undetected — nothing checks its syntax, its types, or whether the symbols it names still exist. The recommended alternative keeps the condition in the language proper, as an ordinary boolean the optimizer will fold away, producing identical output while leaving every branch under permanent scrutiny. Where exclusion genuinely is required, the discipline is to exclude whole named units rather than fragments of expressions, so that what is present and what is absent stays legible to a reader following the logic.

The unifying thought is that error detection has a cost curve across the lifecycle, and the curve is steep. A mistake caught while compiling is free and total: it is found for every configuration and every user, before anything is at risk. The same mistake caught while running is expensive, partial, and lands on somebody who did not choose to take that risk. So you spend effort moving checks leftward — into types, into compile-time assertions, into keeping conditional code compiled — and you become increasingly conservative as you move rightward, until at the far end you prefer to report and limp rather than to be decisive on someone else's behalf.

A programmer who believes this treats reaching for a runtime abort as an admission that they failed to find a compile-time formulation, and treats "I did not want to write the recovery path" as an unacceptable reason to abort. They also stop using the preprocessor as a variability mechanism, because code the compiler cannot see is code nobody is checking.

**Source:** [Linux Kernel Coding Style](../works/linux-kernel-coding-style.md) — the chapter on not crashing, which assigns the crash decision to the user, prefers warn-with-recovery over abort, insists warnings be reserved for genuinely impossible conditions and not repeated, and encourages compile-time assertions for costing nothing at runtime; plus the conditional-compilation chapter's preference for a compiler-visible boolean over preprocessor exclusion.
