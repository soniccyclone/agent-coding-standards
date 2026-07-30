---
type: lesson
title: "Structure is a property of what a reader can see, not a record of the order you built it in"
figure: reynolds
works: [the-craft-of-programming]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Structure is a property of what a reader can see, not a record of the order you built it in

**Lesson:** Two words usually run together are worth prying apart. One names a property of the artifact: the thing is structured when someone reading it can find several levels of detail in it, each level a coherent description in its own right, coarse ones standing above fine ones. The other names a process: working from the abstract toward the concrete. Only the first is a quality of what you shipped. The second is one way — often the best way — of arriving at it, but a thing built in that order can still fail to expose any levels to a reader, and a thing assembled in the opposite order can expose them perfectly. Judge the artifact by whether the levels are visible, and never let "we refined it top-down" stand in as evidence.

Why the visible levels matter is a point about pattern rather than tidiness. A single run of a system is a long, flat sequence of tiny actions. An observer with no idea what any of it is for could watch a hundred such runs and never recover the shape they share, because the shape lives at a level of description that the sequence itself does not exhibit. Different runs agree at coarse grain and diverge as you look closer; the coarse description is precisely the thing that lets diverse concrete behaviors be recognized as instances of one intention. A structure is therefore a claim about a family of possible behaviors, not a decoration on a single one, and if the coarse level is missing from the text, that claim is nowhere.

The process question then has a real answer rather than a dogmatic one. Refining from abstract to concrete works when the target is known well enough that each refinement can be given a complete statement of what it owes before you write it — that is the whole engine, and it stalls the moment the statement is vague. When the goal is genuinely ill-defined or expected to change, the honest order is the reverse: build up solid pieces from the bottom and discover the shape they support. That is not a failure of discipline. It is the correct response to not yet knowing what you are specifying, and the resulting artifact is judged by the same test either way — can a reader see the levels.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — the opening chapter's development of behavior patterns from concrete instances, the observer-unfamiliar-with-motivation argument for why levels of detail are what make a pattern perceivable, and the explicit definitional split between a program being structured and the top-down process of creating one, including the note on when the bottom-up order is called for.
