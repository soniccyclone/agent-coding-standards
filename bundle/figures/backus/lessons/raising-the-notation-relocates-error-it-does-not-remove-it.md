---
type: lesson
title: "Raising the level of notation relocates error rather than removing it, so make the new level's errors mechanically visible"
figure: backus
works: [the-fortran-automatic-coding-system, the-history-of-fortran-i-ii-and-iii]
axes: [verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Raising the level of notation relocates error rather than removing it, so make the new level's errors mechanically visible

**Lesson:** A better notation changes the population of mistakes available to make. Whole categories vanish — mis-assigned storage, botched address arithmetic, the bookkeeping that consumed most of a hand coder's attention — and new categories take their place at the level where the author now works. Two things follow that are easy to miss while celebrating the first half. Only the program in the new notation has to be correct, which means the tool's own defects are a separate class of problem, handled by separate procedures, and must be kept out of the author's debugging loop; a user chasing a bug should never be forced to consider whether the compiler broke. And a constrained notation lets the tool detect a large fraction of the remaining mistakes on the author's behalf, which is a design property of the notation, not a bonus feature of the tool.

The instructive part of the history is the miscalculation. The team predicted their system would nearly eliminate debugging, wrote that down, and shipped weak checking as a consequence of believing it. Reality: most errors were caught during translation, several diagnostics were sharp enough to identify a missing punctuation mark in a specific statement, and the rest still required real work at the level of the source. The checking facilities had to be strengthened soon after release, and the second version's stated priorities began with better diagnostics and clearer explanations of what was wrong. The optimism was not idle — it directly caused the under-investment.

The generalizable practice is twofold. Treat diagnostics as part of the deliverable from the beginning, sized by the assumption that people will make errors in your notation at roughly the rate they made them in the last one. And judge a notation partly by what fraction of plausible mistakes it renders mechanically detectable rather than merely by what it lets you say concisely — a construct whose misuse is indistinguishable from its correct use is expensive no matter how expressive it is.

**Source:** [The FORTRAN Automatic Coding System](../works/the-fortran-automatic-coding-system.md) — the debugging discussion, which argues that the notation's structure lets many errors be detected during translation and insists that faults in the translator be corrected by procedures distinct from debugging a user's program. Also [The History of FORTRAN I, II, and III](../works/the-history-of-fortran-i-ii-and-iii.md) — the admission of having been hopelessly optimistic about debugging, the resulting weakness of the first release's checking, and the second version's stated priority on better diagnostics.
