---
type: figure
title: Jerome H. "Jerry" Saltzer
description: b. 1939, MIT. End-to-End Arguments in System Design - one of the most cited general-architecture papers in CS, about where functionality belongs in a layered system.
status: accepted
layer: implementation-mapping
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [figure, accepted]
---

# Jerome H. "Jerry" Saltzer

**Dates:** b. October 9, 1939, Nampa, Idaho. SB/SM/ScD all in Electrical Engineering from MIT; doctoral dissertation ("Traffic Control in a Multiplexed System") advised by Corbató (see [corbato](../corbato/index.md)). Joined MIT EECS faculty 1966; team leader on Multics, contributing the now-standard kernel stack-switching method for process switching and its security architecture.

## Why a candidate
Surfaced via the cyber/crypto/ML scoping discussion, not the original fan-out — the identified gap once Yao and Rabin (Algorithms & Complexity) and McCarthy (Programming Languages, via Lisp not AI) turned out to already cover the general-abstraction content from crypto and AI respectively. Security *design principles*, not crypto technique: "The Protection of Information in Computer Systems" articulates general systems-architecture reasoning (least privilege, economy of mechanism, fail-safe defaults) rather than narrow cryptographic method. "End-to-End Arguments in System Design" is a first-principles argument about where functionality belongs in a layered system — one of the most cited general-architecture papers in CS, general the same way Parnas's decomposition criteria are general, not domain-specific the way a rendering algorithm or a specific crypto protocol is.

## Top 10 most influential works
Publication list (~50 items) self-archived in full at web.mit.edu/Saltzer. Phase 3 pass verified and formalized 5 works into individual `works/` files (all confirmed public, self-archived on Saltzer's own MIT page, PDFs resolve directly):
1. "End-to-End Arguments in System Design" (1984, with Reed, Clark, ACM TOCS) — `public` — [work file](works/end-to-end-arguments-in-system-design.md)
2. "The Protection of Information in Computer Systems" (1975, with Schroeder, Proc. IEEE) — `public` — [work file](works/the-protection-of-information-in-computer-systems.md)
3. "Protection and the Control of Information Sharing in Multics" (1974, CACM) — `public` — [work file](works/protection-and-the-control-of-information-sharing-in-multics.md)
4. "The Multics Kernel Design Project" (1977, with Schroeder, Clark, Proc. 6th SOSP) — `public` — [work file](works/the-multics-kernel-design-project.md) — replaces the earlier vague "Multics kernel design... documentation (multicians.org)" placeholder with the actual cited paper, cross-verified against its citation in the End-to-End Arguments reference list.
5. "Traffic Control in a Multiplexed Computer System" (1966, Sc.D. dissertation, advised by Corbató) — `public` — [work file](works/traffic-control-in-a-multiplexed-computer-system.md) — added beyond the original 4: explicitly named in this figure's own bio as the origin of his process-switching work, and confirmed public (self-archived + independently mirrored at MIT DSpace and CSAIL Publications).

Still fewer than 10 individually verified — this remains a seminal-works pass against the ~50-item self-archive, not an exhaustive bibliography sweep. Candidates not pursued because they read as narrower/derivative of the above rather than independently central: the Multics ring-based hardware protection paper, the "Origin of Kerberos" retrospective, and the various CTSS/Project Athena technical memos.
