---
type: lesson
title: "Think in the most spartan formalism the problem fits, and let a general theorem generate the concrete algorithm"
figure: knuth
works: [fast-pattern-matching-in-strings]
axes: [primitive-count, expressiveness]
subdomains: [foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# Think in the most spartan formalism the problem fits, and let a general theorem generate the concrete algorithm

**Lesson:** The account of how this algorithm was found is the most methodologically useful part of the paper, and it describes the same route travelled twice independently. Morris, building a text editor, conceptualized his scanning routine using the vocabulary of finite-state machines and arrived at something equivalent to the final method, though his presentation obscured its cost. Knuth got there by a stranger path. He had learned of a theorem stating that anything a certain restricted class of automaton can recognize at all can be recognized on an ordinary machine in time linear in the input, and he knew of a specific automaton of that class recognizing strings that begin with an even-length palindrome — a task he could not see how to do quickly by direct means. So he took the general construction in the theorem and mechanically ground through it on that particular automaton, with the explicit intention of extracting whatever mechanism was making the result come out fast. Hours of following details produced the abstraction, first for palindromes and then generalized. He remarks that this was the first occasion on which automata theory had shown him how to program something better than he already could.

The transferable method has two halves. The first is that a general theorem of the form "anything expressible in formalism F can be executed with cost C" is not merely a classification result; it is a *generator*. If you can force your problem into F, the theorem's proof is a recipe that emits an algorithm meeting the bound, and you can run that recipe by hand on your instance. What comes out is typically unreadable, which is fine — you then do the part Knuth did, which is stare at the machinery until you can name what it is exploiting, and rewrite that directly.

The second half is about the choice of formalism, and it is why both discoveries came through automata. Finite-state machines are almost featureless: no storage you can reach into, no way to revisit input, nothing but a position in a fixed set of positions. Forcing a problem into a basis that austere is exactly what surfaced the key fact here, because in such a formalism *there is no option* of remembering the characters you have read, so if a solution exists at all it must be one in which the current position already implies what you would have wanted to remember. A richer, more comfortable formalism leaves that possibility invisible, since you would simply keep the characters around. Poverty of primitives is not a constraint you tolerate; it is a search technique. What survives translation into a minimal basis is the structure that was actually load-bearing.

A programmer who works this way spends time up front asking what the weakest machine model that could possibly solve the problem is, and treats any general theorem about that model as executable rather than decorative. It is slow, and it periodically produces an algorithm nobody would have guessed at.

**Source:** [Fast Pattern Matching in Strings](../works/fast-pattern-matching-in-strings.md) — the historical remarks section, which recounts both authors reaching the method through finite-automata reasoning and describes grinding a general linear-time simulation theorem through a specific automaton in order to distill the mechanism behind it.
