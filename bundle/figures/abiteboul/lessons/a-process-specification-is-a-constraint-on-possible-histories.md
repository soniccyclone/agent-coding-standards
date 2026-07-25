---
type: lesson
title: "A process specification is a constraint on possible histories, whatever paradigm it arrives in"
figure: abiteboul
works: [comparing-workflow-specification-languages]
axes: [expressiveness, verifiability]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification, distributed-systems-and-concurrency]
tags: [lesson]
---
# A process specification is a constraint on possible histories, whatever paradigm it arrives in

**Lesson:** Process definition arrives in mutually unintelligible dialects. One team draws a state machine with transitions permitted only when a condition holds. Another attaches preconditions and postconditions to tasks and lets the system choose what to run. A third writes formulas over what has already happened and requires the next step to be consistent with them. These look like different kinds of artifact and get argued about as competing philosophies. This work strips the difference away by observing that a system evolves in response to its own computation and to the outside world, that the space of things it could do is a branching set of possible histories, and that every one of these paradigms does exactly one thing: rule some of those histories out. The dialects differ in how they name the histories they forbid, not in what kind of statement they are making.

Taking that seriously reorganizes several things. It supplies a common object for reasoning, since if a specification is a restriction on a tree of runs then any two specifications can be set against each other by asking about the sets of runs they permit. It relocates a lot of behavior that people do not think of as process definition at all: a rule that a document may only be in certain shapes, checked whenever the state changes, forbids histories just as surely as an explicit transition table, and this work's central technical result is that such state-shape rules alone are strong enough to reproduce all three explicit paradigms. It also explains why refinement works as a design method, because if the object is a set of permitted histories then designing by starting with a coarse abstraction and progressively constraining it is a well-defined operation rather than a metaphor.

For a working engineer the payoff is a single question that cuts through the paradigm argument: which sequences of events does this artifact forbid? Ask it of a state machine, of a set of guards, of a temporal assertion, of a validation rule, and of the database constraint that quietly rejects certain updates, and the answers are commensurable. The related discipline is to enumerate the constraints on behavior that live in each of those places rather than only in the one your team calls the workflow, since the effective specification of a system is the union of everything that can refuse a step, and the parts of it nobody has written down are the parts that will surprise you.

**Source:** [Comparing Workflow Specification Languages](../works/comparing-workflow-specification-languages.md) — the introduction's framing of a specification as a constraint on the evolution of a system, the abstract model of a workflow as the branching tree of possible runs, and the closing observation that seeing a workflow this way, separated from any particular mechanism for stating the constraint, is what made the comparison possible.
