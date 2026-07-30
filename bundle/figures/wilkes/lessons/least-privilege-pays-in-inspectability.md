---
type: lesson
title: "The return on minimum privilege is inspectable blast radius, and it is paid mostly in development and change"
figure: wilkes
works: [cambridge-cap-computer-and-its-operating-system]
axes: [verifiability, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# The return on minimum privilege is inspectable blast radius, and it is paid mostly in development and change

**Lesson:** Restricting each part of a system to exactly what it needs is usually defended as a protection against misbehaviour, and that defence understates the case badly. The larger return is diagnostic. If reach is minimal and, crucially, if the reach of a component can be determined by inspecting it rather than by running it, then a whole class of defect — a component touching what it had no business touching — is caught at the moment of the attempt rather than discovered later as inexplicable corruption. And when corruption is nevertheless observed, its possible authors are the enumerable set of components with reach to the damaged thing, which converts an open-ended hunt into a short list. This holds for faults with no author at all: a hardware failure that would otherwise silently corrupt distant state instead violates a constraint that is checked on every access, so it announces itself early and locally.

The consequences run past debugging and into how an organization behaves. A change to a system whose failure modes are contained can be made and shipped on the strength of a bounded argument; a change to a system where any error may corrupt anything cannot. So a team working on a tightly constrained system will make changes with more confidence and will say yes to more requests, not because the code is easier to write but because the cost of being wrong is bounded and known in advance. That is a technical property producing an institutional one, and it is invisible in any evaluation that only asks whether the discipline prevented an attack.

Knowing which argument you are making matters, because the two have different scopes. For material whose corruption or exposure would be serious, the strict case is easy and can justify subdividing structures very finely. For everything else — most of a system — the case has to be made on development speed and resilience, and it must be made explicitly, since it does not appear in any threat model. Working against both is a real cost: changing the reach of running code has overhead, and that overhead sets the practical floor on how fine the subdivision can go.

**Source:** [The Cambridge CAP Computer and Its Operating System](../works/cambridge-cap-computer-and-its-operating-system.md) — Chapter 1's statement of the ideal requirement that a running procedure have access only to what it requires and that this be determinable by inspection or trace, with its development-time and in-service benefits and the containment of hardware faults; and Chapter 5's discussion of the minimum privilege principle, where the case for strict application to non-sensitive material rests on ease of development and ruggedness, against the acknowledged overhead of changing protection domains.
