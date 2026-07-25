---
type: lesson
title: "Reduce a whole design vocabulary to a handful of binding forms, then measure the vocabulary by what derives from them"
figure: cardelli
works: [on-understanding-types-data-abstraction-and-polymorphism, an-imperative-object-calculus, a-semantics-of-multiple-inheritance]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
tags: [lesson]
---
# Reduce a whole design vocabulary to a handful of binding forms, then measure the vocabulary by what derives from them

**Lesson:** Language features arrive as a long list of apparently unrelated inventions: generics, modules, information hiding, interfaces, classes, inheritance, instance variables, message sending. The productive move is to ask what small set of ways-of-binding-a-name each of them secretly uses. Abstraction over a value gives ordinary procedures. Abstraction over a type gives generic code. Asserting that some type exists without saying which gives hiding, and therefore modules and abstract data types. Constraining any of those abstractions to range only over refinements of a stated type gives inheritance-flavoured reuse. With those few forms plus labelled products and labelled sums, the long list collapses into combinations, and features that looked like separate language design problems become the same problem seen from different angles.

The payoff is not economy for its own sake. Once features are expressed in a shared basis you can see which ones interact and how, because the interaction is now a composition of known forms rather than a clash of two implementations. Hiding a representation and parameterizing over an element type stop competing and start nesting. Linking modules turns out to be ordinary application, which means the language you program in is also the language you configure in, and no separate build-time dialect is required. The same collapse happens on the object side: a record whose fields hold functions accounts for method dispatch, recursion at the point of construction accounts for a component's ability to refer to the whole, and lexical scoping accounts for private state, so none of those needs a bespoke mechanism.

There is a discipline attached, which is that the derived constructs must be honestly derived and the cost of derivation must be counted on the operation side as well as the data side. Collapsing passive data into behaviour is only complete if the update operation generalizes to the harder case too, and that generalization can drag in a construct nobody would have written down at the start. Paying that price knowingly is different from pretending the unification was free.

A designer who works this way judges a proposed feature by asking which existing form it is a sugared instance of, and treats a feature that cannot be placed as either genuinely new, and therefore needing its own rules, or confused. A reader gains the same leverage: understanding four binding forms well beats memorizing thirty features, and the residue that refuses to reduce is exactly where the real content lives.

**Source:** [On Understanding Types, Data Abstraction, and Polymorphism](../works/on-understanding-types-data-abstraction-and-polymorphism.md) — the successive extensions of a typed kernel by universal, existential, and bounded quantification, and the module and package examples where linking is expressed as ordinary application. Also [A Semantics of Multiple Inheritance](../works/a-semantics-of-multiple-inheritance.md) — the section of inheritance idioms, which reconstructs self-reference, private variables, and method overriding from recursion and scoping. Also [An Imperative Object Calculus](../works/an-imperative-object-calculus.md) — the derivation of fields, local definitions, sequencing, and procedures from a kernel with a single update operation, including the discussion of what that unification costs.
