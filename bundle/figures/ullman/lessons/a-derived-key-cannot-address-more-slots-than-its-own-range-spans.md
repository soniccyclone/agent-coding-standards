---
type: lesson
title: "A derived key cannot address more slots than its own range spans"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, hardware-affinity]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# A derived key cannot address more slots than its own range spans

**Lesson:** Any scheme that turns a structured value into a slot number does it in two stages: first reduce the value to a number, then fold that number into the available range. It is easy to treat the second stage as the one that determines spread, and to widen the range whenever you want finer distribution. That does not work, because the first stage has its own ceiling. If the reduction typically produces values spanning some magnitude, and you ask for more slots than that, most slots are unreachable and everything piles into the low end. The distribution collapses not because the folding is bad but because there was never enough numeric spread coming in to distribute.

The concrete case makes the shape clear. Reduce a string by summing its character codes and you get a number bounded by the string's length times the size of a character code — a few thousand for ordinary text. Fold that into a few hundred slots and it works. Ask for a billion slots and you have a few thousand distinguishable inputs competing for them, and no choice of divisor rescues you. The fix is upstream, on the encoding: chunk the characters into groups and treat each group's concatenated codes as a single wide number, so each unit of input contributes far more magnitude, and the sum can actually reach across the range you asked for. You changed how the input is read, not how the arithmetic mixes.

The general instruction is to audit intermediate ranges rather than only endpoints. Every derivation pipeline has a stage whose output width caps what all later stages can resolve, and that stage is rarely the one you are tuning. It shows up wherever a coarse quantity feeds a fine consumer: a checksum too narrow for the number of shards it selects, a timestamp at second resolution used to order events arriving thousands per second, a category code with a dozen values used to partition across hundreds of workers, an identifier derived from a small enumeration and expected to spread. Write down the number of distinguishable values each stage can emit for your actual input population and compare it against the resolution the next stage demands. Where the demand exceeds the supply, the excess is decoration.

What makes this failure worth naming is that it is completely silent. Nothing errors. Every value gets a slot, the code is correct on every input, tests pass, and the only symptom is an imbalance that looks like ordinary bad luck with the data — which invites the wrong fix, an endless search for a better mixing function, when the mixing function was never the constraint. The correct diagnosis is a counting argument done before any of that: how many distinct outputs can the reduction produce over the inputs I will actually see, and is that at least the number of buckets I am asking for. Two lines of arithmetic settle it.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 1's review of hash functions on non-integer types, which converts strings by summing character codes and states that this distributes relatively uniformly only while the number of buckets stays below the typical sum for the string population, then prescribes partitioning the characters into groups and treating each group's concatenated codes as one integer when the bucket count is larger — with the worked case of grouping four characters at a time to reach thirty-two-bit values for a bucket count near a billion, and the recursive extension of the same summing rule to records, arrays, sets and bags.
