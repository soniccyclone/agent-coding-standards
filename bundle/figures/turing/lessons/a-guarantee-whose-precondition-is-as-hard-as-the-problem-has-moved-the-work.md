---
type: lesson
title: "A guarantee whose precondition is as hard as the original problem has relocated the work, not removed it"
figure: turing
works: [systems-of-logic-based-on-ordinals]
axes: [verifiability, cognitive-load]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# A guarantee whose precondition is as hard as the original problem has relocated the work, not removed it

**Lesson:** Any sufficiently flexible framework can be made to satisfy an impressive-sounding property by pushing the difficulty into one of its inputs. Build a system that solves everything provided it is handed the right configuration, and then observe that determining which configuration is right is exactly as hard as the problem you started with. The theorem is true; the system is worthless. This failure is nearly invisible from inside the formalism, because the formalism does not measure the difficulty of its own preconditions — it just assumes them satisfied and proceeds. So the property has to be audited from outside, by asking whether the residual obligation on whoever supplies the input is any easier to discharge than the original task.

The honest version of this discipline treats the residual obligation as the real object of design. It is legitimate for a system to leave steps that cannot be mechanized; what is not legitimate is leaving them unmeasured. A good design makes those steps few, uniform in kind, obviously identifiable as non-mechanical when they occur, and small enough that a person can actually be confident in them — and it guarantees that if those steps are right, everything built on them is right. A bad design satisfies the same formal statement while making the manual step an act of clairvoyance. Both meet the specification. Only one is usable, and the difference is not visible in the specification, which is precisely why the specification is not the last word.

Programmers meet this constantly and mostly fail to name it. A type system that will prove anything given the right annotation, a verifier that needs a loop invariant nobody can find, a solver that terminates given a good initial bound, a scheduler that is optimal given accurate cost estimates, a cache that is always correct given correct invalidation — each is a true guarantee resting on an obligation that may carry the entire original difficulty. The correct habit is to state the precondition explicitly and estimate its cost as seriously as the runtime cost, and to prefer the weaker guarantee with the tractable obligation over the stronger one whose obligation is a restatement of the problem.

**Source:** [Systems of Logic Based on Ordinals](../works/systems-of-logic-based-on-ordinals.md) — the completeness discussion, where a system meeting the completeness definition is constructed immediately and then dismissed by its own author as no help at all, alongside the later discussion of what properties a system with unavoidable non-mechanical steps must have to be worth using.
