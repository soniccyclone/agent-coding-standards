---
type: lesson
title: "When the workaround for a slow tool starts dictating how you decompose the program, the tool is the bug"
figure: hoare
works: [hints-on-programming-language-design]
axes: [cognitive-load, verifiability]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# When the workaround for a slow tool starts dictating how you decompose the program, the tool is the bug

**Lesson:** Tool latency does not stay in the tool. Once a build is slow enough to hurt, practitioners restructure their work to avoid paying the full cost, and that restructuring silently becomes the architecture. The historical case is the shift from making translation fast to making it avoidable: split the program into separately processed units so that unchanged units need not be reprocessed. The saving is real and the collateral damage is larger. Unit boundaries get chosen for reprocessing granularity rather than for the structure of the problem, so pieces end up too small to express anything coherent. Interfaces widen and acquire ceremony at exactly the places where the problem wanted no boundary at all. Worst of all, the checking that would have caught mistakes across those boundaries is precisely the checking that separate processing gives up — errors concentrate at interfaces, and the mechanism removes the interface check. Add the reluctance to change a data representation because of what it would cost to reprocess everything, and a latency problem has become a design-freeze problem.

The general shape is worth recognizing on sight: a mechanism introduced to dodge a cost, which then imposes a structural constraint on everything built with it. The reflex to resist is treating the mechanism as the thing to improve. Improving it entrenches it. The productive move is to attack the original cost directly and see whether the mechanism is still wanted afterward — and often the honest measurement is embarrassing, because the avoidance machinery turns out to cost more than the work it avoids. When incremental savings really are needed, prefer mechanisms that snapshot work already done and resume from it, rather than mechanisms that partition the program permanently: a checkpoint preserves the single-artifact, fully-checked property, while a partition destroys it.

The same reasoning applies to escape hatches. A boundary crossing whose only purpose is to reach a lower level of abstraction should not be built out of the general-purpose boundary mechanism, since that pays full interface cost at the one place where cost is the reason for crossing. Let the lower level appear inline, where the surrounding context is still visible and still checkable.

**Source:** [Hints on Programming Language Design](../works/hints-on-programming-language-design.md) — the Fast Translation discussion, its catalogue of what independent compilation does to program structure and interface checking, its alternatives based on saving and restoring compiler or program state, and the closing remarks on linking to machine code.
