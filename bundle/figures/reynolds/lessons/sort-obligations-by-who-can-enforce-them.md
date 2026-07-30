---
type: lesson
title: "Sort every obligation by who can enforce it, and give each class its own notation"
figure: reynolds
works: [the-craft-of-programming]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Sort every obligation by who can enforce it, and give each class its own notation

**Lesson:** The conditions a component imposes on its users do not all have the same character, and treating them as one undifferentiated pile of documentation wastes the ones that could have been mechanized and buries the ones that could not. Three kinds are worth separating. Some conditions describe states of the computation — what must be true when you call, what will be true when you return. Some describe what may syntactically be supplied in each position, and a checker can enforce these before the program runs. And some describe relationships *between* the things supplied — most importantly that two of them must not be the same thing, so that writing through one does not disturb the other — which are generally beyond what syntax can express and beyond what any checker will catch for you. Each kind has a different enforcer: the run, the compiler, and the reader.

Separating them changes what you do with each. The compiler-checkable class should be pushed as far as it will go, since anything you can shift into it gets checked for free forever; the interesting design work is finding formulations that make more conditions expressible there. The state class belongs at the call boundary in the form your correctness argument consumes. And the reader-enforced class — the one nobody will catch — needs the most visible treatment of all: written explicitly, in a fixed notation, in a fixed place in the declaration, because it is the only class with no backstop. A component whose safety depends on two of its arguments being distinct, and which does not say so, is a trap; nothing in its body reveals the assumption, and nothing in the caller reveals the violation.

There is a caution attached to the third class that keeps this from becoming complacent. The boundary between "checkable" and "not checkable" is not fixed; it is where the state of the art currently stands. Conditions about non-overlap in particular have moved, over time, from things only a reader could confirm toward things a discipline can guarantee. So write down the reader-enforced conditions in a form precise enough that they could later be checked, rather than as prose. That way, when the boundary moves, your annotations are already specifications rather than folklore that has to be reconstructed from the code.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 3.1.4 on interference and parameter assumptions, which shows a factorial procedure silently failing when both arguments name the same variable, introduces an explicit notation for non-interference placed between the formal parameter list and the body, states the distinction that assertions describe computational states while specifiers describe syntactic restrictions enforceable by a compiler and parameter assumptions describe restrictions too subtle to be treated syntactically, and notes that devising syntactic restrictions to control interference was then an active research problem.
