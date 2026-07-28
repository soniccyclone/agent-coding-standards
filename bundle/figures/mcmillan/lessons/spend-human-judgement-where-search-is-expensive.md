---
type: lesson
title: "Spend human judgement where search is expensive and machine effort where it is cheap"
figure: mcmillan
works: [symbolic-model-checking-for-sequential-circuit-verification]
axes: [cognitive-load, verifiability]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Spend human judgement where search is expensive and machine effort where it is cheap

Full automation is usually treated as the goal, with any human input counted as a defect. This paper argues something more interesting: automation is a continuum, and the productive question is which end of it each *particular* decision belongs at. The authors are explicit that a user of their method must supply several things the tool cannot find for itself — an ordering for the decision-diagram variables, a way of carving the step relation into pieces, an order for processing those pieces, and sometimes a better starting set for the search. They then report that these hints, cheap for someone who understands the circuit, buy improvements in growth rate that no amount of internal cleverness had produced.

What makes the argument rather than a concession is the reframe that supports it. The authors point out that computing reachable configurations is really the automatic construction of an invariant, which turns a black-box search into a collaboration: the human proposes a candidate region, the machine does the tedious work of closing it under the step relation and checking it avoids the bad configurations. Crucially, the candidate does not have to be right in any strong sense — it only has to discharge the obligation, and a region larger than the truly reachable one is perfectly acceptable if it still excludes failure. That tolerance is what makes human guessing safe: a bad guess costs time, never soundness.

The division of labour that emerges is principled rather than pragmatic. Humans are good at structural intuition — which parts of a system talk to which, which quantities are naturally grouped, what a quiescent configuration looks like — and terrible at exhaustive case analysis. Machines are the reverse. A tool that demands only structural hints and does all the case analysis itself is exploiting both sides. Their asynchronous example makes this vivid: describing every settled configuration of the circuit by hand is easy, and starting the search there instead of from a single power-on configuration collapses the work dramatically.

A programmer who takes this on board stops treating a configuration knob as an admission of failure and starts asking, per decision, whether a person or a search is the cheaper oracle. They design tools that accept hints and validate them rather than tools that either guess silently or demand a full proof. And they look for the reframing — from "compute the answer" to "check my candidate" — that makes human input admissible without making it trusted.

**Source:** [Symbolic Model Checking for Sequential Circuit Verification](../works/symbolic-model-checking-for-sequential-circuit-verification.md) — the discussion of reachability as automatic invariant construction, and the closing section weighing degree of automation against the scalability gains that user-supplied structure provides.
