---
type: lesson
title: "Give each operator a local rule and let the graph compose them"
figure: ullman
works: [mining-of-massive-datasets]
axes: [primitive-count, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Give each operator a local rule and let the graph compose them

**Lesson:** There is a family of problems where you need, alongside the computation you wrote, a second computation derived from it — how its result responds to each input, how to undo it, what it costs, which inputs it depends on. Writing that second computation by hand for a whole system is miserable and it goes stale the moment the first one changes. The alternative is available whenever the composition rule for the derived quantity is *local*: the derived answer for a composite is a fixed combination of the derived answers of its parts. When that holds, you do not need a derived version of the system at all. You need a derived version of each primitive operator, plus a traversal.

The precondition for this to work is that the program be available as a structure rather than only as behaviour. If the computation is a graph of operator applications you can walk, the traversal is mechanical: process nodes in an order where every node's dependents are already done, apply the local rule at each, and where a node feeds several places, combine the contributions from each. Nothing in that description mentions the specific problem. It is the same walk for every program expressible in the operator set, which is why one implementation serves everybody, and why the person writing a model can describe only what they want computed and get the derived machinery without asking.

Two consequences are easy to miss. First, the cost of adding a new primitive is exactly one local rule — a bounded, checkable, independently testable obligation, and a good reason to keep the primitive set small and closed rather than letting arbitrary code in. A primitive without its local rule is not a small gap; it breaks the traversal for every program that uses it. Second, the derived computation can be materialised as more nodes in the same graph rather than as a separate mechanism, which means it is subject to the same scheduling, caching, and optimisation the original enjoyed, and does not have to be re-derived on every run.

The general shape to look for: any time you find yourself maintaining a parallel version of a system — a validator that mirrors the schema, a cost estimator that mirrors the query plan, a serialiser that mirrors the type — ask whether the parallel thing composes locally over the same structure. If it does, the parallel system is not a system, it is a table of per-operator rules plus a walk, and maintaining it as anything larger is a self-inflicted duplication that will drift.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the compute-graph and backpropagation sections of the neural-nets chapter, which model the network as a directed acyclic graph whose nodes carry operands and operators, then process nodes in reverse order picking one whose successors are all done, apply a per-operator local rule at each, sum contributions where a node has several successors, note that frameworks such as TensorFlow already know these rules for common operators so the developer supplies only the forward graph, and add the derived quantities as extra nodes in that same graph to avoid recomputing them each iteration.
