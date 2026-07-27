---
type: lesson
title: "Treat a change request as a claim about the world, not as a prescribed new state"
figure: fagin
works: [on-the-semantics-of-updates-in-databases]
axes: [expressiveness, cognitive-load, verifiability]
subdomains: [databases-and-data-management, formal-methods-and-verification]
tags: [lesson]
---
# Treat a change request as a claim about the world, not as a prescribed new state

**Lesson:** A decade of work on updating derived views had gotten stuck on a question that turns out to be badly posed. The assumed setup was that a user looking at a derived projection of the data knows precisely which new derived value they want, and the system's job is to find the change to the underlying data whose derived image is that value. Under that framing the hard part is defining what it means for the underlying change to "correctly reflect" the requested one, and the literature accumulated competing answers without converging. Fagin, Ullman and Vardi's move is to reject the premise instead of arbitrating the answers: a user who edits a row is not issuing a state transition, they are asserting something they now believe about the world, stated in the only vocabulary they have been given. Whether that assertion changes one stored fact, five, or forces a reconsideration of what else was believed, is not theirs to know and not theirs to specify.

Once the request is understood as an assertion rather than a transition, the whole problem restructures. There is no longer any need to define correct reflection, because nothing is being reflected. The assertion is expressed in terms of the derived vocabulary, so you rewrite it in terms of the stored vocabulary by substituting the definition of the derived thing, and what comes out is an assertion at the base level, indistinguishable in kind from any assertion a user of the base level could have made. The specialized view-update problem dissolves into the general problem of absorbing new information into an existing body of it. The paper is explicit that this generality is the point: the same machinery it needs for derived views is what it needs anyway for the ordinary case, because ordinary stored data also has consequences that interact with what you are trying to change.

The programming discipline here is to interrogate what an interface's operations actually mean before designing the mechanism that implements them. A request arriving as an imperative is not automatically an imperative. When the caller is working through an abstraction, they can only phrase intent in the abstraction's terms, and they usually do not know, and should not need to know, what the underlying state must look like afterward. Building the system as an intent translator rather than a mutation applier removes an entire class of unanswerable questions about which of several possible underlying edits was the one the caller "meant." A programmer who thinks this way stops asking users to specify effects they are not positioned to specify, and stops writing heuristics that guess at intentions the interface never let them state.

**Source:** [On the Semantics of Updates in Databases](../works/on-the-semantics-of-updates-in-databases.md) — the introduction's diagnosis of the shared assumption behind prior view-update work, and the later section that recasts a view edit as an information unit to be reinterpreted in the base vocabulary and then handled by the general update method.
