---
type: lesson
title: "Clarity is not a downstream service function: an unclear specification is a symptom of a defective design"
figure: hoare
works: [the-emperors-old-clothes]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Clarity is not a downstream service function: an unclear specification is a symptom of a defective design

**Lesson:** The standard organizational arrangement treats the description of a system as a deliverable produced after it, by different people with writing skill. That arrangement rests on a premise that does not hold: that obscurity in a description is a property of the prose. It usually is not. Where the description is muddled, the design underneath it is muddled in the same place, and a skilled writer applied to the muddle can only produce fluent text that conceals it — which is worse than the original, because it removes the last visible evidence of the defect. So the two artifacts have to be built together, by the same person, each pulling on the other: the attempt to state what the thing does exposes the parts that were never decided, and the decisions then change what can be stated.

That gives you a gate condition worth enforcing before a project starts rather than a review to perform afterwards. If the specification cannot be made clear, do not begin; the lack of clarity and the deficiency it reflects are one fault with two faces, and both have to be removed at the same time. This is much cheaper than the alternative, since at that point the only cost of a design change is rewriting a description, whereas the same defect discovered during construction costs whatever has been built on top of it. It also gives an honest use for the feeling of not wanting to write the description down — that reluctance is information about the design, not about your writing.

The same non-delegability extends upward and outward. Explaining the work to the people who fund it, schedule it and sell it is part of the engineering job, in a form they can actually use, and treating it as somebody else's function is how a project accumulates decisions imposed from above without appreciation of what they imply. Those imposed decisions are legitimately a grievance, but they are also a consequence: an organization that cannot see inside the work will manage it by the only signals it has. The obligation runs both ways, and both directions are discharged by the same practice of stating plainly, early, what is being built and what it will cost.

**Source:** [The Emperor's Old Clothes](../works/the-emperors-old-clothes.md) — the notes from the October 1965 inquest, which record that the hope of making up deficiencies in program specifications through the skill of a technical writing department was misguided, that the design of a program and the design of its specification must be undertaken in parallel by the same person and must interact, that a lack of clarity in specification is one of the surest signs of a deficiency in the program it describes with both faults to be removed before the project is embarked upon, and that programmers had a duty to educate their managers and other departments by presenting the necessary information in simple palatable form.
