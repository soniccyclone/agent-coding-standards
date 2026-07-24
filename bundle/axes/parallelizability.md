---
type: axis
title: Parallelizability
description: How naturally a construct decomposes into independently executable pieces without hidden shared-mutable-state coordination.
tags: [axis, concurrency, parallelizability]
---

# Parallelizability

## Definition
How naturally a construct splits into pieces that can execute independently —
whether concurrency requires explicit, hidden coordination over shared
mutable state, or whether the construct's own structure (e.g. no shared state
to begin with) makes independent execution the default rather than something
bolted on. Distinct from verifiability: a construct can be easy to prove
correct sequentially while still resisting decomposition into independent
units of work.

## Rollup
No lessons scored on this axis yet.

## Lessons scored here
_(empty)_
