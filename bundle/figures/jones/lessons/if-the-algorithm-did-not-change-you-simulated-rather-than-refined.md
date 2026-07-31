---
type: lesson
title: "If the algorithm did not change, you simulated the description rather than implemented it"
figure: jones
works: [software-development-a-rigorous-approach]
axes: [performance, cognitive-load, hardware-affinity]
subdomains: [software-engineering-and-architecture, algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# If the algorithm did not change, you simulated the description rather than implemented it

**Lesson:** Descriptions of what a system must do are written in whatever structures make the statement clearest — collections, keyed lookups, sequences, sets of candidate answers. Modern languages provide all of those as library types, which creates a trap that is hard to see because everything about it looks like progress. You transliterate the description into the language, the types line up, the tests pass, and it appears the implementation is done. It is not. Providing runnable versions of the description's structures is simulation, and simulation gets you a program with the description's performance profile, which is generally catastrophic, because the description was optimised for being read.

There is a blunt diagnostic. A genuine step toward implementation changes the algorithm. If you replaced the structures and the surrounding code kept its shape — same traversals, same nesting, same order of operations, with the type names swapped — you did not take a step; you re-typed the description. A real change of representation makes the old procedure impossible or absurd and forces a different one: a recursion becomes a sweep because the new structure is indexed rather than nested, a membership test disappears because the new layout makes the answer positional, a set-valued result becomes an accumulation because sets no longer exist below this line. That coupling is the point. Representation and algorithm are not two independent choices, and a step that touches only one of them has not gone anywhere.

The confusion is worth naming precisely because both activities are called "using abstract data types." One use is specification: the abstraction is there so a human can state and check what is wanted. The other use is design: the abstraction is an intermediate structure being progressively replaced. The two look identical on the page and are entirely different in what they oblige you to do next. Treat the first as the second — treat a specification as though it were an abstract algorithm waiting to be typed in — and you will ship the specification.

**Source:** [Software Development: A Rigorous Approach](../works/software-development-a-rigorous-approach.md) — chapter 18's summary, which states that the example is large enough to clarify the distinction between two different uses of abstract data types in program development: that although the early stages use objects such as sets for which simulations would be easy to provide, this would not yield a realistic implementation, that these abstractions must be seen as specifications and not as abstract algorithms, and that the role of true refinement steps is to introduce different data structures which require different algorithms. Also chapter 17's "Language Support for Abstract Data Types", which makes the same point about a specification written in terms of an abstraction the implementation language can simulate, and names the distinction as one between refinement, where the algorithm changes, and simulation.
