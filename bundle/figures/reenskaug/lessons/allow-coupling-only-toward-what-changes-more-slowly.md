---
type: lesson
title: "Permit a dependency only in the direction of the thing that changes more slowly"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load, hardware-affinity]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Permit a dependency only in the direction of the thing that changes more slowly

**Lesson:** Given a layered system, the question of which components may depend on which is usually answered structurally — upward is forbidden, downward is fine, siblings by convention. A more useful criterion is the expected *rate of change* of each participant, because a dependency's real cost is how often it forces you to revisit something, and that is set by how often the thing you depend on moves.

Consider a system split between long-lived shared services and short-lived personal tools. Services accumulate slowly and are expected to persist. Tools are built to fit how one person currently works and should be replaced freely as that changes. Now rank the possible couplings by rate of change rather than by position. A tool depending on several services is *good* coupling: the tool is small and disposable, the services are stable, and using a tool to move information between services is flexible precisely because the fragile end is the cheap end. A service depending on another service is to be used with discretion, since it hardens the slow-moving layer where change is already most expensive. And a tool depending on another tool should be avoided outright — you have coupled two things both expected to churn, so every change to either propagates into something that was supposed to be disposable, and the property that made tools cheap is gone.

The reasoning generalizes past this particular architecture. Before allowing a dependency, ask which side moves faster and whether you are pointing the arrow at the stable thing or the volatile one. Depending on something slower than you is nearly free. Depending on something faster is a standing tax. And two fast-moving things depending on each other is the case that quietly converts a flexible system into a rigid one, because neither can now be replaced alone — which is exactly the outcome that both were designed to avoid.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 7's enumeration of integration levels in the Task/Tool/Service architecture, which endorses integrating services via tools as flexible because tool programs are smaller and simpler, advises using direct service-to-service integration with discretion because it makes the total system difficult to change, and recommends avoiding tool-to-tool integration on the grounds that tools should be created and phased out rapidly.
