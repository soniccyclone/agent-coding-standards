---
type: lesson
title: "When an abstraction fails in practice, suspect that the information was attached to the wrong thing at the wrong granularity"
figure: steele
works: [common-lisp-the-language-2nd-edition]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# When an abstraction fails in practice, suspect that the information was attached to the wrong thing at the wrong granularity

**Lesson:** The original design gave every character object two extra attributes beyond its identity: a numeric style indicator and a set of modifier flags. Five years of use later, this edition performs a public post-mortem, and the diagnosis is precise about *why* it failed rather than merely that it did. Two reasons are given for the style attribute. First, a small integer is simply not an adequate description of a typeface — the real thing wants a family name, a variant, and a size. Second, and more interesting, style information in practice applies to runs of characters rather than to individuals, so encoding it per character is fighting the shape of the data; systems that need it find it more convenient and more efficient to represent style as mode changes spanning many characters. Neither defect is fixable by improving the interface. Both are consequences of having decided which object carries the information.

The generalisable point is that when a well-implemented abstraction stubbornly fails to get used, the productive question is not "what is wrong with the API?" but "is this fact a property of the object I attached it to?" A property attached too finely is redundantly duplicated and expensive; attached too coarsely it cannot express the cases that matter; attached to the wrong entity entirely it will be routinely bypassed by users who reconstruct the information somewhere else. The post-mortem gets at this by asking, for each attribute, whether the data naturally varies at the same rate as the object it is stored on — and the modifier-flag attribute survives the analysis better than the style attribute precisely because a modifier really is a property of one keystroke.

What the specification does with the diagnosis is as instructive as the diagnosis. Rather than deleting the attributes outright or defending them, it demotes them: the two named, standardised attributes become a general notion of implementation-defined attributes, with rules constraining how existing operations must treat whatever an implementation chooses to put there. The mechanism survives, the specific commitments do not. The author then goes on record with a prediction about which half will die and which will persist as an unofficial extension because it serves a small real purpose. Predicting differential survival is a stronger claim than "we got this wrong," and it is only possible because the failure was diagnosed structurally.

A designer who has internalised this reacts to a low-adoption abstraction by re-examining its carrier before its surface. Is this a field on the row or a property of the batch? A per-request setting or a per-connection one? A per-file attribute or a per-directory one? Getting the carrier wrong produces exactly the symptom pattern seen here: the feature works, nobody objects to it, and everybody quietly builds their own version at the granularity they actually needed.

**Source:** [Common Lisp the Language, 2nd Edition](../works/common-lisp-the-language-2nd-edition.md) — the retrospective passage in the characters chapter assessing the font and bits attributes, its two stated reasons for the font attribute's failure, and the replacement of both by a constrained notion of implementation-defined attributes together with the prediction about which will survive.
