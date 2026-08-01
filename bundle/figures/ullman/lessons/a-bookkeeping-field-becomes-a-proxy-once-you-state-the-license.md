---
type: lesson
title: "A bookkeeping field becomes a proxy once you state the license"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, verifiability]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# A bookkeeping field becomes a proxy once you state the license

**Lesson:** The quantity that would explain your data is often one nobody recorded, and the reflex is to give up on it. The alternative is to find a field that was recorded for administrative reasons, and ask what assumption would license reading it as a stand-in. A timestamp on a submitted judgement is stored so rows can be ordered and audited. It is not the elapsed time between the experience and the judgement, which is what actually matters if opinions ripen or sour. But if most people encounter a thing shortly after it becomes available, then the position of a judgement within an item's own timeline approximates that elapsed gap, and the slope of judgements over that timeline becomes readable as how the thing wears on people. The unobservable did not become observable. An assumption about typical behaviour was traded for it.

What makes this legitimate rather than sloppy is that the assumption gets said out loud and can be attacked. It has a shape: it names a population, it claims something about that population's timing, and it fails in specific describable ways, such as an item with a long tail of late discoverers or a re-release that resets the clock. A stated licensing assumption is a thing a colleague can argue with and a thing you can go and test on a subset. An unstated one is just a feature that mysteriously works and will mysteriously stop.

There is a second, sharper observation underneath. If the response to an item depends on when it was measured, then the constant you were modelling is not a constant, and no amount of better estimation will fix a model that has no place to put the dependence. The right response is to add the coordinate rather than to average over it, because averaging over a systematic time effect is not noise reduction, it is the deliberate destruction of a real signal. The general test is worth applying to any modelled quantity: sort the observations by when they were taken and look for a trend. If there is one, the quantity is a function and you have been treating it as a number.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 9's list of unintuitive facts about the Netflix challenge, where the date attached to each rating proved useful because some films are rated better immediately after viewing and others better in retrospect, and where the authors concede that the viewing-to-rating delay cannot be recovered from the data but argue that most people watch a film soon after release, which makes the slope of a film's ratings over time a usable substitute.
