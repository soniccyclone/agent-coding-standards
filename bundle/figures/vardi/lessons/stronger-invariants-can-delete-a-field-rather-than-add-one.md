---
type: lesson
title: "Stronger invariants can delete a field rather than add one"
figure: vardi
works: [reasoning-about-knowledge]
axes: [primitive-count, cognitive-load, expressiveness]
subdomains: [formal-methods-and-verification, foundations-of-computation]
tags: [lesson]
---
# Stronger invariants can delete a field rather than add one

**Lesson:** Committing to more laws feels like taking on more burden, and often the accounting runs the other way. Vardi's model of knowledge carries, in general, a per-state relation saying which alternatives are entertained from where — a genuinely state-dependent component, and the source of most of the model's complexity. Demand the full set of strong laws and restrict to a single participant, and that component collapses: every state entertains every state, the relation carries no information, and it can be dropped from the representation entirely. What remains is a bare set of alternatives that is the same wherever you stand. The state-dependence was never intrinsic. It was the price of admitting weaker relations, and paying the strong invariants up front buys its deletion.

The residue left behind when the collapse is only partial is the more instructive half. Weaken the laws just enough to model believing things that are false and exactly one component survives the flattening: a distinguished actual state, which need not be among the alternatives the participant entertains. One extra element is the entire formal difference between a model that cannot be wrong and one that can. That is the kind of measurement worth wanting about any design decision — not an argument that a guarantee is nice to have, but a count of what the representation costs with it and without it. When the cost of dropping a guarantee is a single distinguished field, the trade is legible; when nobody has done the collapse, the cost is invisible and the discussion turns into taste.

Two disciplines follow. First, before building tooling on the general form of a structure, check whether your actual invariants collapse it, because a representation with fewer moving parts is a better place to reason and every field you keep is one every future reader must consider. The right question about a component is not what could vary but what can still vary given the invariants you have already committed to — and the answer is frequently nothing, at which point the component is decoration. Second, the collapse depended on two things at once, the strength of the laws and the fact that there was a single participant. With several participants the relations must differ from one another and the flattening is unavailable. So a simplification licensed by strong invariants is licensed only at the arity where you proved it, and carrying it across to the multi-party case is exactly the error the single-party proof cannot warn you about.

**Source:** [Reasoning About Knowledge](../works/reasoning-about-knowledge.md) — the proposition closing chapter three's completeness section, showing that for a single agent under the strongest axiom system every structure is equivalent to one whose possibility relation is universal, so that one may speak of a single set of worlds considered possible, identical at every state; and its companion for the belief system, where the equivalent structure reduces to a set of entertained worlds plus one distinguished actual state that need not belong to it.
