---
type: lesson
title: "Broker the match at runtime so installing one part makes it available everywhere it fits"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [expressiveness, cognitive-load]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Broker the match at runtime so installing one part makes it available everywhere it fits

**Lesson:** Two families of components need to be paired — things holding information, and things capable of presenting and editing information — and the naive arrangements are both bad. Have each data type name its editor and adding an editor means touching every data type. Have each editor enumerate the data it handles and adding a data type means touching every editor. Both give a relation that has to be maintained at as many sites as it has entries.

The alternative is a third party that performs the match at runtime. Neither family knows the other. Each editor declares the small interface it requires — a text editor works with anything answering a get-text and put-text pair; a list editor with anything answering size, get-element, and put-element; a graph editor with anything answering a neighbor-query and neighbor-mutation set. A broker holds the registry of candidates, asks each what it requires, asks the data object whether it supplies that, and instantiates the first match. The relation between the two families is now computed rather than recorded, so it costs nothing to maintain and is never stale.

The consequence worth designing for is a deployment property rather than a code-structure one: a customer installs one new editor and it becomes immediately available everywhere it happens to apply, including in combinations nobody enumerated. That is extensibility by registration instead of by modification, and it is qualitatively different from a plugin system where the host still decides where plugins may act. It works because the interfaces the editors demand are deliberately tiny — three messages, not a class hierarchy — which is what makes accidental applicability common rather than rare. A broker over fat interfaces yields few matches and is not worth its machinery.

One constraint is stated flatly and is easy to violate: the broker itself is immutable, meaning it may not be specialized per application. That is not conservatism. A meeting point whose behavior varies by context is no longer a common market, because the guarantee consumers depend on — that anything registered is findable by anything compatible — holds only if there is exactly one set of rules. The moment applications get their own subclassed brokers, registration becomes local again and the property that justified the design is gone. So the general shape is: keep the matched parties ignorant of each other, keep the required interfaces small enough that unplanned matches happen, and keep the matcher itself unforkable.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 11 section 11.2 on runtime configuration and object trading: the five roles (InformationObject, Editor, TraderClient, Trader, EditorFactory), the interface examples for text, list and graph editors, the trading scenario in which the Trader walks its factory list in priority order asking each for its supported interface and asking the information object whether it supports that interface, the note that a customer can install a specific editor and have it immediately available wherever applicable, and the stipulation that the Trader role is immutable and may not be specialized for different applications.
