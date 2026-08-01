---
type: figure
title: C.A.R. Hoare
description: b. 1934, Oxford/MSR. Hoare logic, CSP process algebra. Turing Award 1980.
status: accepted
layer: implementation-mapping
subdomains: [formal-methods-and-verification, software-engineering-and-architecture, distributed-systems-and-concurrency]
tags: [figure, accepted]
---

# C.A.R. (Tony) Hoare

**Dates:** b. 1934. British computer scientist, Oxford University and later Microsoft Research Cambridge.

## Why a candidate
- **Formal Methods & Verification:** Formalized Floyd's assertion method into an axiomatic proof system for imperative programs — "Hoare logic" is the field's namesake formalism.
- **Software Engineering & Architecture:** Brought formal, provable reasoning to program structure rather than relying on intuition about how components should fit together.
- **Distributed Systems & Concurrency:** Developed CSP, a process algebra giving formal, compositional semantics to concurrent processes communicating via synchronized message-passing.

## Top 10 most influential works
1. "An Axiomatic Basis for Computer Programming" (1969, CACM) — `public` (multiple university mirrors)
2. "Communicating Sequential Processes" (1985, book) — `public` (Hoare self-published free PDF at usingcsp.com)
3. "Communicating Sequential Processes" (1978, CACM paper) — `paywalled`/`uncertain`
4. "The Emperor's Old Clothes" (1980 Turing lecture) — `public` (ACM Turing lecture archive)
5. "Monitors: An Operating System Structuring Concept" (1974) — `paywalled`
6. "Hints on Programming Language Design" (1973) — `public` (Stanford AI Lab memo)
7. "An Axiomatic Definition of the Programming Language Pascal" (1973, with Wirth) — `uncertain`
8. "Proof of Correctness of Data Representations" (1972, Acta Informatica) — `uncertain`
9. "Notes on Data Structuring" (1972, in *Structured Programming*) — `paywalled`
10. "The Verifying Compiler: A Grand Challenge for Computing Research" (2003) — `uncertain`

## Lessons
Hoare's first move on any design question is to make the bad case unwritable rather than to adjudicate it. Where a construct has degenerate readings, shape the notation so they cannot be typed; where a model keeps producing arbitrary answers about simultaneity, drop the clock so the question has no expression at all; where a scarce resource must be shared, give each user a private-looking stand-in whose interface is pleasant enough that nobody wants the escape hatch, since an exemption granted to anyone turns a guarantee into a default. A prohibition is cheap to lift later; a special case baked into a semantics is not. Underneath sits a strict ledger of what has actually been promised. A correctness argument may draw only on the weak guarantee in the definition, never on the decency a good implementation happens to show, and nondeterminism is not caprice but the exact residue of what you chose not to observe, so record the choice: an omission with a note is a licence granted to the implementor, while the same omission unremarked is a hole somebody later fills with whatever the code does. He distrusts unfalsifiable design virtues and swaps them for tests you can actually run. An abstraction has earned its place when a second implementation with a different cost profile would be correct; concepts were cut at the joints when the algebra comes out short; modularity and orthogonality are counterfeits of simplicity, and simplicity is the condition under which a limited mind can evaluate the consequences of its own decisions. Hence the refusals, which are the most portable part of him: don't pre-spend your users' efficiency budget, don't ship checks you can turn off, don't chase an optimum needing knowledge you lack when steering away from the persistently pessimal costs almost nothing, don't begin what you cannot yet state clearly, and build nothing the person accountable cannot follow.
