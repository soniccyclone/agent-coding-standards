---
type: lesson
title: "Absence is not a value — keep 'unknown' distinct from 'lowest'"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, verifiability, primitive-count]
subdomains: [databases-and-data-management, algorithms-and-complexity]
tags: [lesson]
---
# Absence is not a value — keep 'unknown' distinct from 'lowest'

**Lesson:** When observations are collected into a grid indexed by two populations, the overwhelming majority of cells will have nothing in them, and the representation you choose for those cells decides what the whole analysis means. Filling them with the bottom of the scale is the natural implementation choice — it makes the structure dense, uniform, and easy to compute over — and it is a substantive falsehood. It asserts that every unobserved pair was evaluated and found wanting, when in fact it was never evaluated at all. Every downstream aggregate then silently averages in an enormous mass of fabricated negative evidence, and because the fabrication is uniform it does not look like noise; it looks like a strong, consistent signal that everything is bad.

The distinction becomes acute with implicitly gathered data, which is the common case, because implicit signals are one-sided by construction. An action taken tells you something; an action not taken is compatible with dislike, with ignorance of the option's existence, with lack of opportunity, and with intending to get to it later. Those are radically different states and the data does not distinguish them. A system built on such signals therefore has exactly one observable value and a great many blanks, and any method that requires a second value has to manufacture it — which is a modelling decision deserving explicit argument, not a default arising from how the array was allocated.

The practical discipline is to make the absent state representable in the type rather than encoded as an in-range value, so that no computation can consume it without deciding what to do about it. Sparse structures that simply omit unobserved pairs enforce this naturally, which is a second reason to prefer them beyond memory. Where an aggregate must be formed, form it over the observed entries only, and carry the count of observations alongside the aggregate so that a confident-looking figure resting on two data points can be recognised as such.

This generalises well past preference data. Missing telemetry is not zero load, an unpopulated column is not an empty string, a metric that stopped reporting is not a metric reading zero, and every one of these confusions has taken down production systems whose alerting averaged in the silence. Whenever a value is being defaulted, ask what claim the default makes and whether the data supports it.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the recommendation-systems chapter's model section, which defines the preference grid as mostly unknown, and its discussion of populating that grid from behaviour, noting that such data has only one value and that a zero written in place of a blank is not a lower rating but no rating at all.
