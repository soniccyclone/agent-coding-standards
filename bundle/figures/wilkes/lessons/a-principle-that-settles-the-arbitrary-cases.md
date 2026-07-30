---
type: lesson
title: "A design principle earns its keep by settling the hundreds of small decisions nobody could argue individually"
figure: wilkes
works: [cambridge-cap-computer-and-its-operating-system]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# A design principle earns its keep by settling the hundreds of small decisions nobody could argue individually

**Lesson:** Principles are usually justified by the properties they produce, and that leaves out the reason they get adopted in practice. A large system is built by many people making a continuous stream of small choices that have no local argument attached to them — how much reach should this particular component have, what exactly should this interface expose, where does this responsibility sit. Each one is genuinely underdetermined by the requirements. A principle that answers such questions mechanically removes the need for judgement in every instance, and that is a first-order benefit even before you count the structural quality it produces, because the alternative is not better decisions but inconsistent ones.

The test for a principle worth adopting is therefore not only whether it is right but whether it is *decidable* by whoever is holding the question. A grand statement that requires interpretation on each application still leaves every decision open and provides only the appearance of guidance. A principle stated so that it can be applied by someone who is not the architect, without escalation, is what actually governs a system built by a team. When a discipline has this shape, it is often difficult to say what other guidance could have been offered at all — which is the strongest possible endorsement, and also an honest warning that the discipline is load-bearing and cannot be relaxed selectively without leaving a vacuum.

The corollary is to notice where a project has no such rule. Any recurring category of decision that is currently settled by whoever happens to be looking at it is a place where the system's structure is being determined by accident. It does not need a better process; it needs a rule crisp enough to be applied without one.

**Source:** [The Cambridge CAP Computer and Its Operating System](../works/cambridge-cap-computer-and-its-operating-system.md) — Chapter 5's argument that a further reason for adopting the minimum privilege principle strictly is that it makes it easy to lay down guidelines for a development team, with the observation that it is not obvious what other guidance could be given to designers deciding what reach a given component should have.
