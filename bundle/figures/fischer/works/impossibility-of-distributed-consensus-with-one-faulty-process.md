---
type: work
title: "Impossibility of Distributed Consensus with One Faulty Process"
figure: fischer
description: Proves that no deterministic protocol can guarantee agreement among asynchronous processes if even a single process can fail, no matter how the protocol is designed. The argument works by showing an adversary scheduler can always find some pending event that keeps the system in an undecided ("bivalent") state indefinitely, so termination and fault-tolerance can never both be guaranteed. This is the FLP result — the founding impossibility theorem of distributed consensus theory, cited constantly to justify why practical systems settle for randomization, weaker failure models, or partial synchrony instead of pure asynchronous determinism.
subdomains: [distributed-systems-and-concurrency]
year: 1985
url: https://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf
access: public
host: self-archived
tags: [work]
---

# Impossibility of Distributed Consensus with One Faulty Process

**Author(s):** with Nancy A. Lynch and Michael S. Paterson
**Venue/year:** Journal of the ACM 32(2):374-382, April 1985
**Source:** https://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf — self-archived PDF on Nancy Lynch's own paper archive at MIT CSAIL (co-author's site), live and directly downloadable (HTTP 200). Confirmed against MIT CSAIL TDS group's own bibliography (reflist.html), which lists this exact file for this exact citation.

## Lessons
- [Reason about a protocol by what it has not yet ruled out, not by tracing its runs](../lessons/reason-about-what-remains-undecided.md)
- [Without a timing assumption, slow and dead are the same observation](../lessons/a-slow-participant-and-a-dead-one-are-the-same-observation.md)
- [The binding constraint on a distributed component is what its local view cannot tell apart](../lessons/what-cannot-be-distinguished-bounds-what-can-be-decided.md)
- [A negative result gets its reach from how little it demands and how much it permits](../lessons/assume-less-to-forbid-more.md)
- [The useful payload of an impossibility result is the short list of assumptions it needs, not the negative verdict](../lessons/the-assumption-ledger-is-the-real-result.md)
- [Connect the executions nobody can tell apart, then walk the chain to a contradiction](../lessons/connect-the-executions-you-cannot-tell-apart.md)
