---
type: lesson
title: "Software has no native geometry, so every diagram is one projection among many and no single picture will ever carry the design"
figure: brooks
works: [no-silver-bullet]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Software has no native geometry, so every diagram is one projection among many and no single picture will ever carry the design

**Lesson:** Floor plans work because buildings live in space. The drawing captures a spatial reality in a spatial abstraction, which is why contradictions leap out and omissions become visible to client and architect alike. Chip layouts and molecular models earn their power the same way. A program has no such embedding. Attempting to draw its structure yields not one graph but several superimposed ones: what calls what, where data moves, what depends on what, what happens in which order, what names are visible where. These graphs generally are not planar, let alone tree-shaped, and they do not agree with each other about which parts are close together.

Two consequences follow. The first is that no notation will ever give you the single overview that a plan gives a builder, and the search for one is a search for something the subject matter does not possess. The second is more useful: since each projection is legitimate but partial, design comprehension has to be assembled from several deliberately chosen views, with the reader responsible for holding the correspondence between them. Some aspects diagram beautifully and some, particularly the step-by-step transformation of data, stay stubbornly textual. Where a projection can be forced into a hierarchy by cutting links, the cutting is itself a design act that buys comprehensibility at a price worth naming.

Someone who accepts this stops expecting a picture to substitute for the design and starts choosing views for what each one makes checkable. The absence of a natural geometry also explains a chronic difficulty that has nothing to do with anyone's laziness: reasoning about a system deprives the mind of its strongest instruments, and communicating a design between minds is harder still, because two people can hold different projections while believing they share a model. That is a cognitive-load fact about the medium rather than a documentation failure, and it argues for making the correspondences between views explicit instead of assuming they are obvious.

**Source:** [No Silver Bullet: Essence and Accidents of Software Engineering](../works/no-silver-bullet.md) — the discussion of software's resistance to visualization among its inherent properties, and the later assessment of graphical programming, where the analogy to chip design is rejected on the grounds that a layout's geometry expresses what the chip is while a program has no comparable spatial content.
