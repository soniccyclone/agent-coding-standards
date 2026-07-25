---
type: lesson
title: "Define a hard task by the cheap test that recognizes a good answer, because the whole difficulty lives between recognizing and producing"
figure: cook
works: [the-p-versus-np-problem, the-relative-efficiency-of-propositional-proof-systems]
axes: [verifiability, expressiveness]
subdomains: [algorithms-and-complexity, foundations-of-computation, formal-methods-and-verification]
tags: [lesson]
---
# Define a hard task by the cheap test that recognizes a good answer, because the whole difficulty lives between recognizing and producing

**Lesson:** The most useful characterization of an enormous class of hard problems mentions no machine and no search at all. It says: there is a short thing that, if you had it, would settle the question, and a cheap test that tells you whether a candidate short thing is that thing. The exotic-looking machinery of guessing is dispensable; what remains is a relation between a question and its evidence, checkable within a modest budget. This reframing is not cosmetic. It says the hardness of the task is precisely the distance between having a good answer and finding one, because the checking half is stipulated to be easy. Every problem in the class has an easy half, and the shape of the difficulty is the same everywhere: search over a space of candidates you can grade individually.

The corollary is that a cheap recognizer is the most valuable artifact you can own about a problem. It fixes what counts as success without committing to how success is reached, it bounds the problem's difficulty from above, and it converts progress on the hard half into something you can measure. Where a cheap recognizer does not exist, you do not merely lack an algorithm — you lack a specification, and any effort spent searching is unanchored. This reverses the usual instinct to design the generator first and evaluate later. Write the grader first; it is both the definition of the goal and, when the search eventually works, the thing that makes its output trustworthy.

The stakes of the gap are visible in what would follow from closing it. If finding were as cheap as checking, then every activity whose products can be graded quickly would become mechanical: theorems with short formal derivations, engineering designs that pass a fast acceptance test, artifacts judged by a computable criterion. The question would shift entirely onto whether a fast recognizer for a good result can be written at all, which relocates the creative work rather than eliminating it. That relocation is the practical version of the lesson even in a world where finding stays expensive: the leverage in any hard generative task is concentrated in the quality and cost of its acceptance test.

The same duality explains why some questions feel harder than their mirror images. Having a certificate that something holds is not the same capability as having a certificate that it fails, and a task where positive instances carry short evidence but negative ones do not is structurally different from one where both do. Noticing which side of a question carries the cheap evidence is often the first real information you get about it.

**Source:** [The P versus NP Problem](../works/the-p-versus-np-problem.md) — the definition of the class by way of a polynomial-time checking relation and a length-bounded witness, plus the discussion of certificates, the reduction of search to decision, and the passage weighing what collapse of the gap would mean for proof, design, and other generative work. Also [The Relative Efficiency of Propositional Proof Systems](../works/the-relative-efficiency-of-propositional-proof-systems.md) — the introductory argument, which turns the same duality into a statement about which side of the tautology question carries short evidence.
