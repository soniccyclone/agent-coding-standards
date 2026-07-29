---
type: lesson
title: "An invariant you cannot point at cannot be maintained"
figure: sutherland
works: [sketchpad-a-man-machine-graphical-communication-system-thesis]
axes: [verifiability, cognitive-load]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# An invariant you cannot point at cannot be maintained

Once a system lets its users assert rules about their model, those rules become
part of the model — and anything that is part of the model must be inspectable
and revisable through the same means as everything else. If the rules are
invisible, a user confronted with behaviour they did not intend has no way to
discover which assertion caused it, and no way to retract it. The model
acquires a hidden layer that only its author can reason about, which is exactly
the failure mode a declarative facility was supposed to prevent.

Sketchpad's response was to give every abstraction a body in the same medium as
the concrete content: relations render as small marked glyphs with limbs
reaching to the values they govern, a numeric value distinct from the digits
displaying it gets its own visible token, and an occurrence of a definition
whose visible content has been emptied still gets a drawn boundary so it cannot
silently disappear from the world. The pointing mechanism was then made
uniform, so anything drawn could be aimed at, and therefore anything drawn
could be deleted or changed. Sutherland is explicit that visibility is what
makes the editing vocabulary complete — the rule is displayable *so that* it can
be erased.

He is equally honest about what this costs, and the honesty is instructive: the
glyphs pile on top of each other when many rules govern the same region, one
character is too little room for a useful name, and giving a rule a position of
its own would make it a value that could be governed by other rules, which
compounds the mess. That tangle is the real content of the lesson. Making the
invisible visible is not free ornamentation, it forces you to solve layout,
naming and self-reference problems that were previously hidden by simply not
showing anything.

A programmer who takes this seriously treats every derived or asserted thing the
system maintains as owing the user a representation and a handle: constraints,
watchers, subscriptions, cached invariants, implicit couplings. The test is
whether a user who has been surprised can locate the cause and remove it using
only the interface they already know. Where they cannot, the surprise is a
permanent feature of the system.

**Source:** [Sketchpad: A Man-Machine Graphical Communication System (PhD Thesis)](../works/sketchpad-a-man-machine-graphical-communication-system-thesis.md) — the display-generation chapter's sections on showing abstractions and on empty displays, including the enumerated difficulties with rendering relations and the reasoning that a universal pointing language requires everything in storage to be showable.
