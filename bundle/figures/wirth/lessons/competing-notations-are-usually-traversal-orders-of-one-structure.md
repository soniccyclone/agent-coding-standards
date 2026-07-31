---
type: lesson
title: "Competing notations are usually traversal orders of one structure"
figure: wirth
works: [algorithms-and-data-structures]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [programming-languages-and-semantics, algorithms-and-complexity]
tags: [lesson]
---
# Competing notations are usually traversal orders of one structure

**Lesson:** When a family of notations argue about which is natural, the productive move is to stop comparing them to each other and ask what structure they are all flattening. A branching structure has only a few sensible ways to be walked as a single sequence — the branch point can be emitted before its parts, between them, or after them — and each choice, applied uniformly, produces one of the notations. Once you see that, the notations stop being rival conventions and become projections of one object, which means every argument about them is really an argument about which flattening loses what.

That reframing gives a criterion sharper than taste. Ask of each order: can the original structure be recovered from the sequence alone? Emitting the branch point first, or last, keeps the correspondence unambiguous, because the position of the connective determines where its parts begin and end. Emitting it in the middle does not — the sequence admits more than one reconstruction — so that order needs auxiliary machinery bolted on to restore what the flattening discarded: grouping marks, and a table of binding strengths so that grouping marks can be omitted in common cases. The everyday notation is therefore the one that costs the most to make unambiguous, and the exotic-looking ones are the cheap ones. Familiarity, not economy, is what recommends the middle order, and that is a legitimate reason to choose it as long as nobody mistakes it for a technical one.

Generalize the criterion, because it applies well beyond arithmetic. Any time you serialize a structure — a wire format, a log line, a configuration syntax, a printed representation for humans — you are choosing a traversal, and the question to ask before arguing about delimiters is whether the traversal you picked is injective. If it is not, you will spend the rest of the design adding disambiguating apparatus, and every consumer of the format will need to implement that apparatus correctly. The apparatus is not part of the data; it is the price of a flattening that threw information away. Choose the order first, and let the delimiters be whatever the order genuinely requires.

**Source:** [Algorithms and Data Structures](../works/algorithms-and-data-structures.md) — section 4.4.2's three principal orderings for visiting the nodes of a binary tree, defined recursively by the position of the root relative to its two subtrees, applied to the tree representation of an arithmetic expression from section 4.4.1, and the accompanying identification of the resulting sequences as prefix, postfix and conventional infix notation, with the explicit note that the infix result lacks the parentheses necessary to clarify operator precedences.
