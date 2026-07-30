---
type: lesson
title: "Every cache asserts that nothing observable has changed; if you cannot witness that, the optimization is a semantic change"
figure: sussman
works: [lambda-the-ultimate-imperative]
axes: [verifiability, hardware-affinity]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Every cache asserts that nothing observable has changed; if you cannot witness that, the optimization is a semantic change

**Lesson:** Deferring a computation and remembering its result look like the same optimization, and for pure expressions they are. The moment mutation exists anywhere in the program they come apart, and the gap is easy to miss because the fast version is right almost all the time. A deferred computation re-evaluated at each reference sees the world as it is at that reference; the same computation evaluated once and cached reports the world as it was at the first reference. Any program whose correctness depends on repeated references yielding different answers — the classic case being a numerical integration that advances a variable and re-reads an expression mentioning it — silently produces the wrong number under caching, with no error and no crash. That is the worst failure mode available: an efficiency change that quietly alters meaning in exactly the cases the naive test suite does not cover.

The repair is not to abandon the cache but to make the invariance it assumes into something checkable. Store, alongside the remembered value, a token representing the state of the world at the moment it was computed, and on each reference compare tokens before trusting the cache. When the token is unchanged the memory is valid and you keep the win; when it changed you recompute. The design work is entirely in choosing the token, because it fixes both correctness and cost: too coarse and you invalidate on changes that could not have mattered, too narrow and you miss changes that did. The authors take the coarsest sound choice — a global count of every effect that might matter — and the choice is deliberate, since a coarse-but-sound witness is a defensible trade and a narrow-but-unsound one is a bug.

Two habits follow. First, when you introduce memoization, name out loud the invariance you are assuming and go looking for the code that violates it, rather than assuming purity because most of the code is pure. Second, keep the mutation you use to *implement* the cache strictly separate from the mutation the program is doing, and make sure the bookkeeping writes cannot themselves trip the validity check — a cache that invalidates itself by filling itself is a genuine and easily-shipped mistake. Both habits come down to the same discipline: an optimization is a claim, the claim has a precondition, and unstated preconditions are how correct programs become subtly wrong ones.

**Source:** [Lambda: The Ultimate Imperative](../works/lambda-the-ultimate-imperative.md) — the by-need section's caching wrapper that replaces itself with its result, then the fast-by-name section showing the integration example whose answer depends on re-evaluation and therefore breaks under caching, the revised wrapper that guards its stored value with a global effect count, and the accompanying insistence that the modelling-level assignment used to update the cache must not itself increment that count.
