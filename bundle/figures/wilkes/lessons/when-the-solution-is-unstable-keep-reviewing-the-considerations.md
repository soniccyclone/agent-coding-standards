---
type: lesson
title: "When a design problem has unstable solutions, keep reviewing the considerations instead of studying the artifacts"
figure: wilkes
works: [best-way-to-design-an-automatic-calculating-machine]
axes: [cognitive-load, hardware-affinity]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# When a design problem has unstable solutions, keep reviewing the considerations instead of studying the artifacts

**Lesson:** Some design problems are ill-conditioned in a specific sense: two comparably skilled teams with comparable backgrounds, working independently on the same problem, will produce entirely different results. That is not a failure of either team, and it is not a sign that the problem is badly stated. It is a property of a problem whose outcome depends sensitively on the project's scale, the team's experience, and the state of the surrounding technology at the moment the decisions were forced. Recognizing that a problem has this character changes what you should do with existing solutions: they are evidence about the conditions their designers faced, not answers to be copied or benchmarks to be beaten.

The corollary is that a designer working such a problem must take decisions without knowing at the time whether they are right, and no amount of care removes that. What can be done instead is to keep the *considerations* under continuous review rather than the conclusions — to hold explicitly which underlying pressures the design is responding to, so that when a technological premise shifts you can tell which decisions were premised on it. A design maintained this way survives change by being re-derivable. A design maintained as a set of conclusions has to be rebuilt from nothing whenever one of its unstated premises fails, and nobody knows which conclusion depended on which premise.

There is a matching stance toward one's own output. On a problem whose solutions are unstable, the honest posture is to raise the issues and expose the trade-offs rather than to present a settled thesis, because a settled thesis about an unstable problem overstates what its author can know. Openly unfinished reasoning that names the pressures is more useful to the next designer than a confident recommendation that hides them.

**Source:** [The Best Way to Design an Automatic Calculating Machine](../works/best-way-to-design-an-automatic-calculating-machine.md) — the opening remarks on the instability of the machine-design problem, the dependence of the outcome on scale, team background and current device technology, and the stated intention to raise issues rather than settle them.
