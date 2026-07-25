---
type: lesson
title: "When a proof gets hard, suspect your design before you suspect the prover"
figure: abrial
works: [formal-methods-in-industry-achievements-problems-future, faultless-systems-yes-we-can]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# When a proof gets hard, suspect your design before you suspect the prover

**Lesson:** A failed proof attempt has several possible readings, and the instinct to blame the tool picks the least informative one. The statement might be false, which tells you the design is wrong. The statement might be true but unreachable from what the model currently says, which tells you the model is missing content and needs enriching. Or the automatic machinery might simply be too weak, which is the only reading that is about the tool, and in practice the rarest. Two of the three readings are diagnoses of your own work, delivered for free, at a stage where acting on them is cheap.

The stronger version of this is quantitative and was apparently a surprise to the people who found it. The fraction of obligations a prover discharges without human help behaves as a measurement of structural quality. When that fraction sags, the model has usually been organized badly, and reorganizing it — fewer entangled variables, invariants that are local to the component they constrain, refinement steps small enough that each one owes only a modest argument — pushes automation back up without weakening any claim. Two comparable industrial developments illustrate the spread: the second, built with more experience and better structure, needed roughly a third as much interactive proof per unit of generated code as the first, and cost less human time in absolute terms despite being nearly twice the size. Difficulty of proof is thus a metric you can watch during development, in the way a compiler's complaints or a profiler's output can be watched, rather than a verdict delivered at the end.

This is the practical reason proof activity earns its keep even when nothing turns out to be broken. Modeling and proving are not goals in themselves; they are an instrument for interrogating a design while it is still soft. A programmer who internalizes it treats every laborious argument as a smell — not "this needs a better prover" but "this needs a simpler thing to prove things about" — and treats a target automation rate as a design constraint on par with any other budget. The corollary is that the structures which survive this pressure tend to be the ones with fewer, cleaner primitives, because those are the ones a mechanical argument can chew through unattended.

**Source:** [Formal Methods in Industry: Achievements, Problems, Future](../works/formal-methods-in-industry-achievements-problems-future.md) — the enumeration of what a prover's failure can mean, the finding that prover difficulty indicated poor model structure, and the comparative proof statistics from the two rail developments. Also [Faultless Systems: Yes We Can!](../works/faultless-systems-yes-we-can.md) — the section on proofs, which sets a target proportion of automatically discharged obligations and argues that simplifying a model raises it.
