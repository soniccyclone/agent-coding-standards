---
type: lesson
title: "Turn the reasoning itself into an inspectable object, and questions about the system become questions about data"
figure: hilbert
works: [uber-das-unendliche]
axes: [verifiability, expressiveness]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Turn the reasoning itself into an inspectable object, and questions about the system become questions about data

**Lesson:** The move that makes Hilbert's whole program possible is a change in what is being studied. Ordinary mathematics reasons about numbers; he proposes to reason about mathematics, and to do that he first has to make mathematics into something reasonable-about. So the symbols are stripped of meaning: formulas are no longer communications about numerals but self-standing configurations, axioms are just distinguished formulas, and a step of inference becomes a rule for placing one formula after others. A proof, on this reading, is a figure — a concrete arrangement of marks, finite, communicable from beginning to end, and fully surveyable. He notes the precedent inside elementary mathematics: algebra already made this move when it stopped treating letter expressions as shorthand for statements about numbers and started treating the expressions themselves as the objects.

The payoff is immediate and structural. Once proofs are finite concrete objects, a global claim about the system becomes a claim about those objects, of exactly the same character as claims one already knows how to settle. Consistency, which sounds like a statement about all possible reasoning forever, reduces to the assertion that a particular formula never appears as the last line of any derivation — a claim that no object of a certain describable shape exists, structurally the same kind of claim as the classical argument that no pair of numerals stands in a certain ratio. He gives this second-level study its own name and treats it as a distinct discipline with its own standards: it must be carried out by finite, concrete means, the same means trusted at the ground level.

For a programmer this is the reflex behind every tool that treats programs as data. When you want to know something about a system's behavior in general rather than on the run you just observed, the productive step is to stop reasoning informally about behavior and instead make the artifact — the syntax tree, the type derivation, the schedule, the execution trace, the query plan — an explicit finite structure your analysis can walk. Global questions then become checks over that structure, and the analysis can be held to the same standard of rigor you would demand of ordinary code. Two cautions come with it. The representation must be genuinely surveyable, or you have moved the vagueness rather than removed it. And the metalevel needs its own trusted foundation: an analyzer whose correctness rests on the very assumptions it is checking has proved nothing.

**Source:** [Über das Unendliche](../works/uber-das-unendliche.md) — the passage moving from meaningful communication to formulas as objects, the formalization of proof as a surveyable figure built by an explicit inference schema, and the reduction of the consistency question to the non-existence of a derivation with a specified last line.
