---
type: lesson
title: "A substrate that can represent anything cannot be used without programming, and that is the trade"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [expressiveness, primitive-count]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# A substrate that can represent anything cannot be used without programming, and that is the trade

**Lesson:** Asked whether the more general data technology would displace the restrictive one, this author says no, and the reason is a mechanism rather than a preference. The general store can represent anything and therefore cannot be used without low-level programming. The restrictive store organizes everything one way, and precisely because it does, a high-level specification of a system can be turned into a working system automatically. Leverage comes *from* the restriction — the tools that generate, validate and optimize can only exist because they know in advance what shape everything has.

Stating it as a trade rather than as a ranking is what makes it usable. Generality is not free and its cost is not paid in performance; it is paid in the loss of every mechanical service that depended on knowing the shape. A representation admitting arbitrary structure has nothing for a generator to generate from, nothing for a validator to check against, and no canonical query surface, so all of that work relocates to a human writing code by hand for each application. The general substrate is thus not a superset of the restricted one in any practical sense: it can express more per unit of effort spent programming, and vastly less per unit of effort spent specifying.

The prediction that follows is the useful part, and it is falsifiable: a general substrate becomes a real competitor to a restricted one only by adding a restricting layer above itself — a schema, a conceptual framework, some commitment about shape that the tools can rely on. That is worth holding as an expectation about how flexible technologies mature. They do not win by being flexible; they win by acquiring conventions strict enough to support tooling, at which point they have paid back the generality in the places that matter and kept it at the edges. Watching for whether such a layer exists is a quick way to assess whether a "more powerful" alternative is actually ready to replace an entrenched restricted one, or is still at the stage where every use is a programming project.

The general reflex applies to any choice between a constrained format and an arbitrary one — configuration, protocols, document models, storage. Ask what the constraint buys mechanically, count the tools that exist only because of it, and treat those as the price of moving to something that permits more. Where a team has already chosen the general option and finds itself writing the same code repeatedly, that repetition is the missing restricting layer announcing itself.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 11 section 11.3, headed with the observation that database technology gives leverage through restricted structure, noting that a conceptual schema can specify a customized information system so that traditional programming is often avoided altogether, and stating that the object-oriented database is not a viable competitor to the relational one because it is too general — it can represent anything and cannot be used without low-level programming — so true competitors must restrict their scope to enable high-level specification and generation tools, and the object-oriented database would have to add a conceptual schema layer to compete.
