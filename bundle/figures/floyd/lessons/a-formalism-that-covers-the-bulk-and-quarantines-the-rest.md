---
type: lesson
title: "Prefer a formalism that covers the regular bulk and quarantines the exceptions over one stretched to cover everything"
figure: floyd
works: [the-syntax-of-programming-languages-a-survey]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Prefer a formalism that covers the regular bulk and quarantines the exceptions over one stretched to cover everything

**Lesson:** The instinct when a formalism fails to capture some of the cases is to extend it until it captures all of them, and the instinct is usually wrong. A formalism that handles nearly everything delivers most of its value precisely by handling the regular part silently: the ordinary rules can be listed compactly with no commentary at all, and every scrap of the reader's attention is freed for the handful of rules that do not fit the pattern. That redirection of attention is the product. An extension that absorbs the exceptions destroys it, because it makes the exceptional rules look like ordinary ones and the compact listing stops being scannable.

There is a converse failure, which is forcing a formalism onto material whose structure it does not match. A language designed before the notation existed, described afterwards in that notation, comes out looking pathological in ways that say nothing about the language and everything about the mismatch — and some things genuinely are better defined in prose. The usable test is not whether the formalism *can* be made to cover the case but whether the structure it imposes lines up with the structure that means something. A general treatment of a function's argument list, written to allow arbitrarily many arguments, will end up asserting that some arbitrary pairing of adjacent arguments constitutes a meaningful unit while another does not. That assertion is not merely inelegant; it is false about the thing being described, and every downstream consumer that trusts the structure inherits the falsehood.

This is also why notational conveniences that add no power are worth adding anyway. A repetition or optionality marker leaves the class of describable languages exactly where it was, so by the measure of raw capability it is nothing. By the measure that matters it changes a great deal: it lets the description carve the artifact at joints that are real, so that only the parts which name something or have a value come out as units. Equal power is not equal fit, and fit is what a description is for.

What follows practically is a tolerance for deliberate partiality. The most useful published descriptions of real languages define something slightly larger than the real language, with the real one picked out as the subset meeting a few extra restrictions stated separately — and this is a virtue, not sloppiness, because it keeps the mechanical part mechanical and puts the awkward part where a human will read it. A programmer who works this way is comfortable saying "the formal part covers this much, and these four rules are prose," and is suspicious of any formalism whose coverage is total, on the grounds that totality was probably bought by making the notation describe itself rather than the problem.

**Source:** [The Syntax of Programming Languages — A Survey](../works/the-syntax-of-programming-languages-a-survey.md) — the introduction's remarks on languages that fit the formalism poorly and on some being best defined in words, the argument that near-adequacy allows most rules to be listed without explanation so attention concentrates on the few that do not fit, the Adequacy and Extensions sections on rules that provably cannot be captured, the bracket notations that raise convenience and explanatory power without raising generative power, and the argument-list example where a fully general treatment yields absurd claims about which fragments are phrases.
