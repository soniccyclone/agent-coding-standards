---
type: lesson
title: "Carry each claim's assumption set with it and compose by union, or the assumptions get lost"
figure: reynolds
works: [the-craft-of-programming]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Carry each claim's assumption set with it and compose by union, or the assumptions get lost

**Lesson:** Once a component's behaviour depends on things supplied from outside, almost nothing you can say about it is unconditionally true. What is true is a pair: a claim, and the set of conditions on the surroundings under which the claim holds. Treat that pair as the unit. The claim alone is not a result you can use, because you have no record of what it was resting on; the conditions alone are not a result either. And the operation that matters is composition: when two components are put in sequence, the resulting claim about the whole holds under the *union* of the two condition sets. That union is the whole content of what it means to compose verified things, and it is exactly what gets dropped when people record only the claims.

Doing this changes what you notice. A component whose condition set is enormous is a component that is hard to place anywhere, regardless of how elegant its claim is, and you can see that before you try to use it. A system's total condition set, accumulated up the composition, is the honest statement of what it needs from its environment — and if it is larger than you expected, the composition has told you something that no local inspection would have. Keeping these sets small becomes a design objective on the same footing as keeping the claims strong.

The mechanism that stops the sets from exploding is conditional independence, and it is worth stating carefully because it is not obvious. Rather than asserting outright that a component leaves some external quantity undisturbed — which is usually false, since it will disturb whatever its caller hands it — assert that it disturbs the quantity *only if* the things it was given disturb the quantity. That formulation is about the component's own body and its globals, so it can be established once, at the declaration, and it discharges to nothing at a call site where the arguments are already known to be well separated. Independence stated conditionally on the arguments composes; independence stated flatly does not, because the flat version has to be re-proved for every combination of arguments the component might ever receive.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — the closing discussion of Section 3.3.5, which observes that specifications of the plain precondition-statement-postcondition form are rarely universal, that the usual situation is universality under some set of assumptions, and that composing two such results yields the statement compounding conclusion under the union of the two assumption sets, with the remark that it is precisely this ability to carry along and combine assumptions about environments that distinguishes specification logic from the earlier chapters' logic; together with Section 3.3.4's clauses defining non-interference for procedures, array expressions and function procedures, each of which states that the phrase interferes only when the corresponding actual parameters do, so that the effect is to specify an absence of interference through globals.
