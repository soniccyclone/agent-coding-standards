---
type: lesson
title: "Re-enter a change at the level where the decision was made, because a design record left stale is worse than no record"
figure: jones
works: [software-development-a-rigorous-approach]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Re-enter a change at the level where the decision was made, because a design record left stale is worse than no record

**Lesson:** A design that was built as a sequence of decisions, each recorded with the reason it was believed to work, has a property nobody mentions when selling the practice: it tells you where a later change belongs. When something has to change — a measurement shows a structure is being hammered far harder than anyone expected, a requirement moves — you can identify which decision the change actually contradicts, and re-do the work from that point. What gets edited is the record, and the code follows from it. That is a different activity from patching the code and hoping the reasoning still applies, and it is much cheaper than it sounds, because most of the recorded decisions are untouched and their arguments survive intact.

The uncomfortable half of this is what happens when you skip it. A design history that no longer describes the system is not neutral; it is actively harmful, worse than never having written one. With no record, the next person reads the code and knows they are reading the code. With a stale record, they read a confident account of decisions and reasons that are no longer true, and they trust it — that is what it is for. So the maintenance cost of the record is not optional overhead attached to the practice; it is part of the practice, and a team that keeps the artifact but abandons the discipline has bought something with negative value.

The immediate consequence is a willingness that has to be cultivated deliberately: you must be prepared to throw work away. When an early decision turns out to be wrong, everything derived from it is suspect, and the revision means redoing that derivation rather than grafting a correction onto the end. People resist this in proportion to how much was built on top, which is exactly backwards — the more that rests on a decision, the more it matters that the decision and its record agree.

None of this makes the process linear. Sketching far ahead is often wise, and discovering mid-descent that something already finished must be revised is normal rather than a failure of method. What the discipline demands is not that you think in order, only that when you finish, the record reads as though you had.

**Source:** [Software Development: A Rigorous Approach](../works/software-development-a-rigorous-approach.md) — chapter 17's "A Top-Down View of the Method", where the top-down aim is described as documentation relating the levels of a hierarchy while explicitly disclaiming any straitjacket on thought, with the statements that sketching ahead and revising finished work both occur, that a preparedness to discard work is essential, and that proceeding without making the corresponding changes to the earlier design history makes that history less than worthless; and chapter 18's "Modifications" section, reporting a real performance failure on a large grammar, its diagnosis by inserted counters showing the state-set insertion loop executing an enormous number of times, and the resulting hash-vector change, which was thought out and documented in terms of the development documentation before any coding — together with chapter 17's closing remark that incorporating modifications into a system developed this way is a more scientific matter than where design documents are inadequate.
