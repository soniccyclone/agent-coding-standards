---
type: lesson
title: "Anticipated flexibility goes unused and does not prevent the extensions you failed to anticipate"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [primitive-count, cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Anticipated flexibility goes unused and does not prevent the extensions you failed to anticipate

**Lesson:** The case against building for imagined future needs is usually argued from principle. Here it is argued from measurement, which is much harder to dismiss. A team with roughly twenty person-years of object-oriented experience built a general-purpose list-display component deliberately equipped with hooks for every requirement they could foresee. Four years later they went back through every program they had written and checked. Two findings, and the second is the one that matters. First, many of the expensive advanced features had never been used at all. Second — despite all that anticipatory flexibility — they had still been forced to write eleven subclasses to meet requirements that arrived anyway.

Both halves of that result are needed to make the point. Unused features alone would only prove they over-built. The eleven subclasses prove the over-building did not even purchase what it was for: the hooks did not anticipate the actual extensions, because the actual extensions were not foreseeable, which was true at the time and would have been true however much design effort was spent. Speculative generality failed on its own terms rather than merely costing more than it returned. The third generation, built from what the usage data showed, covered every known need without the frills — and collapsed all eleven subclasses back into one class.

The honest coda is that they declined to call the new one final, and the reason generalizes. A shared component is an asset and assets depreciate, from technology moving and from requirements moving, so revision is not a sign of failure but a maintenance obligation. The interesting part is that the revision interval has a floor as well as a ceiling: too rarely and the component rots, too often and you destabilize everyone depending on it. A programmer who takes this seriously stops asking "what might someone need here?" — an unfalsifiable question — and starts asking "what have people actually done with this?", which requires having shipped something and gone back to look.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 5's boxed account of the "UltimateListView", including the reverse-engineering audit four years on that found both unused advanced features and eleven subclasses created despite them, the third-generation rebuild that merged those subclasses back into one, and the surrounding argument that reusable components depreciate and must be revised neither too often nor too rarely.
