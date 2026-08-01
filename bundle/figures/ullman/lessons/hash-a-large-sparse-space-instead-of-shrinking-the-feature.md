---
type: lesson
title: "Hash a large sparse space rather than shrink the feature to fit"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, expressiveness]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# Hash a large sparse space rather than shrink the feature to fit

**Lesson:** When a feature is too wide to store comfortably, there are two ways to make it fit and they are not equivalent, though they consume identical space. You can define a narrower feature, or you can keep the wide feature and hash it into the narrow slot. The second wins, sometimes by a large margin, and the reason is that a representation's real capacity is the number of codes its inputs actually occupy, not the number its width permits. A narrow feature drawn from structured data uses only a small, clustered part of its own code space; the same number of bits filled by a hash of a much wider feature uses essentially all of it. Same storage, far more discrimination — an unusually cheap win, and one that is invisible if you reason about representations by counting bits.

The generalisable move is to separate two decisions that get conflated: how much of the world the feature distinguishes, and how many bits you spend recording the answer. Choose the first on the merits — make the feature wide enough that two unrelated items are unlikely to share one by accident — and then treat narrowing as a purely mechanical last step done by hashing, accepting the collisions that come with it. Collisions between unrelated features are harmless in a workload that only ever asks whether two items share features, because a chance collision adds a small uniform noise floor rather than a systematic bias; whereas a feature too narrow to be distinctive produces agreement between genuinely unrelated items *systematically*, which no downstream stage can subtract off.

The corollary is that when you size the feature, the alphabet you count over is the effective one, not the nominal one. Symbol frequencies in real data are heavily skewed, so the number of distinct wide features that actually occur is far below the product of the nominal symbol count, and a sizing calculation done on the nominal alphabet is optimistic in the direction that hurts. Assume a considerably smaller alphabet than the encoding permits and pick the width from that. Both halves of this — hash down rather than narrow, and size against the effective alphabet — come from the same habit of asking what the data does rather than what the type allows.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the shingling sections of the similar-items chapter: the argument that shingle length must make any particular shingle unlikely in any particular document, the rule of thumb of assuming roughly twenty frequent characters rather than the full alphabet because letter frequencies are skewed, and the observation that hashing nine-character shingles into four bytes discriminates better than using four-character shingles despite occupying the same space, because most four-byte sequences never occur as short shingles while hashed long shingles cover the range.
