---
type: lesson
title: "Look for the one description scheme that makes unrelated activities turn out to be the same activity"
figure: goldberg
works: [personal-dynamic-media]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [programming-environments-and-object-systems, programming-languages-and-semantics]
tags: [lesson]
---
# Look for the one description scheme that makes unrelated activities turn out to be the same activity

**Lesson:** Drawing something that moves, arranging sound in time, and writing a program look like three unrelated crafts, each with its own traditions and its own notation. This work's central technical bet is that they are three sensory presentations of one underlying thing — a process unfolding over time under coordinated control — and that a language which describes processes directly will make the shared structure visible rather than leaving it as a loose analogy. That is a claim about where to look for abstractions: not by generalizing upward from existing feature sets, but by asking what the activities *are* once their sensory surface is removed, then providing a vocabulary at that level.

Two things follow if the bet lands, and both show up here. First, a mechanism found in one domain transfers rather than needing reinvention: the recognition that a description of movement is separable from the thing being moved shows up once as a frame sequence that can drive any of several drawings and again as a set of directions that can be handed to any of several voices. Those are the same idea appearing twice because the vocabulary was shared, not because someone noticed the parallel afterwards and copied it. Second — and this is the argument made explicitly on pedagogical grounds — a learner who acquires the description scheme in one domain has already acquired it in the others. Effort spent understanding how to say "this happens, then that, in step with the other thing" is spent once. Under a family of domain-specific notations, the same effort is spent per notation, and the structural identity is never available as knowledge at all because nothing in the tools ever states it.

There is a cost worth naming, because it is the reason this move is not free. Committing to one vocabulary means every domain gives up its native idiom, and specialists will feel that loss immediately and concretely while the payoff (transfer, reuse, unified reasoning) accrues later and diffusely. This work is willing to pay it, and the reported outcome is the justification: practitioners in genuinely different fields built working instruments for themselves in the same medium, which is only possible if the medium sits below all of their specialities rather than beside them.

A programmer holding this view resists the reflex to add a sublanguage per problem area, and instead treats the appearance of a second notation for structurally similar work as evidence that the common substrate has not been found yet. The concrete diagnostic is the transfer test: if learning the second area teaches you nothing you already knew from the first, the two are still being described at the wrong level.

**Source:** [Personal Dynamic Media](../works/personal-dynamic-media.md) — the passage that groups animation, music, and programming as differing views of dynamic processes and credits the common framework with making their similarities apparent, together with the animation and music systems in which directing instructions are deliberately held separate from whatever performs them, and the note on why a single cross-domain vernacular helps a learner.
