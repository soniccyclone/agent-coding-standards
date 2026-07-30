---
type: lesson
title: "Hold the bespoke one percent to different standards than the library it sits on"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Hold the bespoke one percent to different standards than the library it sits on

**Lesson:** In a delivery model where nearly everything shipped comes from an existing library and only the customer-specific remainder is written fresh, that remainder was measured at somewhere between zero and one percent of the delivered system. The conclusion drawn from the measurement is the interesting part: the person writing that fraction should optimize for functionality and robustness, may trade away generality and elegance, and can usually disregard efficiency altogether. Exploratory programming is called ideal for the job.

The argument is arithmetic rather than permissive. Generality has value proportional to how many future uses will exercise it, and code written for one customer at one percent of a system has approximately one future use, so effort spent making it general is spent on a return that does not exist. Efficiency has value proportional to the share of execution it accounts for, and the reused ninety-nine percent is where that share lives. Robustness, by contrast, does not scale down with the code's size — a defect in the one percent fails the whole delivery just as thoroughly as a defect in the library. So the standards that should apply are exactly the ones whose payoff is independent of how much code there is, and the ones that should be relaxed are those whose payoff scales with reuse or with execution share.

What makes this worth holding as a rule is that uniform standards across a codebase feel like integrity and quietly misallocate the effort available. Requiring the bespoke layer to meet library standards taxes every delivery for benefits nobody will collect, and — worse — it consumes the review attention that should have gone to the library, where generality and performance genuinely compound across every customer. The inverse error is the more common one in practice: treating the library as though it were application code, where a shortcut multiplies across every system built on it.

The generalizable move is to stop asking whether code is good and start asking how many times it will be read, run, and depended upon, then let the standard follow from the answer. The corollary is that this only works if the boundary is real and visible — someone must be able to say which side of the line a given file is on, and code that starts as bespoke and drifts into becoming load-bearing needs to be promoted deliberately, with its standards raised at that moment, rather than by silent accretion.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 10 section 10.3's account of production work, which reports that because sales target related markets, special programs are a very small part of the delivered system, typically zero to one percent, and that the Module-Maker can therefore focus on functionality and robustness at the expense of generality and elegance while frequently ignoring efficiency, with exploratory programming ideal for the work.
