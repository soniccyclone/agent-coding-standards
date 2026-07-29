---
type: lesson
title: "Local correctness does not compose when \"correct\" depends on the caller's purpose"
figure: reenskaug
works: [a-dci-execution-model]
axes: [verifiability, cognitive-load]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Local correctness does not compose when "correct" depends on the caller's purpose

The tacit promise of building software out of independently specified parts is compositional: get each part right on its own terms and the assembly will be right too. Reenskaug names this as an assumption rather than a theorem, and then names the condition under which it fails — when the behavior a part ought to exhibit is a function of the collaboration it is currently participating in, no specification of the part in isolation can pin down the correct behavior, because the information that determines correctness is not present inside the part. The specification is not merely incomplete; it is looking in the wrong place.

This is why declaring a component correct against its own interface can be simultaneously true and useless. The interface enumerates what the component will do with each message it receives, and says nothing about which messages are appropriate, in what order, or on whose behalf. A unit that answers every question it is asked can still be participating in a wrong conversation, and no amount of local rigor detects that. Whole classes of production defects live in the gap: not one part malfunctioning, but every part functioning exactly as documented while the assembly does something nobody intended.

The practical shift is where you put verification effort and where you allow yourself to feel confident. A programmer who believes this treats the interaction — the whole set of participants plus the order they speak in plus the purpose they serve together — as itself an object of specification requiring its own artifact, rather than as something to be reconstructed by mentally tracing calls. It also reframes the value of a system as residing in the arrangement of parts rather than being the sum of the parts' individual merits, which means design review that only inspects components is inspecting the cheap half of the problem.

**Source:** [A DCI Execution Model](../works/a-dci-execution-model.md) — the introduction's diagnosis of the "faulty assumption" behind class-based programming, and the accompanying point that a class-only notation can describe one participant at a time and therefore cannot describe a system of communicating participants at all.
