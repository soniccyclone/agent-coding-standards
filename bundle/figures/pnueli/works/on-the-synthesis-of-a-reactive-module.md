---
type: work
title: "On the Synthesis of a Reactive Module"
figure: pnueli
description: Poses the reactive-synthesis problem — given a temporal-logic specification relating inputs to outputs, construct a program satisfying it automatically rather than writing one and verifying it after the fact. Pnueli and Rosner show the problem reduces to validity of a branching-time formula over tree models, prove decidability for finite domains via a new emptiness check for Rabin tree automata, and establish the (doubly exponential) complexity. It reframed verification's endgame: the specification itself becomes the program's source.
subdomains: [formal-methods-and-verification]
year: 1989
url: https://dl.acm.org/doi/pdf/10.1145/75277.75293
access: public
host: institutional
tags: [work]
---

# On the Synthesis of a Reactive Module

**Authors:** Amir Pnueli and Roni Rosner.
**Venue/year:** Conference Record of the 16th ACM Symposium on Principles of Programming Languages (POPL 1989), pp. 179-190. DOI 10.1145/75277.75293.
**Source:** https://dl.acm.org/doi/pdf/10.1145/75277.75293 — ACM's own copy, free under the open backfile program (ACM opened its 1951-2000 publication archive in 2022; POPL 1989 is in range).

**Verification caveat (2026-07-24):** automated fetches of this URL hit ACM's
Cloudflare bot-check rather than the PDF, so unlike every other `work` file
in the corpus this one could not be machine-verified end to end. `access:
public` rests on three independent corroborations instead: Unpaywall reports
`oa_status: gold` at this exact URL, Semantic Scholar reports
`openAccessPdf.status: GOLD` at this exact URL, and ACM's documented
1951-2000 open-backfile policy covers the venue. A human clicking the link in
a browser gets the paper; a bot doesn't. One manual click would close the
loop for good.

## Lessons
- [Treat whatever you do not control as an adversary, not a partner](../lessons/treat-what-you-do-not-control-as-an-adversary.md)
- [A specification must fix what the implementation is allowed to know, and when](../lessons/a-specification-must-fix-what-is-knowable-when.md)
- [The formalism a requirement is natural to state in need not be the one it is settled in](../lessons/state-it-in-one-formalism-decide-it-in-another.md)
- [Bill the unavoidable blowup to the input dimension that stays small in practice](../lessons/bill-the-blowup-to-the-dimension-that-stays-small.md)
