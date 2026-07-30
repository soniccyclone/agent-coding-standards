---
type: lesson
title: "Read a request as evidence in the caller's vocabulary, not as a description of the end state"
figure: vardi
works: [on-the-semantics-of-updates-in-databases]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# Read a request as evidence in the caller's vocabulary, not as a description of the end state

**Lesson:** A long line of work on updating a projected or filtered presentation of data treated the problem as translation: the caller knows what the presentation should look like afterwards, so find the underlying change that produces exactly that appearance. Vardi and his coauthors identify the flawed premise. The presentation is constrained — by whatever governs the underlying data, and additionally by the very construction that produced the presentation — so the picture the caller has in mind may not be an achievable picture at all, and every difficulty about "reflecting the change correctly" descends from trying to honour an unachievable target.

The reframing is to stop reading a request as a specification of the resulting appearance and read it instead as an assertion of new information, phrased in the vocabulary the caller happens to have. Then the work is not to invert a projection but to restate the assertion in the underlying vocabulary — mechanically, by substituting the definition of each derived term — after which it is just an ordinary assertion against the underlying store, resolved by whatever general machinery you already have. The entire special theory of updating derived presentations disappears, replaced by one translation step plus the general case. When a hard subproblem dissolves like that, the reframing was almost certainly closer to the truth than the framing.

There is a striking corollary about how little you need to know. Because the translation goes through the definition of the derived view rather than through its contents, the update can be carried out without any account of what the caller can currently see — and the full logical description of a derived presentation is typically infinite and may not even be finitely statable, so this is not a small convenience. The general habit: when an interface layer forces you into an inverse problem, check whether you were mistaking the caller's phrasing for the caller's intent. Instructions specify outcomes and must be inverted; evidence specifies content and only has to be translated.

**Source:** [On the Semantics of Updates in Databases](../works/on-the-semantics-of-updates-in-databases.md) — section four, which diagnoses the standard view-update framing as resting on the dubious premise that the user knows how the update will affect the view, proposes treating an update as the addition or deletion of an information unit, gives the lemma showing a sentence about the view carries exactly the information of the sentence obtained by substituting the view definition, and remarks that the update is implementable without reference to what the user actually sees even though the view's own theory may not be finitely axiomatizable.
