---
type: lesson
title: "Confidence in a large system's correctness is an empirical result, and that follows from the theory"
figure: chaitin
works: [meta-math-the-quest-for-omega]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Confidence in a large system's correctness is an empirical result, and that follows from the theory

**Lesson:** Chaitin, who spent a career proving things about programs, holds that establishing the correctness of real software by proof is hopeless, and his own conservation law is the reason. Establishing a property requires assumptions carrying at least as much content as the property; a specification small enough for a person to hold cannot determine a system whose behaviour carries far more content than the specification. So knowledge about a large system's behaviour comes from watching it behave. He describes running a new system alongside the old one until people believe it, and above all continuous self-application: compiling the compiler with itself, using the thing you are building all day, so that feedback about design and performance arrives immediately rather than at review time.

He pairs that with a claim about how the design should be reached. A top-down plan settled before any code exists cannot work, because the understanding needed to write the plan is produced by writing the code. The design is discovered incrementally, which is precisely the empirical attitude applied to structure rather than to behaviour.

What keeps this from collapsing into "just wing it" is the other half of his practice, which is aggressively reducing the amount of content in the artifact. He refused ad hoc code and drove everything back onto clean systematic algorithms in order to keep the system intellectually manageable. The two halves are one strategy: shrink the information content until experiments have a chance of covering it, then cover it by continuous use. Neither half works alone, since a small system nobody exercises is unverified and a large system under heavy use is still mostly unexplored.

**Source:** [Meta Math! The Quest for Omega](../works/meta-math-the-quest-for-omega.md) - the concluding chapter, which states the position on formal methods for real software, describes the practice of continuously running and recompiling his own tools, rejects the top-down design plan, and insists at the same time on clean algorithms and conceptual integrity to keep the artifact tractable.
