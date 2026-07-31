---
type: lesson
title: "A computation is only a value if making it does nothing"
figure: strachey
works: [toward-a-mathematical-semantics-for-computer-languages]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# A computation is only a value if making it does nothing

Once a language admits commands into its value space, a small question turns out to be load-bearing: what happens when you evaluate the expression that produces a command? Scott and Strachey answer that it produces the command and changes nothing — the command has been read, in their phrase, but not run. The reason they give is entirely practical. The whole point of letting a command be a value is that you might want to hold onto it, pass it somewhere, put it aside for later. None of that is available if the act of obtaining the value has already discharged it, because then there is nothing left to pass along. First-classness for anything effectful therefore *requires* that its construction be inert, and inertness stops being a stylistic preference and becomes the precondition for the feature existing at all.

That gives a sharp test to apply to your own designs. If building your representation of an action already performs part of the action, you do not have a value that denotes the action; you have a side effect with a return type. Everything the value form was supposed to buy is gone with it — you cannot store it, cannot retry it, cannot inspect or transform it before deciding to run it, cannot hand it to something that will run it differently. The split between describing work and doing work is not an architectural nicety layered on top; it is what makes the description a thing at all.

The companion observation in the same section is about where deferral comes from, and it is the more useful half. Evaluating a function definition is also stateless, and not by fiat: whatever effects are written in the body cannot escape, because they wait on an argument that has not been supplied, and the argument cannot be supplied until someone applies the function. The unfilled parameter is doing the deferral by itself. So the technique for postponing something is not to invent a suspension mechanism but to find or introduce a parameter it does not yet have — the missing input is the barrier, and it needs no machinery to enforce.

Both halves point at the same discipline. When a design needs work to be schedulable, retryable, inspectable, or movable across a boundary, the question to ask is what value denotes that work and whether producing that value is genuinely quiet. When you need something not to happen yet, ask what it is still missing rather than how to hold it back.

**Source:** [Toward a Mathematical Semantics for Computer Languages](../works/toward-a-mathematical-semantics-for-computer-languages.md) — the section on procedures, in the clause interpreting a command used as an expression, which leaves the state untouched and the command unactivated with the explicit motivation of storing or passing a command without executing it, and the neighbouring clause for functional abstraction, whose statelessness is justified by the state changes in the body being unable to emerge before an argument is known.
