---
type: lesson
title: "The class hierarchy will not tell you how the thing works; only the collaboration will"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# The class hierarchy will not tell you how the thing works; only the collaboration will

**Lesson:** Faced with an unfamiliar library, the natural first move is to study its type hierarchy. It is the most visible structure, it is what the documentation is organized around, and it looks like a map. Reported plainly here, after browsing a well-commented library with the explicit goal of understanding how one of its windows was built: the hierarchy did not help. What was needed instead was to look at how the objects in an actual live window talk to each other — a structure the hierarchy does not encode and cannot be derived from it.

The reason is that inheritance and collaboration answer unrelated questions. A hierarchy records where implementation was shared, which is a decision about avoiding duplication among *definitions*. Behaviour arises from which instances hold references to which others and what they send along them, at runtime, in one particular configuration. Two classes far apart in the hierarchy may be the tightly-coupled pair that produces the effect you are chasing, while two siblings may never meet. Studying the hierarchy to learn behaviour is a category error that feels productive because you are learning *something*.

The practical consequence is a different default when you have to understand foreign code. Do not start by reading the type declarations top-down. Get a running instance, capture its actual object graph — who points at whom — and identify the recurring interaction patterns in it. The same recurring shape usually appears several times over in one live structure, and once named it explains far more than the class list did. This is also the honest defence of keeping collaboration descriptions at all: they record something the code's own dominant structure genuinely does not express, which is why an overview that would be hard to reconstruct from classes is worth writing down.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 9's reverse-engineering step, which reports that the class hierarchy did not help the authors understand the design of a window and its parts and that they clearly needed to study how objects collaborate in an actual window rather than how their classes relate; and the later remark that the role models give an overview of the input facilities that would be hard to get by studying the classes.
