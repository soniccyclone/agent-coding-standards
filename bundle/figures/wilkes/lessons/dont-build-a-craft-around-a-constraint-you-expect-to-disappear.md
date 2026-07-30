---
type: lesson
title: "Refuse to build a craft around a constraint you expect the technology to remove"
figure: wilkes
works: [computers-then-and-now]
axes: [cognitive-load, hardware-affinity]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Refuse to build a craft around a constraint you expect the technology to remove

**Lesson:** When an implementation constraint makes naive use of a system slow, a body of skill grows up around evading it, and that skill is genuinely effective — practitioners get real speedups, publish techniques, and acquire status for mastery. The question a designer has to ask anyway is whether the constraint is intrinsic to the problem or an artifact of the current mechanism. If it is an artifact, every hour poured into the evasion technique is an investment in an asset that will be written off, and worse, the technique's presence shapes programs, tooling and habits around a property of the substrate that is about to stop being true.

Acting on that judgment means declining to participate in something demonstrably useful right now, which is uncomfortable and hard to defend at the time. The defence is not that the technique does not work; it is that skill has a shelf life determined by the constraint it exploits, and that effort has better places to go when the constraint is scheduled for removal by forces outside your control. Betting on the constraint disappearing can of course be wrong — the discipline is to make the bet explicitly, on a stated reading of where the substrate is heading, rather than drifting into the evasion because everyone else is doing it.

The general form of the question is worth asking about any optimization that requires knowing something about the layer below: is this fact about the machine permanent, or is it this year's machine? Optimizations against permanent facts compound. Optimizations against transient ones leave behind a codebase whose structure encodes a mechanism nobody remembers, which is the most expensive kind of legacy — not code that is slow, but code whose shape has no remaining explanation.

**Source:** [Computers Then and Now](../works/computers-then-and-now.md) — the passage on the flourishing subject of optimum coding for delay-line and drum memories, and the decision not to pursue it at Cambridge on the grounds that truly random-access memory would arrive and make that ingenuity a poor long-term investment.
