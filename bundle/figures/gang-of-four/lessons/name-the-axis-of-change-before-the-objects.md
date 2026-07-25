---
type: lesson
title: "Ask which aspect of the design must be free to move, and let that answer shape the structure"
figure: gang-of-four
works: [design-patterns-abstraction-and-reuse-of-object-oriented-design]
axes: [expressiveness, cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Ask which aspect of the design must be free to move, and let that answer shape the structure

**Lesson:** Having assembled two dozen recurring structures, the authors ask what they have in common and arrive at an answer more useful than the catalog itself: each one exists to let some single aspect of a system change without disturbing the rest. One isolates which concrete class gets instantiated. One isolates the algorithm a computation uses. One isolates how a structure is traversed. One isolates how an interface is spelled. The structures differ in mechanism but share a purpose — they pick an axis and make movement along it cheap. That observation inverts the design question. Instead of starting from "what are the entities here," you start from "what is going to have to move, and along which axis," and the answer nominates the structure.

This holds because the cost of a design is not paid at first writing, it is paid every time reality demands a change the structure did not anticipate. A design is not flexible or inflexible in general; it is cheap along particular directions and brutally expensive along others, and which directions those are is a decision you make whether or not you make it consciously. Committing to a class name in client code is a decision that instantiation will never vary. Writing an algorithm inline is a decision that only one algorithm will ever be wanted. These commitments are usually invisible because they look like the absence of a decision rather than the presence of one. Naming the axis of variation up front makes them visible while they are still cheap to revise, and it gives the eventual structure a stated purpose — someone reading it later can ask whether the indirection is buying the variation it claims to buy.

There is a second, subtler payoff in expressive terms. When a design is organized around its real axis of change, that axis has a name and a place in the code, so the code says what the system is prepared for. When it is not, the flexibility exists only as a story told in review meetings and eventually forgotten. And the discipline scales down as well as up: the question is worth asking about a single function, where the answer might be "nothing varies, write it straight."

A programmer who has internalized this treats "what should be variable?" as the opening question of a design conversation rather than a late refactoring concern, states the axis explicitly before choosing a mechanism, and — crucially — is willing to answer "nothing." The habit is not a bias toward flexibility. It is a bias toward knowing which flexibility you are buying and which you are declining.

**Source:** [Design Patterns: Abstraction and Reuse of Object-Oriented Design](../works/design-patterns-abstraction-and-reuse-of-object-oriented-design.md) — the conclusion, where the authors identify independent variation as the property common to nearly every pattern in the catalog and name the resulting design activity after it.
