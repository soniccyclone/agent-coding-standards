---
type: lesson
title: "Declare which parts of the notation the machine ignores"
figure: naur
works: [revised-report-on-the-algorithmic-language-algol-60]
axes: [cognitive-load, verifiability, expressiveness]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Declare which parts of the notation the machine ignores

**Lesson:** A notation people write in accumulates material meant for other people: whitespace and line breaks, prose set aside from the code, decorative punctuation that reads like a sentence. All of it is worth having, and all of it is dangerous unless the definition says explicitly that it carries no meaning. So partition the surface text once, in the defining document, into the part that determines behaviour and the part that exists purely for readers, and state which side each feature falls on. The point is not tidiness. An inert feature that has never been declared inert will eventually be treated as load-bearing — by a tool that parses it, by a reader who assumes it was checked, by a maintainer who preserves it during a rewrite for fear of breaking something.

Making the declaration precise costs more than making it. Saying that layout is insignificant but may be used freely to aid reading is a sentence. Saying what a bracketed aside means requires giving it as a textual equivalence — this shape may be replaced by that symbol anywhere outside a literal, with no effect on the action — and then resolving the ambiguity that any such rule creates, by fixing that the first matching structure found scanning left to right wins over later ones contained in it. That last clause is the part people skip, and it is the part that decides whether two implementations agree on where a comment ends.

The sharpest case is decoration that looks like a contract. Allowing a call site to interleave descriptive words with its arguments makes calls read like documented English, which is real value; but if the words are not matched against anything, the definition must say so in as many words — that all such separators are equivalent, that nothing beyond their number need correspond between the call and the definition, and that the information conveyed by the elaborate ones is entirely optional. Now the reader knows the words are a comment. Left unsaid, the same feature invites everyone to believe the names are verified, which is worse than not having them, because it converts a helpful convention into a false guarantee. The general rule: any affordance you provide for human readers should be labelled as unchecked at the point you provide it, in the same breath, or people will spend the guarantee you never issued.

**Source:** [Revised Report on the Algorithmic Language ALGOL 60](../works/revised-report-on-the-algorithmic-language-algol-60.md) — the statement in section 2.3 that typographical features such as blank space and new lines carry no significance while remaining free to use for readability, followed immediately by the comment convention given as a table of textual equivalences with an explicit left-to-right precedence for overlapping matches; and section 4.7.7, which declares all parameter delimiters equivalent, requires no correspondence between the call's delimiters and the declaration's beyond their number, and states that the information carried by the elaborate forms is entirely optional.
