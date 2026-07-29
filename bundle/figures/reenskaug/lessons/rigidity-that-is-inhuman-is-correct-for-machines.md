---
type: lesson
title: "The rigidity that makes an organization inhuman is exactly right for machines"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# The rigidity that makes an organization inhuman is exactly right for machines

Reenskaug takes the classical specification of a perfectly rational bureaucracy — continuous functions bound by rules rather than ad hoc relations, a precisely bounded sphere of duties paired with exactly the authority needed to discharge them, an explicit obligation to know the limits of that authority so as not to undermine anyone else's, positions that no occupant may appropriate as personal territory, and everything recorded rather than passed on by word of mouth — and observes that applied to people this is a nightmare, while applied to a system of software components it is nearly ideal. The properties that make such an arrangement oppressive for humans are the properties that make a machine analyzable.

The mapping is exact enough to be useful rather than cute. Bounded duties with matching authority is a component that answers for its own concern and is granted only the reach that concern requires. Knowing the limits of one's rights is the obligation not merely to respond correctly but to refrain from issuing requests the design did not sanction — a duty of restraint, not just of service. A position that cannot be appropriated by its occupant is encapsulation: influence flows only through declared channels, never through privileged familiarity with someone's internals. And the recording requirement is the sharpest of them: the rules governing conduct must be written where they can be consulted, because norms carried in a team's heads as "how we do things here" are, in Reenskaug's flat judgment, guaranteed to cause trouble eventually.

The inversion runs the other way too, and that is the part worth internalizing. Human organizations survive their formal defects because people improvise, ask around, notice something is off, and route around a broken rule. None of that is available to software. A design that would only work if participants exercised judgment about when a rule should not apply is a design that will not work, and every gap left for informal adjustment becomes a gap where nothing happens at all.

A programmer who holds this stops apologizing for strictness in a design and starts treating the discretion a component is permitted as a liability to be minimized and stated. It also reframes undocumented convention as an outright defect rather than a documentation debt — the system is defined by what is written, and a rule that exists only in practice is a rule the system does not have.

**Source:** [Working with Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — the passage in the model-creation chapter that walks through the Weber/Etzioni characterization of a rational organization point by point, and the derived list of rules Reenskaug proposes for rational object-oriented design, including the duty not to send undeclared messages and the insistence on documented norms.
