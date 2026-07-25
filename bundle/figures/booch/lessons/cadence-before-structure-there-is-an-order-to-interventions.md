---
type: lesson
title: "Interventions have a mandatory order: a project without a release rhythm cannot be reasoned about yet"
figure: booch
works: [architecting-the-unknown, the-future-of-software-engineering, building-the-enchanted-land, the-promise-the-limits-and-the-beauty-of-software]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Interventions have a mandatory order: a project without a release rhythm cannot be reasoned about yet

**Lesson:** Diagnosis of a troubled project usually produces a list of everything wrong, which is useless because the items are not independent and cannot be worked in parallel. There is an order, and the first item is whether the project produces something that runs on a regular period. The specific period is domain-dependent and arguing about it is a distraction; what matters is that one exists, because a regular cadence is what converts opinions about the system into observations of it. Without it, every subsequent judgment, including every architectural judgment, rests on claims that cannot be checked. Advice offered to a project in that state is worthless no matter how good the advice is, which is why the correct response to an irregular release process is to fix that and nothing else first.

Second in the order is whether the group has a shared conception of the system's structure and some means of steering it. This does not require a designated role or a document; it requires that the significant decisions are visible enough to be examined and adjusted deliberately rather than emerging from the accumulated preferences of whoever touched the code last. Without that, the direction of the system is not controlled by anyone, in either the technical or the economic sense, and improvements land unpredictably. With a rhythm and a means of steering in place, most of what remains genuinely is detail, and the standard remedies of consolidation, modelling, and testing become worth discussing because there is now a mechanism for applying them and observing the result.

The clinical framing is worth keeping because it enforces the sequencing. A project bleeding out does not need nutrition; it needs the bleeding stopped, and then it can be treated. The order also has an upper bound worth noting: a cadence so tight that no interval exists in which anything can be reconsidered creates its own pathology, since features accumulate and nobody ever has standing to remove any. A programmer who works this way resists the urge to lead with the most interesting technical criticism, establishes observability of the project before diagnosing its design, and reads a request for architectural advice from a group with no release rhythm as a request for something else.

**Source:** [Architecting the Unknown](../works/architecting-the-unknown.md) — the two health measures taken on entering an organization, build-and-release cadence first and architectural governance second, with the explicit claim that the cadence must be fixed before anything structural is addressed. Also [The Future of Software Engineering](../works/the-future-of-software-engineering.md) and [Building the Enchanted Land](../works/building-the-enchanted-land.md), which restate the same two questions and the same ordering, and [The Promise, the Limits, and the Beauty of Software](../works/the-promise-the-limits-and-the-beauty-of-software.md), which adds the upper bound on cadence: a release interval too short to permit reconsideration produces unchecked feature accumulation.
