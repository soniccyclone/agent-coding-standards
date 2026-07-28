---
type: lesson
title: "Audit both ends of a claim: assume only what the argument uses, and check that what you settled is what was asked"
figure: church
works: [a-note-on-the-entscheidungsproblem]
axes: [verifiability, cognitive-load]
subdomains: [foundations-of-computation, formal-methods-and-verification]
tags: [lesson]
---
# Audit both ends of a claim: assume only what the argument uses, and check that what you settled is what was asked

Halfway through this note Church needs his constructed system to have a soundness property, and the natural one to reach for is the strong condition his earlier paper used. He says outright that establishing it here is harder, and instead isolates a weaker statement — roughly, that an existence claim cannot be provable while every one of its numeric instances is refutable — observes that this weaker statement is all the argument consumes, and cites an existing proof covering a whole class of systems including his. The result stands on a hypothesis he can actually discharge, and it now applies more widely because the hypothesis is cheaper.

That is one end of the claim. The other end gets the same treatment in a footnote most readers skip: his own definition of the decision problem for a system is not quite the formulation Hilbert and Ackermann had posed for the predicate calculus, so he does not silently equate them. He names the discrepancy and closes it with a separate known result, the completeness of the calculus, which makes the two readings coincide. Without that step he would have proved something true about a question nobody asked.

Both moves come from the same instinct: know precisely what a result rests on and precisely what it delivers, and treat any slack at either boundary as work remaining rather than as detail. The failure modes are complementary and both common. Assuming more than you need makes a result fragile and narrow — it collapses the moment someone hands you a system that satisfies your real requirement but not your stated one. Proving a reformulated version of the question makes a result irrelevant in a way that is much harder to notice, because everything inside the proof is correct and only the connection to the original problem is missing.

A programmer who works this way states the actual precondition a routine depends on rather than the convenient one that happens to hold at today's call sites, so the routine survives contact with new callers. And when translating a stakeholder's question into something checkable — a metric, a test, an invariant, a specification — they treat the gap between the informal ask and the formal proxy as an explicit thing to argue about, not as a step to be performed silently. The most expensive kind of correct answer is the one to a question that had been quietly replaced.

**Source:** [A Note on the Entscheidungsproblem](../works/a-note-on-the-entscheidungsproblem.md) — the passage substituting a weaker sufficient consistency property for the harder one, and the footnote reconciling Church's own statement of the decision problem with Hilbert and Ackermann's via completeness.
