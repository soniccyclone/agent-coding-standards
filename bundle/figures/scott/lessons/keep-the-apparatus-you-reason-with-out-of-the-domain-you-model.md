---
type: lesson
title: "Keep the apparatus you reason with out of the domain you are modeling"
figure: scott
works: [a-type-theoretical-alternative-to-iswim-cuch-owhy]
axes: [cognitive-load, expressiveness, primitive-count]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Keep the apparatus you reason with out of the domain you are modeling

**Lesson:** Any serious treatment of data ends up with two kinds of type in play, and confusing them is the first mistake available. One kind belongs to the subject: the sorts of thing your system actually holds and manipulates, each with its own operations. The other kind belongs to the study: function spaces, powersets, higher-order functionals, whatever machinery you need in order to state and prove things about the first kind. The second kind is not data. A powerset or a third-order functional never shows up as a value in the system; it exists so that you can say something like "no proper subcollection of the values is closed under this operation." Once you notice the distinction, the discipline is to keep every derived construction on the side of the ledger it came from — the modeling apparatus grows as freely as you like without any of it becoming a thing the system claims to contain.

The reason to enforce this rather than let it blur is that a model of an object is not the object, and identifying them silently imports the model's structure as if it were the subject's. An organization is a tree of people; a mathematical tree is a set with an ordering. Nothing forces the organization to have exactly the parts that the set-plus-ordering encoding has, and if you conflate them you will find yourself reasoning about artifacts of the encoding. The same gap appears between an expression and the string of symbols it happens to be written as: string-oriented decomposition gives you *a* notion of part, and it need not be the notion of part that matters. Modeling something is fine and unavoidable. Forgetting which side of the model you are standing on is what produces conclusions about your representation that you mistake for conclusions about the thing.

There is a second-order observation worth carrying. A framework can arrange for its type structure to live inside the objects themselves rather than in the notation, so that nothing has to be declared and every object carries its own rank — the checking, in effect, happens when the object is used rather than when it is written. This buys real convenience, and it costs vigilance: a constraint that is nowhere visible is a constraint people stop consulting, even though it still binds and still makes their arguments valid or invalid. Structure kept out of sight gets forgotten, so if you choose to hide it you take on the job of periodically making it explicit again.

**Source:** [A Type-Theoretical Alternative to ISWIM, CUCH, OWHY](../works/a-type-theoretical-alternative-to-iswim-cuch-owhy.md) — Section 1's opening insistence that logical types are what we invoke in order to study data types, with the organizations-as-trees and abstract-versus-concrete-syntax examples; the conclusions section, which holds the line by keeping all data at the lowest type and treating higher functionals as purely logical; and the introduction's aside on set theory's type discipline being carried by the objects rather than the formalism, with the accompanying warning that people forget what is out of sight.
