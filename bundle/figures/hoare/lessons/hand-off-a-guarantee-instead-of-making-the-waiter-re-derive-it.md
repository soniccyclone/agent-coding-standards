---
type: lesson
title: "Decide who establishes a condition, and hand the guarantee over atomically instead of making the waiter re-derive it"
figure: hoare
works: [monitors-an-operating-system-structuring-concept]
axes: [verifiability, parallelizability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
tags: [lesson]
---
# Decide who establishes a condition, and hand the guarantee over atomically instead of making the waiter re-derive it

**Lesson:** Whenever one participant blocks until some situation obtains and another brings that situation about, there is a design decision that is easy to leave implicit: at the instant the blocked party resumes, is the situation known to hold, or must the party check again? Both answers can be made correct, but they distribute the burden very differently. If resumption carries a guarantee, the waiter's code is a plain block that may assume what it was waiting for, and the obligation to establish it sits in exactly one place — with whoever announces the change. If resumption carries no guarantee, every waiter must loop and retest, the announced fact means only "something may have changed," and the correctness of each waiter now depends on a discipline applied at every waiting site.

Making the guarantee real requires closing the window. A notification that grants a fact is worthless if a third participant can slip in between the announcement and the resumption and consume it; so the strong form of the design treats occupancy of the shared region as a privilege explicitly handed from the announcer to the resumed party, with the announcer suspended in the meantime, and only released to the general population when nobody is owed it. That has a price, paid in transfers of control that a weaker rule would avoid, and the price is exactly what buys the absence of retesting. Recognizing that trade for what it is — a fixed cost per handoff in exchange for removing a distributed obligation — is more useful than any particular resolution of it.

The reasoning obligations fall out symmetrically once the decision is made, and they are worth stating in any protocol of this shape rather than only in synchronization primitives. The announcer must make the awaited condition true *before* announcing, since resumption may be immediate. The waiter may assume the condition on resumption but must not assume it persists, because the party it was handed from may have handed the same shared state through others. And the announcer may assume, after the handoff, only the module-wide invariant and nothing about the specific condition, because the resumed party is entitled to consume it. Writing those three obligations down for a handoff you are designing is usually enough to expose whichever of them the implementation quietly violates.

**Source:** [Monitors: An Operating System Structuring Concept](../works/monitors-an-operating-system-structuring-concept.md) — the introduction's decree that a signal is followed immediately by resumption of a waiting program with no intervening entry by a third program, the note on the single-resource scheduler explaining that the acquiring procedure need not retest after waiting because the releasing procedure has guaranteed the condition, the implementation section where possession of the monitor is described as a privilege passed explicitly from process to process with mutual exclusion released only when no one is owed it, and the proof-rule section's paired obligations for waiting and signalling.
