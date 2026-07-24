---
type: lesson
title: "Leave choices the problem does not force unmade: nondeterminacy exposes the essential program"
figure: dijkstra
works: [guarded-commands-nondeterminacy-and-formal-derivation-of-programs]
axes: [expressiveness, parallelizability]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Leave choices the problem does not force unmade: nondeterminacy exposes the essential program

**Lesson:** Most languages force a total order onto decisions the problem itself leaves open: which of two equally valid branches to test first, which of several enabled updates to perform next. Every such forced choice is noise. It splinters one underlying algorithm into a family of superficially different texts, and it invites reasoning that silently leans on the arbitrary tiebreak rather than on anything the specification demands. Writing the program as an unordered set of guarded alternatives, any of which may fire when its condition holds, collapses that family back into a single text whose symmetry is visible. What remains on the page is exactly what the problem requires and nothing it doesn't.

The verification payoff is that a proof over a nondeterministic construct is forced to cover every resolution of the choice, so it cannot accidentally depend on an incidental scheduling property; the parallel payoff is that where the text imposes no order, an implementation is free to evaluate alternatives concurrently. Determinism, when actually wanted, becomes a late and local refinement made for stated reasons like efficiency, rather than an unexamined default inherited from the notation.

There is also a bias to overcome. Machine-level experience trains programmers to read non-reproducible behavior as malfunction, so admitting don't-care outcomes feels like sloppiness. The discipline is to distinguish unpredictability you suffer from freedom you grant: a program whose final state is any member of a characterized acceptable set is fully specified, and insisting on one particular member costs simplicity while buying nothing the specification asked for.

**Source:** [Guarded Commands, Nondeterminacy and Formal Derivation of Programs](../works/guarded-commands-nondeterminacy-and-formal-derivation-of-programs.md) — the comparison of the symmetric guarded-command form of Euclid's algorithm against its traditional lopsided variants, and the closing remarks on the mental resistance to nondeterminacy and why the calculus could not have been found without overcoming it.
