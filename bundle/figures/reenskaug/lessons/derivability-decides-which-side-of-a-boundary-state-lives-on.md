---
type: lesson
title: "Derivability, not layering etiquette, decides which side of a boundary a piece of state belongs on"
figure: reenskaug
works: [thing-model-view-editor]
axes: [cognitive-load, hardware-affinity]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Derivability, not layering etiquette, decides which side of a boundary a piece of state belongs on

The usual rule for separating a core representation from its presentation is stated as a prohibition: presentation concerns must not appear in the core. Stated that way it is a matter of taste, and it collapses the moment a presentation needs to remember something. The sharper version replaces the prohibition with a test. Ask whether a given piece of information can be computed from the core representation. If it can, the core owns it and the presentation asks for it. If it cannot — because the information is a genuine choice the core has no opinion about — then the presentation owns it, and this is not a leak or a compromise but the boundary working correctly.

The test earns its keep because it produces a real answer in the awkward cases rather than a slogan. Where a picture of a structure follows deterministically from the structure itself, no picture-specific state is warranted. Where the picture involves placing symbols in space, an arrangement the underlying structure does not determine, that arrangement is irreducibly presentation-side state and pretending otherwise means either inventing false structure in the core or leaving the user's layout choices nowhere to live. Separately, derivable information may still be held redundantly on the presentation side for speed, but that is a cache with a known owner, and it should be recognized and labelled as such rather than confused with ownership.

The practical effect is a discipline for arguing about boundaries with something other than aesthetics. When two components fight over a field, the question is not which layer feels more appropriate but whether either can reconstruct the field from what it already has. That single question tends to dissolve arguments that would otherwise run on indefinitely, and it makes the resulting structure explainable: every stored value is either primary or an admitted copy of something primary, and nobody has to trace update paths to find out which.

**Source:** [Thing-Model-View-Editor: An Example from a Planning System](../works/thing-model-view-editor.md) — visible in the contrast between the note's insistence that the network representation carry nothing about screen appearance and its treatment of the diagram presentation, singled out as the case whose contents cannot be recovered from the representation and which therefore must keep its own positional state (plus a copy of dependency information kept only for speed).
