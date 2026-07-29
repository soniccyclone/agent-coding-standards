---
type: lesson
title: "Without the question, there is nothing in a model to judge"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [expressiveness, cognitive-load]
subdomains: [software-engineering-and-architecture, foundations-of-computation]
tags: [lesson]
---
# Without the question, there is nothing in a model to judge

Reenskaug settles the question of model correctness with an example nobody can argue with. How many wheels does his car have? Four, if the question concerns braking. Two, if it concerns acceleration, since only two are driven. One, if the question is acceleration on ice and the other is spinning. Five, if the question is which tires need checking, because forgetting the spare will eventually strand you. Three, for a car built to lift a punctured wheel and keep going. Every count is right, and each is right for exactly one question. A model cannot be correct in itself; it can only be more or less serviceable for a stated purpose, and its parts are consequences of that purpose rather than facts about the thing.

Two practical consequences follow immediately. First, a model is never complete and is not supposed to be — the whole point is to leave out more than you keep, and the omissions are the work. Judging a model by what it fails to mention is a category error unless the omission bears on the question at hand. Second, and more usefully in a team, most stubborn disagreements about a design are disagreements about the question, held by people who each believe they are arguing about the answer. Surfacing the purpose usually dissolves the argument or at least converts it into something decidable.

Reenskaug extends this to whole ways of modeling and lands on an uncomfortable point about expertise. Debates over which paradigm is better take on a doctrinal character precisely because being expert in one means having internalized its way of framing things, and the internalization makes questions outside the frame hard to pose and hard to appreciate as answers. The frame that makes you fast is the frame that makes you blind, and no amount of skill inside it substitutes for noticing when the goal has moved.

A programmer who works this way opens a design discussion by writing down what the representation must let someone decide, and treats that as the specification the model is measured against. They also expect to keep several incompatible framings of the same thing and to switch as the question changes, rather than searching for the one true structure.

**Source:** [Working with Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — the general observations about models in the chapter on modeling the real world, including the wheel-counting sequence, the insistence that models are deliberately incomplete, and the closing remarks on why paradigm arguments among experts become religious wars.
