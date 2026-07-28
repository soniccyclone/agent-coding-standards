---
type: lesson
title: "Underspecify deliberately, but name every hole and say who is obliged to fill it"
figure: chamberlin
works: [xquery-1.0-an-xml-query-language]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Underspecify deliberately, but name every hole and say who is obliged to fill it

A specification that pins down everything cannot be implemented on plausible hardware or over plausible storage layers; a specification that hand-waves cannot be written against. The way out is not to find a middle level of detail — it is to make the gaps themselves first-class. Every place the design declines to decide gets a label, and the label carries an obligation. One kind of gap says: implementations will differ here, and each implementation must publish its choice. Another says: implementations will differ here, and nobody owes anyone an explanation. The two look identical from inside the text and are completely different for the person writing portable code against it, because only the first can be programmed around.

That distinction has real teeth when it is paired with an enumerated list of the gaps and a conformance rule that says supporting the base design means documenting every gap of the first kind. Now portability is a checkable property rather than a hope: a program that touches only fully-specified behavior runs everywhere, a program that touches a documented-variance point runs where you have read the documentation, and a program that touches an undocumented-variance point is knowingly betting. The same move applies to whole features rather than single decisions. A capability can be optional, but then the design must say what an implementation lacking it does when it meets the syntax — and the right answer is to fail with a specific, named error rather than to ignore it, approximate it, or silently do something else. Optional features that degrade quietly are how a portable-looking program becomes wrong in production.

The complement is a mechanism for implementations to add things without forking the language: an extension form the parser accepts everywhere, whose contents an implementation that does not recognize them must skip, with a fallback expression right there for it to use instead. That way the vendor gets its index hint or proprietary construct, and the program still runs, more slowly or more generically, elsewhere. The design constraint is that the extension must be inert to anyone who does not know it — which means the syntax has to be reserved up front, before anyone needs it.

For working code the lesson translates directly: distinguish, in writing, between behavior your callers may rely on, behavior that varies but is documented per deployment, and behavior nobody should ever depend on. Undocumented variance is not flexibility — it is a promise you did not know you were making, and someone will build on it.

**Source:** [XQuery 1.0: An XML Query Language](../works/xquery-1.0-an-xml-query-language.md) — the paired definitions of the two kinds of unspecified behavior early in the document, the conformance section that makes documenting one of them a requirement while explicitly excusing the other, the optional-feature clauses that each name the error an implementation must raise instead, and the extension-expression section with its ignorable-pragma-plus-fallback rule.
