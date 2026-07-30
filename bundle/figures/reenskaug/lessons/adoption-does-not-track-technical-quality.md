---
type: lesson
title: "Whether a component gets adopted is uncorrelated with how good it is"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Whether a component gets adopted is uncorrelated with how good it is

**Lesson:** A shared component only pays for itself if people use it, which sounds tautological until you look at what actually predicts use. Not technical merit: sophisticated, carefully built components sit unused in libraries while mediocre ones get picked up by everybody. Not documentation volume either, and this is the part that should unsettle anyone who has tried to fix adoption by writing more — brief instructions fail because they leave the reader unable to apply the thing, exhaustive instructions fail because nobody will read them, and the two failures are not opposite ends of a dial you can tune between. Something else is determining the outcome.

The something else is whether the component fits the consumer's goals, existing habits, and competence — which makes adoption a human problem wearing technical clothing. A builder's instinct is that producing a good component is the hard part. It isn't. The hard part is producing one that people not only need but will actually reach for, and those are different targets that happen to overlap sometimes. This also explains why the usual remedies miss: better implementation and longer manuals are both moves within the technical frame, and the constraint is not in that frame.

The practical consequence is that the interesting design work happens before any of the building. What do these people already do? What vocabulary do they already have? What would they have to stop doing to adopt this, and is that trade obviously worth it from where they stand rather than from where you stand? A related caution from the same material: automating something people currently coordinate by talking to each other often solves a problem they do not have. The example is exact — a proposal for a system letting engineers navigate each other's overlapping drawings turned out to be unwanted, because what the engineers actually needed was the *names* of the two or three people working nearby, so they could pick up the phone. The elaborate version was more impressive and less useful, and it took asking a practitioner to find that out.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 5's introduction to reuse, where the author reports his own successful and unused components, states the success criterion as actual use, observes that outcomes track neither technical excellence nor documentation length, concludes the problem is essentially human, and gives the North Sea drawing-coordination anecdote as illustration.
