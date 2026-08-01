---
type: lesson
title: "Size alone does not qualify a problem for a scale technology"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, cognitive-load, verifiability]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# Size alone does not qualify a problem for a scale technology

**Lesson:** Tools built for large data get adopted on the strength of one number, and that number is almost never the whole admission criterion. A storage layer designed for cluster-scale work wants files enormous *and* seldom modified in place; the two conditions are independent, and failing either one disqualifies you. A retailer with a genuinely vast reservation or transaction database fails the second condition badly enough that the tool is wrong for it, no matter how impressive the first number is — the same organisation may be a perfect fit for the same tool on a different workload against the same data, which is the clearest possible demonstration that scale was never the deciding property. And at the other end, a collection of small files fails the first condition, so the tool is pointless there too: the criteria bound the applicable region from both sides.

Why the second condition gets dropped is worth understanding, because the mechanism repeats. Size is the property the tool advertises, the one that appears in benchmarks, and the one a prospective user already knows about their own data. Mutation rate, read-write ratio, access locality, and result cardinality are properties you have to go measure, and they are the ones the architecture actually assumed. Chunked, replicated, append-oriented storage is what it is because rewriting a byte in the middle means invalidating copies across the cluster; that cost is invisible in a description of the system and decisive in a workload that does it constantly. The advertised property is a consequence of the design; the unadvertised properties are its preconditions.

The transferable habit is to reconstruct the precondition list from the mechanism rather than accepting the pitch. For any tool you are about to adopt, ask what it does on write, what it does on update, what it assumes about how results are consumed, and what it silently makes expensive. Then check your workload against each one, including the ones that make you look like a bad fit. The characteristic failure this prevents is not choosing a slow system — it is choosing a system that is spectacular on the dimension you measured and pathological on a dimension you never thought to state, and then concluding that distributed computing is disappointing.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 2's characterisation of when a distributed file system applies: files must be enormous and rarely updated, with the explicit judgement that an airline reservation system is unsuitable however large its data because the data changes so frequently, that small files have no business there, and the parallel argument that on-line retail transactions are a poor fit while analytic queries over the same company's data are a good one.
