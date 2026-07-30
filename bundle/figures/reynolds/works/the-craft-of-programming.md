---
type: work
title: "The Craft of Programming"
figure: reynolds
description: A textbook that teaches programming with specification and proof as first-class concerns from the start, rather than as debugging bolted on after the fact. It works through fundamental data structures and control constructs with a running emphasis on correctness arguments and cost analysis, reflecting Reynolds's view that a programmer should be able to justify a program's behavior, not just observe it. Went out of print with Prentice-Hall, after which Reynolds reclaimed the rights and released it himself.
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
year: 1981
url: https://www.cs.cmu.edu/afs/cs/user/jcr/ftp/craftprog.pdf
survey_pages: 449
survey_text_layer: full
survey_fetch_mb: 33
access: public
host: self-archived
tags: [work]
---

# The Craft of Programming

**Venue/year:** Prentice-Hall International Series in Computer Science, 1981.
**Source:** https://www.cs.cmu.edu/afs/cs/user/jcr/ftp/craftprog.pdf — live PDF (HTTP 200, ~34MB scanned copy), self-archived by Reynolds in his own CMU FTP directory. His page https://www.cs.cmu.edu/~jcr/craftprog.html explains: "It is now out of print, and all rights have reverted to the author, who has decided to make it publicly available."

## Lessons
- [Comment the part of a program that holds still, because the code already shows you what moves](../lessons/document-what-holds-still-not-what-changes.md)
- [To make a loop faster, loosen the relation it preserves so more of the state is free to move](../lessons/loosen-the-invariant-to-buy-freedom-of-movement.md)
- [Test whether a contract says enough by letting an adversary rewrite the state within it](../lessons/test-a-contract-by-letting-an-adversary-rewrite-the-state.md)
- [Keep facts about your mechanism separate from facts about your subject matter, and give them exactly one joint](../lessons/confine-domain-facts-to-one-designated-joint.md)
- [Learn the formal method so you can tell when the informal argument is enough](../lessons/learn-the-formal-method-to-know-when-to-skip-it.md)
- [Find the loop's invariant by asking how much of the goal you can have for free](../lessons/split-the-goal-into-the-free-part-and-the-earned-part.md)
- [When the uniform algorithm fails at one edge, try extending the definition before adding a branch](../lessons/extend-the-definition-instead-of-branching-on-the-edge-case.md)
