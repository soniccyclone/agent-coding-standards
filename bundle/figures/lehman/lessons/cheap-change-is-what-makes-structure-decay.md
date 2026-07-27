---
type: lesson
title: "Structural decay is the default outcome precisely because changing software is so cheap"
figure: lehman
works: [programs-life-cycles-and-laws-of-software-evolution, on-understanding-laws-evolution-and-conservation-in-the-large-program-life-cycle]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Structural decay is the default outcome precisely because changing software is so cheap

**Lesson:** Software has no physical wear. It does not rot in place; it only ever changes because someone edits it. Yet long-lived systems reliably become harder to work on, and the mechanism is the very property that makes software attractive. A change costs almost nothing to author and nothing at all to replicate across every installation, so the standing temptation is always to superimpose the change on what exists rather than to re-derive the structure that would accommodate it. Each superimposition is locally rational and globally corrosive. Capability that nobody anticipated gets laid over an architecture that was never asked to support it, and the architecture is never revisited because revisiting it is the one expensive option on the menu.

The accumulated effect is that the system gets stiffer: change takes longer, costs more, and is likelier to be wrong, which raises the price of every subsequent improvement. Structural complexity therefore rises monotonically unless effort is deliberately spent to hold it down or reduce it — and that effort is invisible in the release notes, which is exactly why it does not get funded. Meanwhile the same softness fragments the system sideways: different installations acquire different local patches, versions multiply, and keeping track of what is actually running anywhere becomes its own major task.

The distinctive claim is where the causality sits. Complexity growth is not a consequence of bad programmers or of any particular language or methodology; it is a consequence of an economics that rewards patching over restructuring at every individual decision point. That means no amount of individual discipline fixes it, because each individual decision was defensible. Only a policy that spends against the trend does.

A programmer who believes this treats restructuring work as load-bearing rather than optional hygiene, and expects to schedule it explicitly — including releases whose whole content is cleaning up, with no new function to show for them. They also read a system's history for stiffness: rising fractions of the system touched per change, rising ratios of old code disturbed per unit of new code. Those ratios are the visible shadow of coupling, and they say more about whether the next change will go well than any static inspection of the code does.

**Source:** [Programs, Life Cycles, and Laws of Software Evolution](../works/programs-life-cycles-and-laws-of-software-evolution.md) — the second law of program evolution, and the passage on software's three distinguishing properties, which argues that its malleability is what drives change-upon-change and the resulting stiffening. Also [On Understanding Laws, Evolution, and Conservation in the Large-Program Life Cycle](../works/on-understanding-laws-evolution-and-conservation-in-the-large-program-life-cycle.md) — its commentary on the second law, which names structural upkeep as antiregressive work that shows no visible benefit and is therefore omitted from stated objectives, and asks for the balance between functional and structural effort to be planned against the program's expected lifetime.
