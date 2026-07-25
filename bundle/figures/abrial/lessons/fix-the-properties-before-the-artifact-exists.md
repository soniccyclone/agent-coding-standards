---
type: lesson
title: "Properties chosen before the artifact exists are evidence; properties chosen afterward are opinion"
figure: abrial
works: [formal-methods-in-industry-achievements-problems-future, faultless-systems-yes-we-can]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Properties chosen before the artifact exists are evidence; properties chosen afterward are opinion

**Lesson:** Testing has a step that nobody counts as part of it: somebody has to decide which property is worth checking and what the right answer is. That decision is made after the program exists, by a person who has usually read the program, and the expected answer frequently originates in that person's head rather than in any independent statement of intent. Every downstream number inherits the fallibility of that step. A passing test therefore licenses one modest conclusion — the program passed this test — and a failing test is genuinely ambiguous, because the expectation may have been the thing that was wrong. Neither outcome bears on the properties nobody thought to name.

Proof against a model has no such step, and this is the structural reason to prefer it rather than a matter of rigor for its own sake. The properties are not selected to be checked; they constitute the model. An invariant is written down because it is what the system is *for*, before there is any code to be influenced by, and the obligations to be discharged are then generated mechanically from the model's own structure rather than chosen by whoever is doing the checking. This matters more than it sounds: having a tool derive the statements to be proved removes the possibility of quietly proving the convenient subset, which is otherwise the easiest error in the world to make and the hardest to detect, since you would only be relocating the complexity from one place to another.

What changes for a practitioner is where scepticism gets pointed. Coverage of an artifact stops being the interesting question, and the interesting question becomes whether the set of stated properties is the right set — an argument about intent, conducted with the people who own the requirements, at a stage when the answer is cheap to change. In the rail systems developed this way the module-level tests were abandoned outright, at the operator's suggestion, on the grounds that the proofs were the stronger instrument; the testing budget was redirected upward to check the requirements themselves. That is the honest allocation: spend the sampling effort where sampling is the only tool available, not where a decision procedure exists.

**Source:** [Formal Methods in Industry: Achievements, Problems, Future](../works/formal-methods-in-industry-achievements-problems-future.md) — the side-by-side anatomy of a prepared test versus a proof on a model, which turns on the observation that a program's properties are chosen after the fact while a model's properties are constitutive of it. Also [Faultless Systems: Yes We Can!](../works/faultless-systems-yes-we-can.md) — its account of writing the properties down before development begins, and its criticism of retrofitting properties onto finished code.
