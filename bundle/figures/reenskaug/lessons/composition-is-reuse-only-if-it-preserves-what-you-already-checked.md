---
type: lesson
title: "Composition is reuse only when it preserves what you already checked"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Composition is reuse only when it preserves what you already checked

Reenskaug splits combination into two kinds and makes the distinction turn on verification rather than on mechanism. In the good case, combining established pieces automatically retains the correctness each piece already had, so the result needs no fresh examination of what was settled before. In the other case, the combination can invalidate properties the pieces held individually, and the only honest response is to re-examine the whole result from scratch. Both are the same operation as far as the tooling is concerned. They differ entirely in what you are entitled to still believe afterwards.

The distinction is the actual content of the word reuse. If every assembly forces a re-analysis of the assembled whole, then nothing was reused except keystrokes: the expensive part of a component is the confidence in it, and that confidence has not transferred. This is why Reenskaug attaches the strong requirement specifically to things intended for reuse — a piece meant to be applied in situations its author never saw must be built so that its guarantees survive being combined, and a piece that only holds together in contexts you personally checked is not a component but a draft.

He then declines to ban the unsafe kind, which is what makes the distinction usable rather than merely pious. Combining pieces in ways that may break their guarantees is a legitimate and even valuable thing to do while trying to understand a phenomenon: you assemble a picture of how several concerns interact, learn from it, and accept that the result must be verified as a whole. The error is not doing it; the error is doing it without knowing which of the two you did, and then treating an unverified composite as though it inherited its parts' credibility.

A programmer holding this asks of every combining mechanism what it preserves, and keeps exploratory assemblies separate from load-bearing ones. It also reframes the design of a reusable component: the goal is not maximal generality but guarantees stated so they cannot be quietly voided by whoever uses it, since a guarantee that composition destroys was never really available.

**Source:** [Working with Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — the treatment of safe versus unsafe synthesis in the technology overview, including the argument that safe composition is a prerequisite for building large systems from independently correct base models and the deliberate allowance for unsafe composition during analysis.
