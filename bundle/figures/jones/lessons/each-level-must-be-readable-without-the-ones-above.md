---
type: lesson
title: "Each level of a design must be readable without the levels above it"
figure: jones
works: [development-methods-for-computer-programs-including-a-notion-of-interference]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Each level of a design must be readable without the levels above it

**Lesson:** In a design recorded as a sequence of increasingly concrete descriptions, each level restricts its structures with conditions saying which configurations are legal, and most of those conditions are inherited from the level above. There is an elegant way to avoid restating them: refer to the previous level's condition, composed with the mapping back to it. Formally this is the better choice — nothing is duplicated, nothing can drift out of step, and preservation of the inherited part falls out of the obligations you already have. In practice it is often the wrong choice, because it forces whoever works at this level to walk back up the chain to find out what is legal, and someone working at level five has quite enough to hold in mind from level four.

So the honest rule is to expand the constraints in full at each level even though it duplicates, and to accept the duplication as the price of self-contained documents. The exception is instructive: keep the reference form when the inherited part is large and the new part is small and clearly separable, which is exactly the case where restating would swamp the genuinely new content. Deciding between them is a judgement about the reader's working memory, not about formal hygiene, and the reader's working memory is the thing the whole layered discipline exists to protect.

There is a second, sharper observation about which constraints can live where. A condition can only be stated at a level whose vocabulary contains the things it talks about; a condition about how keys steer a search cannot be phrased before keys exist. So the constraints at each level split naturally into ones carried down and ones newly expressible, and the newly expressible ones are precisely the content of the step. That split is a useful thing to write down deliberately: it tells you what the step actually decided, as distinct from what it merely inherited.

**Source:** [Development Methods for Computer Programs including a Notion of Interference](../works/development-methods-for-computer-programs-including-a-notion-of-interference.md) — the inheriting-invariants subsection of the data-refinement chapter: the disjointness condition restated at two levels, the option of expressing it through the retrieve function, the B-tree development where the ordering condition on the key list can only be stated once the keys are present, and the closing judgement that the aims of a development method may only be met by expanding the invariant at each stage rather than making the designer of one level search back through earlier ones.
