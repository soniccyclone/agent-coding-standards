---
type: lesson
title: "Certify that you missed nothing by counting the boundary of what you accepted"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Certify that you missed nothing by counting the boundary of what you accepted

**Lesson:** An approximate first stage gives you a set of answers you believe in and no way to know what it overlooked, because the overlooked things are by definition absent from everything you are holding. There is a construction that closes this gap exactly, and it costs one extra piece of bookkeeping. Alongside your accepted set, compute its immediate exterior: the objects that failed your approximate test but all of whose immediate simplifications passed it. Then verify both sets against the real data. If nothing in the exterior turns out to qualify, you have a proof — not an estimate — that nothing outside your accepted set qualifies either.

The proof rests on the ordering, and it is worth understanding rather than memorising, because the same argument transfers. Suppose something qualified but you missed it. Then all of its simplifications qualify too, by whatever monotone property you are exploiting. Walk down from it to the smallest of its simplifications that your approximate stage rejected. That object failed the approximate test while all of its own immediate simplifications passed it, which is precisely the definition of being in the exterior — and it qualifies against the real data. So an undetected miss forces a qualifying member of the exterior. Contrapositive: an empty exterior verdict means no misses. The boundary acts as a tripwire ringing the accepted region, and a monotone property is what guarantees nothing can hop over it.

The construction comes with a distinctive and underused engineering posture: the procedure is allowed to answer "I cannot tell you this time." When the tripwire fires, you do not get a degraded answer, you get no answer, and you rerun with a fresh approximation. That is a design point people avoid instinctively, and it is often the right one. Compare the alternatives — always answering approximately, with an error you cannot bound, or always answering exactly, at a cost you cannot afford. An occasional honest failure, with a small expected number of retries, gets you exactness at approximate cost. The requirement is that the caller can tolerate variable latency, which is a question to ask rather than assume the answer to.

The general habit is: when a stage of your system decides a boundary, do not only check what fell inside. Check the things that just barely fell outside, because those are where a wrong boundary shows up first, and their collective silence is the only evidence you will ever get that the boundary was drawn correctly.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the Toivonen sections of the frequent-itemsets chapter, which define the negative border of the sample's frequent sets, verify both it and the sample's answers against the full data, and give the minimal-counterexample argument showing an empty border result implies no false negatives, at the price of restarting when the border fires.
