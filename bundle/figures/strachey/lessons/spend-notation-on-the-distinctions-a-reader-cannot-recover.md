---
type: lesson
title: "Spend notation on the distinctions a reader cannot recover"
figure: strachey
works: [continuations-a-mathematical-semantics-for-handling-full-jumps]
axes: [cognitive-load, verifiability]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Spend notation on the distinctions a reader cannot recover

Any description of a language is written in a second language, and the two are in play simultaneously on every line. That situation invites a specific and quiet class of error: reading a symbol at the wrong level, taking a piece of the thing being described for a piece of the description. Strachey and Wadsworth treat the level boundary as the one distinction that gets a permanent mark. Program text always sits inside a dedicated pair of brackets, and those brackets survive even in their most abbreviated formulae — where they have thrown away grouping for function application and the brackets that would show how a chain of applications associates, on the grounds that a reader who knows the convention can put those back unaided.

That is the discriminator, and it is more useful than any particular convention. Some of what notation carries is recoverable: association, precedence, the argument grouping of an application, anything a stated rule reconstructs mechanically. Marking those explicitly is noise, and noise is not free — long formulae stop being read at all. Some of what notation carries is not recoverable, because getting it wrong yields something that still looks well-formed. Which level a symbol belongs to is exactly that kind of distinction, so it gets the ink, and it keeps the ink under abbreviation. The same reasoning motivates the rest of their scheme: a variable's sort is fixed by which letter it is, semantic functions get their own typeface, and a construct whose role is easy to lose in a crowded line gets its own delimiters. All of that is redundant encoding, deliberately, so a reader can check a line locally instead of holding a table of declarations in their head.

The reason this rises above typographic fussiness is that it is a claim about where mistakes come from. In work that spans two levels, the errors are rarely arithmetic; they are confusions of category that the eye slides past because nothing on the page marks the seam. A notation that makes the seam visible turns a whole class of error into something you can see rather than something you have to remember not to make. Whether the notation is beautiful is beside the point — whether it fails loudly is not.

Programmers face the same choice constantly and usually make it by accident. Interpolating a query or a command line, generating code from a template, writing a macro that mixes what happens now with what happens later, threading a configuration value that will be substituted somewhere else — in every case there are two levels and something must show which is which. The move is to identify the distinction whose violation would still look plausible, spend your one durable convention there, and let everything that a rule can reconstruct go unmarked.

**Source:** [Continuations: A Mathematical Semantics for Handling Full Jumps](../works/continuations-a-mathematical-semantics-for-handling-full-jumps.md) — the introduction of the double text brackets as a device to separate program text from the surrounding value-domain expressions, the passage on minimally bracketed form where association and application brackets are dropped but the text brackets are explicitly always retained, and the appendix's statement of notational discipline in which letter, typeface and bracket choices are assigned so that a symbol's nature is determined by its appearance.
