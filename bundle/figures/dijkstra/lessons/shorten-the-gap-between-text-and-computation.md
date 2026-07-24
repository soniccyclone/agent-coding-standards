---
type: lesson
title: "Pick control structures that keep the written program and the running process in lockstep"
figure: dijkstra
works: [go-to-statement-considered-harmful, notes-on-structured-programming]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Pick control structures that keep the written program and the running process in lockstep

**Lesson:** A program is a static object; what it produces is a process unfolding in time, and human minds are far better at static relations than at visualizing evolution over time. So the central design question for control flow is not power or convenience but whether a reader can locate "where the execution is" using coordinates that come from the program itself rather than from the values being computed. Sequencing, selection, iteration, and calls all admit such coordinates: a position in the text, a repetition count, a call stack. Unrestricted jumps destroy them, leaving execution history as the only description of progress, which is unique but useless.

The reason this matters runs deeper than tidiness: the meaning of every variable is relative to how far the computation has progressed. A counter mid-update briefly means something different from what its name says, so you cannot use variable values to define progress without circularity. Whoever wants to state invariants, or even just explain what a variable means, needs a progress coordinate system that exists independently of the data. Disciplined control flow is what makes such a coordinate system exist.

A programmer who internalizes this stops evaluating constructs by what they can express (almost everything can express almost anything) and starts evaluating them by what they let a reader assert. Any proposed control feature earns its place only if a helpful, programmer-independent description of progress survives its use. The same test generalizes beyond jumps: implicit state machines, event soups, and callback webs all fail it in exactly the way the unrestricted jump does.

**Source:** [Go To Statement Considered Harmful](../works/go-to-statement-considered-harmful.md) — the whole letter is this argument: the static/dynamic gap, the textual and dynamic indices, and why jump-riddled programs defeat any useful progress description. Also [Notes on Structured Programming](../works/notes-on-structured-programming.md) — the section on understanding programs re-derives the coordinate-system argument and ties the three decomposition forms to the reasoning pattern each one admits.
