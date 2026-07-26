---
type: lesson
title: "Treat 'undefined' as a decision you have deferred, and know that every plausible default you supply destroys the evidence you would have needed"
figure: dahl
works: [class-and-subclass-declarations]
axes: [verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Treat 'undefined' as a decision you have deferred, and know that every plausible default you supply destroys the evidence you would have needed

**Lesson:** Calling a case undefined is described here without euphemism: it is a convenient way of postponing a hard decision about a situation for which no obvious interpretation exists. Naming the honest function of the word is what makes the rest of the analysis possible, because an undefined case is then a known debt with a due date rather than a settled part of the specification. The hard cases are specifically the ones only recognizable while running, since those are the ones where the choice cannot be pushed onto the compiler.

Two strategies are laid out with their costs. Forbid the case: the programmer must arrange his program so it cannot arise, adding explicit checks where necessary, and the compiled program carries implicit checks that partly duplicate his. Those implicit checks are a debugging aid, and in principle they can be switched off once a program is believed correct, which is the only sense in which the duplication is not waste. Or define an ad hoc but plausible behavior for the case: the language becomes noticeably easier to use, since nobody has to test for the situation explicitly, and in exchange the language has lost any means of locating the occurrences nobody foresaw, the ones where the plausible rule happens to be the wrong rule. The second option is not the safe one. It is the one that trades a loud failure in a case you thought about for a silent one in a case you did not.

The asymmetry is worth stating as a principle: a default answer for a case you do not understand is not a neutral act, it is the deletion of the signal that would have told you the case existed. The empty result, the zero, the nearest-legal-value coercion, and the quietly skipped operation all buy convenience with information, and the information they spend is exactly the information a maintainer will want at the moment something is subtly wrong. Notice also which way the design leaned when it had to choose: dereferencing an absent reference was made a hard failure that stops the program, on the reasoning that the trap will eventually catch most instances of the other undefined case too. One loud check placed where all the bad paths converge is worth more than a policy per site.

A programmer holding this lesson keeps a distinction between defaults chosen because the case is understood and the answer really is the right one, and defaults chosen because the case was inconvenient to think about. The second kind gets replaced with a failure that names the situation. The corollary is that "handle it gracefully" is a request that should be interrogated: graceful for whom, and at the cost of whose ability to diagnose the next occurrence?

**Source:** [Class and Subclass Declarations](../works/class-and-subclass-declarations.md) — the section on undefined cases, which states the deferral framing outright and then compares the forbid-and-check strategy against the plausible-standard-behavior strategy in terms of what each does to the language's ability to locate unforeseen situations, followed by the two specific undefined cases the paper had accumulated and the resolution chosen for each.
