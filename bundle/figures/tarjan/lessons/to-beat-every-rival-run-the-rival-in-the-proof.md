---
type: lesson
title: "To prove you beat every rival, run the rival inside the proof and make disagreement the ledger"
figure: tarjan
works: [amortized-efficiency-of-list-update-and-paging-rules]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# To prove you beat every rival, run the rival inside the proof and make disagreement the ledger

**Lesson:** The claim being proved here is unusually strong: a simple reactive rule costs no more than twice what *any* strategy costs, including strategies given the entire future request stream in advance. There is no way to establish that by studying the simple rule in isolation, because the quantity it is being compared to is not a formula but a quantified statement over an unbounded space of competitors. The technique that makes it tractable is to imagine the arbitrary competitor executing in lockstep with your algorithm on the same input, then define a single number over the *pair* of states that counts how much the two configurations disagree. Each operation's charge is its real cost plus the increase it causes in that disagreement number. Because the number starts at zero and can never go negative, the true total cost is bounded by the sum of these charges, and the whole argument reduces to a local check on one operation at a time.

The leverage comes from where the accounting puts the pain. Yanking an item to the front is expensive in real work, but it destroys disagreement in proportion to how badly your list was ordered relative to the competitor's, so the charge stays small; every position the competitor's arrangement gains on you is a position your own aggressive move will later reclaim for free. The competitor's own reorderings are charged to you as well, which is what makes the bound hold against strategies that reorder cleverly using knowledge you do not have. None of this requires knowing what the competitor is doing or why. The proof never inspects its logic, only the two-state divergence, and that is exactly why the result quantifies over all of them at once.

Two habits generalize. First, when you want to argue about an unknown best alternative, stop trying to characterize it and instead find a scalar over the joint state whose movement you can bound whatever the alternative does; a comparison you cannot compute becomes an invariant you can check. Second, the shape of the scalar is a design hint, not just proof machinery: a measure of how far the current state has drifted from the ideal state tells you which operations are underpriced, and an operation whose real cost is high but whose drift-reduction is proportionally higher is one you should be doing more eagerly, not less. The accounting and the algorithm inform each other, so a designer who cannot name their potential function usually has not understood which of their operations are paying for which.

**Source:** [Amortized Efficiency of List Update and Paging Rules](../works/amortized-efficiency-of-list-update-and-paging-rules.md) — the first theorem and its proof, where the potential-function method is set up over the joint configuration of an arbitrary algorithm and the move-to-front rule with pairwise order disagreement as the potential, together with its generalizations to partial-move rules and to arbitrary convex access costs, each of which reuses the same joint-state argument.
