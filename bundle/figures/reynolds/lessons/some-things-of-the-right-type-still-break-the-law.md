---
type: lesson
title: "Belonging to the type is not obeying the law, so name the law separately"
figure: reynolds
works: [the-craft-of-programming]
axes: [verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Belonging to the type is not obeying the law, so name the law separately

**Lesson:** The most basic thing you believe about a mutable cell is that if you put a value in, the cell then holds that value. It is so basic that it usually appears as an axiom rather than as a claim anyone checks. It is not universally true. A language that admits compound designators — a slot selected by an index that is itself read out of the structure being written — produces phrases that pass every syntactic test for "a cell you may assign to" and yet violate the axiom, because the act of writing changes which slot the phrase now selects. Assign, then look at the same phrase, and it does not hold what you put there. Nothing is corrupt and nothing is a bug; the phrase simply is not the kind of thing your axiom was about.

The general shape here is worth extracting from the example. A type tells you which contexts a thing may appear in. It does not tell you that the thing satisfies the equations you habitually reason with about members of that type. Where the two come apart, the correct move is not to weaken the equations for everybody, nor to pretend the exceptional members do not exist, but to give the law its own name — a predicate you can assert of a particular thing — and to make every rule that depends on the law carry that predicate as an explicit condition. Now the well-behaved case is stated rather than assumed, and the ill-behaved case is describable rather than unspeakable.

The reason this matters more than it seems is that the defect is contagious across an interface. Hand one of these phrases to a component as an argument, and inside the component the corresponding parameter is now a thing that fails the law, even though the component's own text is unremarkable and its author never contemplated the possibility. The component's correctness argument silently depended on an assumption that the caller has just falsified. So the predicate is not decoration for the exotic cases; it belongs in the interface of anything whose reasoning uses the law, in the same place as every other condition the caller must establish. The discipline generalizes past assignment: whenever you find yourself relying on an equation that "obviously" holds for a type, look for the member that satisfies the type and breaks the equation, and if one exists, promote the equation to a named, checkable requirement.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 3.3.4's specification for a good variable, which remarks that at first sight the property might seem to hold of all variables in all environments, then exhibits an array designator whose subscript is itself an element of the same array, shows that after assigning a value the designator no longer possesses it, notes that using such a designator as an actual parameter creates an environment in which the corresponding formal parameter is not a good variable, and gives the formal definition quantifying over an arbitrary property of values expressed as an assertion procedure that the variable does not interfere with.
