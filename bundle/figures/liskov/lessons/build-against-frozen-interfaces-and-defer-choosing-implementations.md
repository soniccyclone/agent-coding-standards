---
type: lesson
title: "Build against frozen interfaces and defer choosing implementations"
figure: liskov
works: [clu-reference-manual]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Build against frozen interfaces and defer choosing implementations

**Lesson:** If a component's correctness is checked against another component's interface, then the interface is the thing the check depends on, and mutating it silently invalidates every check already performed. Most systems tolerate this: an interface is edited in place, everything that referenced it is rebuilt, and the assumption is that rebuilding catches the damage. The cleaner discipline is to treat a published interface as immutable — a changed interface is a new, separately named entity, and the old one continues to exist for everything that was verified against it. Revision by creation rather than by mutation means no previously valid check can silently become invalid.

Once interfaces are the unit that everything depends on, two useful things follow. Development can start from interfaces alone: an abstraction is registered with a declared interface and no implementation at all, and other components can be written and fully checked against it before anybody writes the code behind it. And the choice of implementation can be postponed to the last possible moment, since every implementation is checked against the same interface and every use is checked against the same interface, so any conforming implementation may be substituted at assembly or start-up time. The dependency that matters was never on a body of code, only on a description of behavior.

The names a component uses to refer to its dependencies deserve the same separation. Let each component choose whatever names read well locally, and record the mapping from those names to the actual abstractions as explicit data supplied when the component is built. Now name collisions between independently written components are impossible, teams can share a mapping to establish a common vocabulary, and different parts of a large system can use different mappings where that helps. The binding is data you can inspect and version, not a global namespace everyone must negotiate.

A programmer who believes this stops editing published contracts and starts issuing new ones. They write and check consumers before providers exist, resist wiring a specific implementation into anything that only needs the contract, and treat the resolution of names to dependencies as an explicit artifact rather than an implicit property of the build. The practical test: if changing an implementation forces recompiling its consumers, the consumers were depending on more than the interface.

**Source:** [CLU Reference Manual](../works/clu-reference-manual.md) — the library section, where each abstraction is a description unit holding an interface specification plus zero or more implementations, interfaces cannot change once defined, modules compile against interfaces alone, and an explicit compilation environment binds each module's local names to abstractions.
