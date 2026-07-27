---
type: lesson
title: "Do not assert your rules and hope; state what would make them adequate and derive them"
figure: floyd
works: [assigning-meanings-to-programs]
axes: [verifiability, primitive-count]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Do not assert your rules and hope; state what would make them adequate and derive them

**Lesson:** When you write down a rule for reasoning about a construct, the temptation is to check it against intuition and move on. That gets you a rule that is probably sound and almost certainly weaker than necessary, and worse, it gives you no way to tell the difference. The discipline that avoids this is to first define what adequacy means, independently of any particular rule, and then obtain the rule from that definition. Two properties suffice. A rule is trustworthy when no counterexample can slip past it, and it is maximally informative when anything it rejects genuinely has a counterexample. The second property is the one people skip, and it is the one that distinguishes a rule that captures the construct from a rule that merely fails to lie about it.

Given those criteria, rules stop being inventions. For each construct there is a canonically best answer: the strongest thing you are entitled to conclude on the way out, given what you knew on the way in. Everything you might have written by hand is a consequence of that, so instead of guessing you compute it, and instead of arguing about whether your rule is right you check whether it is the best one. A small number of structural properties then have to hold of the family of rules for the whole language to hang together: joint claims must combine, case analyses must combine, and strengthening what you assume must never weaken what you may conclude. Rules that satisfy those compose; rules that don't will fail the first time two proofs need to be merged.

The general form of this lesson has nothing to do with program semantics. Whenever you are designing a checker, a validator, a type system, a lint rule, or an approximation of any kind, the useful artifact is not the rule but the criterion the rule is answering to. With a criterion you can compare candidate rules, recognize that one is strictly better, and know what you gave up when you weakened one for tractability. Without one, every rule looks defensible and nothing can be improved except by taste.

There is also a floor worth noticing. Adequacy here is relative: the reasoning system can only be as sound and as complete as the underlying logic it is built on. Rules do not manufacture certainty; they transmit whatever certainty their foundation has. That is a good reason to know what your checker's foundation actually assumes.

**Source:** [Assigning Meanings to Programs](../works/assigning-meanings-to-programs.md) — the general axioms section and the derivation of the assignment rule, where consistency and completeness are defined via the existence or absence of counterexamples, the assignment rule is obtained from those criteria rather than posited, and both properties are shown to be inherited from the underlying deductive system.
