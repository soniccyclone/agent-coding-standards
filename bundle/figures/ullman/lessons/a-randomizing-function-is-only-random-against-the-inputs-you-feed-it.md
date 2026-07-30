---
type: lesson
title: "A randomizing function is only random relative to the input population you actually feed it"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, verifiability]
subdomains: [algorithms-and-complexity, operating-systems-and-systems-programming]
tags: [lesson]
---
# A randomizing function is only random relative to the input population you actually feed it

**Lesson:** Reduction modulo a bucket count is the textbook scattering function and it distributes arbitrary integers perfectly evenly. Feed it only even numbers with ten buckets and half the buckets become unreachable — every result lands in one of five. Change the count to eleven and the same inputs spread uniformly again. Nothing about the function changed, and nothing about the data changed; what changed was the arithmetic relationship between the divisor and a structural regularity in the keys.

The general statement is that a hash function has no intrinsic uniformity. It has uniformity with respect to a distribution of inputs, and the property fails whenever the modulus shares a factor with a regularity present in most keys. This is worth holding as a distinct failure mode because of how it presents: not as an error, not as a crash, but as a silent collapse in effective capacity. The table works, lookups return correct answers, and throughput is quietly a small multiple worse than designed because the load concentrated into a fraction of the space. Nothing in the interface reports it, and the defect is invisible to any test that only checks correctness.

Two practices follow. Prefer a prime bucket count, which minimizes the chance of sharing a factor with whatever structure the keys happen to have — a cheap default that costs nothing and removes an entire class of accident. And when deriving integers from composite keys, understand that the derivation itself imposes structure: summing character codes, for instance, produces values in a range determined by string length, so a bucket count larger than typical sums makes most buckets unreachable regardless of primality. The fix there is to group characters so the derived integers span the intended range before reduction. In both cases the reasoning is the same — check the interaction between your reducer and the shape of what you are reducing.

The wider habit is to distrust any claim that a function "randomizes" without reference to what it is being fed. Randomness is a relation between a function and a population, never a property of the function alone, and the assumption most often violated in practice is that real keys resemble arbitrary ones. They rarely do: identifiers are allocated in blocks, timestamps land on boundaries, and generated names share prefixes. Any of those regularities can align with a modulus, and when it does the symptom is a system that is merely slower than it should be, which is the hardest kind of defect to notice.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 1's review of hash functions, which gives the modulo-B function as working well when the key population is all positive integers but distinctly nonrandom when the population is the even integers and B is 10 (only five buckets reachable) while B of 11 restores uniformity; generalizes to the rule that choosing B with a common factor with most possible keys yields nonrandom distribution, so B is normally preferred prime; and covers converting non-integer keys by summing character codes, noting that this works only while B is smaller than typical sums and otherwise requires grouping characters to widen the derived integers.
