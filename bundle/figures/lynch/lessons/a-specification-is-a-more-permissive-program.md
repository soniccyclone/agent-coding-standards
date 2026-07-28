---
type: lesson
title: "Make a specification the same kind of object as an implementation, so correctness is just containment"
figure: lynch
works: [an-introduction-to-input-output-automata]
axes: [verifiability, expressiveness, primitive-count]
subdomains: [formal-methods-and-verification, distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---
# Make a specification the same kind of object as an implementation, so correctness is just containment

**Lesson:** The economical move at the heart of this model is that a problem statement and a program are not different species. A problem is an interface plus a set of externally observable action sequences that are acceptable. A component's meaning is also an interface plus the set of externally observable sequences it can produce. Correctness is then set containment: everything the component can be observed doing is something the problem statement permits. There is no separate specification language, no translation step, and no question of whether the spec and the code mean the same kind of thing.

Two consequences follow that are worth more than the definition itself. First, the correctness relation composes without any new machinery. If a detailed design's observable behavior is contained in a coarser design's, and the coarser one's is contained in the problem's, containment chains and the detailed design is correct. Refinement stops being a special methodology and becomes transitivity, which is why a proof can be staged through several levels of abstraction without changing the notion of correctness at each level. Second, "the spec" is just the most permissive program with the right interface — which means you can hand it to someone as a reference implementation, compare two specs, or compose specs together with the very same operator you compose components with.

The other half of the idea is that nondeterminism is not a defect to be minimized in the description. Leaving a design as unconstrained as you can get away with makes every result about it apply automatically to all the tighter designs obtained by resolving the choices. Under-specifying deliberately is therefore a way of proving more with less work, and of keeping incidental decisions out of the argument entirely. A programmer whose instinct is to pin down every ordering and every tie-break has, without meaning to, made every proof and every test specific to those choices.

There is also a payoff at the level of proof effort. Because both sides are state machines, containment of observable behavior can be established by exhibiting a correspondence between the states of the two machines and checking a local obligation once per transition, rather than arguing about whole executions. A global claim about all possible runs gets discharged by a finite, mechanical, per-step check — which is what makes proofs of substantial concurrent algorithms finishable at all.

**Source:** [An Introduction to Input/Output Automata](../works/an-introduction-to-input-output-automata.md) — the problem-specification section, where a problem is defined as a signature plus a set of action sequences and "solves" is defined as behavior-set inclusion, together with the following section's state-correspondence proof technique.
