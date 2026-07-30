---
type: lesson
title: "Give every component a written statement of the interference it may assume and the interference it may inflict"
figure: jones
works: [tentative-steps-toward-a-development-method-for-interfering-programs]
axes: [verifiability, parallelizability, cognitive-load]
subdomains: [formal-methods-and-verification, distributed-systems-and-concurrency]
tags: [lesson]
---
# Give every component a written statement of the interference it may assume and the interference it may inflict

**Lesson:** Sequential specification already has a working pair of obligations facing in opposite directions: a condition the implementer is granted for free and may lean on, and a condition the implementer owes the caller. What makes that pair work is that both talk only about externally visible state, so a component can be built and judged with no knowledge of its context beyond the two conditions. Concurrency does not need a different idea, it needs the same idea applied to change over time. Add a second granted condition describing how the surrounding world is permitted to disturb shared state while this component runs, and a second owed condition describing the disturbance this component promises not to exceed. Four conditions, two granted and two owed, and the whole apparatus of independent development survives contact with shared mutable state.

The symmetry pays off immediately in the substitution rule. Because a granted condition is something you may depend on and an owed condition is something you must deliver, a component that assumes less about its environment or promises more restraint than its specification demands is always usable in place of the specified one. Interference tolerance and interference restraint become dimensions along which components are comparable, which is what lets you swap implementations without reopening the argument about whether the assembly still works. It also fixes what the defaults have to be: a component with nothing written down is assuming the strongest possible thing (nobody touches anything) and promising the weakest possible thing (it may touch anything), which is precisely the reading that makes every sequential specification a special case rather than a different species.

Two constraints on the interference conditions themselves are worth internalizing, because they follow from what these conditions are for rather than from any formalism. They must be relations between two states rather than properties of one, since interference is by nature a change and there is nothing to say about a single snapshot. And they must survive composition with themselves: a component that is descheduled for an unknown length of time will resume facing the accumulated effect of an unknown number of environmental steps, so an assumption that does not close under repetition is worthless the moment the component stops being the only thing running.

**Source:** [Tentative Steps Toward a Development Method for Interfering Programs](../works/tentative-steps-toward-a-development-method-for-interfering-programs.md) — the section introducing rely- and guarantee-conditions, its explicit analogy between the rely/precondition pair and the guarantee/postcondition pair, the weaker-rely/stronger-guarantee substitutability remark, the stated defaults for an unannotated specification, and the reflexivity/transitivity requirement.
