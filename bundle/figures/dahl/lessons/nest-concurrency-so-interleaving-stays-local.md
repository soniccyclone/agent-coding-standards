---
type: lesson
title: "Make concurrency a nestable construct, so a subsystem's interleaving is invisible from outside it"
figure: dahl
works: [simula-67-common-base-language]
axes: [parallelizability, cognitive-load, verifiability]
subdomains: [distributed-systems-and-concurrency, programming-languages-and-semantics]
tags: [lesson]
---
# Make concurrency a nestable construct, so a subsystem's interleaving is invisible from outside it

**Lesson:** The default architecture for interleaved execution is one global scheduler and one flat population of runnable things. It is the obvious design and it does not compose: any component's suspension is a fact about the whole program, so reasoning about any part requires knowing every part, and two independently written subsystems cannot be combined without their internal interleavings interfering. The alternative is to make the concurrent grouping itself a construct with a boundary. A group has one entry point that owns control on the group's behalf, exactly one of its members holds that control at a time, and the group as a whole appears to its surroundings as a single ordinary component. A member of one group can be the entry point of another, so groups nest.

What the boundary buys is that suspension becomes local. When something inside a nested group gives up control, control goes to that group's own owner, not to the outermost scheduler; the enclosing world never observes that anything was interleaved at all. So a subsystem can use suspension internally as freely as it likes, and callers see a component that runs to completion. This is the same trade that block scope makes for names — locality bought by a boundary that the outside cannot see through — applied to control instead of naming, and it earns the same dividend: the correctness argument for a subsystem does not have to mention its context, and the argument for the context does not have to mention the subsystem's internals.

Getting this right requires taking the boundary seriously in the places where it would be tempting to cheat. Control transfers must be confined to the group they belong to, and a transfer that would jump out of a nested group has to be understood as leaving the whole group, not as an ordinary jump. Lifetime has to respect containment too: destroying a group destroys what it contains, which is what makes it safe to reason about the group as one object. The habit to take from this is to treat "who can suspend relative to whom" as a scoped, declared relationship rather than an ambient global property. A design where any component can be suspended by anything is a design where no component can be reasoned about alone.

**Source:** [SIMULA 67 Common Base Language](../works/simula-67-common-base-language.md) — the quasi-parallel sequencing section, which defines the concurrent grouping as a subtree rooted at a prefixed block instance, assigns each group its own outer control distinct from the components' local controls, builds the chain of currently-operating components across nesting levels, and constrains jumps and deletion to respect the resulting containment.
