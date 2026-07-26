---
type: work
title: "Thrashing: Its Causes and Prevention"
figure: denning
description: Names and diagnoses thrashing, the collapse in system throughput that happens when too many processes are multiprogrammed for the available memory, forcing constant page swapping instead of useful computation. Denning traces the cause to admitting more processes than memory can hold the combined working sets of, and argues the remedy is a scheduler that refuses to add (or suspends) a process whenever doing so would exceed available page frames. It turns the working-set concept from Denning's companion 1968 CACM paper into a concrete admission-and-scheduling policy.
subdomains: [operating-systems-and-systems-programming]
year: 1968
url: https://www.denninginstitute.com/pjd/PUBS/thrashing-1968.pdf
access: public
host: self-archived
tags: [work]
---

# Thrashing: Its Causes and Prevention

**Venue/year:** Proceedings of the AFIPS Fall Joint Computer Conference 1968, Part I, pp. 915-922.
**Source:** https://www.denninginstitute.com/pjd/PUBS/thrashing-1968.pdf — live PDF (verified 2026-07-24, HTTP 200), self-archived on Denning's own institute site. Solo-authored by Denning (Princeton) — the stub's "with Kahn" attribution is a Phase 1 error, most likely confused with Denning & Kevin C. Kahn's unrelated 1975/76 paper "An L=S Criterion for Optimal Multiprogramming"; confirmed against two independent copies (this one and a UWaterloo course mirror) both crediting Denning alone.

## Lessons
- [Differentiate before you tune: a large hardware ratio can leave no safe operating margin at all](../lessons/sensitivity-before-tuning.md)
- [Allocate per unit of work so each one's performance depends only on itself](../lessons/per-unit-isolation-over-global-policy.md)
- [Idle capacity in one resource is usually a symptom of scarcity in another](../lessons/idle-capacity-names-the-real-shortage.md)
- [When a technique "doesn't work," suspect the relation between its parts before condemning any one part](../lessons/failure-lives-in-the-relation.md)
- [Two resources that constrain each other need one allocator, not two good ones](../lessons/coupled-resources-single-decision.md)
- [Find out which variable the outcome actually obeys before improving the one you find interesting](../lessons/measure-which-variable-the-outcome-obeys.md)
