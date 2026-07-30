---
type: lesson
title: "Separate the part of a language that organizes control from the part that touches data, and share only the first"
figure: wilkes
works: [computers-then-and-now]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Separate the part of a language that organizes control from the part that touches data, and share only the first

**Lesson:** Look at where the bulk of a language's syntax and the bulk of its implementation actually go, and most of it is spent on machinery that has nothing to do with the subject matter: introducing names, grouping simple actions into compound ones, choosing between alternatives, repeating. That machinery is entirely indifferent to what the elementary actions do or what the data looks like. So a language is really two languages, one nested inside the other — an outer one concerned with the organization of activity and an inner one concerned with operating on the material. Once you see the seam, the design question changes from "what language do we need for this domain" to "which of the two layers actually varies by domain."

The answer is that the inner layer varies and the outer layer does not, which suggests standardizing on a small number of outer languages and letting inner vocabularies be plugged into them. The payoff is proportional to how many specialized domains you expect: real-time control, graphics, operating-system construction, each arriving with its own genuine need for its own primitives, and none of them with any real need for its own way of writing a conditional. Designing a fresh whole language per domain means paying the outer-language design cost repeatedly, and — worse — making every practitioner learn a new way to express the parts that were never domain-specific to begin with.

The move generalizes past programming languages to any tool that combines an organizing framework with domain-specific operations. Find the boundary between the part of your design that is about coordination and the part that is about subject matter, keep the coordination part stable and shared, and make the subject-matter part replaceable. When a new domain arrives, it should be able to bring its own primitives and inherit everything the framework already knows about sequencing, naming and choice, rather than starting from a blank page and reinventing the parts that were never in question.

**Source:** [Computers Then and Now](../works/computers-then-and-now.md) — the discussion of higher syntax, which observes that declarations, compound statements and conditionals occupy most of a high-level language's syntax and compiler while being independent of the data-operating statements, and proposes standard outer languages with pluggable inner ones as the response to the growing number of special-purpose languages.
