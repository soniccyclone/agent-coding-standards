---
type: work
title: "Fast Pattern Matching in Strings"
figure: knuth
description: Introduces what became known as the Knuth-Morris-Pratt algorithm, which finds every occurrence of a pattern inside a text in time proportional to the combined length of both, without ever backing up over already-scanned input. The trick is a precomputed "failure function" on the pattern itself that tells the matcher exactly how far it can safely resume after a mismatch. It's a staple example in algorithms courses for showing that amortized-linear behavior can come from cheap preprocessing rather than clever data structures.
subdomains: [algorithms-and-complexity]
year: 1977
url: https://www.cs.jhu.edu/~misha/Spring23/Knuth77.pdf
extraction: complete
survey_pages: 28
survey_text_layer: full
survey_fetch_mb: 2
access: public
host: third-party-rehost
tags: [work]
---

# Fast Pattern Matching in Strings

**Author(s):** with James H. Morris, Jr. and Vaughan R. Pratt
**Venue/year:** SIAM Journal on Computing 6(2), June 1977, pp. 323-350
**Source:** https://www.cs.jhu.edu/~misha/Spring23/Knuth77.pdf — third-party rehost (course-page mirror hosted by Johns Hopkins CS, live PDF, verified HTTP 200). Original SIAM version is paywalled.

## Lessons
- [Find the state that makes already-consumed input unnecessary, and a scan becomes a stream](../lessons/find-the-state-that-makes-the-consumed-input-unnecessary.md)
- [When a method needs a table about its own input, try computing it by running the method against itself](../lessons/preprocessing-should-be-the-method-applied-to-itself.md)
- [Write the form you can prove, then transform it into the form that runs — they are different artifacts of one algorithm](../lessons/write-the-provable-form-first-then-transform-it.md)
- [Think in the most spartan formalism the problem fits, and let a general theorem generate the concrete algorithm](../lessons/think-in-the-most-spartan-formalism-that-fits.md)
- [An incremental algorithm is licensed by an algebraic property of its domain, not by the plausibility of its steps](../lessons/an-incremental-algorithm-is-licensed-by-an-algebraic-property-not-by-plausibility.md)
- [How much history to keep is the design variable — deliberate forgetting is legitimate, and its price is paid in the proof](../lessons/how-much-history-to-keep-is-the-design-variable-and-forgetting-is-legitimate.md)
- [Comprehensibility is an operational property: code your colleagues cannot reconstruct gets repaired into rubble](../lessons/comprehensibility-is-an-operational-property-of-subtle-code.md)
- [A theoretical weakness is a hypothesis about your inputs — measure whether it bites before building the machinery that fixes it](../lessons/a-theoretical-weakness-is-a-hypothesis-about-inputs-measure-before-you-fix-it.md)
