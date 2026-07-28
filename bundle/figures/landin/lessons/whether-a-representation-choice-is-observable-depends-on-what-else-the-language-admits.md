---
type: lesson
title: "Whether a representation choice is invisible depends on what else the language admits; adding effects promotes it into a semantic decision"
figure: landin
works: [correspondence-algol-60-church-lambda-notation-part-i]
axes: [expressiveness, verifiability, parallelizability]
subdomains: [programming-languages-and-semantics, foundations-of-computation, software-engineering-and-architecture]
tags: [lesson]
---
# Whether a representation choice is invisible depends on what else the language admits; adding effects promotes it into a semantic decision

**Lesson:** Some implementation decisions are supposed to be beneath notice: whether an intermediate aggregate is built out fully or produced one piece at a time as consumers demand it changes how much store the program needs and how large a job fits, but not the answer. That invisibility is not a property of the decision. It is a property of the language the decision is made inside. In a setting where expressions only denote, a consumer has no way to detect which strategy was used, because the only observable is the result and both strategies give the same one. Once expressions can also disturb shared state, the two strategies become distinguishable — how many of the producing steps ran, and when, is now part of what the program did — and a choice that was free becomes a commitment with consequences.

The structural consequence is unpleasant and easy to miss: as soon as the difference is observable, the two representations have to be named apart. You can no longer have one vocabulary of operations that works on either, because a caller now needs to say which behaviour it wants, and operations that construct must be kept distinct from operations that merely inspect, since construction is exactly where the commitment to evaluate gets made. The cost of admitting effects therefore isn't paid only at the effect site; it is paid in the surrounding vocabulary, which has to grow a parallel set of names for the sequenced case.

For a working programmer this reframes the usual argument about laziness, streaming, batching, memoisation and reordering. None of these are locally good or bad. They are invisible in exactly the region of your system where nothing observes anything but results, and become semantic — thus part of your contract, thus untouchable without a version bump — the moment observation is possible. So the useful question is not "is streaming safe here?" but "what is the largest region of this system in which the difference cannot be detected?" Keep the effectful parts small and identifiable and the whole space of representation strategies stays yours to change; let effects diffuse and every performance decision you have already made silently becomes a promise you did not know you gave.

**Source:** [A Correspondence Between ALGOL 60 and Church's Lambda-Notation: Part I](../works/correspondence-algol-60-church-lambda-notation-part-i.md) — the section on modelling iteration lists, where Landin replaces list-valued control sequences with demand-driven producers and observes that the substitution is undetectable in the purely applicative setting but detectable, and hence in need of its own separate operations, once assignment is present.
