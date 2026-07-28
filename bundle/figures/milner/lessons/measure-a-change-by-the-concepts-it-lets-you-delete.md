---
type: lesson
title: "Measure a change by the concepts it lets you delete"
figure: milner
works: [the-definition-of-standard-ml]
axes: [cognitive-load, primitive-count]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Measure a change by the concepts it lets you delete

**Lesson:** Revisions to anything with users accumulate. Each request is locally reasonable, each addition is small, and the artifact ends up larger every time. The revision documented here adopts a rule that blocks that ratchet: a change is admitted only when at least one of the language, its use, its implementation, or its formal definition becomes simpler, and none of the others becomes more complicated. The test is applied to additions too, not just removals — a convenience feature was accepted specifically because the chosen way of providing it shortened the definition. The stated outcome is that after a decade of criticism and a round of both additions and subtractions, the formal definition contains fewer rules than before.

The mechanism that makes this achievable, rather than merely aspirational, is looking for the load-bearing complexity rather than trimming leaves. One facility — a form of sharing constraint between whole modules — was found to be little used in its full generality, hard to teach, and expensive to describe. Removing it did not save one concept; it deleted a cascade. Principal signatures, module names, a consistency condition, a cycle-freedom condition, a well-formedness condition, a covering relation, an admissibility notion, and an explicitness property all became unnecessary, and one of two kinds of substitution disappeared. The elaboration rules also became deterministic up to renaming. That is what a good deletion looks like: the removed feature was the reason eight other concepts existed.

The same instinct shows in replacing a subtle discipline for polymorphism in the presence of mutable state with a blunt syntactic restriction, on the evidence that the subtle version's extra power was rarely exercised in real code. The trade is explicit and unromantic — a few programs stop being accepted, one whole category of type variable vanishes, and the annoyance is documented along with the workaround. Field evidence about what people actually use is treated as admissible input to a formal design.

The habit worth stealing is to ask, of any proposed change, which existing concepts it retires. If the answer is none, the change is pure growth and should be argued for on those terms. And when hunting for simplification, do not start from the feature that looks most complicated; start from the feature that everything else's complexity is in service of. Nothing shrinks a system like removing the thing the workarounds were working around.

**Source:** [The Definition of Standard ML (Revised)](../works/the-definition-of-standard-ml.md) — the preface's stated criterion governing which amendments were admitted, and the closing appendix enumerating the changes, particularly its account of what became unnecessary once module-level sharing was removed and its rationale for adopting the restriction on polymorphic bindings.
