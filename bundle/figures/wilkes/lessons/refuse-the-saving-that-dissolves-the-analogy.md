---
type: lesson
title: "Refuse the optimization that dissolves the analogy your method depends on"
figure: wilkes
works: [best-way-to-design-an-automatic-calculating-machine]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Refuse the optimization that dissolves the analogy your method depends on

**Lesson:** When a method's value comes from making a hard problem resemble a problem you already know how to attack, that resemblance is an asset with a price, and features that erode it are not free no matter how little material they consume. A generalization can be locally available, locally cheap, and still wrong to take — because what it spends is the property that made the whole approach tractable, and that property does not appear in any resource budget. The decision therefore has to be taken on the resemblance itself: does this extension keep the thing recognizably an instance of the discipline I imported, or does it turn it back into the special-purpose puzzle I was trying to escape?

The discipline is to say which correspondence the design is running on, and then to treat any small dose of it as suspect rather than harmless. Extensions of this kind tend not to announce themselves as violations; each one is presented as a permitted variation available at negligible cost, and the erosion is cumulative — the first instance is genuinely almost free, and there is no instance at which the loss becomes visibly worth objecting to. So the guard has to be stated up front, and it has to be stated in terms of the analogy rather than in terms of the resource being saved, because measuring in resources is exactly the frame in which the trade always looks favourable.

Two useful habits follow. Note the available generalizations you are declining and why, so that a later reader knows the omission was a decision rather than an oversight. And when you find yourself defending an extension on the grounds that it will only be used a little, recognize that as the shape of the argument that spends a structural property in instalments.

**Source:** [The Best Way to Design an Automatic Calculating Machine](../works/best-way-to-design-an-automatic-calculating-machine.md) — the closing note on making elementary steps conditional in their action rather than only in sequencing, where the possibility is described, judged unlikely to save much, and rejected on the grounds that doing it to any extent forfeits the resemblance to ordinary programming that the scheme's value rests on.
