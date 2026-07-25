---
type: lesson
title: "Count your special-case rules: a pile of ad hoc restrictions means the underlying concept has not been found yet"
figure: brinch-hansen
works: [monitors-and-concurrent-pascal-a-personal-history, distributed-processes-a-concurrent-programming-concept]
axes: [primitive-count, cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Count your special-case rules: a pile of ad hoc restrictions means the underlying concept has not been found yet

**Lesson:** Here is a diagnostic that requires no taste and can be applied to your own work. Enumerate the rules in your design of the form "this kind of thing may not appear inside that kind of thing," or "this may not be passed there," or "that may not refer to itself." Each one individually has a defensible justification, usually safety or implementability, and each one individually looks like prudence. But their total number measures something real: how far your concepts are from composing freely, and therefore how much of the design a user must memorize as exceptions rather than derive from the idea. Two dozen such rules is a symptom, and the diagnosis is not that the design is careless — it is that the right concept has not been found, and the rules are the patches holding a nearly-right one together. Brinch Hansen applied this test to his own first language and reported the count against a later, smaller one where three such rules remained and he judged only one of them necessary.

The constructive half of the diagnostic is unification. If several of your constructs differ mainly in scheduling behavior or in who may hold them, ask whether one construct with the right parameters covers all of them, and check the answer by trying to express the things they were each good at. When the unification works, the evidence is not aesthetic but countable in the implementation: instruction repertoires collapse by a large factor, whole categories of special-case handling disappear from the translator, and the proof rules you would have needed separately for each construct become one set. That the same construct can be made to behave as a private data holder, a shared arbitrator, an autonomous activity, a coroutine, a counting semaphore, a buffer, a sequencing constraint, and a device interface is a claim about structure, not a party trick.

What a programmer does differently is treat restriction count as a first-class quality metric alongside the ones they already track, and treat each new exception as a small piece of evidence against the current concept rather than a local fix. The honest form of this is uncomfortable, because the restrictions are usually there for good reasons and removing them requires a better idea rather than more permissiveness.

**Source:** [Monitors and Concurrent Pascal: A Personal History](../works/monitors-and-concurrent-pascal-a-personal-history.md) — the retrospective section on complexity, which lists the language's ad hoc restrictions, names them as a symptom, and contrasts the count with the author's later languages. Also [Distributed Processes](../works/distributed-processes-a-concurrent-programming-concept.md) — the closing remarks, which enumerate the constructs subsumed by a single concept and quantify the resulting reduction in the virtual instruction set and in compiler special cases.
