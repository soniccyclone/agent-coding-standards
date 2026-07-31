---
type: lesson
title: "A rule cluttered with conditions about substitution should be restated over a function instead"
figure: reynolds
works: [the-craft-of-programming]
axes: [primitive-count, cognitive-load]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# A rule cluttered with conditions about substitution should be restated over a function instead

**Lesson:** When a rule is stated over syntactic patterns, the awkward parts of it are almost always bookkeeping about *where things get plugged in*: which occurrences count, which are of the right kind, which names must not be captured, what the free identifiers of the result are. Each rule that does its own plugging-in carries its own copy of these conditions, and they accumulate until the collection is unreadable. The fix is not to simplify each rule but to remove the plugging-in from the rules altogether. Restate the rule with a variable standing for the *function* that was previously expressed by "the pattern with a hole in it," and the rule shrinks to its actual content. The general form is then recovered by supplying an anonymous function and letting one mechanism — application, reduction, whatever your setting calls it — perform the substitution that every rule used to perform for itself.

The economics of this are the same as any factoring. One mechanism is defined once, argued about once, and got right once; the rules that were formerly complicated become instances that you derive rather than statements you must trust. It also relocates the difficulty honestly: substitution really is subtle, so having exactly one place where its subtleties live is much better than having them replicated in a dozen conditions that are individually easy to state slightly wrong. The rules that survive this treatment are noticeably closer to being what you would say in words.

There is a further gain that is easy to miss. Once the abstracted form exists, properties you previously had to assume can turn out to be equivalent to the rule rather than prior to it — the condition that makes an object well-behaved and the rule that governs operating on it become interderivable, so you can take either as the definition. That is a sign you have found the right level of abstraction rather than merely a tidier notation. The practical instruction: whenever a rule's side conditions are longer than its statement, look for the parameter that the conditions are secretly describing, make it explicit, and let one general mechanism do the work that the side conditions were regulating.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 3.3.12 on abstract specification logic, which observes that once lambda expressions with beta reduction are available the logic simplifies significantly because abstract axioms can replace the more complicated inference rules, with much of the complexity encapsulated in the reduction mechanism; the abstract assignment axiom stated over an assertion-procedure identifier and the derivation of the earlier assignment rule from it by substituting a lambda expression and reducing, so that the earlier rule's list of non-interference conditions falls out of right-side decomposition instead of being stipulated; and the pairing of that axiom with its converse, from which the good-variable property and the assignment rule are shown to be equivalent.
