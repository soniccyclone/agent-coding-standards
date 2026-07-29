---
type: lesson
title: "Fluency in the system you left is the main source of bad idioms in the one you built"
figure: ungar
works: [programming-as-an-experience]
axes: [expressiveness, cognitive-load]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Fluency in the system you left is the main source of bad idioms in the one you built

**Lesson:** When designers remove a construct from a system, they rarely stop thinking in it. They know, from years of practice elsewhere, which arrangements of the old construct worked, and they reproduce those arrangements out of whatever the new system provides. The result passes every test, because it is built from legal pieces, and yet it quietly reimports the property the removal was supposed to eliminate. The tell is a structure that presents itself as an ordinary citizen of the new model but cannot behave like one — an object that everything else can talk to, which will fail on most of the messages its own interface advertises, because it was only ever meant to be looked at through something else. Nobody designs that on purpose; it appears when a habit from the abandoned model is transcribed rather than rethought.

The trap is specifically caused by competence. A newcomer with no history would fumble around and eventually find organizations native to the new model, because they have no cached answers to reach for. The expert has cached answers, and they are all shaped by the thing that was just deleted. So expertise makes the first generation of idioms in a new system worse than they need to be, and because those idioms ship in the standard library and the tutorials, they harden into how everyone thinks the system works. Later observers, less invested, are the ones who notice that most of the design space was never explored.

Practically, this means treating your own early idioms in a new system as provisional rather than as the discovered way. When a pattern you reached for immediately turns out to require exceptions — this object is not really usable on its own, that one must always appear in a pair, this layer needs a rule that nothing else needs — read that as a symptom of transcription, not as an unavoidable cost. Budget explicit time to look for organizations with no analogue in the previous system, and do it early, before the first idiom becomes the convention. The removal of a construct only pays off if the idioms get redesigned too.

**Source:** [Programming as an Experience: The Inspiration for Self](../works/programming-as-an-experience.md) — the retrospective on the prototypes-versus-classes discussion, where the group's habitual way of factoring shared behavior is identified as carried over from their previous class-based system, along with the resulting structures that look like ordinary objects but cannot answer most of their own messages.
