---
type: lesson
title: "Bootstrap every tool into its own next use, so your mistakes come back to you first"
figure: wirth
works: [from-programming-language-design-to-computer-construction]
axes: [cognitive-load, verifiability]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Bootstrap every tool into its own next use, so your mistakes come back to you first

**Lesson:** When you build a tool, arrange for the very next thing you build to depend on it. A systems language written in order to implement a compiler; a language whose compiler is written in itself; a language designed to implement the entire software of a machine; a machine built to be the environment for all subsequent work, from programming to documents to circuit layout. The chain is not a stunt, it is a control structure for design judgment. A tool used only by other people returns criticism slowly, filtered, and too late to act on; a tool you are forced to inhabit returns it immediately and unavoidably. Bootstrapping is the most efficient available mechanism both for compounding what you got right and for being punished promptly for what you got wrong, and the second half is the more valuable one.

Notice what this does to the incentive to include a feature you are unsure about. A designer who will personally write a hundred thousand lines against a construct evaluates it differently from one who will only write its specification. The loop also makes cost visible at the right moment: if a facility is awkward to compile, you find out while you are still able to change the definition, rather than after the definition has been frozen and every future implementer inherits the awkwardness. This is the concrete reason a definition should not be finalized before something substantial has been built with it — a rigorous specification untested by construction is a claim made without evidence, however carefully it is written. Clarity of definition is necessary for a reliable implementation and is nowhere near sufficient for one.

There is a warning attached, and it is about what the loop cannot tell you. A bootstrap makes your immediate needs vivid and everything else invisible, so an artifact produced as a stepping stone can escape and become widely depended on while carrying only the care that a stepping stone deserved. An intermediate representation invented to satisfy a few requests cheaply, never expected to outlive them, can turn out to be the thing that carries the whole project into the world — and then its under-designed, under-documented state is permanent. So the practice pairs with a habit of asking, of anything you are about to build carelessly on purpose, whether you would survive its success. Choosing the wrong goal is entirely compatible with good intentions and competent execution.

**Source:** [From Programming Language Design to Computer Construction](../works/from-programming-language-design-to-computer-construction.md) — the closing distillation naming bootstrap as the common technique across the projects and as the way to profit from one's efforts and suffer from one's mistakes, the account of the intermediate-code version that was built as a side effort and became the vehicle for the language's spread, and the remark on clear specification being necessary but not sufficient.
