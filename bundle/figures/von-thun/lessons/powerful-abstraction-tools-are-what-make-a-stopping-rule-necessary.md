---
type: lesson
title: "Powerful abstraction tools are what make a stopping rule necessary"
figure: von-thun
works: [some-simple-programming-in-joy]
axes: [cognitive-load, primitive-count]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Powerful abstraction tools are what make a stopping rule necessary

Three of von Thun's stack operations share nearly all their text, differing only in a name and one word of work. He notices, says the shared part could be factored out, and declines — because the factored version would be harder for a person to read. Later he does it again: a merging program repeats an unpacking step it could hoist, and he leaves it, on the grounds that the version as written is easy to understand and correct. These are small moments in a long paper, and they are worth more than they look, because of who is saying them. This is the author of a language whose whole purpose is to make redundancy eliminable — whose recursion combinators exist so that no one ever writes the same recursion twice, and whose program-construction technique can collapse a family of functions into one. The person with the sharpest deduplication tools in the room is choosing, twice, not to use them.

The reason is that removing repetition is not free. It moves cost from the amount of text to the amount of indirection a reader must hold, and those are different currencies paid by different people at different times. Repetition that a reader can see at a glance is cheap; a parameterisation that a reader must mentally re-specialise for each of three call sites is not, even though it is shorter. So "these three things are similar" is a fact, not an argument, and the argument has to be made separately: does anything downstream actually benefit from their being one thing? Do they change together? Is the shared part meaningful, or merely coincident right now?

The uncomfortable implication is that abstraction capability and abstraction judgment run in opposite directions. The more expressive your tools, the more opportunities you can see, and the fewer of them are worth taking — because with weak tools the unprofitable factorings are simply impossible, and with strong tools nothing stops you. This is why a stopping rule is a requirement rather than a nicety, and why the criterion has to be something outside the code's own structure. Von Thun's criterion is the human reader, invoked explicitly, and it overrides the aesthetic pull of his own machinery. A programmer who adopts this asks not "can these be unified" but "who is better off after the unification," and treats the absence of an answer as a decision to leave the duplication alone.

**Source:** [Some Simple Programming in Joy](../works/some-simple-programming-in-joy.md) — the stack-type library, where the shared structure of three operations is identified and deliberately left unfactored for readability, and the closing remark on the merging programs declining an available optimisation for the same reason.
