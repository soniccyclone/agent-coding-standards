---
type: lesson
title: "Grade a procedure that must decide now against what hindsight could have done"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, distributed-systems-and-concurrency]
tags: [lesson]
---
# Grade a procedure that must decide now against what hindsight could have done

**Lesson:** There is a class of problems where the input arrives one item at a time and each item must be answered before the next is seen, because the answer is itself the product being delivered. Nobody will wait a month for their query to be batched. For these the usual quality question — is the output optimal — is malformed, since optimality is defined against information the procedure structurally cannot have. Asking it anyway leads to endless unproductive tinkering, because every rule you invent can be defeated by some future you were never going to see.

The productive reformulation is to fix a reference that also cannot be achieved and measure the shortfall against it. Take the best result obtainable by a procedure that sees the entire input in advance and may reorder its decisions freely; that is not an implementable competitor, it is a yardstick. Then ask for the largest fraction of that yardstick your procedure is guaranteed to reach on every possible input, worst case included. That single number is a real guarantee rather than an average-case hope, it is comparable across candidate designs, and it converts an argument about anecdotes into an argument about bounds. It also quantifies something otherwise invisible: the gap between the guarantee and one is the price of not knowing the future, so you learn what perfect foresight would actually be worth before anyone proposes buying it.

Two consequences change how you design. First, the guarantee is a property of the pairing of procedure and admissible input set, not of the procedure alone — widen what the adversary may present and the guarantee drops, so stating the input class is part of stating the result. That makes restricting the input class a legitimate engineering move: if the guarantee is unacceptable in general but acceptable once you exclude a shape you can prove never occurs, excluding it is real work with a real payoff. Second, a worst-case guarantee licenses building on top of the procedure, because downstream capacity planning, pricing, and service promises can be derived from the bound instead of from observed behaviour that may not repeat.

The habit transfers well beyond scheduling and allocation. Caching, admission control, load shedding, resource placement, and any decision made under irreversible commitment all have the same shape, and the same reformulation applies: stop comparing to perfection, name the omniscient reference, and go find the guaranteed fraction.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the advertising chapter's sections on on-line versus off-line algorithms and the competitive ratio, including the two-advertiser example where the right assignment depends on how many queries of each kind remain in the month, and the observation that the ratio depends on which inputs the algorithm is allowed to receive.
