---
type: lesson
title: "Search for an evaluation order, not for the answer"
figure: sutherland
works: [sketchpad-a-man-machine-graphical-communication-system-afips-1963]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, programming-environments-and-object-systems]
tags: [lesson]
---
# Search for an evaluation order, not for the answer

When a system holds a web of mutual requirements, the obvious move is to attack the numbers: guess, measure the badness, nudge everything toward less badness, repeat. That works, always terminates eventually for some value of eventually, and gives you no idea when you are done. Sutherland's better move is to stop treating the problem as numerical at all and treat it as a question about the dependency graph: is there a sequence in which each quantity can be fixed once, using only the requirements that were still outstanding when its turn came, such that nothing later disturbs it? If such a sequence exists, finding it is a graph traversal, and executing it costs one pass with an exact result. The object of the search shifts from values to plans.

The reason this pays is that a plan is checkable and a numerical iteration is not. Ordering either exists or it does not; when it exists you have a proof of sufficiency baked into the construction, because each quantity was chosen with enough remaining freedom to absorb every requirement still attached to it. That reframing also makes the shape of the problem legible. Sutherland can say plainly which configurations admit an order and which do not, and the ones that do not are exactly the ones with genuine circular interdependence, where no local choice is free. The failure is informative rather than a mysterious slow convergence.

A programmer who believes this looks for the scheduling question hiding inside every relaxation loop, solver call, or retry storm. Before iterating on values, ask whether the dependency structure has a spine — a topological order, a fixpoint that is reached in one sweep, an evaluation sequence you can compute in advance and then simply run. When it does, you get determinism, exactness, and an audit trail for free. When it does not, you have learned something specific about the problem's topology, which is a better position than watching residuals shrink and hoping.

**Source:** [Sketchpad: A Man-Machine Graphical Communication System (AFIPS 1963)](../works/sketchpad-a-man-machine-graphical-communication-system-afips-1963.md) — the constraint-satisfaction section, where the one-pass method is developed by spreading "freedom" outward through the network of relations and contrasted against the fallback iterative scheme, including the frank admission of which drawn structures admit no such order.
