---
type: lesson
title: "Deferring execution is what turns a program into a plan"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, parallelizability, hardware-affinity]
subdomains: [programming-languages-and-semantics, distributed-systems-and-concurrency]
tags: [lesson]
---
# Deferring execution is what turns a program into a plan

**Lesson:** A sequence of transformations written one after another can mean two very different things. Under eager evaluation each line is a command: build this collection now, in full, then build the next one from it. Under deferred evaluation the same lines are a description of a result, and nothing runs until someone asks for something concrete. The text is identical; what changed is who decides the execution order. That decision is the whole game, because the cost of these pipelines is dominated not by the arithmetic but by whether intermediate collections get written down and moved, and only a system that can see several steps at once can arrange for them not to be.

Concretely, deferral buys stage fusion. If the runtime knows that a filter follows a mapping follows a read, it can drive one element — or one partition's worth — through all three at the place the input already lives, keeping nothing but the final output. The eager version cannot do this no matter how clever the implementation of each step, because each step's contract is to produce a complete, addressable collection that the next line might inspect. Materialising it is not an inefficiency in the implementation; it is what the eager semantics promised. So the gain does not come from optimising the steps. It comes from weakening what each step guarantees, which is only possible if the language never let you observe the intermediate in the first place.

There is a price, and it is the usual price of separating description from execution: the moment things go wrong, the thing that failed is no longer the thing you wrote. Errors surface at the consuming operation rather than the producing one, timing measurements attach to the wrong line, and reasoning about resource use requires understanding the plan rather than reading the code top to bottom. That trade is worth making when the pipeline is long and the data is large, and not worth making when it is neither. The general point to carry away is that eager and deferred are not implementation details of a library — they are different contracts about what an intermediate value *is*, and the performance difference between them is a consequence of the contract, not something a tuning flag can recover.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the chapter on cluster programming systems, in its account of lazy evaluation of distributed datasets, where transformations are not applied until an action demands a concrete result, so that intermediate splits are produced and consumed locally and never written to storage or shipped between nodes.
