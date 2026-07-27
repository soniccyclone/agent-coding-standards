---
type: work
title: "Assigning Meanings to Programs"
figure: floyd
description: Floyd's foundational paper showing how to attach logical assertions to points in a flowchart and prove, purely from those assertions and the program's control structure, that the program computes what it claims to. It introduces the machinery of verification conditions generated at each branch and loop, laying the groundwork for what Hoare would later formalize as axiomatic semantics. Also treats termination separately from partial correctness, a distinction that became standard in the field.
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
year: 1967
url: https://www.cs.tau.ac.il/~nachumd/term/FloydMeaning.pdf
access: public
host: third-party-rehost
tags: [work]
---

# Assigning Meanings to Programs

**Venue/year:** Proceedings of Symposium on Applied Mathematics, Vol. 19 (Mathematical Aspects of Computer Science), American Mathematical Society, 1967, pp. 19-32.
**Source:** https://www.cs.tau.ac.il/~nachumd/term/FloydMeaning.pdf — verified resolving (HTTP 200). Hosted on Tel Aviv University CS faculty Nachum Dershowitz's course-materials page, a third-party course mirror of the original AMS proceedings paper.

## Lessons
- [A program's meaning is the set of conclusions it licenses, not the trace some machine produces](../lessons/meaning-is-what-a-program-licenses-you-to-conclude.md)
- [Trade one unmanageable whole-program argument for many tiny local ones, and let induction assemble the result](../lessons/buy-global-guarantees-with-local-obligations.md)
- [Do not assert your rules and hope; state what would make them adequate and derive them](../lessons/derive-your-rules-from-an-adequacy-criterion.md)
- [Find the smallest set of facts only a human could have supplied, and treat everything downstream of them as machine work](../lessons/separate-invention-from-derivation.md)
- [Getting the right answer and getting an answer are two different proofs with two different mechanisms](../lessons/getting-the-right-answer-and-getting-an-answer-are-two-proofs.md)
- [If you cannot explain a feature without inventing a machine to run it, the feature is costing more than it looks](../lessons/a-feature-you-cannot-explain-without-a-machine-is-expensive.md)
