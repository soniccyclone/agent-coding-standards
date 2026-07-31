---
type: lesson
title: "A unique representation turns a property into arithmetic"
figure: schonfinkel
works: [entscheidungsproblem-der-mathematischen-logik]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [formal-methods-and-verification, foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# A unique representation turns a property into arithmetic

Ordinary normal forms are not unique: the same statement has many equivalent conjunctive forms, which is fine for checking a criterion and useless for indexing. So the authors impose extra demands until uniqueness is forced — every clause must be built from the full list of available atoms, each atom appearing either plain or negated, and no clause may repeat. Now a formula is determined by which clauses are present out of a fixed, enumerable set of possibilities. That determination can be written as a table of zeros and ones, one entry per possible clause. Uniqueness is what makes the table well defined, and the table is what makes the next step available.

With formulas represented as coefficient tables, the conditions for validity stop being statements about syntax and become equations about numbers. Expanding a disjunction of these forms distributively obeys the ordinary rules of algebra, and the requirement that every resulting clause contain some atom at both polarities translates into a family of equations saying that certain products of coefficients must vanish — indexed products, one family per cycle length. The decision procedure is then a matter of computing coefficients from the input formula and checking whether the equations hold.

The payoff is larger than a faster test. Because the conditions are equations over the representation rather than tests applied to a candidate, they characterize the entire set of formulas with the property, not merely classify the one in front of you. You can ask which coefficient systems satisfy the constraints and read off the answer as a description of every valid formula of that type — which the paper does, working out the single-relation case completely and finding that only two clause shapes are possible. A generative description of the solution set is a strictly stronger asset than a recognizer for it.

The lever, for anything you build, is that this all rests on making the representation canonical first. Non-canonical representations force you to compare by semantics, which usually means search. Canonical ones let equality be identity, membership be a lookup, and structural properties become computations over an index — interned symbols, hash-consed terms, sorted normalized keys, and de Bruijn-indexed terms all buy the same thing. It is worth paying to canonicalize, including paying in extra conditions that feel arbitrary at the time, because the properties you want to decide afterwards frequently turn into arithmetic once the representation stops being ambiguous.

**Source:** [Zum Entscheidungsproblem der mathematischen Logik](../works/entscheidungsproblem-der-mathematischen-logik.md) — section 2's construction of the distinguished conjunctive normal form made unique by requiring full-length clauses without repetition, and section 4's encoding of that form as a system of zero-one coefficients whose vanishing products express the necessary and sufficient conditions for validity, worked out explicitly for a single relation symbol.
