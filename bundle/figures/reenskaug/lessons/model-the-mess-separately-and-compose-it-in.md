---
type: lesson
title: "When the ugly requirement arrives, describe it somewhere else and compose, rather than spoiling the clean description"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# When the ugly requirement arrives, describe it somewhere else and compose, rather than spoiling the clean description

**Lesson:** A description that captures a problem cleanly is a real asset, and the ordinary way it gets destroyed is one justified addition at a time. Error handling has to go somewhere. So does the retry logic, the audit trail, the special case for the one customer, the thing that only happens at month end. Each is individually necessary and each is individually small, and the cumulative effect is that the clean description is gone and nobody can point at when it went. The instinct to just add them is strong precisely because refusing feels like refusing the requirement itself.

The alternative is to treat the arrival of an awkward concern as a signal to open a *second* description rather than to extend the first. Model the error handling as its own thing, with its own participants and its own account of what happens, and then produce a third description that is explicitly the composition of the two. You now have three artifacts where you previously had one, which sounds worse and is usually better: the original clean description survives intact and can still be reasoned about and reused on its own, the awkward concern is somewhere it can be understood without wading through unrelated logic, and the composite exists for exactly the questions that require seeing both at once.

The judgement this demands is knowing which additions deserve their own description and which genuinely belong in the original — a rule of thumb worth carrying is that a concern deserves separation when you can state its purpose without mentioning the host's purpose. It also demands that your composition mechanism be good enough that the third artifact is cheap to produce and trustworthy once produced; if composing is expensive or unreliable, people will keep inlining. And it reframes what a "clean" design is: not one that never met an ugly requirement, but one where you can still find the part that was clean.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 3's argument for choosing derived models over in-place extension, which uses error handling as the worked example of a concern that would clutter away a clean solution and recommends a separate model plus a combining one instead.
