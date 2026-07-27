---
type: lesson
title: "Give every distinction that changes an obligation its own visible form, including the ones that break your uniformity claim"
figure: manna
works: [temporal-verification-diagrams]
axes: [cognitive-load, expressiveness, verifiability]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# Give every distinction that changes an obligation its own visible form, including the ones that break your uniformity claim

**Lesson:** The diagrams have three kinds of edge, drawn differently, and the reason is disciplined rather than decorative: each kind generates a different obligation. A plain edge permits a step that makes no progress, so its obligation merely constrains where the successor may land. A doubled edge marks a step that must make progress and that the scheduler's weak fairness guarantees will be taken, so it carries the extra obligation that the step is currently possible. A third kind marks a step that only strong fairness guarantees, and its obligation is different again. The rule the notation follows — one visible form per distinct obligation, and no transition wearing two forms at the same node — means a reader can tell what must be checked by looking, and a tool can generate the checks without heuristics.

The more interesting discipline is what happens at the seam. The entire selling point of this methodology is that verification reduces to first-order reasoning about single steps, with no temporal reasoning left for the user. For the third edge kind that claim fails: the obligation attached to it is itself a liveness property, not a state formula, and must be established by a nested argument of the same species. Manna and Pnueli do not paper this over. They flag it in the text as the exception, and in practice they hang a reference on such an edge pointing at the auxiliary diagram that discharges it — the sub-argument becomes a named, locatable artifact rather than an unstated debt. The overall story becomes "everything reduces to local checking except these edges, and each one visibly owes you a subproof."

That is the transferable move, and it generalizes past proof systems to any abstraction that advertises a uniform interface with a small number of genuine escapes: an allocator that is wait-free except under one condition, a pure functional layer with a handful of effectful operations, a synchronous API with one call that may block, a type system with an unchecked cast. The failure mode is to describe the abstraction by its clean case and leave the exceptions in prose or in the maintainer's memory. The better move is to make the exception a distinct, visible construct in the notation, so that "this is the case that costs more" is something a reader trips over rather than something they must know, and every instance of it names where its extra justification lives.

The same paper shows the complementary tactic for keeping such notations usable at scale: nest nodes inside enclosing nodes, where an enclosing node's assertion is conjoined into everything it contains and an edge touching it distributes over its contents. Conditions that hold throughout a region get stated once at the region rather than repeated in every node — the notational form of factoring a shared invariant out of a family of cases, which also makes the region itself a visible object with a name.

**Source:** [Temporal Verification Diagrams](../works/temporal-verification-diagrams.md) — the definitions of single, double, and solid edges with their respective verification and enabling requirements; the remark that the requirement attached to solid edges is a response formula rather than a state formula, together with the worked producer-consumer example where such edges carry references to auxiliary diagrams; and the compound-node encapsulation conventions.
