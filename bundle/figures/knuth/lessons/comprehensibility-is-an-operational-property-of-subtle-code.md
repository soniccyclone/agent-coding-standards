---
type: lesson
title: "Comprehensibility is an operational property: code your colleagues cannot reconstruct gets repaired into rubble"
figure: knuth
works: [fast-pattern-matching-in-strings]
axes: [cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Comprehensibility is an operational property: code your colleagues cannot reconstruct gets repaired into rubble

**Lesson:** Buried in the historical section is a short account of what happened to the first working implementation. Morris wrote the routine into a text editor, it was correct, and his colleagues on the project could not follow it. Months later he found that other people had applied unnecessary corrections to it and destroyed it. Nothing failed — no bug, no incident, no requirement change. The mechanism of destruction was maintenance by people acting in good faith on code whose reasoning they could not reconstruct, which is a category of failure that testing does not catch and code review as usually practised does not prevent, because the reviewers are the same people who cannot follow it.

The general form is that comprehensibility behaves like uptime rather than like style. A routine nobody but its author can reason about has a decay rate, and the decay is driven by ordinary well-intentioned activity: someone reads it, sees something that looks wrong or looks like it could be simplified, and changes it. The subtler the invariant, the more likely it is that a reasonable-looking local edit violates it while leaving the tests green, because the tests were written against the behaviour the author was thinking about. This means that when an algorithm's correctness rests on a non-obvious invariant, writing the invariant down where the maintainer will hit it is not documentation politeness — it is the only thing standing between the code and its eventual dismantling.

The same section furnishes a second observation about human judgment applied to subtle code, and it cuts in the opposite direction. Knuth notes people's persistent expectation that this algorithm will run *slower* than the naive one, despite it plainly doing less work, and diagnoses the cause: because the method is conceptually hard for a person to grasp, people half-expect the machine to have trouble with it too, as though subtle instructions were harder to execute. That is a real and specific bias worth naming, because it is the reason clever-looking code gets rejected on performance grounds without measurement, and it is the mirror image of the maintenance problem. In one direction, difficulty of understanding gets mistaken for machine cost; in the other, it gets ignored as a mere aesthetic concern when it is in fact predicting the code's destruction.

The practical stance that falls out is asymmetric and slightly uncomfortable. Machine cost is not something to reason about from how the code feels — measure it, always, because your intuition about it is systematically biased by your own comprehension. Human cost, conversely, *is* something to reason about from how the code feels, and it should be treated as a real operational risk with a real mitigation: state the invariant, keep the readable version, and expect that anything you leave unexplained will be helpfully corrected.

**Source:** [Fast Pattern Matching in Strings](../works/fast-pattern-matching-in-strings.md) — the historical remarks on the original text-editor implementation being ruined by other implementors' unnecessary fixes, together with the observation at the end of the efficiency section that readers expect the conceptually harder algorithm to run more slowly.
