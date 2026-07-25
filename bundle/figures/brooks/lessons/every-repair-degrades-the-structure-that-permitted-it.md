---
type: lesson
title: "Design for the cost of changing the thing, knowing that every repair erodes the structure that made repair possible"
figure: brooks
works: [mythical-man-month]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Design for the cost of changing the thing, knowing that every repair erodes the structure that made repair possible

**Lesson:** Fixing a defect carries a substantial probability of introducing another, high enough that maintenance advances roughly two steps for every one it loses. The mechanism is instructive. A subtle fault presents as a local symptom while having consequences spread through the system, so a repair aimed at the symptom cures what is visible and leaves what is not, unless the structure is clean enough or the record complete enough to make the reach of the change apparent. The person doing the repair is usually not the person who wrote the code, and is often the least experienced hand available. Both conditions are normal rather than exceptional, which means the expected cost of a change is a property of the design rather than of anyone's diligence.

Measured across successive releases of a large system, the count of modules grows steadily while the count of modules disturbed per release grows far faster. Effort migrates from correcting the original design toward correcting the corrections, and the ordering that made the system tractable decays until forward progress stops. Construction reduces disorder and is therefore inherently precarious; maintenance increases it, and even excellent maintenance only postpones the point at which the thing is no longer usable as a base to build on. Meanwhile machines, configurations, and needs move underneath it, so the arrival of that point is certain.

Two consequences follow for how to design. First, every technique that localizes the effect of a change repays itself many times over, and the payment is collected in the maintenance years rather than the construction months. Encapsulating a module so that its interior is genuinely private, and reachable only through operations proper to it, is the strongest known form of that localization; the competing instinct, to expose everything to everyone so that mismatched assumptions get caught by inspection, catches interface errors at the price of a system nobody can change safely. Second, change should be quantized rather than continuous: numbered versions, freeze dates, and batched updates give everyone downstream intervals of stability, and a fix applied urgently should be marked as provisional in the source itself so the distinction between a patch and a considered repair survives.

**Source:** [The Mythical Man-Month](../works/mythical-man-month.md) — the chapter on planning for change, with its account of maintenance as an order-destroying process and the release-over-release evidence for structural decay, together with the retrospective chapter's reversal of the book's earlier hostility to shielding programmers from each other's internals.
