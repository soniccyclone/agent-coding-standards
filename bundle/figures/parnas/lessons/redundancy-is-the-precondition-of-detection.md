---
type: lesson
title: "Nothing can be detected in a description that says everything only once"
figure: parnas
works: [active-design-reviews-principles-and-practices]
axes: [verifiability, primitive-count]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Nothing can be detected in a description that says everything only once

**Lesson:** A description with no repetition has a hidden property: it contains no
internal disagreement, and therefore no error in it can ever be *found* — only
suffered later, when reality contradicts it. Detection is comparison, and comparison
needs two independently produced statements of the same thing. This is ordinary
engineering practice everywhere else, and it argues against a reflex that feels like
rigour: compressing a specification until each fact appears exactly once produces an
artifact that is elegant, minimal, and unreviewable.

The concrete move is to write down separately what a component's description already
implies. Offering an operation that reports a device's current condition silently
asserts that the condition is detectable at all — an assumption that is present in
the interface, invisible in it, and unlikely to be questioned by anyone reading only
the operations. State it explicitly in its own section and now two things exist that
must agree, and a reader can go looking for the assumption that licenses each
operation and notice when there isn't one. The same trick applied to misuse gives a
second list, of usages the designers assume will not happen, which can be checked
against the described failure conditions. Omitted operations, missing parameters,
unhandled situations, and outright contradictions all become findable by comparison
rather than by inspiration. Parnas is explicit that this is a real cost, not a free
lunch: the redundancy you add is redundancy that must now be kept consistent, and
you pay for the checking you bought.

Because it costs, redundancy has to be spent where it buys detection. Assumptions
true of every design in the world — that arguments can be passed, that an input is
not silently overwritten — add cross-checking obligations while distinguishing
nothing, so they stay out. What goes in is the specific, load-bearing, easily
overlooked commitment this particular component is making about its world. The
programmer who works this way stops treating duplication as uniformly bad and starts
asking what each description is supposed to be checkable *against*. Where the answer
is "nothing," they add the second statement deliberately, aware they have just taken
on the job of keeping the two aligned.

**Source:** [Active Design Reviews: Principles and Practices](../works/active-design-reviews-principles-and-practices.md)
— the section on making a design representation reviewable, which argues for explicit
assumption lists as engineered redundancy, gives the two lists kept per component,
and draws the line at assumptions that hold for all designs.
