---
type: lesson
title: "Let the framework hold the global problem and ask each participant exactly one local question"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Let the framework hold the global problem and ask each participant exactly one local question

**Lesson:** Faced with a problem that is genuinely global — an operation over an arbitrary portion of an arbitrary reference graph, where the correct extent depends on meanings only the individual participants know — the team's move was not to solve it centrally or to distribute it evenly. They split it along a specific seam. The framework takes the structural and inter-participant work: traversing, accumulating, holding the correspondence between originals and results, sequencing the phases. What is left for each participant is a question answerable while looking at one type at a time and nothing else.

The seam is chosen by what a contributor can be expected to get right, which is a sharper criterion than the usual "separate generic from specific." The stated goal was to limit the application programmer's task to overriding particular methods where she need consider only one class at a time — and the reason that matters is what preceded it: their history was several rounds of solution followed by unpleasant surprise, each surprise caused by an interaction nobody had in view. Interactions are what people get wrong. So the partition is designed to leave no interaction in any contributor's hands, and the framework absorbs precisely the class of decision that had been generating the failures.

The mechanics reinforce it. The global operation runs in two passes rather than one, because a participant cannot decide what its references should become until it is known which other things were included — so the framework establishes that context first and only then asks each participant to resolve its own references against it. Doing it in one pass would push exactly the global knowledge back onto the participants that the design exists to spare them. The two-phase structure is not an implementation detail; it is what makes the local question answerable at all.

Equally instructive is that the split is reported as imperfect. One case in their taxonomy — where something outside the operation needs to learn about a result, though neither the original nor the result knows of it — falls outside what the framework covers, and the application programmer must handle it specially. Naming the uncovered case is what makes the framework trustworthy: a contributor knows the boundary of the protection rather than discovering it as a surprise. The generalizable form: for any problem too big to hold at once, look for the partition where every contributor's obligation is decidable from local information, give everything cross-cutting to the shared machinery, and enumerate what you failed to cover rather than implying full coverage.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 11 sections 11.4 and 11.4.3, where the goal is stated as a framework protecting programmers and users against nasty surprises stemming from unforeseen side effects, with framework programs taking the structural and interobject aspects while the application programmer handles individual objects one class at a time; the two-phase structureCopy algorithm (collect and shallow-copy into a dictionary of correspondences, then ask each copy to fix its references given that dictionary); the three reference cases enumerated; and the admission that the uncopied-to-copied case is not covered by the general framework and requires special action from the application programmer.
