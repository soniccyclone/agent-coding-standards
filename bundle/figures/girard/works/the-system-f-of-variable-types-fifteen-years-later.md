---
type: work
title: "The System F of Variable Types, Fifteen Years Later"
figure: girard
description: A retrospective, English-language survey of System F written fifteen years after Girard's original 1972 thesis introduced it, aimed at making the system's semantics accessible outside the French proof-theory tradition it came from. It reworks the denotational semantics of variable (polymorphic) types using the category-theoretic notion of a direct limit, showing that a type's behavior over any domain is pinned down by its behavior on finite approximations, which sidesteps the apparent circularity of quantifying over all types including itself. It became the standard English-language reference point many later programming-language treatments of System F cite instead of the original French thesis.
subdomains: [programming-languages-and-semantics, foundations-of-computation]
year: 1986
url: https://web.archive.org/web/20240913204718/https://core.ac.uk/download/pdf/82258639.pdf
extraction: complete
access: public
host: third-party-rehost
tags: [work]
---

# The System F of Variable Types, Fifteen Years Later

**Venue/year:** Theoretical Computer Science 45, pp. 159-192, 1986.
**Source:** https://web.archive.org/web/20240913204718/https://core.ac.uk/download/pdf/82258639.pdf — Wayback Machine snapshot (Sept 2024) of a direct-download PDF aggregated by CORE, the open-access repository harvester; CORE's own domain currently sits behind a Cloudflare bot challenge that blocks direct fetches, so the live copy is cited via its archived snapshot per the Wayback-fallback rule. Not on Girard's own self-archive list (Archives.html covers 1972 onward but omits this title), and the ScienceDirect/TCS copy is paywalled.

## Lessons
- [When a definition seems to require the whole universe, look for the uniformity constraint that makes the finite cases decide everything](../lessons/kill-circularity-with-a-uniformity-constraint.md)
- [An account that begins by erasing the feature has not explained it — and the leftover mismatch is where your next design decision hides](../lessons/an-account-that-erases-the-feature-explains-nothing.md)
- [If every instance of a choice is arbitrary, abstract over the choice and study what survives all of them](../lessons/promote-the-arbitrary-choice-to-a-parameter.md)
- [Trace every complication in an inherited framework back to the single decision that forces it, then check whether that decision was ever justified](../lessons/trace-inherited-complexity-to-the-one-decision-that-forces-it.md)
- also contributes to [Suspect your most familiar primitive of being a composite, and let a semantics that disturbs you go looking for the seam](../lessons/suspect-that-your-primitives-are-composites.md)
