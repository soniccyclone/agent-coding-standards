---
type: lesson
title: "Instantiating gives you what the programmer specified; copying a validated master gives you what was learned"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load, primitive-count]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Instantiating gives you what the programmer specified; copying a validated master gives you what was learned

**Lesson:** There are two ways to bring a new thing into existence, and they are usually discussed as interchangeable mechanics when they differ in meaning. Construct from a definition and you get exactly what was specified, with every parameter at its declared default — all such things are created equal. Copy an existing one and you get something carrying the state its source had accumulated at the moment of copying. The distinction is not about efficiency; it is about which of two questions you are answering. If you want what the author intended, construct. If you want what somebody arrived at through use, copy.

The consequence for building systems is a technique that gets overlooked because it looks unsophisticated: the cheapest and safest route to a particular configuration is to duplicate a master that has already been validated. The strength of that route is exactly the accumulated history — someone instantiated the pieces, arranged them, tuned them, and confirmed the result works, and copying transfers all of that without re-deriving it. Attempting the same thing by construction means encoding every one of those settled decisions as a default or a parameter, which is more work, is never finished, and reintroduces the possibility of getting one wrong. The document-template habit is the everyday instance: rather than starting empty and reconstructing margins, headers and boilerplate, keep a validated example and copy it. The author adds that the less bureaucratic version — duplicate a recent one of the right kind and delete what does not apply — is what he actually does, which is worth noting because the informal practice has the same structure as the industrial one.

What makes this worth holding as a design principle rather than a shortcut is that accumulated-state-as-specification is often more reliable than written specification, precisely because it was produced by running rather than by reasoning. A validated master is a configuration that has been tested as a whole; a set of defaults is a claim that each value is individually correct, which is a weaker guarantee and a much larger surface to review.

The reflex, then, is to ask of any creation path whether the thing being created should reflect intent or experience, and to stop treating "just copy a known-good one" as a stopgap on the way to a proper generator. It is a different answer to a different question, and where the question is "give me one like that one," copying is not the crude approximation of construction — construction is the expensive reconstruction of copying.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 11 section 11.4's opening, which contrasts creating a new instance of a class with copying an existing master (all instances of a class are created equal, while a copy reflects the master's state at duplication time), states that the cheapest and safest way to produce a particular object structure is to copy a validated master, and gives the word-processor example of master documents for letters, faxes and reports alongside the author's own admission that he simply duplicates a recent document of the required kind and deletes what is not needed.
