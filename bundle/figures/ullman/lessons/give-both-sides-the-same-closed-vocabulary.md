---
type: lesson
title: "Give both sides the same closed vocabulary and the matching problem dissolves"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [databases-and-data-management, programming-languages-and-semantics]
tags: [lesson]
---
# Give both sides the same closed vocabulary and the matching problem dissolves

**Lesson:** Two ways of connecting supply to demand are put side by side and the second one is easy to walk past. The first is the obvious one: let both parties write free text, build an inverted index over the words, and return the entries containing all the query's words. The second is to have the supplier describe the item by choosing from fixed menus, store those choices as structured fields, and then give the demander the same menus to search with. The second design does not have a better matching algorithm than the first. It has removed the matching problem, because both sides are now drawing symbols from one enumerated set and equality is exact.

The load-bearing detail is that the same vocabulary is presented on both sides. A controlled vocabulary imposed only on the supplier is a schema, and it still leaves the demander typing free text that has to be mapped onto it, which is the original problem relocated. Presenting the identical menu to both parties means the mapping happens once, in the interface, at the moment a human who knows what they mean is choosing. Every ambiguity that a matching algorithm would have had to resolve statistically and imperfectly is instead resolved by the person who actually holds the answer, at a cost of one click. Nothing downstream has to guess.

What you pay is expressiveness, and the payment is real. Anything not on the menu cannot be said, which excludes the unanticipated, the newly invented, and the idiosyncratic. That makes the design a question about the domain rather than a question about technique: it fits where the space of meaningful descriptions is genuinely closed and stable, and it fails where the interesting cases are the ones nobody enumerated. The reason to state the tradeoff this way is that the choice is usually made by default in the direction of free text, on the grounds that free text is more general, without anyone pricing the permanent ambiguity that generality buys.

The reflex worth acquiring is to check, before building a similarity measure or a fuzzy matcher, whether the two sides could have been made to speak the same finite language in the first place. Search filters, issue labels, error taxonomies, product attributes, configuration options, and API enums are all instances. A fuzzy matcher over free text is often the expensive repair for a vocabulary decision that was never made.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 8's section on direct placement of ads, which contrasts using an inverted index of words against asking the advertiser to specify parameters from pull-down menus so that only clearly understood terms can be used, and notes that queryers can use the same menus of terms in their queries.
