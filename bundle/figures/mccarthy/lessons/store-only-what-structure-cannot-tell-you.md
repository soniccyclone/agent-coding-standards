---
type: lesson
title: "Store only what the structure of a thing cannot already tell you, and treat every stored derivable fact as a cost decision you must justify"
figure: mccarthy
works: [programs-with-common-sense]
axes: [expressiveness, cognitive-load]
subdomains: [databases-and-data-management, programming-languages-and-semantics]
tags: [lesson]
---
# Store only what the structure of a thing cannot already tell you, and treat every stored derivable fact as a cost decision you must justify

**Lesson:** McCarthy proposes a criterion for whether something in a system deserves an attached record at all, and the criterion is sharper than most data modelling advice written since. A thing earns its own entry only if there is something to say about it beyond what follows from the form of its name. He illustrates with two numerals: one of them is merely a number, everything true of it being computable from its digits, while the other has an unrelated historical fact filed against it that no amount of staring at its structure would ever produce. The first needs no record. The second does. Applied to programs, the question becomes: for each attribute you are about to persist, is it a function of what you already hold, or is it genuinely new information that entered from outside? Only the second kind is data.

The criterion then admits a carefully bounded exception, and the boundary is the interesting part. Derivable facts may be stored anyway, but only when the derivation was actually performed and turned out expensive enough that the system does not want to repeat it. That makes caching an explicit, cost-justified deviation from the rule rather than the default habit, and it clarifies what you are taking on: every stored derivable fact is a second source of truth that can now disagree with the first. If the derivation was cheap you have accepted that risk for nothing.

The complement of the rule appears in McCarthy's reply to his critics, where he defends omitting the obvious-looking reachability facts from his example. If there are some number of known locations, the family of pairwise statements about getting from one to another grows as the square, and nobody carries that in their head, so a system that started with them pre-loaded would be cheating rather than reasoning. The general form: when instances of a relation grow combinatorially in the size of your domain, the relation must be represented as a rule and computed on demand, because enumeration is not merely wasteful but a different and weaker design pretending to be the same one. A rule states the whole family at once, which is what makes it more expressive than any finite prefix of the family it generates.

A programmer who holds this line asks of every field whether it is input or output, and keeps outputs out of the store unless a measured cost says otherwise. They spot the quadratic-blowup shape early, since a table whose rows are pairs drawn from a growing set is the signal to write the predicate instead. And when they do cache, they say so, name what the cache is derived from, and expect to answer for how it stays consistent.

**Source:** [Programs with Common Sense](../works/programs-with-common-sense.md) — the construction section's definition of when an entity warrants a property list, contrasting a numeral with nothing to say about it against one carrying externally supplied significance, along with the accompanying allowance for recording hard-won derived results; and McCarthy's closing reply, which argues from the square-law growth of pairwise reachability statements that such facts must not be pre-loaded.
