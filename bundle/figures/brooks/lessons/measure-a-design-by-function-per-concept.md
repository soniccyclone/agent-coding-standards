---
type: lesson
title: "Score a design by how much function it delivers per concept the user must carry; maximising function and minimising primitives both fail this test"
figure: brooks
works: [mythical-man-month]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Score a design by how much function it delivers per concept the user must carry; maximising function and minimising primitives both fail this test

**Lesson:** A system exists to make a machine easier to use, and every facility it offers is bought with something the user has to learn, remember, and search for. The description of a rich programming system runs an order of magnitude longer than the description of the bare machine underneath it, which is a real cost paid in exchange for a real saving in how quickly a task can be stated. The design is a good one when the second exceeds the first. That makes the ratio of delivered function to conceptual burden the measure, and it has two symmetrical failure modes that its partisans each mistake for excellence.

One failure is measuring by function alone. Systems whose builders competed on capability accumulate features of marginal value, each defensible on the day it was proposed, each charging performance and, more insidiously, charging ease of use in increments too small to notice while the manual thickens. A general-purpose tool is harder to design than a special-purpose one precisely because it requires weighting needs that differ across a diffuse population, and the temptation is to satisfy all of them additively. The other failure is measuring by minimality alone. A formalism can be spare in its count of elementary notions and still be awkward, because saying an ordinary thing in it requires involuted and unobvious combinations. Then learning the elements and their combination rules is not enough; there is a body of idiom to absorb on top, and that idiom is conceptual burden that the primitive count does not report.

What closes the gap between the two is coherence: every part reflecting the same choices, the same balance of priorities, analogous notions carrying analogous notation and meaning. Directness of expression is a consequence of that coherence rather than an independent property to be tuned. A designer who holds this measure asks of each proposed addition not whether it is useful but whether its usefulness exceeds what it adds to the model the user must hold, and is therefore willing to omit good ideas that do not fit the ones already there. It also gives a principled reason to scrap a design outright: when the count of important but non-integrating ideas grows large, the honest move is to restart from different basic concepts rather than to bolt them on.

**Source:** [The Mythical Man-Month](../works/mythical-man-month.md) — the chapter on system design and the coherence of concepts, which sets ease of use as the criterion and names both an operating system praised for maximal function and a language spare in elementary notions as opposite failures of it; the retrospective chapter extends the same analysis to feature accumulation in mass-market products.
