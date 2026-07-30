---
type: lesson
title: "Thread an effect explicitly and it will tell you what it acts on and who is exempt"
figure: reynolds
works: [definitional-interpreters-for-higher-order-programming-languages]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Thread an effect explicitly and it will tell you what it acts on and who is exempt

**Lesson:** Mutation is the feature everyone believes they understand and nobody can state. The way to get a grip on it is to refuse the ambient version and make it an argument: introduce an object standing for the whole current state of what has been assigned, pass it into every operation that could be affected, and have every operation that could assign hand back an updated one. The moment this is done, an ordering question that was implicit becomes a visible data dependency — the updated state produced by evaluating the first thing is the state passed to the second — and any place where the threading is ambiguous is a place where the language's evaluation order was previously unspecified and nobody had noticed.

Doing this forces a distinction that ambient mutation lets you blur. Assignment cannot be to a name, because several names can denote the same assignable thing, and updating through one must be visible through the others. So the assignable thing is a separate kind of object with its own identity, and a name is bound to one of *those* rather than to a value. Once the separation exists, the whole vocabulary that surrounds mutation becomes statable: creating a fresh one, reading the value it currently holds, replacing that value, and the abstract properties that these four operations must satisfy relative to each other. The most consequential design choice in the area then becomes a clean question — whether every context that could hold a value holds one of these instead, or whether they are simply an additional kind of value that can appear wherever values appear — instead of the muddle it usually is.

The last dividend is the exemptions. Having threaded the state everywhere, work out which components genuinely cannot be affected and remove it from their signatures: evaluating a constant, looking up a name, and constructing a function value cannot cause an assignment, so none of those needs the state and none of them returns one. This is not tidying. Each exemption is a claim about the reach of the effect, checkable and falsifiable, and the shape of the resulting interfaces documents exactly where mutation can and cannot occur — which is precisely the information a reader needs and the ambient version never provides. Generalize past mutation: for any pervasive effect, thread it explicitly first, then prune, and treat the surviving signatures as the specification of the effect's blast radius.

**Source:** [Definitional Interpreters for Higher-Order Programming Languages](../works/definitional-interpreters-for-higher-order-programming-languages.md) — section 10, which introduces memories as explicit arguments threaded through evaluation and passed onward to continuations, argues that assignable entities must be distinguished from variables because several variables may denote the same one, characterizes references abstractly by an initial memory plus operations to obtain a fresh reference, augment, update and look up, contrasts the L-value and reference approaches, and notes that constants, variables and lambda expressions neither accept nor produce memories.
