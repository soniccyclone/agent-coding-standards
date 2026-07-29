---
type: lesson
title: "Mechanize a medium only where the model gives back more than the output"
figure: sutherland
works: [sketchpad-a-man-machine-graphical-communication-system-thesis]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Mechanize a medium only where the model gives back more than the output

Having built a system that could plainly do the job, Sutherland ends his
dissertation with a judgement most builders avoid: for work whose only product
is the artifact itself, the machine is the wrong tool and pencil and paper are
better. He grounds it in his own failures rather than in argument. Diagrams of
circuits — the application that looks like the most obvious fit — went badly, and
he reports a user spending ten hours before concluding the thing would have been
faster by hand, because nothing downstream consumed the structure he had paid to
enter. The cases that paid were the ones where the structural model was fed to
something else: relations solved to reveal how a mechanism moves, a load
analysis reporting forces from a drawn truss, immense repetitive patterns
generated from one definition.

The general principle is a test on the ratio between what a formal
representation costs to construct and what can be derived from it once
constructed. Formalizing something is never free — every relationship you make
explicit is a relationship you had to state, and the effort scales with the
detail of the model. That cost is only recovered when the model answers
questions the informal version could not be asked at all. Where the deliverable
is the rendering, formalization is pure overhead dressed up as rigour, and the
sophistication of the tool makes it worse rather than better because it invites
more of it.

This cuts against the instinct that structured is always superior to
unstructured. It also explains a common failure: a team builds a rich model of a
domain, no analysis ever consumes it, and the model degrades into an expensive
second copy of the output that must be maintained alongside it. The discipline
Sutherland's conclusion suggests is to name the consumer before building the
representation — the simulator, the solver, the generator, the checker — and to
be willing to say that for a given task the informal artifact wins. His most
telling remark is about the circuits: it would have been worth drawing them in
the system *if* a simulator had been attached to tell him whether they worked.
The representation was not too weak; nothing was waiting to read it.

**Source:** [Sketchpad: A Man-Machine Graphical Communication System (PhD Thesis)](../works/sketchpad-a-man-machine-graphical-communication-system-thesis.md) — the concluding chapter's comparison of the pattern, linkage, bridge and circuit applications, and its claim that computer drawing pays only when something more than a drawing comes back out.
