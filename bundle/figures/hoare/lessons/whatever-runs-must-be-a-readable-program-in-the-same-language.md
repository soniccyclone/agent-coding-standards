---
type: lesson
title: "Defer the packaging problem, but bind it in advance: whatever runs must be a readable program in the same language"
figure: hoare
works: [communicating-sequential-processes-paper]
axes: [cognitive-load, verifiability, expressiveness]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Defer the packaging problem, but bind it in advance: whatever runs must be a readable program in the same language

**Lesson:** Every design that gets the core semantics right runs into a second problem it did not sign up for: how independently written pieces are named, parameterized and combined so they can be reused without knowing about each other. That problem is real, large, and mostly orthogonal to the semantics, and trying to solve both at once corrupts the semantics — you start choosing meanings for the convenience of the linker. Setting the packaging question aside is legitimate. Setting it aside *silently* is not, because the eventual answer can quietly introduce behavior the base language never had, at which point the semantics you carefully pinned down describes only a sublanguage nobody actually writes in.

The way to defer without losing control is to publish, now, a constraint that any future packaging mechanism has to satisfy: after the pieces are assembled, the result must be expressible as a single text entirely in the base language, and that text must describe the execution independently of which parts came from where. Anything meeting this constraint is doing substitution; anything that cannot be printed back out as an ordinary program is doing something extra, and whatever it is doing has escaped every proof rule and every reader's model. The constraint costs the mechanism designer little and buys a great deal: one object to reason about, a debuggable artifact, no privileged status for imported code, and no possibility that reuse machinery becomes a second semantics maintained by nobody.

Applied outside language design, this is the criterion for judging code generators, macro layers, configuration systems that assemble behavior at startup, and frameworks that wire components together by reflection. Ask whether the running system can be exhibited as a plain program in the language you claim to work in. When it can, the abstraction is a shorthand and you keep the ability to reason at either level. When it cannot, the composed behavior lives only in the mechanism's head, which is why debugging such systems means debugging the mechanism rather than the program. And notice the flip side of the deferral: accepting a real inconvenience in the core — direct, explicit naming of partners rather than something more accommodating — is often the right trade, because inconvenience is a tax on writing while a compromised semantics is a tax on all subsequent reasoning.

**Source:** [Communicating Sequential Processes](../works/communicating-sequential-processes-paper.md) — the explicit-naming discussion, which concedes that requiring every communication to name its partner makes library construction inconvenient, declines to solve the library problem in order to keep the focus on semantics, and lays down as a recommended principle for whatever facility eventually arrives that every program, after assembly with its library routines, be printable as a text expressed wholly in the language that describes the execution regardless of which parts were drawn from a library.
