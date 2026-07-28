---
type: lesson
title: "Size a robust aggregate by how far two honest observers' views can diverge, not by how many liars there are"
figure: lynch
works: [reaching-approximate-agreement-in-the-presence-of-faults]
axes: [verifiability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity]
tags: [lesson]
---
# Size a robust aggregate by how far two honest observers' views can diverge, not by how many liars there are

Any function that combines reports from partly untrustworthy sources needs two separate properties, and conflating them is the usual error. The first is containment: whatever the liars submit, the output must land inside the span of what the honest sources actually hold, so that garbage cannot drag the result outside the legitimate range. That property is governed by the number of liars, and trimming that many extremes from each end of the sorted reports secures it. The second property is convergence: two honest parties, applying the function to *different* report sets, must end up closer together than their inputs were. That one is governed by something else entirely — by how many entries two honest views can differ in — and it is the property people forget to size for.

The distinction has teeth because the two counts come apart. When everyone reliably hears from everyone, two honest observers see identical reports from all honest sources, so their views can diverge only in the liars' entries. Loosen the setting so each party proceeds after hearing from a bare majority-plus-margin rather than from everyone, and view divergence roughly doubles: the liars can still say different things to different listeners, and now honest reports counted by one listener may simply be missing from the other's set. The convergence machinery must be widened to match this larger divergence, and the price shows up in the participant count needed for the whole scheme to contract at all. Same trimming for containment, wider spacing for convergence, and a stricter requirement on how many participants you need — all traceable to one quantity that has nothing to do with the fault bound directly.

The transferable habit is to make "how much can two honest replicas' inputs differ" an explicit, named quantity in any voting, averaging, or reconciliation design, then derive filter widths from it rather than from the fault tolerance. This is the difference between a median-of-reports scheme that provably contracts and one that merely looks robust because it discards outliers. It also explains why moving such a component from a setting where everyone waits for everyone into one where participants proceed on partial information is never a free refactor: the containment argument survives untouched, the convergence argument silently breaks, and nothing in the code visibly changes at the moment it stops working.

**Source:** [Reaching Approximate Agreement in the Presence of Faults](../works/reaching-approximate-agreement-in-the-presence-of-faults.md) — the split is visible in how the two parameters of the averaging function are justified: the trimming parameter is argued from the fault bound and underwrites validity, while the sampling parameter is argued from the maximum difference between two honest processes' received multisets, and it is the latter that changes between the synchronous and asynchronous algorithms.
