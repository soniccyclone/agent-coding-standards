---
type: work
title: "Oral History of David Cutler"
figure: cutler
description: A roughly three-hour recorded interview in which Cutler walks through his entire career in his own words, from an accidental start fixing bugs in DuPont's EXEC-II operating system through RSX-11M and VMS at DEC, the PRISM/Mica project's cancellation, and the ground-up design of the Windows NT kernel at Microsoft. It's the closest thing to a first-person design retrospective this non-publishing engineer ever gave, covering concrete engineering decisions and the reasoning behind them rather than just career anecdotes.
subdomains: [operating-systems-and-systems-programming]
year: 2016
url: https://archive.computerhistory.org/resources/access/text/2018/10/102717163-05-01-acc.pdf
extraction: complete
access: public
host: institutional
tags: [work]
---

# Oral History of David Cutler

**Author(s):** David Cutler (interviewee); Grant Saviers (interviewer)
**Venue/year:** Computer History Museum oral history, recorded February 25, 2016, in Medina, WA. CHM reference number X7733.2016.
**Source:** https://archive.computerhistory.org/resources/access/text/2018/10/102717163-05-01-acc.pdf — PDF transcript hosted directly on the Computer History Museum's own archive subdomain, verified live (HTTP 200). A companion video recording of the same interview is cataloged at https://www.computerhistory.org/collections/catalog/102717162 (also CHM-hosted).
**Host:** institutional — Computer History Museum, an official oral-history archive.

## Lessons
- [Correctness is bought at the point of authorship, and its price scales with depth](../lessons/defects-are-cheapest-at-their-origin.md)
- [Turn a global limit into per-owner budgets before anyone writes code](../lessons/turn-a-global-limit-into-per-owner-budgets.md)
- [The fastest route to a working model of a system is being forced to explain its failures](../lessons/learn-a-system-by-hunting-why-it-fails.md)
- [Minimality is a means, and treating it as the goal loses to whoever spends their budget on outcomes instead](../lessons/minimality-is-not-the-objective-function.md)
- [When predictability is the requirement, remove the sharing instead of scheduling it better](../lessons/partition-instead-of-scheduling-when-predictability-is-the-product.md)
- [Scoping a system means enumerating what cannot change, then isolating the obligation](../lessons/compatibility-is-inherited-not-chosen.md)
- [Compatibility with what already runs is the mass of a system, and the only way to carry it is at a boundary you design on purpose](../lessons/compatibility-is-the-mass-of-a-system.md)
- [Portability comes from naming the seam where the machine shows through, not from hiding the machine](../lessons/name-the-seam-where-the-machine-shows-through.md)
- [As a system's defects thin out, the survivors are almost all synchronization, so design for concurrency at the start or not at all](../lessons/synchronization-is-where-the-residual-bugs-live.md)
- [A decision repeatedly revisited costs more than a mediocre one held, because stability of the target is itself an engineering resource](../lessons/re-deciding-costs-more-than-deciding-wrong.md)
- [An interface is a promise about every future implementation, so whatever it leaves unsaid is where incompatibility will grow](../lessons/an-architecture-is-a-promise-across-implementations.md)
