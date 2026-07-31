---
type: lesson
title: "When the space of behaviours is combinatorial, shrink the space instead of checking it"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [verifiability, parallelizability]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification]
tags: [lesson]
---
# When the space of behaviours is combinatorial, shrink the space instead of checking it

**Lesson:** Two processes of three steps each, running with no constraint on how they interleave, admit twenty distinct global orderings consistent with each process's internal order. The authors write all twenty out. The point of writing them out is to make the obvious method visibly untenable: you could consider each ordering and confirm its outcome is acceptable, and that approach becomes unwieldy the moment either the number of processes or the number of steps grows. The conclusion drawn is not "be more careful" but that the practical route is to devise mechanisms that constrain the interleaving, so that the orderings you must reason about are few enough to reason about.

That reframes what a concurrency primitive is for. A lock, a serializer, a transaction, a single-writer channel is not a safety device bolted onto a correct program. It is an instrument for reducing the size of the space you have to argue over, from a combinatorial explosion to a handful of cases with a structural argument covering them. Judge such a mechanism by how much of the space it eliminates and how simple the remaining argument becomes, not by whether it makes a particular known bug go away.

The move generalizes past concurrency to any situation where behaviour is a product of independent choices — feature flag combinations, permission matrices, retry-and-timeout interactions, protocol state machines, configuration surfaces. Testing samples such a space and never covers it, and each new dimension multiplies rather than adds. The productive response is always structural: make combinations unrepresentable, force choices through one point, establish an invariant that holds regardless of which branch was taken. Enumerate-and-check is a method whose cost grows with the thing you were trying to manage.

There is a complementary discipline in the same passage that is easy to skip past. Even when a program will run on a sequential machine, writing it as though it were concurrent forces you to avoid inessential timing constraints, and the authors say this makes the program more modular. That is a forcing function worth borrowing generally: adopt a restriction the platform does not impose, so that dependencies you never intended to have become impossible to write rather than merely unnoticed. Assumptions about order that were never deliberate are exactly the ones that survive review, because nobody wrote them down to be reviewed.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) - the opening of chapter 3 section 3.4.2, which lists all twenty orderings of two three-event processes consistent with each process's internal order, observes that a designer would have to consider the effects of each and check that every behaviour is acceptable, notes that this approach rapidly becomes unwieldy as the numbers of processes and events increase, and concludes that a more practical approach is to devise general mechanisms constraining the interleaving so that program behaviour can be known correct — introducing the serializer as one such mechanism, defined as creating distinguished sets of procedures of which only one execution may happen at a time; together with the remark in section 3.4 that even for programs to be executed on a sequential computer, writing them as if they were to be executed concurrently forces the programmer to avoid inessential timing constraints and thus makes programs more modular.
