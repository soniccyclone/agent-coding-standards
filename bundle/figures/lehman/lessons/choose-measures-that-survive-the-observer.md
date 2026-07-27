---
type: lesson
title: "Choose a coarse measure that survives the observer over a fine one that drifts, and order your data by causality rather than by the clock"
figure: lehman
works: [metrics-and-laws-of-software-evolution-the-nineties-view]
axes: [verifiability]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Choose a coarse measure that survives the observer over a fine one that drifts, and order your data by causality rather than by the clock

**Lesson:** When you set out to measure something about a system's history, the instinct is to pick the finest-grained available quantity. That instinct is usually wrong. What a measure needs is not resolution but invariance under the things you are not studying: who did the counting, which programmer wrote the code, what incentives were operating that year, which decade the data comes from. Counting lines of code is finer-grained than counting units of decomposition, and it is worse — because units of decomposition carry at least some functional integrity within a given domain while a line carries none, and because line counts move with individual style and collapse entirely once anyone is rewarded for producing them. A coarser measure that means the same thing to every observer supports comparisons across twenty years and across unrelated organizations; a finer one that means something different to each observer supports nothing.

The same test disqualifies measures that require judgment to compute. A quantity whose value depends on how a rater interprets definitions and assigns weightings has an unknown reproducibility across raters, resists automation, and — decisively for historical work — will not be found in anyone's archives, because nobody was recording it. Availability is not a lesser criterion than validity here. A slightly wrong number you can obtain for a hundred releases across several decades will teach you more than a better-defined one you can obtain for nothing. The honest position is to say plainly that the chosen measure is coarse and to keep looking for a better one, while refusing to wait for perfection before measuring at all.

The choice of independent variable deserves the same scrutiny as the choice of measure. Calendar time looks like the natural axis, but for a system that only becomes uniquely defined at the moment of release, the meaningful ordering is by release rather than by date, and the ordering by release is not always the ordering by date. A version can ship before an earlier-numbered one is finished, while still having inherited work first done for that earlier one — so its true predecessor in the evolution is the one it inherited from, not the one that happens to have the nearer date. Ordering by inheritance rather than by clock is not bookkeeping fussiness; it decides whether the trend you plot reflects how the system actually developed or an artifact of shipping schedules.

A programmer who thinks this way builds their instrumentation around quantities that will still mean the same thing when someone else reads them in ten years, and is explicit about which axis their history is plotted against and why. They also treat the discovery that a measure has become an incentive target as a reason to stop trusting it, not a reason to try harder to normalize it.

**Source:** [Metrics and Laws of Software Evolution - The Nineties View](../works/metrics-and-laws-of-software-evolution-the-nineties-view.md) — the section on system growth, which argues for module count over lines of code and over function points, and the earlier discussion of release sequence numbering as a pseudo-time axis with its worked example of a release whose date order and evolutionary order disagree.
