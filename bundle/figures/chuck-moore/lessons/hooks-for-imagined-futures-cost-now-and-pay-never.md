---
type: lesson
title: "Provision for an imagined future is a certain cost against an improbable benefit"
figure: chuck-moore
works: [programming-a-problem-oriented-language, the-evolution-of-forth]
axes: [cognitive-load, primitive-count]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Provision for an imagined future is a certain cost against an improbable benefit

**Lesson:** The set of directions a program might be extended in is effectively unbounded, so any single one of them has a vanishing chance of being the direction actually taken. Structure added today to accommodate a guessed-at tomorrow therefore buys an expected value near zero while charging full price immediately: more parts to keep consistent, more surface to document, more shapes a reader must understand before touching anything. The arithmetic is not close, and it does not improve with experience at guessing, because the problem is the size of the space of futures rather than the quality of the guess.

The economics also run the wrong way in time. Whatever extension eventually turns out to be needed can be built when it is needed, and it will be built better then, because by that point the requirement is known concretely instead of imagined. Meanwhile the anticipatory scaffolding decays: it was designed against an understanding of the problem that has since been superseded, and the extension point does not fit the extension that arrives. Worse, whoever eventually needs the extension has to discover that the provision exists and infer how it was meant to be used, which is generally harder than writing the thing outright.

There is a defensible counter-argument, and recognizing it clarifies the rule rather than weakening it. People leave extension points because rework is expensive, so the honest response is to attack the expense rather than to pre-pay for guesses. A system small enough and malleable enough to be reshaped on demand does not need to predict, and that is the trade actually being made: pay for genuine flexibility in the substrate, refuse to pay for speculative flexibility in the design. A programmer holding this view writes for the requirement in front of them, deletes provision that has not earned its place, and treats the urge to leave room as a signal that the underlying tools are too rigid to be reshaped later.

**Source:** [Programming a Problem-Oriented-Language](../works/programming-a-problem-oriented-language.md) — the corollary against speculation stated alongside the governing simplicity principle, with the probability argument and the questions about whether anyone will ever notice or document the provision. Also [The Evolution of Forth](../works/the-evolution-of-forth.md) — the philosophy section, which identifies the appetite for generality as simplicity's main adversary and connects the refusal to speculate with the need for a genuinely malleable base.
