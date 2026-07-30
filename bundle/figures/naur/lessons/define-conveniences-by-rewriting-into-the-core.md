---
type: lesson
title: "Define every convenience by rewriting it into the core you already defined"
figure: naur
works: [revised-report-on-the-algorithmic-language-algol-60]
axes: [primitive-count, expressiveness, verifiability]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Define every convenience by rewriting it into the core you already defined

**Lesson:** Most constructs in a designed system are conveniences: they exist because a common pattern deserves a short spelling, not because they add power. For each of those, the honest definition is a rewriting into constructs already defined, exhibited concretely rather than described. Give the loop's meaning as a short program made of assignment, test and jump. Give the abbreviated alternative's meaning as the full alternative with a constantly true guard. Give the comment convention as a textual equivalence with an explicit left-to-right precedence for overlapping matches. The reader who wants to know what a construct does reads a program they can already read, and the implementer who wants to know whether their translation is right has an oracle instead of an interpretation.

The technique extends past pure syntax through the device of the deliberate fiction: an as-if construction stated in the system's own vocabulary, introduced solely to make a rule reduce to rules that already exist. Argument passing by value is explained by imagining an extra enclosing scope containing local copies, so the visibility of those copies needs no new rule — it is the scope rule you already wrote. Evaluating an index is explained as an assignment to an imaginary variable of the appropriate type, so the coercion and rounding rules need not be restated. Argument passing by textual substitution is explained as literal replacement of names by argument text, with a stated renaming discipline for the collisions that replacement creates. In every case the new construct costs one paragraph instead of a fresh semantic apparatus, because the apparatus is reused.

What makes this discipline pay is that it forces you to know what your core actually is, and to keep it small enough that everything else can be pushed through it. The constructs that resist rewriting are exactly the ones carrying real semantic weight, and they are then visible as a short list you can afford to examine hard. The constructs that rewrite easily are proven to be free: they cannot introduce inconsistency, because they introduce nothing. The cost is that the rewriting must be exact and not merely suggestive, and a rewriting stated in terms the reader can execute is where inexactness gets caught. If you cannot write the equivalent program, you do not yet know what the construct means.

**Source:** [Revised Report on the Algorithmic Language ALGOL 60](../works/revised-report-on-the-algorithmic-language-algol-60.md) — the definition of the iteration list elements in 4.6.4.2 and 4.6.4.3 by equivalent programs, the comment conventions in section 2.3 given as textual equivalences with a precedence rule, the reduction of a bare alternative branch to a guarded one in 3.3.3 and 4.5.3.2, the fictitious enclosing block for value parameters in 4.7.3.1, the fictitious index variable in 3.1.4.2, the substitution and renaming account of name parameters in 4.7.3.2 and 4.7.3.3, and the equivalence given for automatic type transfer in 4.2.4.
