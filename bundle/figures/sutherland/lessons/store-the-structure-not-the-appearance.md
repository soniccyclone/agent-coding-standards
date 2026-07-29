---
type: lesson
title: "Store the structure that produced the artifact, never the artifact's appearance"
figure: sutherland
works: [sketchpad-a-man-machine-graphical-communication-system-thesis]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Store the structure that produced the artifact, never the artifact's appearance

Most representations of a designed object record its final form: the marks, the
pixels, the flattened output. Such a record can be reproduced but not
reasoned about, because everything the designer knew while making it — which
parts are the same part, which parts must stay attached, which measurement
governs which dimension — was discarded at the moment of flattening. The
alternative is to store the derivation: named definitions, references to those
definitions with a transform attached, and explicit links recording what
depends on what. The visible form then becomes a computed consequence, cheap to
regenerate and never itself the thing being edited.

The payoff is not economy of storage; it is that edits acquire reach. When
every occurrence of a symbol is a reference rather than a duplicate, revising
the definition revises every occurrence at once, at every level of nesting, and
the change costs the same whether there are seven occurrences or nine hundred.
When connectivity is recorded rather than inferred from coincidence of
coordinates, moving one part drags its neighbours instead of tearing the
structure apart. And the machine gains knowledge it could not otherwise have:
a reference to a definition tells the system *what a thing is*, so downstream
programs can consume the model directly rather than trying to recognize
intent in a bag of marks. Sutherland's sharpest illustration is that replacing
one small master definition instantly converts an entire large pattern built
from it into a different pattern with identical structure — an operation with no
counterpart in the flattened medium.

The cost is real and worth naming: derived representations demand that the
system maintain consistency itself. Deleting something that others depend on
must propagate, combining two things must combine everything related to them,
and moving a thing that holds no numbers of its own must move the things it is
made of. Sutherland's system carried a family of such propagating operations
precisely because the structural representation created the obligation. A
programmer who accepts this trade edits definitions rather than instances,
treats duplication in the model as a defect rather than a convenience, and
expects to invest up front in propagation machinery in exchange for edits whose
cost stops scaling with the size of the output.

**Source:** [Sketchpad: A Man-Machine Graphical Communication System (PhD Thesis)](../works/sketchpad-a-man-machine-graphical-communication-system-thesis.md) — the introductory argument that a computer drawing differs in kind from a trail of carbon, the master/instance treatment in the chapter on recursive functions, and the recursive deletion, merging and moving operations that keep such a representation consistent.
