---
type: lesson
title: "Price a metaphor by the actions it actually produces"
figure: wirth
works: [project-oberon]
axes: [cognitive-load, hardware-affinity]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Price a metaphor by the actions it actually produces

**Lesson:** A design metaphor is adopted because it is evocative, and it is then defended on the same grounds, which is why bad ones survive. The corrective is to stop arguing about whether the metaphor is apt and instead trace what a user does under it, step by step, in the common case. Very often the trace reveals that the distinguishing feature of the metaphor is undone before any real work happens: the state it so carefully models is one that people move out of immediately, so the machinery that maintains that state faithfully is machinery that maintains a transient. Once you can say that, the comparison becomes concrete — this much implementation effort and ongoing complexity, in exchange for fidelity to a configuration nobody operates in — and the decision makes itself.

The habit generalizes to any feature justified by resemblance to something familiar. Ask what sequence of operations the resemblance actually causes. Ask whether the situations the feature exists to handle are ones the user passes through or ones the user stays in. Ask what the simpler alternative would cost the user in the cases the feature was meant to cover — not in the cases the metaphor makes vivid. A feature whose benefit is real but small, and whose cost is structural and permanent, is worse than one whose benefit is zero, because the small benefit keeps it from ever being removed.

The reason this matters beyond individual features is compounding. Each complication that is not commensurate with its benefit also becomes a constraint on everything built afterwards, because subsequent parts must be compatible with it, and the effort it consumed was effort not spent on the parts that carry the design. A system's compactness is not achieved by shrinking things at the end; it is achieved by declining, one at a time, the complications whose payoff nobody has bothered to estimate. And the estimate is usually easy to make — a walk through the actual sequence of user actions — which means the reason it goes unmade is not difficulty but the fact that nobody asked.

**Source:** [Project Oberon](../works/project-oberon.md) — section 2.2.1's assessment of overlapping windows, which reports the desk-of-piled-documents metaphor as not entirely convincing on the specific ground that partially hidden windows are typically brought to the top and made fully visible before any operation is applied to their contents, contrasts that insignificant advantage with the substantial implementation effort the scheme requires, names it a good example of a case where the benefit of a complication is incommensurate with its cost, and records the choice of a tiled arrangement as much simpler to realize with no genuine disadvantage; together with section 1's ground rule, adopted in response to a deliberately small team, to concentrate on essential functions and omit embellishments that merely cater to established conventions and passing tastes, and section 2.3's remark on the correlation between a system's size and its reliability and on consuming a resource lavishly merely because it happens to be cheap.
