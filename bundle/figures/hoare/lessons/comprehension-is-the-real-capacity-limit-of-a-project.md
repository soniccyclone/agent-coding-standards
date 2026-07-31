---
type: lesson
title: "Comprehension is a project's real capacity limit: build nothing the accountable person cannot follow"
figure: hoare
works: [the-emperors-old-clothes]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Comprehension is a project's real capacity limit: build nothing the accountable person cannot follow

**Lesson:** The standard reply to "you let people build things you do not understand" is that no individual could possibly hold a whole modern system in their head, so the objection is naive. It is not naive; it is a statement about what your throughput actually is. Delegation distributes the work of construction, but it does not distribute the work of judging whether the pieces fit, whether the schedule is real, or whether the whole thing is worth building. Whoever is accountable performs that judgement using their own model of the system, and where the model is absent the judgement is not made by someone else — it is not made at all. Every part nobody accountable understands is a part whose plan, resource use and interfaces are being checked by no one, and the failure shows up late, in aggregate, as an inexplicable inability to deliver.

Taken as a constraint rather than an insult, this reshapes planning. The size of what you may attempt is bounded by what the responsible party can hold, so the way to attempt more is to raise that ceiling — by simplifying the design until it fits, or by splitting accountability so that each part has someone who genuinely holds it — not by pretending the ceiling is irrelevant because the org chart has more boxes. It also explains why a rescue works when it applies the rule literally: allow only work whose design and schedule you can follow, cap each piece at a duration short enough that the follow-through stays intact, require the person proposing it to convince you that both the need and the plan are real, and refuse everything that fails those tests regardless of how strategic it looks.

The rest of the rescue pattern follows from the same root. Prefer the request you can actually satisfy soon over the ambitious one you can only promise; delivered small things restore the trust that promised large things destroyed, and the gratitude they earn is out of all proportion to their difficulty. Make plans and withhold promises until you have calculated rather than estimated. And treat any re-estimate produced by the same process that produced the last missed one as containing no information whatsoever: when a team that has slipped twice reports that three more months will do it, they are not lying, they are running the procedure that has already failed twice, and the only remedy is to go into the project yourself far enough to understand it — which is exactly the thing that was skipped when it was set up.

**Source:** [The Emperor's Old Clothes](../works/the-emperors-old-clothes.md) — the senior manager's diagnosis that the project failed because its designer let programmers build what he himself did not understand, Hoare's initial dismissal and later acceptance of it, the recovery procedure of assigning small teams per customer group, choosing the easiest request, capping features at three months, making plans but not promises, and permitting nothing the manager did not understand, together with the earlier passage where he disregards the third round of revised schedules and digs into the project instead.
