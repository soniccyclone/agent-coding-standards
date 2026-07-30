---
type: lesson
title: "Locality is something you discover in the contract, not something you decide when declaring"
figure: reynolds
works: [the-craft-of-programming]
axes: [cognitive-load, verifiability]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Locality is something you discover in the contract, not something you decide when declaring

**Lesson:** Whether a name belongs inside a component or outside it is not a matter of preference, and it is not settled by where you happen to have typed the declaration. It is a fact about the component's contract, and you can read it off directly: if the name occurs in neither the entry condition nor the exit condition, then whatever value it held on the way in cannot matter, and whatever value it holds on the way out cannot matter to anybody else. Those two negatives are the definition of local. A declaration is therefore not a decision — it is a record of something already true, and the right move is to derive the scope from the specification rather than guess it and hope.

Two dividends come from making that fact explicit, and they are of different kinds. The visible one is that the name is freed for use elsewhere, and the reader of any other region need not wonder about it. The invisible one is that the storage is freed too — nothing has to preserve the value outside the region, so the same space can serve other purposes at other times. That second dividend is what forces the discipline to be honest, because an implementation that reclaims the space also destroys the value on exit and hands you an unpredictable one on entry. If your claim of locality was wrong, that is precisely where you find out. The formal counterpart makes the same demand: the rule that lets you push a declaration inward is only applicable when the declared names are absent from the surrounding conditions, so the proof system refuses to let you localize a name you are still depending on.

The style rule that follows is to place every declaration as far in as it will go. On a small program this looks like fussiness. On a large one it is the difference between a reader holding a handful of names in mind at any point and holding hundreds, and the ratio only worsens with size. It also converts a global question into a local one: to understand a region, you need to know about exactly the names whose scopes reach it, and each name's scope announces the largest region that could possibly be affected by it. The habit generalizes past variables to any binding of a name to a meaning — a helper, a configuration value, an imported symbol. Push each one inward until the contract stops you, and where it stops you is information worth noticing, because a name that refuses to be localized is telling you it is part of an interface whether you intended that or not.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 1.5.1, which defines a local variable by the absence of its identifier from the precedent and consequent of the statement's specification, distinguishes the static scope from the dynamic scope over which storage exists, gives the inference rule for declarations with its side condition on free occurrences, and argues for placing declarations as far in as possible.
