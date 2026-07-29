---
type: lesson
title: "Deleting a distinction can buy expressive power, because every case the distinction forbade becomes ordinary"
figure: ungar
works: [self-the-power-of-simplicity]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
tags: [lesson]
---
# Deleting a distinction can buy expressive power, because every case the distinction forbade becomes ordinary

**Lesson:** The usual assumption is that simplicity and power trade off: strip concepts out of a language and you lose the ability to say things. This work is a demonstration that the trade can run the other way. Two relationships between objects — "is an instance of" and "is a kind of" — collapse into one; the split between holding data and computing it collapses; the split between an object, a procedure, and a closure collapses. What makes the collapse a gain rather than a loss is that each distinction had been quietly ruling out a family of useful programs. Once there is no instance/class divide, an object with behavior nobody else shares is not an awkward singleton needing a scaffold erected around it, it is just an object. Once state access and computation are the same act, a stored field can be replaced by a computed one, or shared with another object, or trapped for debugging, without any construct existing for those purposes. The expressive power was never added; it was released by removing the thing that had been blocking it.

The mechanism behind this is worth naming, because it tells you when to expect the gain and when not to. A distinction in a language partitions the space of things you can express into privileged cases and second-class cases, and it defines a boundary that every other feature must then be defined across. Remove it and the second-class cases join the first-class ones, and every other feature stops needing a story about which side it applies to. That is also why the removals compound: eliminating classes is what lets the inheritance chain take over the job of scoping, which is what lets a procedure's frame be an ordinary object, which is what makes a method activation just a temporary specialization of its receiver. The reductions were not independent tidying-ups but a chain, each one made available by the last.

The practical discipline is to treat every distinction in a design as a claim requiring defense, and to interrogate it by asking what it forbids rather than what it enables. When you find yourself building a mechanism whose purpose is to work around one of your own categories — a way to guarantee a type has exactly one instance, a way to make a field look computed, a special rule for how the top of a hierarchy terminates — you have located a distinction that is costing you rather than paying. The infinite regress of describing every describer is the sharpest example: it is not a hard problem to be solved with cleverness, it is an artifact of insisting that no thing may carry its own description, and it evaporates the moment that insistence is dropped.

**Source:** [Self: The Power of Simplicity](../works/self-the-power-of-simplicity.md) — the stated design principles (conceptual economy, messages as the sole access to state) and the comparison of prototypes against classes, which works case by case through singletons, initialization, and meta-regress; the concluding argument that the language became more powerful by becoming smaller.
