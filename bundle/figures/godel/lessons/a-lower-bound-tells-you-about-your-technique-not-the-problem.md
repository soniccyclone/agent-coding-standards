---
type: lesson
title: "A best-known bound describes the reach of your technique, not the difficulty of the problem"
figure: godel
works: [letter-to-von-neumann]
axes: [verifiability]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# A best-known bound describes the reach of your technique, not the difficulty of the problem

**Lesson:** Gödel states the strongest lower bound anyone had for his problem and then, in the same breath, discounts it — not because he doubts it, but because he can see where it came from. The bound is what you get by pushing the one available proof method, the generalization of the undecidability argument, as far as it goes. Knowing that, he treats the bound as a fact about the method rather than a fact about the problem, and concludes that the truth being far below it is entirely plausible. This is a specific and unusual kind of epistemic bookkeeping: separating what you have established from what you have merely failed to improve, by identifying which technique produced the current state of knowledge and how much of the gap is attributable to that technique's known reach.

The move matters because unimproved bounds acquire authority they have not earned. A figure that has stood for years starts being cited as though it were the answer, and the reason it has stood — that everyone who tried used the same handful of methods — drops out of the citation. Gödel's discipline is to ask, before believing any negative or limiting result, what argument produced it and what that argument is structurally capable of showing. If a single technique is responsible for every bound in the area, then the area's apparent consensus is one technique's shadow, and the honest confidence interval is much wider than the literature's tone suggests. He applies the same standard in the other direction as well, treating repeated historical successes at collapsing search costs as evidence about what is possible rather than as anecdotes.

In practice this is how to read every performance ceiling, scalability limit, and "that can't be done" in a codebase or an organization. The relevant question is never just what the current number is, but what produced it: which measurement, which implementation strategy, which assumption about the workload. A latency floor that comes from one architecture is not a latency floor. A throughput limit measured on one data distribution is a fact about that distribution. A colleague's confident impossibility claim is worth exactly the argument behind it, and often the argument turns out to be one technique's limit reported as a law. The corresponding obligation is symmetric and unglamorous: when you report your own bound, say what method produced it, so the next person can tell how much of it is the problem and how much is you.

**Source:** [Letter to John von Neumann](../works/letter-to-von-neumann.md) — the aside noting that the linear lower bound appears to be all that a generalization of the undecidability proof can yield, used as grounds for taking seriously the possibility that the true growth is dramatically slower than that argument suggests.
