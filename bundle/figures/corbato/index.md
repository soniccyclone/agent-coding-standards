---
type: figure
title: Fernando Corbató
description: 1926-2019, MIT. Led CTSS (first general-purpose time-sharing system) and Multics, which directly inspired Unix.
status: accepted
layer: implementation-mapping
subdomains: [operating-systems-and-systems-programming]
tags: [figure, accepted]
---

# Fernando Corbató

**Dates:** 1926-2019. MIT professor.

## Why a candidate
Organized and led the team that proved interactive multi-user timesharing worked, establishing the OS-as-resource-scheduler model Unix inherited wholesale.

## Top 10 most influential works
1. "Introduction and Overview of the Multics System" (1965, with Vyssotsky) — `public` (multicians.org, third-party rehost)
2. "Multics: The First Seven Years" (1972, with Clingen, Saltzer) — `public` (multicians.org, third-party rehost, posted with AFIPS permission)
3. "On Building Systems That Will Fail" (1991 Turing lecture) — `public` (self-archived by Corbató, larch-www.lcs.mit.edu:8001/~corbato/turing91/; the CACM/ACM DL originals 403 to unauthenticated requests)
4. "An Experimental Time-Sharing System" (1962, the original CTSS paper) — `public` (self-archived by Corbató, larch-www.lcs.mit.edu:8001/~corbato/sjcc62/). Stub title corrected: no paper titled "A New Remote-Accessed Man-Machine System" exists under Corbató's name; this is the actual 1962 CTSS launch paper.

4 distinct, verifiable works. All 4 confirmed public — see bundle/figures/corbato/works/ for individual work files (Phase 3).

## Lessons

Corbató's thinking starts from a reordering of what a computing system is for: the scarce resource is the person's attention, not the processor's cycles, so the quantity to minimize is the delay around a human's question-and-answer loop and machine utilization is merely a term inside that larger accounting. Everything downstream follows from taking that seriously under real constraints. Because latency is the objective, overload behavior becomes part of the specification rather than an accident, and the mechanism worth choosing is the one whose worst-case bounds fall out of its own structure instead of out of a benchmark — with policy driven by what the system can observe for itself rather than by what users declare about their own work. Because layout decisions must stay open across hardware generations, identity goes in the interface and location in the implementation, with indirection spent deliberately on the axes where change actually arrives and nowhere else. Because a system meant never to stop cannot be improved by stopping it, in-place modification and self-hosting become functional requirements, and the system's own kernel gets built out of the same facilities handed to its users — a discipline that both removes ceilings and guarantees the shared mechanism is the most heavily exercised one. Because central attention does not scale, the authority to allocate and to extend is subdivided downward, while duties like multiprogramming and backup migrate to whichever level can both see enough to discharge them and amortize their cost. And running underneath all of it is an unusually honest epistemology: a system breaking new ground cannot be reasoned about until it has been run, simulation does not rescue you, the hard intellectual work is finding the decomposition rather than writing the code inside it, and mistakes in ambitious systems are certain — which argues for narrowing what a notation permits, recording the preconditions a decision silently rests on, and treating every efficiency gain as a change to the failure model and not only to the cost model.
