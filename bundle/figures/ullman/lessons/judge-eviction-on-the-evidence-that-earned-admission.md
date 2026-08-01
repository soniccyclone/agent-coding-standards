---
type: lesson
title: "Judge eviction on the same evidence that earned admission"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---
# Judge eviction on the same evidence that earned admission

**Lesson:** A common architecture admits members to a tracked set by an expensive batch computation over a large body of evidence, then maintains the set cheaply by watching new arrivals and dropping anything whose observed rate falls below the bar. The two halves look symmetric and are not, because the maintenance loop starts its counters at zero the moment it takes over. It is judging a member on the evidence accumulated since monitoring began, while the member was admitted on evidence accumulated over a much longer stretch, and the shorter the monitoring window is the more its estimate is dominated by noise.

The consequence is churn that looks like responsiveness. Something genuinely durable goes through a quiet spell of ordinary length, its short-window rate dips under the bar, and out it goes — and since re-admission usually requires the expensive batch path, the system has just paid a large cost to undo a decision that was correct. Worse, the eviction rate is a function of window length rather than of anything real, so the system's apparent volatility can be tuned up and down by an implementation detail nobody thinks of as a policy knob. Teams then debug the wrong thing, because the members leaving really did look infrequent by the number the code computed.

The correction is unglamorous and exact: carry the admitting evidence into the maintenance loop as the counters' initial state, so the running estimate is over everything ever seen rather than everything seen since the handover. A member's rate then moves slowly at first and becomes responsive only when the new observations are numerous enough to be worth responding to, which is the behaviour you wanted. If the maintenance loop uses a different weighting from the batch — a decay, a sliding window, a rate rather than a count — then the initialisation is a conversion problem rather than a copy, and the value to install is whatever the incremental scheme would be holding right now had it been running all along. That conversion is worth deriving explicitly; guessing it reproduces the original bug in a subtler form, since too small a starting value evicts immediately and too large a one keeps dead members alive long after the evidence has gone.

Stated generally: any handover between two mechanisms that estimate the same quantity must transfer state, not just responsibility. The check to run on such a design is to ask what each side would say about a member right after the handover. If the answers differ, the boundary between the mechanisms is producing decisions that the data does not support, and every crossing of that boundary is a place where the system forgets something it paid to learn.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 6's stream sections, which maintain frequent itemsets found from a sampled file by counting further occurrences and dropping any set that falls well below the threshold fraction, and insist that the occurrences from the original sample be included in the fraction so that a short lean period does not discard a genuinely frequent set; and the same chapter's hybrid scheme, which converts a set's batch-measured support into the decaying window's own units before it starts being maintained there.
