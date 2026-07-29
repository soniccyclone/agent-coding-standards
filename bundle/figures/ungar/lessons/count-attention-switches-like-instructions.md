---
type: lesson
title: "Count the programmer's attention shifts the way you count instructions, because that is the resource being spent"
figure: ungar
works: [debugging-and-the-experience-of-immediacy]
axes: [cognitive-load]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Count the programmer's attention shifts the way you count instructions, because that is the resource being spent

**Lesson:** Tool designers count things the machine spends and ignore things the person spends, even though the person is the bottleneck. The costs worth counting are concrete: how far the eye must travel between two facts that have to be related, how many operations separate a question from its answer, how long a wait sits between an action and its consequence, and how much has to be held in memory across each of those gaps. Every one of them is a fixed tax charged on each repetition of the innermost loop of the work, which for debugging is a very tight loop indeed. Put a value display in a panel on the far side of the screen from the code and you have charged an eye movement plus a memory item per step, thousands of times over.

The reason these costs behave badly is that the capacity being consumed is small and non-negotiable. Short-term memory does not scale with effort or experience, and once it is full the programmer stops making progress on the bug and starts making progress on bookkeeping. Worse, a gap that has to be bridged consciously never becomes automatic; the association stays effortful indefinitely. Close the gap — put the value adjacent to the expression that produced it, keep every view synchronized without being asked, make any related fact reachable in a single operation — and the connection drops below deliberate attention entirely. The programmer stops maintaining a mental correspondence between the display and the system and starts treating them as the same thing, which is the point where all that capacity comes back for the actual problem.

This turns interface quality into something arguable with numbers rather than taste. You can count the eye movements and operations in a workflow, and you can compare two designs on that count. It also explains why adding a feature can make a tool worse: a new panel that answers a question is a loss if answering it now requires a look away from where the work is. A programmer who accepts this budget stops asking whether the information is available and starts asking how many attention shifts stand between the person and it.

**Source:** [Debugging and the Experience of Immediacy](../works/debugging-and-the-experience-of-immediacy.md) — the spatial and semantic immediacy sections, which price screen distance and interaction steps as demands on the programmer's short-term memory and argue for adjacency, automatic view synchronization, and a one-operation bound between any two related pieces of information.
