---
type: lesson
title: "Attach state to the level you want to have several of"
figure: wirth
works: [project-oberon]
axes: [expressiveness, cognitive-load]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Attach state to the level you want to have several of

**Lesson:** Some state can be argued onto either side of a model/presentation split with equal plausibility. A mark denoting where the next input goes, or which stretch of a body of data is currently designated, is *about* the data, so it seems to belong to the data; but it is also produced by, and only meaningful within, one particular presentation of that data. Arguments from where the state "really belongs" are unresolvable here, and are the wrong question. The decidable question is: how many of these do you want to be able to have at once? State attached to the model is necessarily singular — one body of data, one mark — and that singularity is a silent prohibition on every arrangement that would need two. State attached to the presentation is automatically plural, one per presentation, and plurality is what makes cross-presentation composition even sayable.

The payoff is not merely that several presentations can each carry their own copy. It is that the *relationship between* the copies becomes available as a design surface. Two presentations of the same data, positioned adjacently, each carrying its own designated stretch, can be interpreted as one designation spanning both — an interpretation that simply does not exist as a possible thought if the data owns a single designation. This is the general reason to push contested state outward: the layer that has several instances is the only layer at which you can define combining rules over them. Push the state inward and you have not simplified the design, you have deleted a family of behaviours from the space of things the design can express, and you will discover which ones only when a user asks for one.

Two cautions keep this from becoming a rule to apply blindly. It is a genuine trade — plural state must be kept coherent against changes to the shared data, which is why systems that make this choice also need an explicit notification path telling every presentation that the underlying data changed and over what range. And the direction of the argument matters more than its conclusion: what is worth copying is not "put the cursor in the view" but the practice of settling an ownership question by asking which placement leaves more compositions expressible, then saying out loud in the design record that the choice was made for that reason and naming the composition it bought. A decision recorded with the alternative it beat and the capability it purchased survives review; a decision recorded as an obvious fact gets reversed by the next person who finds the other side obvious.

**Source:** [Project Oberon](../works/project-oberon.md) — section 5.3's treatment of the caret and the selection as fields of the text frame rather than of the text, with the explicit acknowledgement that they could equally well have been regarded as ingredients of the underlying text, the stated reason for choosing the frame being increased flexibility, and the given example that two selections in adjacent viewers displaying the same text are normally interpreted as one extensive selection spanning them; together with the same section's `UpdateMsg`, which carries an operator and a restricting range so that frames displaying a changed text can be told what changed.
