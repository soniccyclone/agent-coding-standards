---
type: work
title: "History of Lisp"
figure: mccarthy
description: McCarthy's own first-person account of how Lisp came together between 1956 and 1958, including the details later scholarship (and this bundle's correction to the figure's "why a candidate" note) draws on: that lambda was adopted as a convenient notation for functions rather than as an attempt to implement Church's calculus, and that eval emerged somewhat by accident once it became clear the interpreter could be written in the language itself. It also traces the FUNARG problem and the drift from LISP 1 to LISP 1.5, and is candid about which design choices were deliberate versus incidental.
subdomains: [programming-languages-and-semantics]
year: 1978
url: https://www-formal.stanford.edu/jmc/history/lisp/lisp.html
access: public
host: self-archived
tags: [work]
---

# History of Lisp

**Venue/year:** ACM SIGPLAN History of Programming Languages Conference I (HOPL I), June 1978; published in R. Wexelblat (ed.), "History of Programming Languages" (Academic Press, 1981), pp. 173-185.
**Source:** https://www-formal.stanford.edu/jmc/history/lisp/lisp.html — live page, self-archived on McCarthy's Stanford page, confirmed 200 OK.

## Lessons
- [Whatever runs first becomes the specification, so treat every provisional notation as a candidate permanent one](../lessons/the-first-implementation-freezes-the-design.md)
- [When the machine forecloses an option, check whether what survived is cleaner before you mourn the loss](../lessons/let-the-machine-prune-your-primitives.md)
- [Shape the internal representation for the transformations you will perform, and push human-facing notation out to the boundary](../lessons/optimize-the-internal-form-and-translate-at-the-edges.md)
- [Keep a core that obeys equational laws, and keep an explicit list of the features you have not been able to give semantics to](../lessons/keep-a-ledger-of-what-you-cannot-give-semantics-to.md)
