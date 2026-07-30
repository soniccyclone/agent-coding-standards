---
type: lesson
title: "Write the textual grammar even when your tool is graphical — the grammar is where you find out if the concepts cohere"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [expressiveness, verifiability]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Write the textual grammar even when your tool is graphical — the grammar is where you find out if the concepts cohere

**Lesson:** This method's models live in a database and are authored through direct-manipulation graphical tools. Defining a textual language for the same information is therefore redundant by the usual reckoning, and the author defines one anyway, for three stated purposes: interchange between different implementations of the tools, precise documentation on paper, and — listed first — as a summary of the concepts and the relationships between them.

That third purpose is the one worth extracting, because it inverts how a grammar is normally regarded. A grammar is usually a means to an end, written because something has to parse. Here it is also an audit of the conceptual model. Every notion must appear as a production, every relationship between notions must appear as a nesting or a reference, and the scoping rules must state exactly which names are visible where. A diagram tolerates vagueness about all of that indefinitely — arrows can mean whatever the caption says, and containment can be suggestive. A grammar cannot. If two concepts turn out to have no expressible relationship, or one has no place to live, or the nesting a picture implied is not actually a nesting, writing the productions is where you find out. So the exercise is worth doing for its diagnostic value even if nobody ever writes a line in the resulting language.

The other two purposes are practical and worth keeping distinct from each other. Interchange between independent implementations requires a form that is not a database dump: an internal representation is a bet on one tool, and a specified text is a bet on none. And the author notes that for some purposes — documenting interfaces and attributes in detail — the textual form is not merely adequate but *preferred*, which is the honest observation that graphical presentation wins for structure and loses for dense enumerable detail. A tool that offers only one form is worse at one of those two jobs.

The reflex generalizes to anything modelled in a structured editor, a visual builder, or a configuration UI: define the serialized text, publish its grammar, and treat writing that grammar as a review of whether your concepts are actually well-defined. The three payoffs come in a useful order — the audit happens immediately, the documentation utility appears as soon as the detail gets dense, and the interchange value arrives the first time someone needs to read your models without your tool.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — appendix A's introduction, which notes the technology was developed around an object-oriented database with direct-manipulation graphical tools yet holds it useful to define a textual form for all model information, preferred for purposes such as documenting interfaces and role attributes, and lists the language's three purposes: as a summary of the OOram concepts and the relationships between them, as a language for precise documentation on paper, and as an interchange language for communicating models between different implementations of the tools — followed by A1's lexical conventions, A2's Extended Backus-Naur grammar, and A3's scoping rules naming modules, role models, interfaces, messages and roles as the scoping constructs.
