---
type: lesson
title: "Settle design arguments by building whole systems, not with exercises or with objections nobody has tested"
figure: brinch-hansen
works: [monitors-and-concurrent-pascal-a-personal-history, the-solo-operating-system-processes-monitors-and-classes, the-programming-language-concurrent-pascal]
axes: [expressiveness, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Settle design arguments by building whole systems, not with exercises or with objections nobody has tested

**Lesson:** Small examples are the wrong instrument for evaluating a construct, and they mislead in a specific direction: they reward whatever is most elegant at small scale, which is rarely what matters at working scale. The question of which waiting-and-signalling discipline a coordination primitive should have looks like a question about tiny producer/consumer fragments, and at that size all the candidates look fine and the choice looks like taste. It resolves only after several complete systems have been written, at which point the plainest first-come discipline turns out to be the convenient one — a conclusion no amount of reasoning over exercises produced. The general form is that a construct's real cost is in what it does to a program too large to hold in your head, and only a program of that size can measure it.

The same standard applies with more force to objections. A published concern about nested calls through mutually-exclusive modules ran for years across multiple papers, accumulating restatements and worried elaborations, and never once arriving with a program or a measurement, until somebody finally pointed out that the problem had never been stated well enough to be solvable. Meanwhile the author had already used the supposedly dangerous pattern throughout three working systems, where it was not merely harmless but the inevitable consequence of the structure. The asymmetry is worth internalizing: a design objection unaccompanied by a construction is a hypothesis, and treating it as a finding has real costs, because effort spent defending against imaginary failure modes is effort not spent on the ones that actually appear.

The other half of the discipline is publishing what you built in a form that can be checked. A complete system with every line open to inspection lets a reader form their own judgement about whether the approach scales, and invites the reuse that eventually produced the strongest external evidence — modules lifted from one system into an unrelated one, integrating without interface trouble and yielding a single defect. A programmer who works this way is slower to have opinions and much harder to argue out of the ones they have, because the opinions are attached to artifacts.

**Source:** [Monitors and Concurrent Pascal: A Personal History](../works/monitors-and-concurrent-pascal-a-personal-history.md) — the retrospective sections on neglected problems, which report that the choice among signalling schemes was settled only by writing operating systems and that the nested-call objection circulated for years without evidence while the pattern was already in service. Also [The Solo Operating System](../works/the-solo-operating-system-processes-monitors-and-classes.md) — published as a complete annotated system rather than as excerpts. Also [The Programming Language Concurrent Pascal](../works/the-programming-language-concurrent-pascal.md) — presented alongside a working system built in it rather than as a paper design.
