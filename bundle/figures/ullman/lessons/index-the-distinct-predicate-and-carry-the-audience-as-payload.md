---
type: lesson
title: "Index the distinct predicate and carry the audience as payload"
figure: ullman
works: [mining-of-massive-datasets]
axes: [parallelizability, hardware-affinity, cognitive-load]
subdomains: [databases-and-data-management, distributed-systems-and-concurrency]
tags: [lesson]
---
# Index the distinct predicate and carry the audience as payload

**Lesson:** A system that evaluates registered interests against arriving items appears to have a cost that scales with the number of registrations, and that number is the one that grows without bound as the product succeeds. The observation that defuses this is that registrations are not distinct. Many people ask to be alerted on the same term. If the structure is keyed by the interest rather than by the interested party, an interest shared by a million people occupies one entry, matching costs one lookup, and the million identities sit in a list hanging off that entry, touched only after a match has already been established. The evaluation cost then scales with the number of distinct predicates, and the number of subscribers becomes a fan-out cost paid only on hits.

The distinction between those two quantities is the thing to look for, because they diverge enormously and in a favourable direction. Distinct predicates are drawn from a vocabulary shaped by what people actually care about, which is a small, slow-growing, heavily repeated set. Subscribers are drawn from your user base. Building the index on the wrong one of these means the matching work grows with adoption, which is precisely the failure mode where success degrades the service. Building it on the right one means adoption adds rows to payload lists and nothing to the matching path.

The same reasoning is what makes some variants of this problem far easier than others, and the chapter lays the comparison out. Alerts on a single word or a fixed phrase are cheap for two independent reasons: the match test is a scan rather than a combinatorial subset search, and the set of terms anyone is likely to register from is limited, so the number of distinct predicates is small even when the number of registrations is not. Allowing arbitrary sets of words instead of single terms loses both properties at once. That is worth noticing at design time, because the expressiveness of what a user may register is the parameter that decides whether the deduplication works, and it is usually chosen casually.

Generalised: whenever a system holds a large population of stored requests, ask what the equivalence classes are before designing the storage. Deduplicate the request, attach the requesters as data, and check whether the request language is narrow enough for the classes to be large. If the language is rich enough that every request is unique, that richness is the actual cost driver, and constraining it is a cheaper lever than any amount of engineering downstream.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 8's discussion of standing queries for news alerts, which notes that the set of terms one can search for is limited so there are not many bids, and that even when many people want alerts on the same term only one index entry is required with the list of all those people associated with it.
