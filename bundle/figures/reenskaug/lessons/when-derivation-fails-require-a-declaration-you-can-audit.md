---
type: lesson
title: "When automatic derivation fails, require a declaration and mechanically audit it for completeness"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# When automatic derivation fails, require a declaration and mechanically audit it for completeness

**Lesson:** Two sides of an interface needed to agree on what a change meant, and each side could only speak its own language. The data holder knows which of its internal attributes it just modified. The dependent knows only the queries it calls, and what it needs told is which of those queries will now return something different. Neither vocabulary is convertible into the other by inspection, so a map between them is required — and the team's attempts to generate that map automatically all failed.

The instructive part is what they did instead of either retrying the automation or abandoning the design. First they refused the tempting shortcut of making one side learn the other's vocabulary: they had tried having the data holder name the affected queries directly, and it proved almost impossible to keep correct, because every query added to the interface silently invalidated notification code elsewhere. That failure mode is the general one for cross-boundary knowledge — it does not break loudly when the other side changes, it just goes quietly out of date, and there is nothing to test against. Letting each side name things in its own terms and putting an explicit map between them confines the fragility to one artifact, and an artifact you can point at is an artifact you can check.

Second, and this is what makes the manual map acceptable rather than merely tolerable, they built a checker that flags any class whose map is missing or that fails to mention every attribute the class announces changes to. The completeness property here is worth isolating because it is much weaker than correctness and much more useful than nothing: a tool cannot tell whether a programmer mapped an attribute to the right set of queries, but it can tell with certainty whether every attribute appears at all, and omission is the failure that actually happens. Forgetting an entry is silent and produces a stale dependent much later; mapping an entry wrongly is a visible bug found on the first test. So the automation should be spent on the failure mode humans cannot detect, not on the one they can. A generator for a first-draft map is fine as a convenience, provided its output is presented as something to be checked rather than trusted.

The transferable rule: when a needed correspondence cannot be derived, do not conclude the design is wrong and do not push the knowledge across the boundary. Make the correspondence a declared, single-location artifact, then find the strongest structural property of it a tool can verify — usually exhaustiveness over some enumerable set — and enforce that.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 9 sections 9.5.5 and 9.6, where the changeParameterAssociations class method maps model attribute names to the message selectors whose return values depend on them; the text records that attempts to create the map automatically all failed, that having the model programmer list affected selectors directly was almost impossible to maintain as new messages were added, that the Taskon Quality Checker flags implementations which are missing or do not mention all attributes named in changedAttributes:areas:, and that the browser's generator produces a default the programmer must check carefully.
