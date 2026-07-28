---
type: lesson
title: "A vocabulary missing a distinction does not stay silent about it — it gets abused into stating it wrongly"
figure: knuth
works: [big-omicron-and-big-omega-and-big-theta]
axes: [expressiveness, primitive-count, verifiability]
subdomains: [algorithms-and-complexity, programming-languages-and-semantics]
tags: [lesson]
---
# A vocabulary missing a distinction does not stay silent about it — it gets abused into stating it wrongly

**Lesson:** The occasion for this letter is an error Knuth kept finding in print: people rejecting an algorithm on the grounds that its cost was *at most* quadratic. Read literally that is not a reason to reject anything, since an upper bound is compatible with the method being fast. The writers did not mean it literally; they meant the cost was genuinely that bad, a lower bound. They reached for the only growth-rate symbol the field had and used it to say something it does not say. The failure mode is worth naming precisely, because it is not a typo and it is not ignorance. It is a well-formed sentence in the available vocabulary that carries a meaning the vocabulary cannot carry, and nothing in the notation flags it.

That is the general shape. When a formalism has one construct where the domain has two distinguishable situations, practitioners do not stop needing the distinction — they keep needing it, and they encode it in tone, in context, in what a sympathetic reader will assume. Those channels are invisible to checking. A reader who takes the notation at face value gets a claim that is technically true and practically backwards; a reader who reads the intent gets the right claim from a symbol that does not license it. Both readings are available simultaneously, which means no amount of care in reading recovers the author's meaning. The remedy is not more discipline in usage. It is enlarging the vocabulary so that "at most," "at least," and "exactly this order" are three different things you write, and so that a claim about one is no longer expressible as a claim about another.

The paper also shows what enlarging a vocabulary honestly costs. Knuth did not invent the lower-bound symbol; he found it in analytic number theory, where a definition already existed — and then changed it, because the inherited version bounded a function from below only on infinitely many inputs rather than on all large ones, which is too weak to support the kind of claim an algorithm analysis wants to make. He justifies the change on the grounds that the old definition was barely used and had other ways of being said. The move is instructive precisely because it treats a definition as engineering rather than inheritance: you pick the definition that makes the theorems you actually need come out clean, and you pay the migration cost of diverging from a prior field when the prior definition does not serve your use.

For a working programmer the transferable habit is to treat systematic misuse of a construct as a specification request. When people in a codebase keep pressing one type, one status code, one error class, or one configuration flag into service for a case it does not cover, the correct reading is not that they are sloppy — it is that the type system, the protocol, or the API is short a distinction the domain contains, and every such misuse is a place where a checker could have caught a real error and could not, because the wrong thing was spelled the same as the right thing.

**Source:** [Big Omicron and Big Omega and Big Theta](../works/big-omicron-and-big-omega-and-big-theta.md) — the opening complaint about upper-bound notation being used for lower bounds, and the later passage explaining why the number-theoretic lower-bound definition was strengthened before adoption.
