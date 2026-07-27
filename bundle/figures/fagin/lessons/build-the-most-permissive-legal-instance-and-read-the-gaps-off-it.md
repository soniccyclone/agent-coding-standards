---
type: lesson
title: "Build the most permissive instance your spec allows, then read the missing rules off it"
figure: fagin
works: [horn-clauses-and-database-dependencies]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [formal-methods-and-verification, databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# Build the most permissive instance your spec allows, then read the missing rules off it

**Lesson:** The hardest failure mode in specification is not a wrong rule but an absent one, and absence is invisible by inspection: reading a list of constraints tells you nothing about the constraint you forgot to write down. Fagin's central object attacks this directly. It is a single structure that satisfies every consequence of the stated constraints and no other constraint of the kind under consideration, so it is simultaneously a counterexample to every rule the specification fails to entail. He draws a sharp line between a constraint that is decreed to hold in every state the system will ever reach and one that merely happens to hold in the state in front of you, and the object he constructs is precisely the one containing no accidents.

The consequence for design practice is a change of medium. A designer confronting a candidate rule has to reason about whether their existing rules already force it, which is a question about entailment in a formalism, and people are bad at it. Given the constructed instance instead, they only have to look. Fagin stages this for the reader: he presents a small example, invites inspection before reading on, and lets the reader be the one to notice that the same person manages two different groups, which is legal precisely because the rules as written never forbade it. The designer never had to consider that rule in the abstract or ask whether it followed from the others. They saw a state they would not accept and named the rule that excludes it.

This is a general technique for closing the gap between what someone means and what they wrote. Any specification defines a space of permitted behaviors, and the specification's defects live in the part of that space the author never pictured. Producing the extremal element of the space, the one that exercises every liberty the spec grants, converts an unbounded search for missing constraints into an act of recognition. Fagin notes the technique had been built into a design tool for exactly this purpose, and that it also travels: someone working on program testing used the same equivalence to guarantee test data carrying no unintended relationships among its values.

The engineering habit that follows is to generate adversarial-but-legal instances from your own rules rather than writing more rules from imagination. A schema, a type, a config format, an API contract, a permission model: each admits a maximally permissive witness, and building one and showing it to a domain expert surfaces omissions faster than any amount of re-reading. Fagin is also honest about the cost, noting the construction can be exponential in the size of the description and can in some settings only be built as an infinite object, which means the technique buys clarity with computation rather than for free.

**Source:** [Horn Clauses and Database Dependencies](../works/horn-clauses-and-database-dependencies.md) — the section on Armstrong relations, particularly the worked example the reader is asked to inspect for themselves, the distinction drawn there between decreed and accidental constraints, and the reported design-aid and program-testing applications.
