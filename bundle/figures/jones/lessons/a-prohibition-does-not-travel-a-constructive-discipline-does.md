---
type: lesson
title: "A prohibition does not travel; a discipline that tells you what to do next does"
figure: jones
works: [software-development-a-rigorous-approach]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# A prohibition does not travel; a discipline that tells you what to do next does

**Lesson:** Two ideas of comparable soundness were pushed at working programmers in the same decade. One said: solve a large problem by breaking it into smaller ones and record the hierarchy as you go. The other said: do not use this control construct. The first was absorbed almost without argument. The second met resistance out of all proportion to how contentious it actually was, and burned years in a debate that produced nothing. The difference is not that one was better founded. It is that the first tells you what to do when you sit down in front of the problem, and the second only tells you what to feel bad about once you have already written something.

That asymmetry is worth treating as a design criterion for any rule you intend other people to follow. A rule phrased as a test applies at the end, when the cost of failing it is rework, and it supplies no help with the part that was actually hard. A rule phrased as a discipline applies at the start, when it is cheap, and its output is the next thing to work on. The practical consequence for how you introduce any standard — a review checklist, a lint rule, an architectural constraint — is to ask whether it can be restated as a procedure with an artifact at the end of it. If it can, restate it. If it genuinely cannot, expect it to be resented and largely ignored, and consider whether the underlying concern would be better served by changing what the constructive path produces than by policing what people do off it.

There is a second thing a constructive discipline buys that a test cannot: a positive criterion for being finished with a stage. Without one, "done" is a matter of nobody having objected yet, so the temptation is to keep moving and let integration decide. With one, each stage terminates in something checkable against what was asked for, which is what makes it safe for the next stage to depend on it. The rule that only rejects has no way to say you have arrived; it can only ever say you have not yet been caught.

**Source:** [Software Development: A Rigorous Approach](../works/software-development-a-rigorous-approach.md) — the background section's comparison of the reception of top-down development against the reception of the argument for avoiding GOTO, identifying the key difference as constructive proposal versus negative one, and drawing from it the requirement that a useful new method must offer a constructive discipline rather than a simple test of created programs; together with the claim in the following section that moving from proofs of finished programs to correctness arguments made during development is what at last supplies positive criteria for the successful completion of a design stage.
