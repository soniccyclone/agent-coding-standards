---
type: lesson
title: "The formalism a requirement is natural to state in need not be the one it is settled in"
figure: pnueli
works: [on-the-synthesis-of-a-reactive-module]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---

# The formalism a requirement is natural to state in need not be the one it is settled in

**Lesson:** A requirement on a long-running component is a statement about one history at a time: whatever happens, this must hold along the way. Notation that speaks of a single unfolding sequence is exactly right for writing that down, and reaching for anything richer would be waste. But the question of whether such a requirement can be met is not a statement about one history. It is a statement about the whole fan of histories the uncontrolled side could force, together with a chosen response at every point in that fan. That object branches. So the requirement belongs in one formalism and its buildability belongs in another, and insisting that a single notation carry both is a category error that costs you either expressive economy in the specification or the ability to answer the question at all.

Generalized, the move is: identify what species of mathematical object would witness the claim you are making, before choosing the machinery. Here the witness is a tree of responses indexed by input history, and once that is recognized every downstream choice falls out — machinery for recognizing sets of trees rather than sets of sequences, and, in the bounded case, a finite device that walks the tree emitting responses, which is not a description of a program but literally is one. Getting the witness's shape wrong is the expensive mistake, because it sends you looking for the answer among objects that could never have been the answer. Confirming buildability and obtaining the artifact stop being two activities when the witness is the artifact.

There is a second, subtler discipline here. The same question usually admits several formulations that are provably interchangeable, and choosing among them is a real decision rather than a matter of taste. One arrangement can push a problem down into a weaker fragment where existing decision procedures already apply, which is what you want when a machine will answer it. A different arrangement of the same question can be preferred precisely because it displays a structural fact you need a human to keep in view — in this case, the asymmetry between the quantities the implementor assigns and the quantities imposed on it, which one framing makes visually unmissable and another buries. Equivalence up to truth value is not equivalence up to usefulness.

A programmer who has taken this on stops treating "which notation should I use" as a single question with a single answer, and asks it once per purpose: one for capturing intent economically, one for mechanical checking, one for the artifact that ships. They also stop expecting a translation between the three to be free, and instead ask what each translation preserves, since the point of moving between formalisms is to gain a property the previous one lacked while carrying the meaning across intact.

**Source:** [On the Synthesis of a Reactive Module](../works/on-the-synthesis-of-a-reactive-module.md) — the central claim that a requirement written in single-history notation must nonetheless be resolved in a branching framework, the development section establishing that buildability corresponds to the existence of a strategy tree and that a bounded strategy is realized by a finite emitting device, and the introduction's remark that an alternative framing quantifying only over unchanging parameters would also do, with the explicitly quantified version preferred for the asymmetry it exposes.
