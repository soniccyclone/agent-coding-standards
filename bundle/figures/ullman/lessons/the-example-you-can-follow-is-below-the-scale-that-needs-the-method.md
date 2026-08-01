---
type: lesson
title: "The example you can follow is below the scale that needs the method"
figure: ullman
works: [mining-of-massive-datasets]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, algorithms-and-complexity]
tags: [lesson]
---
# The example you can follow is below the scale that needs the method

**Lesson:** Techniques get demonstrated on examples chosen for legibility, and legible means small enough to hold in your head, which is almost always small enough that the naive method would have been better. The demonstration is therefore systematically misleading in one direction: it shows the machinery working, in a regime where the machinery is unnecessary. A reader who takes the example as evidence takes it as evidence of applicability, which is the one thing the example cannot supply. This is not a flaw in teaching by example, it is a structural property of examples, and the only repair is for the presenter to state the regime and for the reader to check which side of it they are on.

The presenter's obligation is small and rarely met: alongside the worked case, name the crossover. Say how many distinct entities, how many streams, how much arrival rate it takes before the exact method stops fitting, and say plainly that the illustration sits below that line and was chosen because it is familiar. That admission costs a sentence and inoculates the reader against the most common misuse of any technique, which is adoption at a scale where a hash table and a loop would have been correct, exact, faster, and testable. An author who says outright that their own example does not need the method they are teaching has told you the most useful thing in the section.

The reader's obligation mirrors it. When you find a technique attractive, locate the crossover before adopting it, and estimate your own quantity against it. The estimate does not need to be good; being within an order of magnitude decides the question in most cases, because these crossovers are usually far away rather than nearby. What makes this hard in practice is that approximate machinery is more interesting to build than exact machinery, so the incentive runs toward adopting early and the argument for it is always available — data grows, after all. Growth is a reason to know the crossover, not a reason to assume you have passed it.

The durable version of this is to put the crossover in the system rather than in a design document. Record the quantity that determines which regime you are in, and check it: the count of distinct entities, the peak arrival rate, the size the exact structure would have been. Then the decision is revisitable from data by whoever is on call in two years, and the answer might be that the approximation can be removed. That direction of change almost never happens, not because it is rarely warranted but because nobody records the number that would show it.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 4's decaying-window example of tracking popular films, whose footnote concedes that there are not enough films for the technique to be necessary and asks the reader to imagine a far larger set, echoing the same chapter's remark that a single slow sensor's stream would be uninteresting to keep and its note that per-item counting fails only once the catalogue is large.
