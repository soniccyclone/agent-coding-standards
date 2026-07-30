---
type: lesson
title: "Built-in flexibility is a wager paid up front; adaptability comes from people, not parameters"
figure: naur
works: [programming-as-theory-building]
axes: [cognitive-load, primitive-count]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Built-in flexibility is a wager paid up front; adaptability comes from people, not parameters

**Lesson:** Designing in the ability to absorb changes nobody has asked for yet is routinely treated as prudence, but price it honestly and it is a purchase of an option. Each point of variability has to be conceived — which range of futures it covers, what knob controls it — then built, exercised, and explained, and every one of those costs is certain while the payoff is contingent on events that may never arrive. Cheap flexibility, where the general shape costs no more than the specific one, is worth taking. Beyond that the trade is a forecast about the world dressed up as an engineering practice, and the forecast is usually made by the people least positioned to make it: whoever is at the keyboard before the system has met its users.

There is a compounding cost past the build price. Variability that nothing currently exercises still has to be held in mind by everyone reasoning about the system afterward, and it enlarges the set of configurations any claim about behavior must cover. So speculative generality does not sit inertly waiting to be useful; it taxes every subsequent change, including the ones that turn out to be needed. Machinery that is finally used once, years later, may still have cost more in accumulated drag than writing the specific thing twice.

The argument's real force is in what it forces you to fall back on. Since the world will keep changing in ways no parameterization anticipated, the general capacity to adapt a system cannot be built into the system at all; it lives in people who understand what the system is doing and can therefore restructure it when the demand arrives. Investing in comprehension — keeping the people who have it, growing more of them — is the response that scales with unforeseen change, whereas investing in configurability only covers changes you already imagined. Build for the case you have, and buy your adaptability in the form of people who can build the next case.

**Source:** [Programming as Theory Building](../works/programming-as-theory-building.md) — the discussion of program flexibility within the analysis of modification costs: the itemized cost of each flexibility feature against a payoff dependent entirely on future events, and the conclusion that built-in flexibility cannot answer the general need to adapt programs to changing circumstances.
