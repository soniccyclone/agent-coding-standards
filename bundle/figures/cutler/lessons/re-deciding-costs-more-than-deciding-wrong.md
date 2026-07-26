---
type: lesson
title: "A decision repeatedly revisited costs more than a mediocre one held, because stability of the target is itself an engineering resource"
figure: cutler
works: [decwest-sdt-agenda-prism-vs-mips, oral-history-of-david-cutler]
axes: [cognitive-load]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# A decision repeatedly revisited costs more than a mediocre one held, because stability of the target is itself an engineering resource

**Lesson:** Engineering estimates are made against a fixed target and are silently invalidated when the target moves, so a project that re-opens its foundational choices on a regular cadence has no schedule at all, only a sequence of restarted schedules. The cost is not merely the discarded work. It is that every decision downstream of the moved one has to be re-derived, that the design rationale nobody wrote down has to be reconstructed, and that the people who built against the previous answer have to be re-convinced. Past some frequency of revisiting, an organization can no longer complete anything regardless of how competent its engineers are or how good any individual decision was, and asking for the strategy to be held stable long enough for products to be built is a technical request rather than a plea for comfort.

The same pattern accounts for how a project's scope inflates past its premise. Requirements added mid-flight do not arrive as a single large decision anyone would refuse; they arrive as individually plausible additions, each justified by a real constituency, each apparently small relative to the whole. Accumulated, they can invert the project's original rationale — an architecture chosen because it was simple enough to implement and verify cheaply becomes an architecture whose feature list makes that premise false — and they compound, since every added target multiplies the emulation, testing, and compatibility work rather than adding to it. A programmer who sees this pattern learns to ask, of each new requirement, not whether it is worth having but whether it is still the same project afterward.

The corresponding discipline is to make targets deliberately reachable and defend them, and to prefer completing a modest thing over converging on an ambitious one. When two candidate directions exist and one is speculative, building the conservative one in parallel and being willing to discard whichever loses is a legitimate use of resources, because it guarantees something ships. Splitting a shared foundation to let two constituencies pursue different quality bars, by contrast, tends to be the version of this that fails: the divergent lines end up needing each other's work, and one of them has to be brought back at a cost nobody priced when the split looked like a way to go faster.

**Source:** [DECwest/SDT Agenda: PRISM vs. MIPS](../works/decwest-sdt-agenda-prism-vs-mips.md) — the recommendations, which lead with a request to execute one strategy and hold it stable long enough for products to actually be built. Also [Oral History of David Cutler](../works/oral-history-of-david-cutler.md) — the account of repeatedly negotiating a charter only to have it revoked, of an architecture's width and feature set being reversed across years of review until its founding premise no longer held, of a five-year kernel project absorbing additional processor targets and compatibility environments after it began, and of a codebase split over differing quality expectations that he judged the wrong call.
