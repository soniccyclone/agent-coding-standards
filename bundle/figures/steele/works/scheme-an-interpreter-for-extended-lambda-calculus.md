---
type: work
title: "Scheme: An Interpreter for Extended Lambda Calculus"
figure: steele
description: The founding memo of Scheme, written as an MIT AI Lab report while Steele and Sussman were investigating actor-model semantics. It gives Scheme's first reference manual and a self-hosted interpreter, and is the document where lexical closures over the definition environment (rather than the calling environment) first appear as a working language feature. The lambda calculus is extended with side effects and multiprocessing primitives while staying close to its substitution semantics.
subdomains: [programming-languages-and-semantics, foundations-of-computation]
year: 1975
url: http://web.archive.org/web/20260425080506/https://dspace.mit.edu/handle/1721.1/5794
access: public
host: institutional
tags: [work]
---

# Scheme: An Interpreter for Extended Lambda Calculus

**Author(s):** Gerald Jay Sussman, Guy L. Steele Jr.
**Venue/year:** MIT AI Lab Memo AIM-349, December 1975.
**Source:** http://web.archive.org/web/20260425080506/https://dspace.mit.edu/handle/1721.1/5794 — Wayback Machine snapshot of the MIT DSpace record (dspace.mit.edu/handle/1721.1/5794); the live DSpace host currently answers automated requests with an AWS WAF bot challenge, so the snapshot is used as the verified-resolving link. A community transcription with the same source PDF also exists at research.scheme.org/lambda-papers/.

## Lessons
- [Judge a control structure by how its state grows, not by whether the code appears to call itself](../lessons/iteration-is-a-property-of-reduction-shape-not-of-syntax.md)
- [You cannot implement a mechanism more general than the host mechanism you borrowed to implement it](../lessons/never-inherit-the-mechanism-you-are-trying-to-generalize.md)
- [Pick the binding rule that keeps your reasoning laws true, then check the cost model before believing it is expensive](../lessons/choose-the-binding-rule-that-keeps-your-reasoning-laws-true.md)
- [A model that works by copying can never express sharing, so its blind spots tell you which features are really primitive](../lessons/a-semantic-model-that-copies-cannot-express-sharing.md)
- [When two camps' concepts look different, implement both in one substrate and see whether they collapse](../lessons/test-whether-two-concepts-are-the-same-by-implementing-both.md)
