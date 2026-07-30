---
type: lesson
title: "Separate what a reader can already do from what they can only recognize, and layer the documentation on that seam"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Separate what a reader can already do from what they can only recognize, and layer the documentation on that seam

**Lesson:** Linguists distinguish active vocabulary — the words you use — from passive vocabulary, the larger set you understand when someone else uses them. Carry the distinction over to skill and you get active competence, the things you can do, versus passive competence, the things you can follow when you watch someone else do them but could not easily produce yourself. Almost everyone's passive competence vastly exceeds their active competence, and the gap is not a deficiency; it is what makes it possible to work with systems you could not have built.

That gap is the right organizing principle for documentation, and it explains why the usual two options both fail. A terse instruction list works only for someone whose *active* competence already covers the task — it jogs memory, it does not teach — and it is dangerous otherwise, because it reads like road directions: reliable if you are starting where the author assumed and going where the author assumed, catastrophic if you improvise slightly, since you have no way to tell that you have left the path. An exhaustive explanation fails differently: it teaches, but nobody reads it under time pressure. Neither is wrong; each is aimed at a different competence and fails when it is the only thing on offer.

So stack them, cheapest first. On top, the terse instructions — deliberately near-cryptic, aimed at producing a sudden "aha" that starts a competent reader down the right track without binding the details, which are within their ability and must be adapted anyway. Beneath that, a map: enough structure to orient someone whose passive competence needs activating, and — the load-bearing part — enough context to make misuse recognizable, which the instruction layer structurally cannot provide. Beneath that, the implementation account, which is a supplier's active competence and most consumers' passive competence. A reader descends only as far as their own gap requires. The design question for any explanation therefore becomes "which competence am I writing for, and what protects the reader who does not have it?" — and where you grant freedom to use something in many ways, that layer is also where the constraints belong, separated into the ones that must not be violated and the ones that may be, deliberately, by someone who understands the risk and accepts it.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 5's treatment of communicating with component consumers, which introduces active and passive competence by analogy to vocabulary, proposes the three layers (List of Instructions, Logical map, Implementation description) with the road-directions caution about the terse layer, and separately distinguishes required from recommended constraints.
