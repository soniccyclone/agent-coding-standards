---
type: lesson
title: "An abstraction is right when the informal description transcribes without residue"
figure: von-thun
works: [some-simple-programming-in-joy]
axes: [cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# An abstraction is right when the informal description transcribes without residue

Von Thun's method through most of this paper is the same: state the algorithm as numbered English, then write the program. What makes it more than a presentation device is the accounting he does between the two. Every numbered line of the informal description becomes exactly one argument of the control combinator, in order. And one line of the description carries no number — the line that says "recurse" — because the combinator performs the recursion itself, so there is nothing in the program text corresponding to it. The transcription is complete and the leftovers are visible: what you had to write is precisely what varied, and the machinery you did not have to write is the machinery that never varies.

This gives a usable test for whether an abstraction sits at the right level. Take the informal statement of what the code does — the version you would say out loud to a colleague — and try to transcribe it. Residue in one direction means the abstraction is too weak: you are writing plumbing that the informal description does not mention, which is exactly the code that carries no information and is therefore where mistakes hide. Residue in the other direction means it is too strong or wrong-shaped: the description mentions things the abstraction gives you no place to put, so you contort the description to fit, and now the code no longer corresponds to any statement a human made. A clean one-to-one mapping means the abstraction has captured the fixed part and nothing else.

The test is cheap and it is honest, because it grades the abstraction against a description written before the code and not tuned to flatter it. It also gives a concrete reading of what an abstraction is worth: not lines saved, but description-to-code distance. Von Thun's own worked examples show the payoff and the boundary — when an algorithm's recursion happens in three separate branches, the simple linear combinator cannot take it, and rather than distorting the description he reaches for the combinator whose shape does match, one that fuses multiway case selection with the recursion. Finding that the description does not transcribe is information about which abstraction to use, not a reason to rewrite the description.

**Source:** [Some Simple Programming in Joy](../works/some-simple-programming-in-joy.md) — the derivation of the sublist-producing operators, where von Thun numbers the pseudocode lines and matches them against the recursion combinator's four arguments while noting that the unnumbered recursive step has no counterpart in the program, and the later merge programs where a three-branch recursion forces a different combinator.
