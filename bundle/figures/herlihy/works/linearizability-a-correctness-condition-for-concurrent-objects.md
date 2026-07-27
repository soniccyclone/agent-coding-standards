---
type: work
title: "Linearizability: A Correctness Condition for Concurrent Objects"
figure: herlihy
description: Defines linearizability, a correctness condition requiring every concurrent operation on a shared object to appear to take effect atomically at some single point between its invocation and its response, matching some legal sequential execution. Distinguishes it from earlier database-style serializability by being local and composable - a system built entirely from linearizable objects is itself linearizable - which makes it tractable to prove correctness object-by-object. It has since become the default correctness contract for concurrent data structure implementations, cited well beyond its original object-oriented-language framing.
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification]
year: 1990
url: http://www.cs.cmu.edu/~wing/publications/HerlihyWing90.pdf
access: public
host: self-archived
tags: [work]
---

# Linearizability: A Correctness Condition for Concurrent Objects

**Author(s):** Maurice Herlihy and Jeannette M. Wing
**Venue/year:** ACM Transactions on Programming Languages and Systems (TOPLAS) 12(3), July 1990, pp. 463-492.
**Source:** http://www.cs.cmu.edu/~wing/publications/HerlihyWing90.pdf — live PDF, self-archived on Jeannette Wing's own CMU CS publications page.

## Lessons
- [Convert the concurrent question into a sequential one, and let the data type's meaning pay for the concurrency](../lessons/reduce-concurrent-correctness-to-a-sequential-question.md)
- [Insist that a correctness property hold object by object, or you have bought a global scheduler without noticing](../lessons/insist-the-correctness-property-be-local.md)
- [A pure safety condition can quietly forbid progress; audit what your consistency contract makes impossible](../lessons/a-safety-condition-can-silently-cost-you-liveness.md)
- [While operations are in flight, an object's meaning is a set of possible values, not a value](../lessons/in-flight-state-is-a-set-of-possibilities-not-a-value.md)
