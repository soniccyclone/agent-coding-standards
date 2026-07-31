---
type: work
title: "Introduction to Mathematical Logic"
figure: church
description: Church's graduate textbook synthesizing three decades of his own and others' work on the propositional and predicate calculus, formalized languages, and the theory of effective calculability, into a single systematic reference. It's dense and notation-heavy even by the standards of the field, but it's the volume where the lambda-calculus-era results of the 1930s got assembled into a teachable, self-contained logical foundation. Long treated as the standard entry point for formal logic as it bears on computability.
subdomains: [foundations-of-computation]
year: 1956
url: https://archive.org/details/dli.ernet.449121
survey_text_layer: ocr
survey_pages: 378
access: public
host: third-party-rehost
tags: [work]
---

# Introduction to Mathematical Logic

**Venue/year:** Princeton Mathematical Series no. 17, Princeton University Press, 1956 (Volume I; no further volumes were published).
**Source:** https://archive.org/details/dli.ernet.449121 — full freely-downloadable scan (PDF/EPUB/full text, no lending restriction) hosted by the Internet Archive under the Digital Library of India collection.
**Reading copy:** `scratchpad/ocr-text/church__introduction-to-mathematical-logic.txt` — the Internet Archive's own OCR of this scan (167,804 words, high quality: 37% of tokens are common English function words). Read that file rather than the 181MB PDF. This is a full-length textbook, so read it in sequential chunks. As with any OCR, the prose is reliable but the logical notation is not — Church's formalism will not have survived, so ground every lesson in his prose argument about method, not in a formula.

## Lessons
- [Choosing a notation is choosing a theory of the domain, and surface similarity is no evidence of shared structure](../lessons/choosing-a-notation-is-choosing-a-theory.md)
- [Denoting the same thing does not make two expressions interchangeable; substitution has a scope and you must know where it ends](../lessons/same-value-does-not-mean-interchangeable.md)
- [Make checking decidable even when finding is not, or the check itself will need checking forever](../lessons/checking-must-be-decidable-even-when-finding-is-not.md)
- [Whatever stays in the scaffolding was never really formalized, and the finished thing must stand without it](../lessons/whatever-stays-in-the-scaffolding-was-never-formalized.md)
- [Any notation you can actually write in names only countably much, so the expressive ceiling is arithmetic, not a failure of cleverness](../lessons/a-notation-can-only-name-countably-much.md)
- [When a second theory would duplicate the first step for step, collapse the two concepts — then state the law the collapse breaks](../lessons/collapse-the-duplicate-concept-then-name-what-the-collapse-costs.md)
- [Reduction bottoms out at the act of combining, and a regress that reappears one level up is a floor rather than a step](../lessons/reduction-bottoms-out-at-the-act-of-combining.md)
- [Define an operation by its value in every case; the word it is read aloud as is a mnemonic that will import promises the definition never made](../lessons/the-name-is-a-mnemonic-the-table-is-the-definition.md)
- [The order in which you alternate 'for every' and 'there is' is the whole content of a guarantee](../lessons/the-order-of-for-all-and-there-exists-is-the-claim.md)
- [A closed claim admits no degrees: an invariant with a known exception is false, and the exception belongs inside the statement](../lessons/a-closed-claim-admits-no-degrees.md)
- [Analyze only as deep as the argument needs, and remember that which things you treat as atomic is a choice with no canonical answer](../lessons/analyze-only-as-deep-as-the-argument-needs.md)
- [You can buy unconditional downstream laws by totalizing a partial operation with one arbitrary fixed choice, and the bill comes due wherever the filler value is read as an answer](../lessons/totality-by-arbitrary-convention.md)
- [Letting a term stand for itself is safe only when the two readings provably cannot collide, and a quoting mark is not a function from values to names](../lessons/letting-a-term-name-itself-requires-a-no-collision-proof.md)
- [An identity that looks trivially true is usually a relation with a parameter suppressed by convention; vary the parameter and the triviality dissolves](../lessons/a-trivial-looking-identity-hides-a-suppressed-parameter.md)
- [Test every claim against the observer who thinks your system is a game with no meaning, because intended interpretation is never recoverable from the artifact](../lessons/test-a-claim-against-the-observer-who-thinks-it-is-a-game.md)
- [Know whether a definition is eliminable shorthand or a genuine extension, because a definition facility rigorous enough to trust is also one you did not need](../lessons/know-whether-a-definition-is-shorthand-or-an-extension.md)
- [A rule set does not determine its own consequences: the same axioms under a stronger surrounding logic are a different subject entirely](../lessons/the-rules-plus-the-inference-machinery-are-the-theory.md)
- [Every property you claim splits into a tool-relative version and a truth-relative version, and the implication runs only one way](../lessons/every-property-splits-into-tool-relative-and-truth-relative.md)
- [Evidence gathered in a setting that already assumes the claim would persuade nobody who actually doubted it](../lessons/evidence-that-presupposes-the-claim-convinces-nobody.md)
- [Any set of requirements can be a foundation you build inside or a predicate you quantify over, and the second turns every specific result into a general one](../lessons/requirements-as-a-predicate-you-quantify-over.md)
- [Minimizing a basis and factoring it by concern are opposite goals, and only the factored one lets you vary a part](../lessons/minimize-the-basis-or-factor-it-but-know-which-you-chose.md)

_Coverage note: extraction is PARTIAL and `extraction: complete` is deliberately withheld. The Internet Archive text derivative for this volume runs ~1.16 MB (roughly 300k+ tokens), which exceeds a single agent's context, so the volume is being mined across passes._

_Read in full so far: front matter and preface; the **entire Introduction**, sections 00 (logic), 01 (names), 02 (constants and variables), 03 (functions), 04 (propositions and propositional functions), 05 (improper symbols, connectives), 06 (operators, quantifiers), 07 (the logistic method), 08 (syntax), 09 (semantics); Chapter I §11 (definitions); and Chapter V §55 (postulate theory)._

_Not yet read: Chapter I §§10, 12-19; Chapter II §§20-29 (including the §29 historical notes); Chapter III §§30-39; Chapter IV §§40-49 (including §43 validity and satisfiability, §§46-47 on the decision problem, and the §49 historical notes); Chapter V §§50-54 and §§56-59; and all exercise sets. The two historical-notes sections (§29, §49) and §§46-47 are the highest-value remaining prose for a follow-up pass; §§12-14, 20-23, 30-39 and 50-54 are dense formal derivation whose notation did not survive OCR and are correspondingly low-yield. A follow-up pass should resume at line 5774 (§12) of the reading copy, and jump ahead to lines 11906 (§29), 17803 (§46) and 20840 (§49) first._
