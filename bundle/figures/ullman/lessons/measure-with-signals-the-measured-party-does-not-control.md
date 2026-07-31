---
type: lesson
title: "A metric survives adversaries only if the measured party doesn't own its inputs"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# A metric survives adversaries only if the measured party doesn't own its inputs

**Lesson:** When a score determines who gets rewarded, the people being scored will optimise against it, so the only durable question about a ranking function is not how well it correlates with quality but who controls the data it reads. A metric computed entirely from artifacts its subject authors is not a measurement, it is a request — the subject simply writes whatever produces the number they want. Relocating the inputs so they come from parties with no stake in that particular subject's score changes the cost of gaming from "edit your own file" to "convince strangers," and that cost differential, not any statistical property, is what makes the metric hold up.

The move generalises past ranking. Any time a system reads self-reported state and acts on it, ask what it costs the reporter to lie. Self-declared priority fields, client-supplied timestamps, user-set retry counts, agent-reported health, contributor-declared test coverage: all of these are scoring functions whose inputs are owned by the party the score is about. The fix is structurally identical — derive the value from observations made by components that do not benefit from the outcome, or from aggregate behaviour too diffuse for any one participant to move. Note that this is not about trusting people less; it is about arranging the dependency graph so that trust is not load-bearing in the first place.

The second half of the technique matters as much as the first, and it is the part usually skipped. Sourcing a metric externally is not enough if the external sources can themselves be manufactured cheaply. A naive external count — how many other parties vouched for you — collapses the moment creating a voucher is free, because the adversary just creates a million of them. What rescues it is making the weight of a vouch depend recursively on the weight of the voucher, so that fabricated endorsers carry almost none. That recursion is the real design idea: the score's own scarcity is defined self-referentially rather than by an external gatekeeper, which means it needs no allowlist to maintain and no manual policing to keep working as the population grows.

The practical discipline is to write down, for every quality signal a system consumes, the cheapest action that inflates it. If the answer is an action the measured party can take alone, the signal is decorative and will eventually be worthless. If the answer requires shifting the behaviour of parties who are themselves expensive to influence, the signal has a defensible floor. That analysis takes minutes and should happen before the metric is implemented, because retrofitting adversary-resistance onto a deployed score usually means discarding it.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the opening of the link-analysis chapter, which recounts how term-based ranking collapsed under pages stuffed with invisible keywords, and explains why judging a page by anchor text on pages that link to it, combined with a recursively defined importance score, resists both keyword stuffing and mass-produced link farms.
