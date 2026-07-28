---
type: work
title: "Go at Google: Language Design in the Service of Software Engineering"
figure: pike
description: Pike's account of why Go looks the way it does, framing the language as a response to software-engineering problems Google hit at scale — slow builds from deep dependency graphs, unreadable code from unconstrained abstraction, and the difficulty of writing reliable concurrent network services — rather than as a language-theory exercise. It argues that Go's comparatively small, orthogonal feature set (no generics at the time, structural interfaces, built-in CSP-style goroutines and channels) is a deliberate engineering trade-off favoring compile speed, legibility, and large-codebase maintainability over expressive power. Added beyond the Phase 1/2 stub: Go is one of the two achievements named in Pike's "why a candidate" case but had no representative work in the original top-10 list.
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
year: 2012
url: https://go.dev/talks/2012/splash.article
extraction: complete
access: public
host: institutional
tags: [work]
---

# Go at Google: Language Design in the Service of Software Engineering

**Venue/year:** Expanded from a keynote at SPLASH 2012 (Tucson, AZ, October 25, 2012); published as an essay on the Go project site.
**Source:** https://go.dev/talks/2012/splash.article — live page, hosted on go.dev, the official Go programming language project site.

## Lessons
- [Design against the costs you measured, not the feature checklist](../lessons/design-against-the-costs-you-measured-not-the-feature-checklist.md)
- [An annoyance now beats a decision deferred forever](../lessons/an-annoyance-now-beats-a-decision-deferred-forever.md)
- [Let structure be discovered rather than committed up front](../lessons/let-structure-be-discovered-rather-than-committed-up-front.md)
- [Mechanical analyzability is what buys the right to change your mind](../lessons/mechanical-analyzability-is-what-buys-the-right-to-change-your-mind.md)
- [Weigh a reuse's dependency price against copying](../lessons/weigh-a-reuses-dependency-price-against-copying.md)
