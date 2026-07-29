---
type: lesson
title: "Reach the middle ground by composing the extremes, not by parameterizing them"
figure: sutherland
works: [sketchpad-a-man-machine-graphical-communication-system-afips-1963]
axes: [primitive-count, expressiveness]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Reach the middle ground by composing the extremes, not by parameterizing them

**Lesson:** When a design offers two opposed constructs — one rigid, one fully malleable — the reflex is to imagine users wanting something in between and to bolt on a knob that dials rigidity partway. Sketchpad's answer is better and cheaper: leave both constructs pure and let one contain the other. A rigid unit whose interior cannot be touched, and a loose expansion whose parts are all individually editable, together generate the entire spectrum, because a loose expansion of rigid units is exactly a structure that is soft where you wanted softness and hard where you wanted hardness. The intermediate degrees of freedom were never a missing feature; they were a composition nobody had tried yet.

The reason this works is that rigidity is a property of a boundary, not a scalar. A knob presumes the axis is quantitative — "how much can be edited" — when what users actually want to control is *which* things are frozen and which are free, and that is a shape, not a magnitude. Composition expresses shapes; parameters express magnitudes. So the parameterized version is not merely more code, it is a worse model of the requirement, and it will keep growing knobs as users describe freezing patterns the single axis cannot name.

The programmer who believes this reacts differently to the feature request that begins "we need something between X and Y." First question: can Y contain X, or X contain Y? If either nests, the request is already satisfiable, and answering it costs documentation rather than machinery. This is also a strong argument for keeping your primitives extreme instead of moderate — a construct that is uncompromisingly immutable and a construct that is uncompromisingly open compose into far more configurations than two constructs that were each softened toward the middle to be "more practical," and softened primitives tend not to compose cleanly at all, since each one's built-in compromise fights the other's.

**Source:** [Sketchpad: A Man-Machine Graphical Communication System (AFIPS 1963)](../works/sketchpad-a-man-machine-graphical-communication-system-afips-1963.md) — the discussion of building drawings, where the fixed-interior subpicture is contrasted with the freely editable expansion and the whole range between them is obtained by expanding structures whose members are subpictures, illustrated by a part-rigid, part-flexible composite figure.
