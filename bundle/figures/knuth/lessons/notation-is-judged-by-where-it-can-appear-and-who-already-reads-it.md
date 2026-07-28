---
type: lesson
title: "Notation is judged by where it can appear and who already reads it, not by its formal elegance"
figure: knuth
works: [big-omicron-and-big-omega-and-big-theta]
axes: [expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Notation is judged by where it can appear and who already reads it, not by its formal elegance

**Lesson:** Having spent the letter arguing for a particular set of growth symbols, Knuth turns and argues against himself. There is a competing scheme, older than the one he is defending, built from ordering relations between functions — and by every formal criterion it wins. Its relations are transitive in the obvious way, it has none of the asymmetric-equality embarrassment, and it predates the notation that displaced it. He then rejects it anyway, for a reason that has nothing to do with logic: a relation must be written *between* two things, so using one forces you to move everything except the quantity being estimated to the far side of an equation. The bound-symbol form can be dropped into the middle of a formula, the middle of an English sentence, or a cell of a table comparing several algorithms. He makes the point by exhibiting a chain of successive approximations, each line refining the error term of the last, and observing that the same derivation in relational form would be unbearable.

That is a substantive claim about what makes notation good, and it is not the claim a formalist would make. The value of a piece of notation is dominated by its *positional freedom* — how many syntactic contexts it can occupy without forcing the surrounding text to be rearranged — because notation earns its keep during derivation, where you are transforming an expression step by step and every forced rearrangement is a place to make an error. A construct that is elegant in isolation but only legal at the top level of a statement imposes a cost on every use, and that cost compounds across a long argument in a way that its elegance does not.

The second movement of the argument is about ownership, and it is sharper. Knuth mentions that on his own scratch paper he uses a different, more uniform scheme of his own devising, one that would cover more cases than the three symbols he is proposing. He will not publish in it. His reason is that the established notation is universally recognized and has accumulated mnemonic weight, and he does not consider a private invention entitled to displace that however well-conceived it is — the same reason he keeps writing numbers in base ten while finding another base more logical. So the notation he advocates is not the one he thinks is best designed; it is the one whose adoption cost the field has already paid. And in the same breath he draws the boundary: for a concept arising rarely, invent whatever local symbol you like and confine it to the one document that needs it, because standardizing vocabulary is only worth its cost for concepts that recur.

A programmer who internalizes this stops treating "my design is cleaner" as sufficient grounds for introducing a new abstraction, a new naming convention, or a new DSL. The relevant question is how many contexts the construct composes into and how many readers already decode it fluently — and there is a threshold below which the right answer is a local convention scoped to one module and one comment, never promoted to house style.

**Source:** [Big Omicron and Big Omega and Big Theta](../works/big-omicron-and-big-omega-and-big-theta.md) — the closing discussion weighing the older relational notation against the bound symbols, including the worked chain of asymptotic refinements, the remark about scratch-paper notation never reaching publication, and the aside on local notation for rare concepts.
