---
type: lesson
title: "State that cannot detect its own drift needs a scheduled recomputation"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, hardware-affinity, cognitive-load]
subdomains: [databases-and-data-management, distributed-systems-and-concurrency]
tags: [lesson]
---
# State that cannot detect its own drift needs a scheduled recomputation

**Lesson:** Incrementally maintained summaries are usually designed around a candidate set: rather than re-deriving the answer from all the data on every update, you keep a handful of plausible alternatives and swap among them as evidence arrives. The scheme works while the true answer stays inside the candidate set. The failure that matters is not that it can leave — everyone expects that — but that the summary contains no information capable of revealing that it has left. Every check you could run is a check against the retained candidates, and the retained candidates are precisely what has gone stale. There is no cleverness available in the update path that fixes this, because the evidence needed lives in data the update path deliberately does not read.

Recognising that distinction changes what you build. If drift were detectable from the retained state, the right answer would be a validity check and a repair triggered on failure — event-driven, cheap in the common case. If it is undetectable, no trigger exists, and the only correct response is a periodic sweep that reads the full underlying data and rebuilds. That is a scheduled cost with no signal to justify any particular schedule, which is uncomfortable and is exactly why the step gets omitted. The honest version of the design names the sweep, names its period, and accepts that the period is a policy choice about how much staleness is tolerable rather than something derivable.

The question worth asking early, then, is not "how accurate is my incremental update" but "what would have to be true for me to notice it is wrong." Ask it of caches keyed on a value that can change without notification, of materialised views whose refresh depends on a change feed that may not carry every relevant edit, of a leader elected from a membership list that no longer reflects who is alive, of any statistic maintained by additions that no deletion path ever reverses. Each is the same shape: a compact state that answers questions accurately right up to the point where it is quietly answering from a stale premise, with no internal contradiction available to expose it.

There is a design lever as well as a maintenance one. The size of the candidate set is a direct trade between memory and how long the summary can go before it needs the sweep. Keeping more alternatives is not merely more accurate; it lengthens the interval over which the true answer is likely to remain covered, which lets the expensive sweep run less often. Framing the parameter that way — as purchasing time between reconciliations rather than as buying accuracy — usually leads to a better choice than treating it as a precision knob.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 7's account of maintaining a cluster's representative in the GRGPF algorithm, which keeps the nearest points to the current representative as its replacement candidates, concedes that the true representative may eventually cease to be any of them, states plainly that there is no way to know this because the remaining points are not in main memory, and resolves it by bringing the cluster's points back from disk periodically to recompute the features.
