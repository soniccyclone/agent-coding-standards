---
type: lesson
title: "Choose the conformance check that works in every case over the one that would be elegant"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [verifiability]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Choose the conformance check that works in every case over the one that would be elegant

**Lesson:** Suppose you want to know whether a running program still obeys the design it was built from. Three approaches present themselves. Analyse the source and compare it against the design — appealing, complete in principle, and honestly assessed as a hard research problem that probably will not work in the general case. Invent a higher-level language whose constructs map directly onto the design concepts, so conformance is structural — genuinely interesting, and it makes conformance somebody's *language* project rather than something you can do today. Or record what the program actually does while it runs and compare the recording against the design automatically, flagging every interaction the design does not permit.

The third is the weakest in theory: it only sees the paths you exercise, so it can never prove conformance, only detect specific violations. It is the right choice anyway, on two grounds. It applies in all cases, needing no new language and no research breakthrough. And it produces something the other two do not — a record of how the design actually behaves under load, which routinely teaches the designer things about their own design that no static check would have surfaced. A partial answer available today beats a complete answer available never, and the partial answer has a side benefit the complete one lacks.

One practical wrinkle is worth carrying, because it is the first thing you hit. The checker flags everything the design does not sanction, and your test scaffolding is not in the design. In the worked example every non-conformance reported was a timer attached to a *dummy* door, added to simulate the door taking real time to open and close. The tool was right each time; the violations were instrumentation. So a clean report is not the default state you drift from — it is something you achieve by explicitly accounting for your own harness, and a checker that could tell design violations from scaffolding would have to be told which is which.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 8's section on executable specifications, which enumerates the three ways of establishing that program logic conforms to a role model, dismisses static code analysis as a hard research problem probably not feasible in general, notes the new-language option as under exploration, and selects monitored execution because it gives the designer insight and is applicable in all cases; plus the worked trace where every flagged non-conformance traces to a timer in the dummy Door implementation.
