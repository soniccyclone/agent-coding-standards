---
type: work
title: "The Part-Time Parliament"
figure: lamport
description: The original paper presenting what became known as Paxos, an algorithm for reaching consensus among processes that may crash and messages that may be lost or delayed, without ever compromising correctness. Frames the whole thing as an allegory about a fictional Greek legislature conducting business despite legislators wandering in and out. Notoriously hard to parse because of that framing, which is exactly why Lamport later wrote a plainer follow-up.
subdomains: [distributed-systems-and-concurrency]
year: 1998
url: https://lamport.azurewebsites.net/pubs/lamport-paxos.pdf
access: public
host: self-archived
tags: [work]
---

# The Part-Time Parliament

**Venue/year:** ACM Transactions on Computer Systems 16(2), May 1998 (also SRC Research Report 49; first submitted 1990)
**Source:** https://lamport.azurewebsites.net/pubs/lamport-paxos.pdf — self-archived PDF on Lamport's own site, live and directly downloadable (HTTP 200).

## Lessons
- [Derive the algorithm from the conditions that make it correct, so the proof precedes the code](../lessons/derive-the-algorithm-from-its-invariant.md)
- [Reason about concurrent programs through invariants over states, never by enumerating interleavings](../lessons/prove-concurrent-programs-with-invariants-not-interleavings.md)
- [Reduce every distributed coordination problem to agreeing on one sequence of commands](../lessons/reduce-coordination-to-an-agreed-command-sequence.md)
