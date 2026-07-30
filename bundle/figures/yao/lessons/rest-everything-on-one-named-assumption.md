---
type: lesson
title: "Rest the whole edifice on one named assumption, stated before the first result"
figure: yao
works: [how-to-generate-and-exchange-secrets]
axes: [verifiability, primitive-count]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Rest the whole edifice on one named assumption, stated before the first result

**Lesson:** Every non-trivial guarantee is conditional on something unproved. The engineering question is not whether you have such a dependency but how many you have, whether each is written down, and whether a reader can find them without reconstructing your reasoning. A result that quietly draws on several unstated hardness claims, timing properties, or environmental invariants is not more powerful for having more support; it is weaker, because its failure modes are unenumerable. Nobody can tell which of the assumptions a new attack invalidates, so nobody can tell what survives. Collapsing the dependency set to one clause, giving it a name, and placing it ahead of every theorem it feeds turns a diffuse liability into a single audit point.

Two things follow from that consolidation, and both are worth more than the tidiness. First, falsification becomes localized: if the assumption is broken tomorrow, exactly one repair is needed and its scope is known, whereas a construction resting on a bundle of interacting premises has to be re-examined premise by premise, and the interaction terms are where the surprises hide. Second, the assumption becomes comparable. A single named clause can be lined up against the assumptions other people's constructions require, so claims about relative strength are checkable rather than rhetorical, and the field can order results by what they cost rather than by what they achieve. That ordering is what lets later work reuse yours with confidence about what it is inheriting.

The transferable discipline is to write the dependency list first and treat its length as a design metric. When a construction seems to need a second assumption, that is a signal to look for a formulation that does not — usually by weakening what the construction promises, or by deriving the second capability from the first at some cost, rather than by helping yourself to it. The same audit applies far outside cryptography: a service whose availability argument rests on clock synchronization *and* bounded message delay *and* a particular retry policy has three independent ways to be wrong and no single place to check any of them. Name them or fold them; do not leave them implicit and plural.

**Source:** [How to Generate and Exchange Secrets](../works/how-to-generate-and-exchange-secrets.md) — the introduction, where the intractability of factoring is set out as a single labeled assumption before any of the four theorems, and the accompanying remark contrasting an earlier protocol for the same exchange problem that rested on several assumptions and consequently attracted follow-up scrutiny of those assumptions.
