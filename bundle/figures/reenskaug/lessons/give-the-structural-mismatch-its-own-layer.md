---
type: lesson
title: "When two structures legitimately disagree, give the disagreement its own layer"
figure: reenskaug
works: [mvc-its-past-and-present]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, databases-and-data-management]
tags: [lesson]
---
# When two structures legitimately disagree, give the disagreement its own layer

Shared data services get organized for throughput, integrity, and central control. The way a particular person conceives of the same information is organized around the job they are trying to do, and different people doing different jobs conceive of it differently. Reenskaug's move is to treat the mismatch between these as normal rather than as a defect on either side: if the storage structure happens to match someone's conception, fine, nothing is needed; when it does not, the answer is neither to distort the shared services toward one constituency's view nor to force that constituency to think in storage terms, but to interpose a layer whose declared purpose is to sustain the appearance of a structure the substrate does not have.

Naming the layer for what it does is the substantive part. Every system already contains this translation work; the question is whether it is a located, owned thing or whether it is smeared across whichever code happened to need it. Smeared, it is invisible, duplicated inconsistently, and impossible to change deliberately, and it quietly leaks storage-shaped concepts upward into code that was supposed to be about the problem. Given a home, it becomes reviewable, and each side of it gets to be optimized honestly for its own criterion — the substrate for integrity and efficiency, the upper layer for match with how people think.

Reenskaug is candid about the instability this creates, which is what makes the pattern usable rather than glib: there is a standing pull to migrate logic downward into the shared services for easier maintenance and central control, and an equal pull to hoist it upward into the illusion layer so the people who own the problem control it. That tug is not resolvable once and for all. It is a boundary you keep adjudicating, and knowing that in advance is more useful than a rule about which side wins.

A programmer who works this way stops treating a mapping layer as regrettable overhead to be eliminated by making the two ends agree. Some pairs of structures are both correct and cannot be made to agree, because they answer to different criteria. The design question becomes where the translation lives and who owns it, not how to avoid needing it.

**Source:** [The Model-View-Controller (MVC): Its Past and Present](../works/mvc-its-past-and-present.md) — the domain/user matrix pattern, which introduces a layer above the domain services whose job is to create the impression that the system implements each user's own model, along with its statement of the opposing pressures on where logic settles.
