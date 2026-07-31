---
type: lesson
title: "Define a fault-masking layer's correctness as indistinguishability from the ideal component it imitates"
figure: hoare
works: [communicating-sequential-processes-book]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---
# Define a fault-masking layer's correctness as indistinguishability from the ideal component it imitates

**Lesson:** A layer whose purpose is to hide a defect — loss, corruption, reordering, delay — resists being specified by listing what it does about each defect. The list is never complete, every clause is about mechanism rather than obligation, and the whole thing has to be revisited whenever the defect catalogue changes. Specify it instead by exhibiting the component you wish you had, defining that ideal precisely, and demanding that the assembly be indistinguishable from it. Say exactly what a perfect conveyance is: everything emerging has been submitted, in the order submitted, and it is never unwilling to hand over something it is holding. Then the correctness of the entire arrangement — sender, defective medium, receiver — is one statement rather than a catalogue: this assembly is one of those.

Three properties make that formulation better than a list of behaviours. It is complete by construction, because any observable deviation is by definition a difference from the ideal and therefore a violation, including deviations nobody thought to enumerate. It composes, because two ideal conveyances in series form another one, so a chain of such layers needs no fresh argument. And it grants the implementer the maximum freedom the requirement permits, since nothing whatever is said about how the masking is achieved, only about what may be observed afterwards. Note that the ideal needs both halves of its definition — the relation between what went in and what came out, *and* the requirement that it not decline to deliver — because the relation on its own is satisfied perfectly by a layer that swallows everything and emits nothing.

The generalizable move: whenever you build something to compensate for an imperfection, name the perfect thing it is pretending to be, write that thing down as a specification, and make your obligation an equality rather than a list of mitigations. Retry logic is pretending to be a call that does not fail. A cache is pretending to be the store behind it. A replica set is pretending to be a single copy. Each becomes checkable the moment the pretence is stated rather than left as an intention, and — the part that matters — each becomes a claim you can lose honestly. A list of mitigations can never be lost, which is precisely why teams like writing them.

**Source:** [Communicating Sequential Processes](../works/communicating-sequential-processes-book.md) — the buffers and protocols subsection of the pipes section: the definition of a buffer as a process which never stops, is free of livelock, outputs exactly what it has input in the same order though possibly after delay, and when non-empty cannot refuse to output; the statement that a protocol consists of a transmitter and receiver in series and that it is correct exactly when the pair, together with a wire subject to corruption or loss, is a buffer; and the laws showing that two buffers in series are again a buffer and that a pair satisfying a particular equational form is one.
