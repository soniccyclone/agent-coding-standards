---
type: lesson
title: "The shape of the data dictates the shape of the program: each way of composing data has exactly one matching control structure"
figure: hoare
works: [notes-on-data-structuring]
axes: [cognitive-load, verifiability, expressiveness]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# The shape of the data dictates the shape of the program: each way of composing data has exactly one matching control structure

**Lesson:** The ways of building compound data and the ways of building compound programs are the same small list, paired off. A value with several components of fixed kinds is processed by a straight-line block that deals with each in turn. A value that is one of several alternatives is processed by a discrimination with one arm per alternative. A value that is a fixed-size collection indexed by some finite range is processed by a loop whose trip count is bounded by that range. A value whose description mentions itself once, so its length is unbounded, is processed by a loop with a termination test rather than a count. A value whose description mentions itself more than once is processed by a procedure that calls itself more than once. The correspondence is not a mnemonic; it holds because the reason a structure has the shape it has is the reason the program traversing it must have that shape.

Used forward, this settles arguments about control flow without any appeal to taste: once the data is described, the processing skeleton is determined, and code that departs from it is either handling a structure other than the one you documented or is about to get something wrong at the edges. Used backward, it is a diagnostic. A loop with an unbounded termination test over data that is genuinely fixed-size means someone is guessing where the guessing was unnecessary; a recursive walk over data that mentions itself only once means an unnecessarily general mechanism; a chain of tests where the data has explicit alternatives means the discrimination is being reconstructed by inference rather than read off. In each case the mismatch is the finding, and it points at whichever of the two descriptions is wrong.

The deeper payoff is that it tells you where the cost of a data-structuring decision actually lands. Admitting self-reference into a description is what makes a type unbounded, and it is simultaneously what forces the processing code up a level of control-flow power — from counted iteration to conditional iteration, or from iteration to recursion. So the question "should this component be allowed to be another one of these?" is never only a question about data. It is a decision to make every program that touches the structure more powerful, and correspondingly harder to bound, than it would otherwise have needed to be.

**Source:** [Notes on Data Structuring](../works/notes-on-data-structuring.md) — the opening of the chapter on recursive data structures, which pairs the Cartesian product with the compound statement, the discriminated union with the conditional or case construction, arrays and powersets with bounded iteration, and the sequence with the while loop, explains the sequence's unboundedness by its being built from a component of its own type just as a while loop's remaining work is the same statement as before, and extends the analogy to types that name themselves in more than one place matching procedures that call themselves from more than one place.
