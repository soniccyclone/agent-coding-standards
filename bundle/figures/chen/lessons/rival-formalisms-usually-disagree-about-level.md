---
type: lesson
title: "Rival formalisms usually disagree about level, not about truth"
figure: chen
works: [the-entity-relationship-model-toward-a-unified-view-of-data, english-sentence-structure-and-entity-relationship-diagrams]
axes: [cognitive-load, primitive-count]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# Rival formalisms usually disagree about level, not about truth

**Lesson:** Chen walks into a three-way argument about how data should be described and does not begin by advocating. He begins by building a ladder: what exists as a matter of the enterprise's own understanding, how that understanding is organized into recorded information, structure that knows nothing about search or indexing, and structure that does. Then he puts each contending formalism on the rungs it actually occupies. Once they are placed, most of the claims of superiority stop being contradictions — one camp was describing traversal machinery, another was describing a storage-neutral algebra, a third was describing conceptual objects, and they were talking past each other about which question they answered. Deadlock in a design argument is often a symptom that the participants have not agreed on what is being described.

The constructive half is what makes the ladder more than diplomacy. Having identified the highest rung as the one where the domain's own categories live, Chen models there and then shows the lower rungs as things you can derive from it. That inverts the usual economics of a design argument: instead of one formalism defeating two others, one small set of constructs at the top yields all three as projections, which is a claim about primitive count rather than taste. The same discipline appears in his handling of presentation — the same assertions about a domain drawn as a diagram or laid out as tables are the same content in two costumes, so an argument about the drawing is not an argument about the design.

The reflex extends to what belongs on which rung. Facts about how many and how often — the average fan-out of one category into another, the annual rate at which a population turns over — are real and useful, but Chen rules them out of the conceptual picture and down to where physical structure is chosen, because they constrain layout without changing what the domain is. A programmer who has this reflex, faced with two designs that seem incompatible, first asks what each one is a description of, and expects a good fraction of apparent conflicts to evaporate. When they do not evaporate, the disagreement is now sharp enough to settle, because both parties are finally arguing about the same rung.

**Source:** [The Entity-Relationship Model — Toward a Unified View of Data](../works/the-entity-relationship-model-toward-a-unified-view-of-data.md) — the multilevel framing that opens the model's development, and the closing analysis deriving each competing view from it. Also [English Sentence Structure and Entity-Relationship Diagrams](../works/english-sentence-structure-and-entity-relationship-diagrams.md), where statements carrying only counts and change frequencies are assigned to physical design rather than to the conceptual model.
