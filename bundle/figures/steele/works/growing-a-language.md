---
type: work
title: "Growing a Language"
figure: steele
description: Steele's 1998 OOPSLA keynote arguing that a well-designed language should ship with a small primitive core and let its own users extend it toward domain-specific vocabulary, rather than trying to anticipate every feature up front. The talk performs its own argument stylistically, restricting itself to short English words unless a longer one is first "defined" on stage, mimicking how a minimal language bootstraps new terms from old ones.
subdomains: [programming-languages-and-semantics]
year: 1998
url: https://homepages.inf.ed.ac.uk/wadler/gj/Documents/steele-oopsla98.pdf
extraction: complete
survey_pages: 14
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: third-party-rehost
tags: [work]
---

# Growing a Language

**Venue/year:** ACM OOPSLA '98 keynote; later published in Higher-Order and Symbolic Computation 12(3), October 1999, pp. 221-236 (paywalled at the publisher).
**Source:** https://homepages.inf.ed.ac.uk/wadler/gj/Documents/steele-oopsla98.pdf — course-reading mirror hosted on Philip Wadler's University of Edinburgh faculty page; the original OOPSLA/Kluwer venues are paywalled, so this is used as the public copy.

## Lessons
- [Small loses to real needs and large loses to the clock, so design the pattern for growth and hand the growing to your users](../lessons/design-the-pattern-for-growth-rather-than-the-artifact.md)
- [If what users add is distinguishable from what was built in, they will stop adding; the seam is what kills extensibility](../lessons/user-added-vocabulary-must-be-indistinguishable-from-the-builtin-kind.md)
- [When every feature request is individually justified and collectively impossible, the requests are a family and you should ship its generator](../lessons/when-requests-form-a-family-ship-the-generator-not-the-members.md)
- [Shipping a known compromise is fine; the design work is making it removable, and an omission is a compromise too](../lessons/design-your-compromises-so-they-can-be-removed-later.md)
- [Every term you introduce has a price you normally cannot feel, and anyone writing a large program is designing a language whether they admit it or not](../lessons/every-new-term-has-a-price-and-writing-a-large-program-is-language-design.md)
