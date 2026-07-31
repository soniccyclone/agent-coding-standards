---
type: lesson
title: "Run independent constraint-checkers side by side and you enforce conjunctions no single traversal can"
figure: hoare
works: [communicating-sequential-processes-book]
axes: [expressiveness, parallelizability, cognitive-load]
subdomains: [foundations-of-computation, distributed-systems-and-concurrency]
tags: [lesson]
---
# Run independent constraint-checkers side by side and you enforce conjunctions no single traversal can

**Lesson:** Some requirements are conjunctions of constraints over one stream, where each constraint alone is easy and the conjunction appears to demand a machine tracking everything simultaneously. Do not build that machine. Build one component per constraint, give each a vocabulary containing only the occurrences it actually cares about, and run them together under the rule that every occurrence requires the participation of exactly those components naming it. Each component is then written as though it were the only requirement in the world; occurrences it does not name go past without it noticing or being able to interfere. The conjunction is enforced by the composition rather than by anything inside any component, which is why no component has to know that the others exist.

What this buys is not primarily speed, which is the usual excuse for reaching for concurrency. It is expressive power. Two independent counters running alongside each other accept combinations that no single traversal of the input can accept, because a single traversal has one locus of state and must somehow interleave the bookkeeping of both constraints, whereas the pair simply is not obliged to. That is a genuine increase in what can be recognized, obtained by composition rather than by any component becoming more capable — and it is the strongest available argument that concurrency is a structuring device before it is a performance device. Anyone who reaches for parallel composition only when something is too slow is leaving this behind entirely.

Two conditions make it work and both concern vocabulary. Each component must name exactly the occurrences it constrains and no others, because whatever it names it can block and whatever it omits it cannot see — so the choice of vocabularies is the whole design, and getting it wrong produces either accidental synchronization between unrelated checkers or a constraint that is silently not enforced. And the components must agree about finishing: the assembly has completed only when every one of them has, which is what makes the result a conjunction rather than a race between checkers. Where those hold, adding a new constraint means writing one more small component and joining it, with no existing component touched, and that additivity is the property that makes the technique worth adopting rather than admiring.

**Source:** [Communicating Sequential Processes](../works/communicating-sequential-processes-book.md) — the introduction to the sequential processes chapter: the recursive process accepting equally many leading and trailing symbols around a separator, and the following example which places that process in parallel with a renamed copy of itself so that one operand enforces the first equality while ignoring the symbols outside its alphabet and the other enforces the second, the pair terminating together when both have completed their allotted tasks; together with the accompanying remark that although the sequential notation alone is weaker than context-free grammars, the introduction of parallel composition permits definition of languages that are not context-free.
