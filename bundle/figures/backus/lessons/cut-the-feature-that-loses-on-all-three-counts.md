---
type: lesson
title: "Cut the feature that is hard to specify, awkward to implement, and barely more powerful than its simpler form"
figure: backus
works: [the-history-of-fortran-i-ii-and-iii]
axes: [primitive-count, cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics]
tags: [lesson]
---
# Cut the feature that is hard to specify, awkward to implement, and barely more powerful than its simpler form

**Lesson:** A design retreat during construction gives a usable triage rule. The original loop construct could name both endpoints of the region it governed and a third destination to continue at, and it was replaced with something much plainer. The reason was three-fold and the parts were assessed together: it was hard to describe precisely, it was awkward to compile, and it added little power over the simple version. Any one of those alone is an argument to be weighed against the feature's value. All three at once is not a trade-off, it is a mistake with a cost attached, and the honest move is deletion. The rule is worth stating because designers habitually evaluate only the third question, treat specification difficulty as the specifier's problem and implementation difficulty as the implementer's, and thereby keep features that no one can describe, nobody enjoys building, and few people needed.

The same project supplies two companion criteria that also refuse pure elegance as the standard. Blanks were made insignificant partly on evidence about human failure: keypunch operators miscounted spaces in handwritten input, producing errors, so the design removed the category of error rather than asking people to be more careful — and the same choice let authors lay out programs readably without changing meaning or inventing formatting rules. Mixed-mode arithmetic was excluded although the earlier specification had allowed it, on the reasoning that if the system was going to insert conversion code then the author should have to say so, because the reliable way to ensure someone knows a conversion is happening is to make them write it. Field evidence about the errors people actually make, and the author's need to see what the machine will do, are both legitimate grounds for restricting a language.

A designer who works this way keeps three questions live for every proposed feature and one for every feature already present: can this be described precisely, is it awkward to implement, and how much can it do that the simpler form cannot. When the answers converge, the feature goes, and the retreat almost never costs what its defenders predicted. Of the features cut in this history, only one was felt as a real sacrifice, and that one was the one that would have been genuinely difficult to implement.

**Source:** [The History of FORTRAN I, II, and III](../works/the-history-of-fortran-i-ii-and-iii.md) — the comparison of the preliminary specification against the shipped manual, including the stated three-part reasoning behind simplifying the loop construct, the rationale for ignoring blanks, the exclusion of mixed-mode expressions, and the assessment of which cuts were actually felt as losses.
