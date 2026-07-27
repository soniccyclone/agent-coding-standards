---
type: lesson
title: "Connect the executions nobody can tell apart, then walk the chain to a contradiction"
figure: fischer
works: [a-lower-bound-for-the-time-to-assure-interactive-consistency, easy-impossibility-proofs-for-distributed-consensus-problems, impossibility-of-distributed-consensus-with-one-faulty-process]
axes: [verifiability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification]
tags: [lesson]
---

# Connect the executions nobody can tell apart, then walk the chain to a contradiction

**Lesson:** There is one reusable engine behind most claims that a distributed problem cannot be solved, or cannot be solved cheaply, and it is worth owning as a habit of thought rather than as a family of theorems. Treat the set of all possible executions as a graph. Join two executions when some participant that must behave correctly in both cannot distinguish them from what it locally sees. Any requirement that correct participants agree then propagates equality along every edge: if they must agree inside each execution, and consecutive executions share a participant whose view is identical, the answer is forced to be constant along the whole connected chain. Now find two executions at the ends of a chain whose answers are forced apart by a validity requirement — everyone started with one value here, everyone started with the other value there. The chain says equal, the ends say different, and the problem is dead.

The power lies in where the work goes. Nothing in the argument depends on how a participant computes, how much state it keeps, or how clever its strategy is. All the work goes into constructing the chain, and that construction is elementary: flip one participant's input at a time; hand one participant a script assembled from behaviors two other participants exhibited elsewhere; stitch two copies of a network into a larger one that looks locally identical to each of its members. The technique also measures cost, not just possibility. If each link in the chain can only be built by expending one more round of communication, the length of the shortest chain connecting an all-zeros world to an all-ones world becomes a lower bound on rounds — the reason tolerating some number of faults forces one more round than that number, no matter how the protocol is written.

What a programmer does differently: when you suspect a coordination scheme cannot work, stop looking for the clever failure trace and start looking for two situations that demand different outcomes but are locally identical to somebody who must act. That is a much easier object to find, and finding it is decisive. Used positively, the same move tells you what information a participant must have before acting, because an action can only be justified by something in the local view that actually differs between the cases where the action is right and wrong.

**Source:** [A Lower Bound for the Time to Assure Interactive Consistency](../works/a-lower-bound-for-the-time-to-assure-interactive-consistency.md) — the equivalence relation on last-round views and the ordered family of views bridging the all-zeros view to the all-ones one; [Easy Impossibility Proofs for Distributed Consensus Problems](../works/easy-impossibility-proofs-for-distributed-consensus-problems.md) — the sequences of correct behaviors that pairwise share a correct node's behavior; and the adjacency chain over initial configurations in [Impossibility of Distributed Consensus with One Faulty Process](../works/impossibility-of-distributed-consensus-with-one-faulty-process.md).
