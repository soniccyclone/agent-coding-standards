---
type: work
title: "Synchronization in Distributed Programs"
figure: schneider
description: Develops a general technique for synchronizing processes in a distributed program that may itself experience process failures — extending synchronization concepts built for single-machine shared memory into a setting where messages and machines can be lost. Shows the technique both as a way to solve synchronization problems directly and as a building block for implementing higher-level synchronization mechanisms and distributed versions of familiar ones. Sits between Schneider's earlier work on proving concurrent-program correctness and his later state-machine-replication framework, part of the same throughline toward making fault-tolerant coordination rigorous.
subdomains: [distributed-systems-and-concurrency, programming-languages-and-semantics]
year: 1982
url: https://www.cs.cornell.edu/fbs/publications/synchDistProg.pdf
extraction: complete
survey_pages: 24
survey_text_layer: full
survey_fetch_mb: 1
access: public
host: self-archived
tags: [work]
---

# Synchronization in Distributed Programs

**Venue/year:** ACM Transactions on Programming Languages and Systems 4(2), April 1982.
**Source:** https://www.cs.cornell.edu/fbs/publications/synchDistProg.pdf — self-archived PDF on Schneider's own Cornell publications page (`cs.cornell.edu/fbs/publications/`), live and directly downloadable (HTTP 200, `application/pdf`, ~1.5MB). Phase 1 pass had flagged this `paywalled` (it does sit behind ACM DL at dl.acm.org/doi/10.1145/357162.357163); the author's self-archived copy resolves that.

## Lessons
- [When a technique cannot express a requirement, suspect the requirement: use the failure as a probe](../lessons/an-unimplementable-condition-indicts-the-specification.md)
- [Make every distributed decision rule immune to learning more, and interference disappears](../lessons/decisions-that-later-news-cannot-falsify.md)
- [Derive knowledge from what a participant can no longer say, not from what it has said](../lessons/infer-from-what-a-participant-can-no-longer-say.md)
- [Start from the extravagant version nobody could build, then compress it to exactly what the decisions read](../lessons/start-from-the-extravagant-version-then-compress.md)
- [Broadcast the reason you are waiting, not just the fact of it, and global questions turn into local ones](../lessons/broadcast-the-reason-you-are-waiting.md)
- [The cost of coordination is set by the size of its audience, so shrink the audience before tuning the protocol](../lessons/shrink-the-audience-before-optimizing-the-protocol.md)
- [A designated role is hidden state that has to be rebuilt after a crash; symmetric designs have nothing to re-elect](../lessons/a-role-is-state-that-must-be-rebuilt.md)
