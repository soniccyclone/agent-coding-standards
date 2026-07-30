---
type: lesson
title: "Attack your own specification with a cheating program, then add the clause that stops it"
figure: reynolds
works: [the-craft-of-programming]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Attack your own specification with a cheating program, then add the clause that stops it

**Lesson:** A specification that states the property you want is usually still wrong, and there is a fast way to find out. Try to satisfy it with the laziest destructive program you can think of and see whether it passes. Ask a sorting routine only for a sorted result and a program that overwrites everything with zeros qualifies — the output is impeccably sorted. The gap is not subtle once exposed: the requirement named a property of the final state and said nothing relating that state to the initial one. The cheating program is a diagnostic instrument, and it is more reliable than rereading the specification sympathetically, because reading it sympathetically is precisely the failure mode. You know what you meant; the text does not.

Closing such a gap usually requires two additions, and the second gets forgotten more often than the first. You must relate the final state to the initial one — naming the initial value with something the program cannot touch, then requiring the result to stand in the right relation to it. And you must say what was left alone: everything outside the region you were asked to work on must be unchanged. Without that second clause the specification permits a program that sorts the requested part and vandalizes the rest, which is a real bug and a common one. So the discipline is to state, for every operation, what it produces, what its output must be as a function of its input, and what it promises not to disturb.

The encouraging part is what the strengthened specification costs to prove. Take the new condition and require it at every point in the program — conjoin it to every assertion. Almost every component now discharges it for nothing, because a component that does not touch the state in question preserves any claim about that state trivially. The proof obligation concentrates entirely in the few places that do touch it, and in a well-built program that is a small number of small operations, often exactly one primitive whose whole job is the change. That concentration is worth noticing as a design signal too: if adding a cross-cutting condition forces you to argue at dozens of scattered points, the state it constrains is being modified in dozens of scattered places, and that, rather than the proof, is the thing to fix.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — the opening of Section 2.3.4, which calls the sorting specification seriously incomplete because it could be trivially met by a program that sets every element to zero, introduces a ghost identifier to state the rearrangement condition, and observes that the strengthened specification is proved by showing every part of the program preserves the condition — trivial for the parts that do not assign to the array, with only the exchange step requiring argument; together with the exercise adding the clause that elements outside the segment are left unchanged.
