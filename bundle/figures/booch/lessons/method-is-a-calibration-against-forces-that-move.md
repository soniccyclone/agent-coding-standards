---
type: lesson
title: "Design is the resolution of forces that keep moving, so method is a calibration and never a doctrine"
figure: booch
works: [architecting-the-unknown, the-future-of-software-engineering, building-the-enchanted-land]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Design is the resolution of forces that keep moving, so method is a calibration and never a doctrine

**Lesson:** Building a system is not optimizing one objective; it is finding a settlement among pressures that pull in different directions and that have no common unit. Budget and schedule pull one way, tolerated failure rate another, compatibility with what already exists another, the capabilities of the actual people on the team another, and legal and ethical exposure another still. None of these reduces to the others, so there is no scalar to maximize, only a balance to strike and defend. Recognizing this stops two common failures: pretending a technical decision was purely technical, and pretending a hard constraint imposed from outside the engineering group is not a design input.

Because the settlement depends on where you sit in that force field, method choice is a measurement problem rather than a matter of conviction. At minimum, three readings matter: how much ceremony the actual team composition requires, how bad failure is, and how large the thing and its coordination surface are. A practice that is correct for a small group of exceptional people building something disposable is wrong for a distributed organization of ordinarily skilled engineers building something that can kill someone, and the reverse is equally true. Anyone claiming a single practice is universally right has implicitly assumed one point in that space and generalized from it. The productive question about any methodology is not whether it is correct but for which region of that space it was calibrated, and where you are relative to that region.

The hardest part is that the forces are not static. Regulation shifts, hardware economics shift, the market's expectations shift, and, worst of all, deploying the system changes the environment the system was designed for, so success itself invalidates parts of the original balance. There is no equilibrium to reach and hold. A programmer who internalizes this does not seek the right architecture once; they build the capacity to re-resolve, keeping the reasoning behind each balance point explicit enough to revisit when a force moves, and treating any design justification of the form "this is simply best practice" as a claim that has quietly dropped its arguments.

**Source:** [The Future of Software Engineering](../works/the-future-of-software-engineering.md) — the enumeration of business, contextual, developmental, and human pressures on a project, the insistence that they are dynamic and that a deployed system perturbs its own environment, and the three-dimensional characterization of methodology by formality, risk, and scale. Also [Architecting the Unknown](../works/architecting-the-unknown.md), which uses the same three dimensions to argue against any single correct process, and [Building the Enchanted Land](../works/building-the-enchanted-land.md), which restates development as force resolution and adds the social and ethical pressures now bearing on it.
