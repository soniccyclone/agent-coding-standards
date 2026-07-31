---
type: lesson
title: "Give nothing a name, then route every degenerate case to it"
figure: naur
works: [revised-report-on-the-algorithmic-language-algol-60]
axes: [primitive-count, verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Give nothing a name, then route every degenerate case to it

**Lesson:** Absence is the case that designs get wrong, because it is usually described rather than constructed. The fix is cheap and structural: before defining anything else, define the empty thing as a named object of your system — a category whose sole member is the null sequence — and afterwards never say "this part may be omitted." Say instead that this part is either the thing or the empty thing. Optionality then stops being a property of the notation that tools must special-case and becomes an ordinary alternative that the same machinery already handles. Every place that would have needed an "if present" branch gets one uniform treatment, and the count of constructs does not grow when you add a fourth or fifth optional position.

Then do the same one level up, at the level of behaviour. Define an operation that does nothing, whose body is exactly that empty object, and note the one thing it is nonetheless useful for — it gives you a place to attach a name. Now every degenerate outcome elsewhere in the system can be specified by declaring it equivalent to that operation rather than by explaining, differently each time, that nothing happens. A transfer of control whose target came out undefined is that operation. A multi-way choice where no guard held is that operation. Each of those is one sentence, and each of those sentences says the same thing, which is why a reader can trust that all the degenerate paths agree with each other.

What you gain is totality where you would otherwise have holes. Neither of those degenerate cases becomes an error condition, a trap, or an implementation liberty; each has a defined, minimal, composable meaning, so a program that reaches one keeps running with semantics you can still reason about. That is the general form of the trick, and it transfers well past language design: pick the identity element for whatever you are combining — the no-op action, the empty collection, the unit of the monoid — make it a first-class value with a name, and define the edges of every operation by mapping them onto it. The alternative is a scattering of prose about what does not happen, which is exactly the material that rots first, because nothing in the system depends on any two such sentences being consistent.

**Source:** [Revised Report on the Algorithmic Language ALGOL 60](../works/revised-report-on-the-algorithmic-language-algol-60.md) — the definition of the empty category as the null string of symbols at the close of section 1.1, and its subsequent use to make the actual and formal parameter parts, the value part and the specification part optional without extra rules; the dummy statement of section 4.4 defined as that empty category with its stated use as a site for a label; and the reduction to it of the undefined switch target in 4.3.5 and of a conditional statement none of whose guards holds in 4.5.3.2.
