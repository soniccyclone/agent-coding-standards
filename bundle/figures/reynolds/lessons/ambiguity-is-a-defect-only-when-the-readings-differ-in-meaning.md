---
type: lesson
title: "Ambiguity is a defect only when the readings differ in meaning; when they agree it is free generality"
figure: reynolds
works: [the-craft-of-programming]
axes: [expressiveness, primitive-count]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Ambiguity is a defect only when the readings differ in meaning; when they agree it is free generality

**Lesson:** The rule that a description should admit exactly one reading of each thing it describes is a good default and a bad absolute. The reason ambiguity is usually fatal is not that two readings exist but that two readings *mean different things*, so the artifact fails to determine its own interpretation. Where the readings coincide — same value, same effect, same everything an observer could detect — the multiplicity costs nothing, and insisting on removing it costs something real. So the test to apply is semantic, not structural: derive the alternatives, compare their meanings, and only treat a difference as a defect.

Confluent ambiguity is worth deliberately keeping when the alternative readings connect the same construct to different parts of the system. A composite accessed with an index can be read as one indivisible act of retrieval, or as taking the aggregate as a value and then applying it — the two produce the same result, but only the second makes the aggregate itself a thing that can be named, passed, and used wherever a value of that kind is expected. Forbid the second reading and the notation gets tidier while the language of what can be passed around gets smaller, and the loss shows up somewhere far from the rule that caused it. Uniqueness is a property of the *description*; expressiveness is a property of what the system can do. Do not spend the second to buy the first.

There is an obligation attached, and it is the thing that makes this responsible rather than sloppy. Deliberate ambiguity must be labelled as deliberate and justified where it is introduced, with the reason recorded — that the readings agree, and what the extra reading is there to enable. Otherwise it is indistinguishable from an oversight, and the next person to tidy the description will remove it, break something distant, and have no way to discover why the rule was there. Every intentional exception to a stated rule needs a note saying it is intentional; the note is not documentation overhead, it is the part that keeps the exception alive.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Appendix B.2.2, whose productions for array-element access are described as introducing an intentional ambiguity, with two derivation trees given for the same subscripted form: one treating the value as that of a variable obtained by applying the array to a subscript, the other treating it as obtained by applying the function that is the value of the whole array; Reynolds states that the ambiguity is permissible because both trees give rise to the same meaning, and that it must be included in order to permit the full variety of parameter forms described in the following section — set against Appendix A.1's treatment of the dangling-else ambiguity, which is removed precisely because there the two decompositions imply different meanings.
