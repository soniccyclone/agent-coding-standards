---
type: lesson
title: "Publish your system's scope as a testable predicate, with examples on both sides of the line"
figure: turing
works: [proposed-electronic-calculator-ace-report]
axes: [expressiveness, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Publish your system's scope as a testable predicate, with examples on both sides of the line

**Lesson:** "General purpose" is a claim nobody can act on. A far more useful statement of what a system does is a small set of quantified conditions a candidate problem must satisfy — how much working state it may need at once, how much total work it may cost relative to the machine's rate, how complex its procedure may be to describe — such that anyone holding a problem can check the conditions themselves without consulting you. The quantities matter more than the prose: a limit expressed as a number invites someone to measure their problem against it, while a limit expressed as an adjective invites argument.

Examples then do the work that the predicate cannot, and they must include the failures. Problems that fall outside for lack of a suitable input path, and problems that fall outside because the state simply will not fit, both teach more about the boundary than another success story does. The most instructive category is the third one: the problem the system can handle and should not, because its rate would be pinned by some slow external stage while the machine's actual strengths never engage, so a cheaper existing tool does the job just as well. Capability is not fitness. Whatever resource binds first is what decides, and a scope statement that ignores the binding resource will attract work the system is technically able to do and economically wrong for.

Adopting this changes how you document and how you say no. Instead of a feature list you write down the operating envelope with numbers in it, plus a handful of worked cases including rejections and including at least one "yes but use the other tool." That document is what lets other people route work correctly without you in the loop, and it is honest in a way capability claims never are — it tells a reader what happens as they approach the edge, which is precisely where they will be operating.

**Source:** [Proposed Electronic Calculator (Report on the ACE)](../works/proposed-electronic-calculator-ace-report.md) — the chapter on the machine's scope, which states three quantified admissibility conditions and then works through ten candidate problems, among them one excluded for want of an appropriate input and one the machine could do but which would be limited by card-reading speed and so belongs on ordinary punched-card equipment.
