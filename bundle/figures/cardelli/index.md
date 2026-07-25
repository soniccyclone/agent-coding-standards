---
type: figure
title: Luca Cardelli
description: b. 1954, Bell Labs/DEC/MSR. Formal object calculi - mathematical grounding for encapsulation, message passing, subtyping.
status: accepted
layer: design-thought
subdomains: [programming-environments-and-object-systems]
tags: [figure, accepted]
---

# Luca Cardelli

**Dates:** b. 1954. Italian-born computer scientist; Bell Labs, then Digital/Compaq SRC, then Microsoft Research Cambridge.

## Why a candidate
Provided the formal theoretical grounding for objects — object calculi that model encapsulation, message passing, and subtyping mathematically rather than just implementing them — giving the "objects as a rigorous lineage of abstraction thought" claim actual theoretical teeth rather than folklore.

## Top 10 most influential works
Maintains an extensive self-archived personal papers page (lucacardelli.name) — many nominally paywalled works have practically-public author copies:
1. "On Understanding Types, Data Abstraction, and Polymorphism" (1985, with Wegner, ACM Computing Surveys) — `public` (self-archived)
2. "A Semantics of Multiple Inheritance" (1984) — `public` (self-archived)
3. "An Imperative Object Calculus" (1996, with Abadi) — `public` (self-archived)
4. *A Theory of Objects* (1996, book with Abadi) — `paywalled` (drafts self-archived)
5. "Basic Polymorphic Typechecking" (1985, with Wegner) — `paywalled` (likely self-archived)
6. "A Language with Distributed Scope" (1995, POPL/Obliq) — `paywalled` (likely self-archived)
7. "Structural Subtyping and the Notion of Power Type" (1989, with Canning et al.) — `paywalled`
8. "The Functional Abstract Machine" (1983) — `uncertain`

_(Note: the stub list above stopped at 8 of a nominal "top 10." Phase 3 verified all 8, corrected several bibliographic errors introduced in the low-rigor pass, and added one paper — "A Theory of Primitive Objects: Untyped and First-Order Systems" — as a public stand-in for item 4, which turned out to be inaccessible; see the access flag below and `works/` for details.)_

## Phase 3 access flag

**"A Theory of Objects" (Abadi & Cardelli, Springer, 1996) — the book — is not available as public full text anywhere checked.** This is the single work most central to Cardelli's "why a candidate" case (it's the full monograph treatment of the object calculus that gives OO encapsulation/subtyping/message-passing a formal semantics), so flagging rather than silently dropping it.

Checked:
- `lucacardelli.name/TheoryOfObjects.html` (the author's own book landing page, live and via curl): only front matter is linked (Preface, Prologue, Table of Contents, Concept Map, Index, Order Information, FAQ, Related Work, Errata) — no full-text PDF.
- The page does contain an "eBook" link, but its href is a literal local Windows filesystem path (`C:\Dropbox\Luca\Research\...\A+Theory+of+Objects.pdf`) explicitly labeled `(private)` in the visible text — a stray artifact from the author's own file browser, not a working public URL.
- Wayback Machine snapshots of `TheoryOfObjects.html` going back to 2006 show the same front-matter-only link set; no era where a full-text PDF was linked.
- Springer's page (`springer.com/.../978-0-387-94775-4`) is the paywalled commercial listing.

Mitigation: Cardelli and Abadi's "A Theory of Primitive Objects: Untyped and First-Order Systems" (Information and Computation 125(2), 1996; self-archived, `works/a-theory-of-primitive-objects-untyped-and-first-order-systems.md`) is the paper the book's core theory was expanded from, and is fully public. It's added to `works/` as the closest available substitute, but it is not the book — no work file exists for the book itself.

## Lessons

Cardelli's method is to refuse folklore about a construct and ask what it denotes, because once that is fixed the relations everyone was arguing about (substitutability, hiding, inheritance, ambiguity) become computable facts rather than tastes, and rules that intuition would have gotten backwards — the reversal on function arguments, the invariance forced by self-reference — are derived instead of guessed. Around that core sits a repeatable working loop: identify which feature of a bundled paradigm is actually definitional and study it alone; reduce the surviving vocabulary to a few binding forms and judge the design by what derives from them; state the permissive rule you wish held and then build the four-line program that breaks it, treating the counterexample as a diagnostic that names the dependency you overlooked; specify the resulting judgment before writing any checker, so the code has something to be answerable to and any deliberate conservatism is a recorded decision. He is equally explicit about what such choices cost, treating decidability of his own tooling as a budget to overspend knowingly, warning that merging two levels for elegance forfeits the staging questions a compiled system later needs, and insisting that compatibility follow the shape of a value while any invariant the shape cannot express gets sealed behind operations rather than protected by a name. The systems work applies the same discipline in the other direction: minimality belongs to the layer you reason in and richness to the layer you execute on, obligations flow downhill and must be stated, the semantics should be written over the stacks and store you will actually run, the dominant operation is factored so its common sequences cancel, and performance is bought with an invariant the language itself guarantees while the constructs that violate it are quarantined. Extended to distribution, one invariant — a name means what its binding site says, wherever it runs — is carried across the boundary and everything else follows from preserving it: computations travel as environments rather than text, authority reduces to reachability, the lock discipline reuses the same internal-versus-external distinction that decides protection, and mobility of state is programmed from cloning and redirection rather than granted as a feature.
