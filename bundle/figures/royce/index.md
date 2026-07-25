---
type: figure
title: Winston W. Royce
description: 1929-1995, Lockheed. Author of the widely (mis)cited origin of the "waterfall model" - a paper that actually argues against naive sequential process.
status: accepted
layer: implementation-mapping
subdomains: [software-engineering-and-architecture]
tags: [figure, accepted]
---

# Winston W. Royce

**Dates:** 1929-1995. Director of the Software Technology Center at Lockheed.

## Why a candidate
Included mainly as a historical fault-line marker — the paper is nuanced and actually argues *against* the naive sequential process later attributed to it, making it a useful primary source for evaluating methodology folklore versus what was actually said.

## Top 10 most influential works
Single-paper figure historically — not padded:
1. "Managing the Development of Large Software Systems" (1970, WESCON) — `public` (praxisframework.org, cs.huji.ac.il mirrors)

## Lessons
Royce's one paper is an argument about where knowledge comes from and what it
costs to be wrong. He divides a system's properties into those you can reason
out in advance and those that only exist once something runs, then organizes
everything else around that division: build a disposable version early because
measurement is the only cure for an assumption you cannot derive, fix the
resource envelope before detailed work quietly spends it, and judge any layered
arrangement by how far a discovered mistake has to travel back and how much
finished work its correction destroys. Two further lessons concern
externalization. A design that has not been written down does not exist yet, so
transferability to people who did not build it is a property of the artifact
rather than of the staffing plan; and verification should be ordered by the cost
of each detector, since the cheap trivial defects mask the expensive structural
ones until they are cleared. The sixth lesson comes from the paper's own
reception: the diagram survived transmission while the argument qualifying it
did not, which is a durable reminder that a constraint left beside a compact
representation instead of encoded inside it is a constraint already lost.
