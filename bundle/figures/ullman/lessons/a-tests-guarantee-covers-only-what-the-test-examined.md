---
type: lesson
title: "A test's guarantee covers only what the test actually examined"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# A test's guarantee covers only what the test actually examined

**Lesson:** When filters are chained so that each stage only inspects what survived the previous one, it becomes tempting to drop the earlier conditions from the final check, on the reasoning that anything the earlier stage rejected never reached the later stage and therefore could not have influenced it. The reasoning is wrong, and wrong in a way that produces a defect no test will find, because the result is merely incorrect rather than crashing. What the later stage's evidence actually says is: among the things I examined, these are the ones that look promising. It says nothing whatsoever about the things it never saw. A candidate excluded upstream might well have passed the downstream test had it been offered, so the downstream verdict cannot be used to readmit it.

The general form is that conditional evidence is not unconditional evidence, and a chain of filters accumulates conjunctions rather than replacing them. Every stage's certificate is scoped to the population that stage observed, and the final acceptance rule has to restate all the conditions, in order, even when some of them feel redundant given how the pipeline is wired. The apparent redundancy is exactly the trap: it is redundant for the items that flowed through, and load-bearing for the items that did not — and the failure only manifests for the latter, which is the set nobody is looking at.

This shows up well outside staged algorithms. Cached authorisation decisions carry the scope of the request that produced them; a validation that ran on a filtered subset cannot vouch for the unfiltered set; a health check that only probes reachable instances says nothing about the unreachable ones; a benchmark run on inputs that passed a pre-filter tells you nothing about the rejected inputs' performance. In each case the mistake is treating a conditional result as a global one because the condition happened to be enforced by the plumbing rather than written down.

The discipline is to state each stage's guarantee as an explicit sentence beginning with the population it ranged over, and to derive the final rule from those sentences rather than from a mental picture of the data flow. Diagrams of pipelines encourage the error, because an arrow suggests that everything relevant travelled along it. Sentences about populations do not.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the boxed warning in the multistage section of the frequent-itemsets chapter, which corrects the belief that the first stage's condition can be omitted from the final candidate test because unfiltered pairs were never hashed in the second stage, and points out that such a pair could still have landed in a surviving bucket had it been hashed.
