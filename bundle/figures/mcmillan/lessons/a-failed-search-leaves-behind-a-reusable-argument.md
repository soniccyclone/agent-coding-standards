---
type: lesson
title: "A failed search leaves behind a reusable argument, not just a verdict"
figure: mcmillan
works: [interpolation-and-sat-based-model-checking]
axes: [verifiability, expressiveness]
subdomains: [formal-methods-and-verification, algorithms-and-complexity]
tags: [lesson]
---
# A failed search leaves behind a reusable argument, not just a verdict

Most engineering treats a decision procedure as an oracle that returns a bit. You ask "is there a bug within twenty steps?", the tool says no, and you throw everything else away. McMillan's move is to notice that the *no* is backed by a structure — a resolution derivation — and that this structure knows far more than the single bit it was asked to produce. The bounded answer is logically almost worthless on its own: proving there is no short counterexample says nothing about whether the property holds. But the shape of the argument that established it encodes which configurations the machine can actually get into, and that information generalises past the bound the question was posed at.

The principle worth carrying is that a proof is a data structure you can compute over, not a certificate you file away. Whenever a solver, type checker, constraint engine or test-generation pass fails to find something, it has necessarily constructed a reason. That reason is denser than the answer. Reading it back out turns a procedure that only refutes into a procedure that can also confirm — which is exactly the gap that separated the cheap, bounded, counterexample-hunting technique from the expensive, unbounded, exhaustive one.

This holds because a refutation is forced to mention exactly the facts it depended on. Anything the argument never touched was irrelevant to the failure, and anything it touched repeatedly is load-bearing about the system's real behaviour. The proof is therefore a free relevance filter, automatically fitted to the specific problem instance rather than hand-tuned by an engineer guessing at what matters. McMillan's benchmarks make the practical stakes concrete: the same problems that were untouchable when only the yes/no answer was consumed became routine once the argument was harvested.

A programmer who believes this stops designing tool interfaces that return booleans. They ask what their checker, compiler pass, or solver knows at the moment it gives up, and they make that knowledge addressable. They also stop assuming a cheap incomplete method and an expensive complete one are different tools — often the complete method is the cheap one plus a habit of reading its own scratch work.

**Source:** [Interpolation and SAT-Based Model Checking](../works/interpolation-and-sat-based-model-checking.md) — the framing in the introduction and the interpolation construction that follows, where the refutation graph produced by a bounded satisfiability check becomes the raw material for an unbounded verification method.
