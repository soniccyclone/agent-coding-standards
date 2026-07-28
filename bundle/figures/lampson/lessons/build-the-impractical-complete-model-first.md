---
type: lesson
title: "Build the impractically simple model that is obviously complete, then name exactly what it lacks — the conventions you add back are the real system, and they will grow their own lives"
figure: lampson
works: [protection]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Build the impractically simple model that is obviously complete, then name exactly what it lacks — the conventions you add back are the real system, and they will grow their own lives

**Lesson:** A good way to attack a problem you cannot see the shape of is to first construct a version of the system that is unarguably adequate and unarguably too slow to build. Take the extreme: participants that share literally nothing, communicating only through an ordered stream of messages whose sender is stamped by the substrate. Nothing is shared, so nothing can be reached without permission, and the entire question of access control disappears by construction. That model is not a proposal. Its value is that it settles what the problem is by exhibiting one complete answer, and it makes every subsequent decision legible as a departure taken for a reason rather than as an unexamined feature of whatever you happened to build.

The second step is where the real work happens: state precisely what the ideal model cannot do. Here, two things. You cannot regain control of a participant that stops cooperating — it can waste resources indefinitely and there is no way to compel or destroy it, which is what makes it impossible to develop software against. And you cannot get participants to work together without an elaborate scaffolding of shared agreements about names, formats, and meanings, all of which must be arranged out of band. Both deficiencies are about the absence of a shared frame rather than about protection at all. Recognizing that is what tells you the next layer is a naming and convention layer, not a security layer, and that the security properties you already have will be preserved or destroyed by how you build it.

The analogy Lampson draws is the one to keep: a bare protection mechanism is as unusable on its own as a bare processor is for writing programs, and for the same reason. A processor needs loaders and formats and assemblers before anyone can work with it, and those accessories rapidly become their own subject, with their own complexity and their own designers. The same fate is certain for the conventions layered over a minimal mechanism. That is not a failure of the minimal mechanism; it is a prediction about where the system's real mass will end up, and therefore where the design attention should go. Anyone who has ever thought a small elegant kernel would keep the whole system small has ignored this prediction.

A programmer who works this way starts every unfamiliar design with a deliberately unaffordable reference version whose correctness is self-evident, uses it to enumerate what practicality costs, and treats the convention layer as a first-class design problem with its own naming schemes and its own tendency to sprawl. The habit pays twice: it produces a specification of the intended semantics that survives all later optimization, and it keeps you honest about which of your departures from it were forced and which were merely convenient.

**Source:** [Protection](../works/protection.md) — the protection-domains section, which introduces the idealized message system, works through the properties it delivers for free (protected call and return, unforgeable sender, external timeout), then names its two flaws and compares a bare protection mechanism to a bare central processor awaiting its conventions.
