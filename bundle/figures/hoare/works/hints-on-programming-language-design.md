---
type: work
title: "Hints on Programming Language Design"
figure: hoare
description: A keynote address distilling practical design advice from Hoare's experience building and standardizing languages, framed around the claim that a language's main job is to help programmers with design, documentation, and debugging rather than to please compiler writers or theoreticians. Argues for orthogonality, minimality, and readability as design virtues, and warns against accumulating features because they seem individually useful. A direct precursor to the harder-edged argument he'd make seven years later in "The Emperor's Old Clothes."
subdomains: [programming-languages-and-semantics]
year: 1973
url: https://rebelsky.cs.grinnell.edu/Courses/CS302/2007S/Readings/hoare-design.pdf
survey_pages: 5
survey_text_layer: full
extraction: complete
survey_fetch_mb: 0
access: public
host: third-party-rehost
tags: [work]
---

# Hints on Programming Language Design

**Venue/year:** Keynote address, ACM SIGACT/SIGPLAN Symposium on Principles of Programming Languages, Boston, October 1973. Published as Stanford Artificial Intelligence Laboratory Memo AIM-224 / Stanford CS Report STAN-CS-73-403.
**Source:** https://rebelsky.cs.grinnell.edu/Courses/CS302/2007S/Readings/hoare-design.pdf — course-reading mirror hosted by Grinnell College (CS302, Spring 2007); PDF metadata confirms title "CS302 2007S : C.A.R. Hoare - Hints on Programming Language Design". The Defense Technical Information Center's official archive copy (apps.dtic.mil/sti/pdfs/AD0773391.pdf) is the institutional original but returned 403 Forbidden to automated fetches during this check.

## Lessons
- [Judge a tool by which of the hard parts it removes, not by the list of things it can express](../lessons/judge-a-tool-by-which-hard-part-it-removes.md)
- [Simplicity has counterfeits: modularity and orthogonality are means, and adopting either as the goal produces complexity](../lessons/simplicity-has-counterfeits.md)
- [The checks you ship are the only checks you have, and every failure must be explicable in the user's own vocabulary](../lessons/the-checks-you-ship-are-the-only-checks-you-have.md)
- [When the workaround for a slow tool starts dictating how you decompose the program, the tool is the bug](../lessons/when-a-workaround-reshapes-the-program-fix-the-tool.md)
- [Don't pre-spend your users' efficiency budget, and make any optimization visible in their own terms](../lessons/dont-pre-spend-your-users-efficiency-budget.md)
- [Nested expressions are the model of good structure, and their narrow interface is the source of both their power and their limits](../lessons/why-nested-expressions-are-the-model-of-structure.md)
- [The interface between two consecutive steps is the whole machine until you deliberately narrow it](../lessons/the-interface-between-consecutive-steps.md)
- [The machine's tolerance is exactly why you must declare your meaning above it](../lessons/the-machines-tolerance-is-why-you-need-declarations.md)
- [Inventing a feature and assembling a system are different jobs, and assembly is consolidation, not invention](../lessons/inventing-a-feature-and-assembling-a-system-are-different-jobs.md)
