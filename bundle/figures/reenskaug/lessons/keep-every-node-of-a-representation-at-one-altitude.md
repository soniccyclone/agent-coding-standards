---
type: lesson
title: "Keep every node of a representation at one altitude, and pick the altitude from whoever owns the problem"
figure: reenskaug
works: [models-views-controllers]
axes: [cognitive-load, expressiveness]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Keep every node of a representation at one altitude, and pick the altitude from whoever owns the problem

Two rules govern the internal structure of anything meant to represent a domain, and they are stronger together than either is alone. First, the pieces of the representation should stand in one-to-one correspondence with the pieces of the world as the person who owns that world perceives it — not as the storage layer finds convenient, and not as an analyst thinks the world *ought* to be carved. Second, the pieces must all sit at a single level of the problem. A structure that mixes entities the domain owner would recognize with artifacts of how those entities happen to be rendered or stored has no coherent level, and therefore no coherent meaning.

The first rule is what makes a representation usable, and the second is what keeps it usable as it grows. Correspondence gives you a translation you never have to think about: every question the domain owner can ask has an obvious address in the structure, and every change they describe has an obvious edit. Uniform altitude is what protects that property. Once one low-level artifact is admitted as a peer of the domain entities, every traversal, every invariant, and every piece of code that walks the structure has to be prepared for both kinds of node, and each such site has to re-decide what level it is operating at. The confusion is not aesthetic; it is a real loss of the ability to reason locally about any part of the structure.

The practical consequence is that "who perceives this?" becomes a question you ask about a data structure before you ask what fields it has. Choose the owner, adopt their carving of the world verbatim, and then defend the boundary — when something arrives that is real but lives at a different altitude, it belongs in a different structure that references this one, never as another node inside it. This is unglamorous work with an unglamorous payoff: nobody notices a representation whose levels are clean, and everybody feels one whose levels are not, usually as a vague sense that the code is hard to talk about.

**Source:** [Models-Views-Controllers](../works/models-views-controllers.md) — both rules are laid down in the note's opening section on models, which also insists that a view must query a model in the model's own vocabulary rather than assuming anything about how it is implemented.
