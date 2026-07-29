---
type: lesson
title: "The field's history is your cheapest experiment"
figure: stonebraker
works: [what-goes-around-comes-around]
axes: [primitive-count, cognitive-load]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# The field's history is your cheapest experiment

Reading three decades of proposals side by side produces an uncomfortable result: the supply of genuinely new modelling ideas is tiny, and most "next generation" designs are recombinations of things already built, already shipped, and already found wanting. That is not a complaint about originality — it is a source of free evidence. If a proposal's structure matches something that was tried before, then its failure modes were measured by someone else, on real users, at full scale, at no cost to you. Ignoring that record does not make you an innovator; it makes you rerun an expensive experiment whose result was published.

The survey's sharpest use of this is predictive rather than historical. It takes a then-ascendant proposal, strips the marketing, and observes that what remains is a hierarchy plus inter-record references plus set-valued fields plus multiple inheritance plus type unions — that is, a superset of a model that had already collapsed under its own complexity, with a few features nobody had dared attempt. From that structural match it forecasts specific consequences: harder view definition, harder independence, complexity pressure toward a sane subset. A designer who can perform that reduction gets to argue about a design before it has any users, using nothing but a correspondence to prior art.

So the practice is to translate every proposal, including your own, into a neutral vocabulary that discards the syntax and names, and then ask what it is isomorphic to. The vocabulary matters: as long as each camp describes its design in its own idiosyncratic terms, the recurrence is invisible and the debate reduces to two sides talking past each other. A programmer who believes this reads old papers as a form of testing, treats "this resembles X, which failed for reason R" as an actionable objection rather than a snub, and keeps enough historical vocabulary to notice the resemblance in the first place.

**Source:** [What Goes Around Comes Around](../works/what-goes-around-comes-around.md) — the paper's framing device throughout, most concretely where it reduces the semi-structured proposals to a superset of the earlier network model and predicts the consequences.
