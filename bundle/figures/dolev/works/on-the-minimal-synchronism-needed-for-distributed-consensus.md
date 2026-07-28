---
type: work
title: "On the Minimal Synchronism Needed for Distributed Consensus"
figure: dolev
description: Maps out exactly which combinations of timing assumptions — bounds on message delay, on relative processor speed, and on message order — are enough to make consensus solvable despite faults, and which combinations are not. Sits between the two extremes already known at the time: full synchrony (solvable) and full asynchrony (impossible per Fischer-Lynch-Paterson). Gives a fine-grained taxonomy of partial synchrony that later work on practical consensus protocols builds directly on.
subdomains: [distributed-systems-and-concurrency]
year: 1987
url: https://www.cs.huji.ac.il/~dolev/pubs/p77-dolev.pdf
extraction: complete
access: public
host: self-archived
tags: [work]
---

# On the Minimal Synchronism Needed for Distributed Consensus

**Author(s):** with Cynthia Dwork and Larry J. Stockmeyer
**Venue/year:** Journal of the ACM 34(1), 1987, pp. 77-97 (conference version: FOCS 1983)
**Source:** https://www.cs.huji.ac.il/~dolev/pubs/p77-dolev.pdf — self-archived PDF on Dolev's own HUJI publications page, live and directly downloadable (HTTP 200).

## Lessons
- [An omnibus assumption hides several independent dials; separate them before believing anything proved about it](../lessons/split-omnibus-assumptions-into-independent-dials.md)
- [Mine your proofs for a rule of thumb you can guess with before proving anything](../lessons/turn-your-proofs-into-a-rule-you-can-guess-with.md)
- [What a participant cannot tell apart is the whole argument](../lessons/what-participants-cannot-distinguish-bounds-every-protocol.md)
