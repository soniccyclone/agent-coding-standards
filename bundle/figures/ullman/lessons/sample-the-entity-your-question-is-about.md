---
type: lesson
title: "Sample the entity your question quantifies over, not the records in front of you"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [databases-and-data-management, algorithms-and-complexity]
tags: [lesson]
---
# Sample the entity your question quantifies over, not the records in front of you

**Lesson:** A sample is not a smaller version of the data; it is a smaller version of the data *with respect to some question*, and which question survives is decided entirely by what unit you sampled. Keeping a tenth of the records preserves anything that is a simple average over records. It destroys anything that is a statement about entities — how often a typical user repeats themselves, what fraction of groups have some property — because a property that requires seeing several of an entity's records survives only when all of them are retained, and independent record-level coin flips retain all of them with quadratically or worse diminished probability. The damage is systematic, not noisy: you can write down the ratio the biased sample converges to and observe that it never equals the true ratio for any input. More data does not fix it, and no confidence interval reveals it, because the estimator is consistently estimating the wrong quantity.

The repair is to name the key your question ranges over and sample on the key, keeping every record of the keys you keep and none of the records of the keys you drop. The sample is then a complete picture of a random subpopulation rather than a partial picture of everyone, and per-entity statistics come out unbiased. Notice how much this constrains you: different questions over the same stream want different keys, so a single sample cannot serve all ad-hoc queries, and pretending otherwise is where the error creeps in. Being explicit about the key is simultaneously an admission of what the sample cannot answer.

The habit worth taking is to write the target quantity down as a formula before choosing a sampling scheme, then check the scheme against the formula rather than against intuition — intuition says a tenth of the rows gives a tenth-scale picture of everything, and intuition is wrong here in a way that is easy to demonstrate and easy to miss. The same discipline applies to every reduction that gets applied "just to make it manageable": deduplication, truncation, top-N filtering, retention windows. Each one silently fixes which questions remain answerable, and the choice is much cheaper to make deliberately at the start than to discover from a result nobody can reproduce.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the stream-mining chapter's opening treatment of sampling, which works out exactly how a per-query sample corrupts the fraction of a user's repeated queries and then generalises to selecting on designated key components.
