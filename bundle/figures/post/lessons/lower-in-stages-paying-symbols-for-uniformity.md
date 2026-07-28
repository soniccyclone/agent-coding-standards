---
type: lesson
title: "Lower a rich notation in stages, paying in symbols for uniformity"
figure: post
works: [formal-reductions-of-the-general-combinatorial-decision-problem]
axes: [expressiveness, primitive-count, cognitive-load, verifiability]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# Lower a rich notation in stages, paying in symbols for uniformity

There are two ways to get from a permissive notation to an austere one. You can try to hit the target in a single clever encoding, or you can build a staircase where every step gives up exactly one convenience and nothing else. Post takes the staircase. Rules that may have many premises become rules with one premise; rules whose one premise can rearrange, drop, or duplicate its variables become rules that keep the variables in place; rules with several variables become rules with one; rules that hold their fixed material on both sides of the variable become rules that hold it only in front and only behind. Each step is a small, separately checkable claim, and the composite theorem is just the four claims chained.

The trade being made is explicit and worth internalizing: every step buys uniformity by spending alphabet and rule count. The austere system needs bookkeeping symbols the permissive one never required, and one original rule may explode into a family of them. That is the correct direction to spend. A rule set that is bigger but shaped identically everywhere is cheap to reason about mechanically, whereas a rule set that is small because each rule is allowed to be structurally different is expensive to reason about at all. Compactness of the basis and cheapness of analysis pull against each other, and analysis usually deserves to win.

This is the shape of every lowering pipeline a compiler engineer has ever built, and Post's version is worth studying because he never pretends the steps are free. A programmer who takes this seriously stops trying to write the one heroic translation from surface language to machine and instead defines a sequence of intermediate forms, each strictly poorer than the last, each with a stated invariant, each with its own correctness argument. When a bug appears you can bisect the pipeline instead of re-deriving the whole encoding. And when a later result needs proving, you prove it once against the poorest form and let the staircase carry it back up.

The staircase also tells you where to stop shrinking. Post's final form is not the smallest conceivable rewriting discipline; it is the smallest one his four reductions actually reach while preserving the property he needs. Minimality is a destination you arrive at by construction, not a target you declare in advance and then bend the design to hit.

**Source:** [Formal Reductions of the General Combinatorial Decision Problem](../works/formal-reductions-of-the-general-combinatorial-decision-problem.md) — the second section, which carries out the reduction from the general rule format down to the one-rule-shape format as four successive simplifications, each described together with the added letters it costs.
