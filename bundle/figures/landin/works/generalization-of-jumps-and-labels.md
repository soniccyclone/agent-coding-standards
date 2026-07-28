---
type: work
title: "A Generalization of Jumps and Labels"
figure: landin
description: Landin generalizes the goto-and-label pair into the "J operator," a functional value that captures where a computation should resume — a direct ancestor of the first-class continuation. The paper shows that unrestricted jumps, usually seen as the antithesis of clean functional programming, can be given a purely functional treatment once "the place to jump to" is reified as an ordinary value that can be passed around and invoked. It circulated for decades as an internal UNIVAC report before being formally reprinted, and later papers (e.g. "A Rational Deconstruction of Landin's J Operator") still treat it as the reference point for reasoning about control-flow operators.
subdomains: [programming-languages-and-semantics]
year: 1965
url: https://www.math.bas.bg/softeng/bantchev/place/iswim/j.pdf
survey_pages: 19
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: third-party-rehost
tags: [work]
---

# A Generalization of Jumps and Labels

**Venue/year:** Originally a UNIVAC Systems Programming Research report (1965); reprinted in Higher-Order and Symbolic Computation 11(2), December 1998, pp. 125-143.
**Source:** https://www.math.bas.bg/softeng/bantchev/place/iswim/j.pdf — hosted on a personal ISWIM-history page under the Bulgarian Academy of Sciences' Institute of Mathematics and Informatics domain. Confirmed via decompressed PDF content: the file's reference list cites Landin's other papers by correct title/year/page-range (matching this corpus's other entries), and its embedded CreationDate (1998-11-20) matches the Higher-Order and Symbolic Computation reprint date.

## Lessons
- [Features arrive welded together; audit which dependencies are real and which restrictions are accidents](../lessons/audit-the-bundle-you-inherited.md)
- [Sugar cannot break a law, so a broken law is proof that an addition is genuinely primitive](../lessons/a-broken-law-proves-a-new-primitive.md)
- [Ask what an apparently non-denotable construct stands for; the answer is the surrounding situation it silently refers to](../lessons/ask-what-the-unaskable-thing-denotes.md)
- [Hand the failure path in as an argument, and error handling stops being the part that escapes structure](../lessons/pass-the-failure-path-in-as-an-argument.md)
