---
type: lesson
title: "A symbol means exactly the rules you gave it; its suggestive name is a mnemonic with no force, and reviewers will read the name anyway"
figure: mccarthy
works: [programs-with-common-sense]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# A symbol means exactly the rules you gave it; its suggestive name is a mnemonic with no force, and reviewers will read the name anyway

**Lesson:** The recorded discussion following McCarthy's paper contains a clean demonstration of a failure mode that recurs in every formal artifact, including ordinary typed code. A critic objects that one of the relations in the worked example is asserted to be transitive when the everyday notion its name evokes plainly is not: being immediately next to something does not chain. McCarthy's reply is that he never intended the symbol to formalize the ordinary word, and that the name was chosen only as a convenient reminder of a narrower relation between a place and a sub-place, for which transitivity holds. Both parties are right about different things, and that is what makes the exchange useful. Formally, a symbol denotes nothing but what the stated rules pin down; the identifier is decoration the system never reads. Practically, the identifier is the only thing a human reader consults before deciding whether an assertion looks sound.

The consequence is that a well-chosen name and a well-chosen axiom set are two different obligations, and satisfying one does not discharge the other. When the two disagree, every reader's intuition silently substitutes the name's meaning for the rules', and the resulting objections are not confusions to be waved off but reports that a name is doing damage. The narrower and more technical the intended meaning, the more misleading a friendly everyday name becomes, because the reader will import the everyday properties and reason with them. The cheapest fix is almost always to rename, not to explain.

There is a second lesson stacked underneath, which McCarthy also states in his reply: any program that acts on the world encodes commitments about what that world contains and how it can be known, whether or not anyone wrote those commitments down. His position is that making them explicit first would be preferable but that the explicit account is in worse shape than the programs, so one proceeds and expects the discipline to firm up later. That is an honest description of how modelling actually goes, and it implies a working habit rather than a paralysis: assume your model embeds assumptions you have not stated, expect critics to hit them, and treat a hit as information about your model rather than as an attack on the project.

A programmer who takes this seriously spells out the intended reading of any relation, type, or predicate whose name is shorter than its meaning, and treats "the name suggested something else" as a legitimate review finding. They also read every objection to a model twice: once for whether the formal content is wrong, and once for whether only the naming is, since those need entirely different repairs.

**Source:** [Programs with Common Sense](../works/programs-with-common-sense.md) — the appended discussion, in which the transitivity of the example's location relation is challenged on the basis of what its name ordinarily means, and McCarthy's reply clarifying that the symbol was a mnemonic for a place-to-subplace relation rather than a formalization of the English word; his same reply also concedes that programming a machine to learn builds an unstated theory of knowledge into the program.
