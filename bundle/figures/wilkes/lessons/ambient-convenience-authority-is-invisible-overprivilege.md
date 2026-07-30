---
type: lesson
title: "A convenience pool of ambient authority is invisible overprivilege, and its harmlessness is relative to a model you may change"
figure: wilkes
works: [cambridge-cap-computer-and-its-operating-system]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# A convenience pool of ambient authority is invisible overprivilege, and its harmlessness is relative to a model you may change

**Lesson:** Every system with an explicit account of what each part may reach also acquires a bag of things everything gets automatically, because putting them in the bag saves plumbing them through individually. Each item is defensible: none of them can do harm, most components need most of them, and the alternative is tedious. The result is that a carefully constructed account of reach has a hole in it exactly the size of the bag, and the hole is invisible in exactly the way that matters — the parts of the system that need none of it are indistinguishable from the parts that need all of it. Ambient authority is the same thing as a global variable, and it earns the same verdict, for the same reason: it removes the possibility of reading a component and knowing what it depends on.

The sharper point is that "none of these can do harm" is not a fact about the items. It is a claim relative to what you are defending against, and it expires without notice when the question changes. Authority that is harmless when the concern is containing bugs can be exactly the lever that matters when the concern is what a component might do deliberately: the ability to learn whose behalf you are acting on threatens nothing under one model and enables discriminating between users under another. Nothing about the system changed — the model did, and the judgement that was correct became wrong silently.

So the practical discipline has two parts. Record which model each "harmless" judgement was made under, so that a change of concern comes with a list of things to re-examine rather than a general unease. And resist the bag on structural grounds even where the current model says the contents are safe, because its real cost is not what an item might enable but the loss of the property that made the rest of the account worth having.

**Source:** [The Cambridge CAP Computer and Its Operating System](../works/cambridge-cap-computer-and-its-operating-system.md) — Chapter 5's discussion of the global capability segment as a source of overprivilege, noting that none of its contents could harm the system yet many are surplus to the requirements of many programs, that the segment has something in common with global variables now considered bad practice, that had the project's aim been security rather than protection some of its contents would have been serious — the capability revealing the user on whose behalf a process runs enabling a dishonest programmer to discriminate against a particular user — and the conclusion that a new version of the system would make less use of it.
