---
type: lesson
title: "Build the language from one template and a uniform nesting rule"
figure: boyce
works: [sequel-a-structured-english-query-language]
axes: [primitive-count, cognitive-load]
subdomains: [programming-languages-and-semantics, databases-and-data-management]
tags: [lesson]
---
# Build the language from one template and a uniform nesting rule

**Lesson:** Complexity in a language should live in composition, not in vocabulary. Give the user a single basic block — a fill-in-the-blanks template whose slots have fixed, predictable meanings — and one rule: wherever a slot takes a value, it may instead take another instance of the same block. Arbitrarily deep expressions then cost nothing new to learn, because every level of the structure is the level the user already knows. The block-structured discipline that was reshaping control flow at the time applies just as well to a query surface: top-down, linear, each unit readable in isolation.

The design tell is what happens mid-expression. When the writer reaches a point needing a condition they can't state as a simple comparison, the escape hatch should be the language's own basic form again — not a second sublanguage, a special operator family, or a mode switch. If the recursive case and the base case are the same shape, the user's knowledge composes as freely as the syntax does. If they aren't, every new capability multiplies the learning surface instead of adding to it.

A programmer holding this principle resists the urge to solve each new requirement with a new construct. They ask first whether the existing template, nested or slightly generalized, already covers it — and they measure a language proposal by how few distinct shapes a complete grammar for it needs. A grammar that fits on a page is not a toy; it is evidence the design found the right primitive.

**Source:** [SEQUEL: A Structured English Query Language](../works/sequel-a-structured-english-query-language.md) — the presentation of the basic query block as the language's one component, the discussion of nesting a block inside a condition slot as the structured-programming-influenced move, and the compact appendix grammar.
