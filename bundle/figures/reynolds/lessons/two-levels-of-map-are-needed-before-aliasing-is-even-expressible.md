---
type: lesson
title: "You need two separate maps — names to things, things to values — before aliasing is even expressible"
figure: reynolds
works: [the-craft-of-programming]
axes: [cognitive-load, verifiability]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# You need two separate maps — names to things, things to values — before aliasing is even expressible

**Lesson:** The everyday phrase "the value of x" hides a composition of two lookups, and collapsing them into one is why a whole class of bugs is invisible in the vocabulary most programmers use. The first lookup takes a name to the thing it currently denotes; the second takes that thing to what it currently holds. Keep them apart and a statement like "x and y are both seventeen" splits into two genuinely different situations: two distinct cells that happen to agree, or one cell reached under two names. Collapse them and the two situations become the same sentence — at which point you have no way to say the thing you most need to say, which is that writing through one name may or may not disturb what the other name sees.

The two maps also differ in how they change, and this is the sharper reason to keep them apart. Assignment changes the second map and the change persists; entering a scope changes the first map and the change is undone on the way out. So a construct that binds does something categorically unlike a construct that assigns, even when both are described loosely as "setting" something. Recognizing this tells you where to look for each kind of error: bad values come from the persisting map, and surprising identity — two names that turned out to be one thing, or one name that turned out to mean something else here — comes from the transient one.

The payoff of separating them is that a name-to-thing map is a first-class object you can quantify over. Claims about a piece of code stop being flatly true or false and become true relative to a binding, which is exactly the right shape once the code takes its collaborators as parameters. It also explains why substitution and binding are the same phenomenon seen from two sides: replacing a name by a phrase throughout a fragment has precisely the effect of evaluating the fragment under a map that sends that name to that phrase's meaning. Once you have that equivalence, the textual operation and the semantic one can be used interchangeably, and a rule proved about one transfers to the other without further argument.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 3.3.1, which defines an environment as a function from identifiers to meanings and a state as a function from variables to values, insists these are different entities both needed to describe an Algol-like language, works the example distinguishing two variables that both hold seventeen from one variable denoted by two identifiers and identifies that distinction as how interference is described, observes that statements change the state while binding mechanisms change the environment and that environments do not persist as state changes do, and states the substitution law equating a type-correct substitution with the corresponding change of environment.
