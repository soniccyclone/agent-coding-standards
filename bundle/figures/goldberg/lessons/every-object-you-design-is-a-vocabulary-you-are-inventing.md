---
type: lesson
title: "Designing an object is designing a vocabulary, so the real work is choosing what may be asked of it"
figure: goldberg
works: [smalltalk-80-the-language-and-its-implementation]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Designing an object is designing a vocabulary, so the real work is choosing what may be asked of it

**Lesson:** The claim this book makes about its own activity is stronger than the usual advice about good interfaces: whenever a programmer fixes the set of requests an object will answer, a language has been designed. Not metaphorically — the names and argument shapes chosen become the terms in which everything downstream will be written and read, and they constrain what can be said as tightly as any grammar. Under that reading, deciding which objects exist and what may be asked of each *is* the design work; writing the bodies that answer is bookkeeping that follows. That reframing has teeth because it changes what you review. A vocabulary is judged on whether the statements it enables read like the intent behind them, not on whether each individual operation is implemented well.

Two disciplines follow, and this book applies both consistently. First, the request set should be semantically complete rather than sized to today's caller: a thing that can be added to but never subtracted from is a poorer concept than the one that supports both, even when nothing currently subtracts, because the truncated vocabulary silently forecloses uses you have not thought of. This is the same bet as designing a substrate instead of a feature list, applied one level down at the granularity of a single type. Second, the vocabulary may be deliberately redundant when redundancy buys legibility — offering both a keep-these and a discard-these form of the same filtering operation adds nothing to what can be computed, and adds something real to how directly a criterion can be stated the way the programmer actually thinks it.

The same principle reappears explicitly when this book builds a larger application. Constructing a simulation framework, it names the set of messages the modeler will use to describe an entity's activities as a task language, and treats designing that set as the framework's substance. The framework's classes are just what makes the language work. So the escalation is deliberate: a class is a small vocabulary, a framework is a larger one, and an application built on a framework is a sentence in it. Nothing about this ladder introduces a new mechanism at any rung — it is the same act of choosing terms, repeated at different scales.

A programmer who accepts this stops treating naming as a polish step. The concrete change in behavior is to write the calls before the definitions: state the code you want the caller to be able to write, and only then decide what has to exist for that to be legal. When a caller's expression reads awkwardly, the diagnosis lands on the vocabulary rather than on the caller.

**Source:** [Smalltalk-80: The Language and Its Implementation](../works/smalltalk-80-the-language-and-its-implementation.md) — the discussion in the early chapters on designing an application, which identifies specifying an object's messages with designing a language and argues for specifying a full set of operations rather than only those a current program needs; the paired filtering-message rationale in the collection-protocol chapters; and the simulation framework in Part Three, where the modeler-facing message category is presented as a language in its own right.
