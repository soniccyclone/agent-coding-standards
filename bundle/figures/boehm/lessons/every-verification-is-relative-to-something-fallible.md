---
type: lesson
title: "Every verification is relative to something that can also be wrong"
figure: boehm
works: [software-engineering-1976]
axes: [verifiability]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Every verification is relative to something that can also be wrong

**Lesson:** The familiar hierarchy puts testing at the bottom and proof at the top: testing samples behavior and can only exhibit defects, while proof reasons over all behaviors and establishes their absence. Boehm accepts the technical asymmetry and then closes the gap from an unexpected direction. A proof establishes agreement between two artifacts, a program and a specification. It says nothing about whether the specification describes the behavior the system actually needs, and nothing about whether the proof itself is sound, a failure mode with a documented history. So the confident slogan about testing shows only presence and never absence applies, with the same force, to proof. Neither technique escapes its frame of reference; each one relocates the trust rather than eliminating it.

The useful consequence is to stop treating verification as a binary the system either has or lacks, and instead ask what each technique buys and what it leaves uncovered. Boehm's framing makes the boundary concrete: a program is a mapping from an input space to an output space, and if that input space is genuinely finite you can settle correctness by exhausting it, which is why exhaustive enumeration over a finite portion is a legitimate formal argument rather than a poor substitute for one. Infinity is what forces the shift from sampling to inductive argument. Between the two extremes sit techniques that reason over symbolic inputs and thereby cover whole families of concrete ones at once, collapsing a large or infinite input space into a finite number of cases. Where that collapse is possible, it is the best available trade.

He also names the limits that will not yield to more machinery: computations over approximate numeric values whose error behavior resists analysis, and inputs whose properties are only roughly characterized because they come from the physical world. Those are not gaps waiting to be closed by a better tool. They are places where the formal frame simply does not reach, and knowing that is part of using the tools honestly.

A programmer who believes this asks "verified against what, and how do we know that thing is right" as a reflex, keeps effort on validating the specification rather than only the implementation, and hunts for the finite structure hiding inside an apparently infinite input space, because finding it converts an argument into a check.

**Source:** [Software Engineering](../works/software-engineering-1976.md) — the testing and reliability section, specifically its treatment of when exhaustive testing constitutes a sufficiency argument, its account of symbolic execution as the intermediate between testing and proof, and its inversion of the standard aphorism about what proof can demonstrate.
