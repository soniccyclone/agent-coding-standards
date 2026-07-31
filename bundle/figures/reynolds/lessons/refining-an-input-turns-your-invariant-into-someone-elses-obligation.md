---
type: lesson
title: "Refining an input converts your private invariant into somebody else's obligation"
figure: reynolds
works: [the-craft-of-programming]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Refining an input converts your private invariant into somebody else's obligation

**Lesson:** Choosing how to store something you own is a decision with two obligations attached — restore the relationship after every write, rewrite every read through it — and both are yours to discharge. Choosing how to store something handed to you is a different act wearing the same clothes. There are no writes to augment, so the work collapses to rewriting reads, which makes the step look cheap. It is not cheap; the cost has moved. The relationship you invented between the ideal thing and its layout is now a condition that must already hold when you are entered, which means it is a demand on whoever produces the value. You did not simplify a derivation, you exported a requirement.

The right thing to do with that is to put it where requirements go: the precondition, stated in full, in the same terms you used internally. This is uncomfortable because those terms are detailed and unglamorous — the exact indexing scheme, the fact that a listing has no repeats, the bounds relationships — and it feels like an admission that your interface is not really abstract. It is exactly that admission, and hiding it does not make it false. A caller who satisfies a vague version of the condition will produce a value your code reads incorrectly, and the failure will be attributed to your code, because from the outside your code is the thing that broke.

Generalize past the setting and this is the rule for anything you receive rather than construct: file formats, wire protocols, the shape of a table you did not create, the ordering a message queue does or does not promise. Every internal decision that assumes something about incoming data is a clause somebody upstream has to honour, and the only question is whether it is written down or discovered during an incident. The invariant you were going to keep for yourself becomes, the moment the data crosses a boundary you do not control, a term in a contract — so publish it while you still remember why you needed it.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 5.1.5's observation that transforming the input successor function has a different flavour from transforming a local variable, since the function is used but never changed, leaving no assignments to augment and only a single occurrence to eliminate; together with Section 5.1.6's note on the resulting program, that because the concatenated-segment arrays are produced by an external program, the representation invariant for the successor function appears as the precedent of the whole program — a requirement to be met by whoever computes those arrays.
