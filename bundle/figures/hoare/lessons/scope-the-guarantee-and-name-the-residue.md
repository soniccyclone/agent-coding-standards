---
type: lesson
title: "Scope a guarantee to what you can actually discharge, and push the residue somewhere it can be detected"
figure: hoare
works: [an-axiomatic-basis-for-computer-programming]
axes: [verifiability, hardware-affinity]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Scope a guarantee to what you can actually discharge, and push the residue somewhere it can be detected

**Lesson:** A guarantee about a program usually bundles together claims of very different character, and the bundle is only as portable as its worst member. Claims about the relationship among values when the work is done are a matter of the program's text; claims that the work will be done at all depend on things the text does not contain — how much storage exists, how wide a number can be, how long the surrounding system will tolerate the attempt. Insisting on the combined claim drags every one of those environmental facts into the argument, which is how a piece of reasoning that should be valid everywhere becomes valid only on the machine it was performed for. The productive move is to weaken the claim deliberately: assert what will be true *given that the program finishes*, prove that much from facts about the text alone, and treat finishing as a separate question with its own methods.

The weakened claim is not a cop-out because the residue does not evaporate; it relocates to where it can be handled. Some of it is genuinely provable — an argument that a repetition cannot run forever is a real argument about the text. The rest is resource exhaustion, and resource exhaustion is best answered not by a proof but by an implementation that refuses to fabricate an answer, stopping loudly at the moment a limit is violated instead of producing a value derived from a limit nobody reasoned about. Split this way, each part is attacked with the instrument suited to it, and neither part is quietly assumed.

The general habit is worth more than the particular split. Whenever a desired guarantee turns out to be unprovable, ask what weaker guarantee *is* provable and what precisely is left over, rather than abandoning the attempt or asserting the strong version on faith. The weaker claim is often nearly all of the value, and the leftover is usually a small, nameable set of environmental conditions — at which point the honest design is to convert each into an explicit condition of use or an explicit runtime check. A system that states "this holds provided X" and enforces X at the boundary is in far better shape than one that states the unqualified claim and is wrong in cases nobody enumerated.

**Source:** [An Axiomatic Basis for Computer Programming](../works/an-axiomatic-basis-for-computer-programming.md) — the general-reservations section, which reads the notation as a conditional claim contingent on termination, identifies non-termination as arising from both infinite repetition and violated implementation limits, and argues for proving conditional correctness while relying on the implementation to warn when a limit forced abandonment.
