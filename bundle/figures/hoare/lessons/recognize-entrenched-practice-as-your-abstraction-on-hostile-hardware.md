---
type: lesson
title: "Recognize an entrenched practice as your abstraction implemented on unsympathetic hardware"
figure: hoare
works: [notes-on-data-structuring]
axes: [cognitive-load, hardware-affinity, expressiveness]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# Recognize an entrenched practice as your abstraction implemented on unsympathetic hardware

**Lesson:** Established industrial practices tend to arrive as folklore: a sequence of steps everyone in the field performs, justified by tradition and by the shape of the equipment, with no evident connection to anything in your theory. The productive question is whether the practice is your abstraction already, implemented under a constraint you do not have. Often it is. A whole discipline of collecting changes, sorting them, and merging them into a stored file in one pass looks like a domain-specific ritual until you notice it is exactly the operation of updating a mapping whose entries are mostly absent — performed on a medium that permits only sequential access, which is why the sorting and merging appear at all.

The reframing pays in both directions. It tells you which parts of the practice are essential and which are artifacts: the entries and their keys are the abstraction, and the sorting, the batching and the merge windows are the price of the medium. So when the medium changes, you know precisely what may be dropped and what may not, instead of carrying the whole ritual forward out of caution or discarding it wholesale and rediscovering why each step was there. It also tells you that the practitioners were solving your problem all along, which means their accumulated judgement about sizes, failure modes and edge cases is evidence about your abstraction rather than trivia about their industry.

There is a discipline in applying this that keeps it from becoming a way of dismissing other people's work. The claim is only worth making if you can exhibit the mapping in detail — this concept corresponds to that record layout, this operation to that processing step — and if the mapping explains the parts of the practice that looked arbitrary. A theory that "covers" a practice while leaving its distinctive features unexplained has not recognized anything; it has just relabelled things. When the mapping does come out clean, though, you have gained a worked, battle-tested instance of your abstraction at a scale you could not have tested at, and the practitioners have gained a name for what they were doing and the ability to reason about variants of it.

**Source:** [Notes on Data Structuring](../works/notes-on-data-structuring.md) — the sequential-representation section of the sparse data structures chapter, which represents a sparse mapping as a default value plus a sequence of key-and-information entries, notes that the entry order is immaterial and so is usually chosen to match the scanning order, and identifies the standard commercial practice of batch processing and updating sequential files as a practical implementation of the abstract sparse array on the unsympathetic medium of magnetic tape.
