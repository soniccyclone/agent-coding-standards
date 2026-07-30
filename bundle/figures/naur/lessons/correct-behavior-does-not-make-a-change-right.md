---
type: lesson
title: "Behavioral correctness does not make a change right; judge it against the account the system embodies"
figure: naur
works: [programming-as-theory-building]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Behavioral correctness does not make a change right; judge it against the account the system embodies

**Lesson:** Any given change to a working system can usually be realized many different ways, and a large number of them produce exactly the right observable behavior. Testing, type checking and review of the diff in isolation all accept that whole set equally, because they inspect what the program does rather than whether the change belongs. The distinction that actually predicts long-term viability is invisible at that level: some of those equally-correct edits extend the system's existing account of its problem in its own terms, and others bolt on machinery that answers the immediate request while contradicting the structure it was grafted onto. The bolted-on ones pass every check and destroy the system anyway, one at a time, until the original structure is still legible but no longer does any work.

This means the quality words used in review — simple, well-structured, clean — are not properties of the text being reviewed. They are comparisons between the text and the other texts that could have produced the same behavior, and those alternatives exist only in the head of someone who understands what the system is for. A reviewer without that understanding can check the change against the rules and still be unable to see the damage, which is why decay accumulates fastest in systems that are heavily reviewed by people who did not build them and are inherited by people who have only the text.

Deciding correctly turns on recognizing whether the new demand is genuinely like something the system already handles. That resemblance is between situations in the world, not between code shapes, and it resists reduction to criteria the way resemblances between faces or between melodies do — you can act on it reliably and still be unable to write down the test. So the practical form of this lesson is a staffing and sequencing rule rather than a checklist: put the change in front of someone who can say what the system takes its problem to be, get the resemblance judged before the diff is written, and be suspicious of any process that can only evaluate the change after it exists.

**Source:** [Programming as Theory Building](../works/programming-as-theory-building.md) — the analysis of program modification, covering the many equally correct realizations of a change, the dependence of the judgment on perceived similarity between world situations, the irreducibility of that similarity to criteria, and the argument that simplicity and good structure are meaningful only relative to the alternatives the programmer can conceive.
