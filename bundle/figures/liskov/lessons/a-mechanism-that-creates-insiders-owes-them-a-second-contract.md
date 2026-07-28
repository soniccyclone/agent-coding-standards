---
type: lesson
title: "Any mechanism that creates insiders owes them a second contract"
figure: liskov
works: [data-abstraction-and-hierarchy]
axes: [cognitive-load, verifiability, expressiveness]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Any mechanism that creates insiders owes them a second contract

**Lesson:** The whole payoff of hiding an implementation is that there is exactly one way in, so exactly one description governs everyone, and the implementation can be replaced by reasoning about that description alone. Derivation mechanisms usually breach this by admitting a privileged second population — code that extends the module and is permitted to see the state, invoke non-public operations, or reach past its immediate parent. From that moment the module has two audiences with different views, and only one of them has a written contract.

The unwritten contract does not go away; it accumulates as expectations in the extending code. And the moment a maintainer touches the internals, the question "who could this break" no longer has a local answer: reasoning has to span the combined text of parent and children, and a reworked parent may force every child to be reworked too. The clean version of this situation is to admit the second audience exists and write down what it may rely on — necessarily more detail than the outside view, ideally still far less than the code. That document is the price of admission for the privilege.

Two things make the price steep. The more the insider contract commits to about how the parent currently works, the smaller the space of future implementations that can satisfy it, so a generous insider contract quietly forecloses the very freedom encapsulation was purchased to preserve. And if each extender is allowed to depend on its own private understanding, there is no shared contract at all, only a pile of incompatible ones — which is the state most codebases with deep hierarchies are actually in. The workable discipline is one insider contract for all extenders, held deliberately thinner than the code.

A programmer who believes this treats every escape from encapsulation as creating a documentation obligation rather than saving effort, and reads a hierarchy where children read their parent's state as a hierarchy with no encapsulation at all. It also reframes the appeal of building by extension: it is a fine way to get something running, and an expensive way to have something maintainable, and knowing which situation you are in is the decision that matters.

**Source:** [Data Abstraction and Hierarchy](../works/data-abstraction-and-hierarchy.md) — the inheritance section's account of a class having both outside users and subclass users, the three ways encapsulation gets violated, and the argument that a separate, thinner specification is needed for the subclass audience.
