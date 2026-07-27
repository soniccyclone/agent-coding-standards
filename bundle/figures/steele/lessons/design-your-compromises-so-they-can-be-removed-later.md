---
type: lesson
title: "Shipping a known compromise is fine; the design work is making it removable, and an omission is a compromise too"
figure: steele
works: [growing-a-language]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Shipping a known compromise is fine; the design work is making it removable, and an omission is a compromise too

**Lesson:** Having accepted that whatever ships first tends to win, this work draws the practical conclusion without flinching: you will probably have to put flaws into the design in order to get it out on time. What it insists on is that flaws differ enormously in kind. A compromise can be built so that extracting or repairing it later is bounded work, or it can be built so that the rest of the design grows around it and it becomes permanent. That difference is decided at the moment you introduce it, by whether you thought about removal, and it costs almost nothing to think about then and cannot be recovered afterwards. The talk's cautionary case is a language whose strings were fixed in size, a limitation that had to change for the language to be usable on real work, in a design that had not anticipated changing in that direction — so the change was largely never made.

The move that gives the lesson its edge is the reclassification of absences as compromises. Something good you left out is as much a debt as something bad you put in, and it carries the same obligation: have a plan for adding it, and make sure the parts you are shipping now do not foreclose it. This turns a large class of decisions that normally feel free into decisions with a recorded cost. Deciding not to support a capability yet is fine; deciding it in a way that lets the surrounding design assume the capability will never exist is the actual error, and it is invisible at the time because nothing is broken.

What this asks of a designer is a specific and unusual habit: enumerate what you are consciously not doing, and for each one identify the assumption elsewhere in the design that would have to be false for it to remain addable. Most foreclosures happen through exactly such assumptions rather than through explicit prohibition — a representation exposed to callers that would have to change, a contract that promised an ordering, a name claimed that the future feature needed. The talk's companion argument makes the reason this matters concrete, since the whole case for planning growth collapses if the growth points get accidentally welded shut in version one.

A programmer with this instinct writes down the shortcuts as shortcuts, adjacent to the code, with the ceiling and the exit named. They distinguish debt they chose from debt they inherited by accident, and they treat "we can add that later" as a claim requiring evidence rather than a reassurance. And they apply the same reading to other people's systems: the interesting question about a young platform is not what it lacks but whether what it lacks is still reachable from where it is.

**Source:** [Growing a Language](../works/growing-a-language.md) — the late passage distinguishing compromises designed for later removal from compromises you get stuck with, its extension of the idea to good things deliberately left out, and the earlier account of a language whose unanticipated fixed-size strings could not be fixed.
