---
type: lesson
title: "Announce change at the granularity of intent, not of mutation"
figure: reenskaug
works: [mvc-its-past-and-present]
axes: [cognitive-load, hardware-affinity]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Announce change at the granularity of intent, not of mutation

The obvious way to keep dependents current is to tell them every time something changes. Reenskaug notes the obvious way's symptom without dressing it up: the display visibly churns, because a single meaningful operation decomposes into many small writes and each write triggers its own refresh. The mechanism is correct and the result is unusable, which is the interesting case — the bug is not in the propagation, it is in the choice of what event to propagate.

Two independent corrections apply. The first is temporal: accumulate the writes belonging to one coherent operation and announce once when the operation completes, so that the notification unit matches the unit the initiator considers a single act. Intermediate states within an operation are not merely wasteful to publish, they are frequently invalid — a half-applied change can violate invariants that hold before and after — so batching improves correctness as well as cost. The second is informational: say what changed rather than merely that something did. A bare signal forces every dependent to rescan everything and rediscover the delta, which is redundant work that scales with the number of dependents; carrying the affected property, or the affected region when the data has a spatial notion, lets each dependent do work proportional to the actual change.

Both corrections depend on the notifier and the notified sharing enough vocabulary to describe a delta, which is a real coupling and worth naming as the price. The interface through which dependents read the data supplies that shared vocabulary, so the cost is bounded — the delta description is expressed in terms already exposed, not in terms of internal representation.

A programmer holding this designs event boundaries from the initiator's intent downward instead of from the storage layer upward, and treats a chatty change feed as a design defect rather than something for consumers to debounce. The general shape recurs well outside user interfaces: any published stream of small mechanical events makes its consumers reconstruct the meaningful units, and reconstruction is both wasteful and error-prone compared with publishing the meaningful units in the first place.

**Source:** [The Model-View-Controller (MVC): Its Past and Present](../works/mvc-its-past-and-present.md) — the synchronize-model-and-view pattern, which contrasts the naive per-change notification with a transaction-based scheme that accumulates changes per composite operation and with change descriptors that identify the affected property or region.
