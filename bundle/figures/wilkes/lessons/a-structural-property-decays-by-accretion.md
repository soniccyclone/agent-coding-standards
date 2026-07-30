---
type: lesson
title: "A structural property decays through additions that individually violate nothing, so audit the property rather than the changes"
figure: wilkes
works: [cambridge-cap-computer-and-its-operating-system]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# A structural property decays through additions that individually violate nothing, so audit the property rather than the changes

**Lesson:** A component can begin with a clean structure, accumulate facilities one at a time over years, and end up with a property thoroughly broken that no single addition broke. Each new facility looked reasonable in isolation and nobody involved had a proper appreciation of the cumulative effect, because the effect is a fact about the whole and reviewing changes one at a time cannot see it. This is a general failure mode of change review, not a lapse of attention: a property that holds over an aggregate has to be checked against the aggregate, periodically, by something that recomputes it from scratch. A mechanically checkable structural property should be checked mechanically, since the audit will find what every individual review passed.

Worse, the window for repair closes at exactly the point the problem becomes visible. By the time the drift is understood, the code usually works — it has been debugged, its clients depend on it, and nothing observable is wrong. At that moment the incentive to restore the structure is close to zero, and the ruggedness that repair would have bought is invisible precisely because it is a reduction in the severity of failures that have not happened. So the practical rule is that structural repair has to be done while the thing is still being fought with. Any plan of the form "we will clean up the structure once it works" is a plan not to clean it up.

Behind both of these sits an admission worth adopting as an expectation rather than a regret: a designer's understanding of a program grows while the program is being built, so it is rarely possible to produce a genuinely well-structured program on the first attempt. That is an argument for planning the restructuring pass into the schedule, and for placing it before the point of working rather than after — not for trying harder to get the structure right in advance, which the growth of understanding makes impossible.

**Source:** [The Cambridge CAP Computer and Its Operating System](../works/cambridge-cap-computer-and-its-operating-system.md) — Chapter 5's account of how the system's internal-name manager began simple and accumulated facilities until its authorities were no longer properly separated, the independent static audit that found considerable overprivilege, the absence of incentive to fix it once the dependent programs had been debugged, and the concluding observation that designers' understanding grows with development so a well-structured program is rarely achieved on a first attempt.
