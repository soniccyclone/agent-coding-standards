---
type: lesson
title: "Define a composition mechanism by reduction to a construct whose rules you already trust"
figure: dahl
works: [class-and-subclass-declarations, simula-67-common-base-language]
axes: [primitive-count, verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
tags: [lesson]
---
# Define a composition mechanism by reduction to a construct whose rules you already trust

**Lesson:** Inheritance could have been specified as a lookup rule: when a name is not found here, search upward. That is how many later languages describe it, and it is why their scoping, initialization order, and name-collision behavior each need separate rules that interact badly. Simula specifies it instead as a syntactic operation on text. The general declaration and the specific one are merged into a single declaration: their parameter lists join, their specifications sit side by side, and their bodies fuse into one block whose head carries both sets of local declarations and whose statement part runs the general contribution and then the specific one. There is no inheritance semantics to define, because after the merge what remains is a block, and blocks were already defined.

The savings compound in exactly the places that usually cause trouble. Two prefix levels declaring the same identifier is not a novel situation requiring an override rule or a shadowing rule; it lands in one block head as a repeated declaration, which the base language already calls an error. Initialization order is not a policy question; the general statements precede the specific ones because that is where the merge put them. Attribute layout, name resolution, and the meaning of a nested declaration all come along free. This is the primitive-count axis paying off in reasoning rather than in aesthetics: one construct with one set of rules, and a derived feature that cannot develop behavior inconsistent with it.

The merge is deliberately asymmetric, and the asymmetry encodes a dependency direction. Attributes contributed by the general part are ordinary locals as far as the specific part is concerned, freely usable. Attributes contributed by the specific part are not visible to the general part at all, except through the same explicit remote-access mechanism any outside code would use. So the general text is writable, readable, and checkable without knowing which specializations exist, and it cannot silently acquire a dependency on one of them. A composition mechanism that permitted visibility in both directions would look more convenient and would destroy the property that makes the general layer reusable.

A programmer who works this way is suspicious of features specified by their runtime search behavior and prefers features specified as a transformation into code they can already reason about. The practical version of the question: can I write down, by hand, the single flat construct this composite is equivalent to? If yes, its corner cases are the flat construct's corner cases and I already know them. If no, every corner case is new, undocumented, and waiting.

**Source:** [Class and Subclass Declarations](../works/class-and-subclass-declarations.md) — the concatenation rules in the semantics section, which define a prefixed declaration as the recursive merge of parameter lists, specification parts, and block bodies, together with the stated one-way visibility between prefix and main part; the discussion transcript following the paper makes the collision consequence explicit. Also [SIMULA 67 Common Base Language](../works/simula-67-common-base-language.md), whose class-declaration chapter carries the same concatenation definition in reference form.
