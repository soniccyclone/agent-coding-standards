---
type: lesson
title: "A dynamic phenomenon cannot be governed by a construct with lexical scope, and shipping one anyway is worse than shipping nothing"
figure: steele
works: [the-revised-report-on-scheme]
axes: [verifiability, parallelizability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, programming-languages-and-semantics]
tags: [lesson]
---
# A dynamic phenomenon cannot be governed by a construct with lexical scope, and shipping one anyway is worse than shipping nothing

**Lesson:** The report contains a retraction that teaches more than most designs do. An earlier version of the language had offered a way to mark a region of program text as uninterruptible, and the report withdraws it, giving a diagnosis rather than an apology: the extent of the guarantee was determined lexically, by where the text sat, whereas the thing being guaranteed — that no other process observes an intermediate state — is a property of what is executing at a moment in time. Those two notions of extent do not coincide. A lexically delimited region says nothing about the procedures it calls, and the procedures it calls are exactly where the interference happens. The construct had appeared to work in the original examples only because the primitives used inside them happened to be indivisible for unrelated reasons, which is the worst possible kind of evidence: the mechanism was never doing the job, and the environment was covering for it.

The general form of the diagnosis is a question to ask of any control construct. Is the phenomenon it governs decided by program text or by execution history? Scope, name resolution, and type discipline are textual; mutual exclusion, resource lifetime, timeouts, cancellation, error propagation across a call chain, and transactional extent are historical. A construct whose extent is fixed at read time cannot bound something whose extent is determined at run time, and a design that pairs them will pass small tests and fail exactly when the call graph gets deep enough to matter. The report's paired treatment of dynamic bindings and escape objects shows the correct shape by contrast: both are described as having their extent determined by the chain of pending calls, and the report observes that the two are closed over a dynamic context in the same way an ordinary procedure is closed over a textual one.

The second half of the lesson is what the report does after the diagnosis, which is nothing. It removes the construct and declines to replace it, stating plainly that the authors have no good theory of the problem and so are not going to invent a primitive for it — while noting which operations happen to be indivisible in the current implementation and inviting users to build their own on that footing. Leaving a visible hole is a design choice with real advantages over filling it. A hole is discoverable, forces callers to confront the problem explicitly, and costs nothing to fill later. A plausible-looking primitive that is subtly wrong gets built upon, spreads its wrongness into every dependent, and cannot be withdrawn.

A programmer who has internalized both halves checks the extent of every safety mechanism against the extent of the hazard, and treats "I do not yet understand this well enough to abstract it" as a shippable state rather than a failure — documented, unabstracted, and honest about which part of the system nobody should trust yet.

**Source:** [The Revised Report on Scheme: A Dialect of LISP](../works/the-revised-report-on-scheme.md) — the note explaining why the uninterruptible-evaluation primitive was removed and why no replacement was defined, read alongside the section on dynamic binding and escape objects and the note on their symmetry with lexical closure.
