---
type: lesson
title: "Separate the proposal from the decision to admit it"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, verifiability]
subdomains: [software-engineering-and-architecture, distributed-systems-and-concurrency]
tags: [lesson]
---
# Separate the proposal from the decision to admit it

**Lesson:** A state update written as one expression is doing two jobs that deserve to be separated: computing what the new information would be, and deciding how much of the existing state it should displace. Fused together, the second job is invisible — it is implied by whatever the expression happens to do — and it is almost always the crude answer, which is "all of it." Split apart, the second job becomes an explicit, per-element quantity that can be reasoned about, tuned, or determined from evidence like anything else. You end up with a candidate value, a decision about how much of the old state to keep, and a decision about how much of the candidate to let in, composed at the end.

Making retention and admission separate quantities has consequences beyond tidiness. Each becomes a graded amount rather than a binary, so the update can partly preserve and partly overwrite element by element instead of choosing one policy for the whole state. Each can be conditioned on different things — how much to discard is naturally a function of what just arrived signalling that a context has ended, while how much to admit is naturally a function of whether the new information is the kind worth keeping. And because retention now appears as an explicit multiplier on the existing state, its default can be set to preserve, which is what keeps information alive across long runs instead of being ground away by repeated wholesale replacement.

A related split is worth making at the same time: separate the state you keep from the view of it you expose. A durable store holding everything accumulated so far, and a narrow working view selected from it for immediate use, is a strictly more expressive arrangement than one state serving both purposes, because it lets the system remember something without currently attending to it. The selection is a third graded decision, and it too can be determined rather than fixed.

Read generally, this is the argument for pulling policy out of mechanism at the point where they are most often welded together — the write. Caches that evict as a side effect of insertion, buffers that drop as a side effect of being full, reconciliation loops that overwrite as a side effect of observing, all have an admission policy that nobody wrote down and nobody can change without editing the update path. Naming it as its own value is the whole intervention, and it is what makes the policy available for tuning, testing, and eventually for being derived from data rather than guessed.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the long-short-term-memory section of the recurrent-networks chapter, which computes a candidate update separately from two gate vectors with entries between zero and one, combines the retained portion of the previous long-term state with the admitted portion of the candidate, keeps a separate cell state for long-term memory and hidden state for working memory, and derives the working memory by applying a third gate to the long-term state.
