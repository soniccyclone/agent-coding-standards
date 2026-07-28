---
type: lesson
title: "Step outside the system and reason about every expression it admits, not the ones you happen to want"
figure: post
works: [introduction-to-a-general-theory-of-elementary-propositions]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [foundations-of-computation, formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# Step outside the system and reason about every expression it admits, not the ones you happen to want

Whitehead and Russell worked inside their system, deriving the particular results they needed further downstream, each one interesting on its own merits. Post's move is to stop deriving and start describing: he treats the totality of expressions the grammar can produce as a single mathematical object, pictures it as an ever-widening array, and then proves things about that object. The change in altitude is the whole contribution. Statements like "the axioms reach exactly the right conclusions and no others" and "nothing further can be added without collapse" are not results you can reach by proving one more theorem inside the system, however many you prove. They live one level up, and you can only get at them by treating the machinery as data rather than as a tool you are currently using.

The same gap shows up constantly in engineering and is usually mistaken for a testing shortfall. A suite of passing cases is a set of inside-the-system derivations: each is real, and no accumulation of them tells you the property you actually want, which is invariably universally quantified over inputs, over schedules, over configurations, over versions. Grammar ambiguity, protocol deadlock freedom, whether a permission model can be escalated, whether a config space contains an unreachable state — every one of these is a statement about the space of admissible artifacts, and every one requires stepping out and enumerating or characterizing that space rather than sampling it. The characteristic symptom of not having stepped out is a project that keeps discovering surprising-but-legal inputs.

Post also insists on an uncomfortable part of the discipline, and it is what makes this more than a slogan. Reasoning about a system requires reasoning *in* something, and when the thing you are studying is also the thing you think with, the standing of your result gets murky — he says so plainly about his own consistency argument, noting that the informal logic he reasons with is itself an interpretation of the formal system under study, and marks that the conclusion's significance is therefore uncertain while the formal content is unaffected. The engineering analogue is a compiler that miscompiles its own test harness, a monitoring system that cannot observe its own outage, a proof of a checker's soundness carried out using the checker. Stepping out is necessary and it is never entirely clean; a programmer who takes this seriously names the level she is standing on and what that level assumes, rather than pretending the vantage point is free.

**Source:** [Introduction to a General Theory of Elementary Propositions](../works/introduction-to-a-general-theory-of-elementary-propositions.md) — the introduction's framing that these theorems are about the logic of propositions without being part of it, together with the closing note on the ambiguous standing of a consistency argument conducted in a logic the studied system interprets.
