---
type: lesson
title: "A rule you validated on closed code can be false the moment a name can be supplied from outside"
figure: reynolds
works: [the-craft-of-programming]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# A rule you validated on closed code can be false the moment a name can be supplied from outside

**Lesson:** Rules that look like facts about syntax are usually facts about syntax *plus* an unstated assumption about who gets to decide what the names mean. Assigning to one variable leaves an unrelated condition on two others undisturbed — obviously, and provably, as long as "unrelated" is guaranteed by the fact that they are three different declarations in one program you can see. Introduce parameters and the guarantee evaporates: the three names can be bound, at some call site you have never read, to overlapping things, and the rule that was sound becomes a falsehood. Note what did *not* happen. The rule was not discovered to have been wrong; it was discovered to have been implicitly quantified over a world that parameterization takes you out of.

This is why a specification about a fragment containing free names is not, by itself, true or false. Its truth depends on what those names denote, and the fix is not to guess a default binding but to make that dependence part of what a claim means: a claim is now a function from bindings to truth, and the interesting claims are the ones that hold under *every* binding. Trying to duck this by saying "the meaning is determined by the enclosing declaration" fails on exactly the case that motivated the whole exercise, because a fragment can sit inside a component that receives its collaborators as arguments, so the same textual occurrence has different meanings on different runs. There is no enclosing declaration to point at.

The practical instruction is to check your local reasoning for closed-world assumptions before exporting the code that relies on it, and to check for them by asking which two names your argument treats as certainly distinct. Those are the assumptions parameterization will break. Once found, they have to be promoted into stated conditions on the binding — the ones the caller must satisfy — rather than left as properties the code appears to have. This is also a warning about how much a facility costs: passing behavior as an argument is powerful, and part of what you pay for it is that a whole class of previously self-evident local facts stops being self-evident and has to be established at every boundary.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — the opening of Section 3.3, which observes that a specification of a call cannot be judged true or false without knowing what the called identifier means, rejects the proposal to read the meaning off the binding declaration on the grounds that the call may sit in the body of a higher-order procedure where the meaning varies between executions of the same occurrence, and then exhibits an assignment specification inferable in the logic of the earlier chapters which formal parameters can falsify through interference; leading to the conclusion that the meaning of a specification, and of any phrase occurring in one, depends on an environment mapping free identifiers to meanings, and to the introduction of specifications that are true in all environments.
