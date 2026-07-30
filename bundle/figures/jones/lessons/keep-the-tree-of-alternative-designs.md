---
type: lesson
title: "Keep the tree of alternative designs, not just the branch you shipped"
figure: jones
works: [development-methods-for-computer-programs-including-a-notion-of-interference]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Keep the tree of alternative designs, not just the branch you shipped

**Lesson:** A design is normally recorded as a single chain from requirement to code, because that is what the finished system needs. But the work itself is a tree: most steps admit several defensible next moves, and only one gets taken. Recording the tree — naming each alternative refinement of a given description, and each alternative refinement of those — costs little at the time and changes what the artifact can be used for. It turns "why is it like this" into a question with a written answer, it lets a later change re-enter the tree at the branch point rather than at the leaf, and it makes the sibling designs available as real options instead of things someone would have to invent from scratch.

The mechanics matter less than the habit, but a naming scheme that mirrors the tree structure is what makes it usable, and it needs one asymmetry: when a step chooses a representation or a strategy, the alternatives are siblings and must be distinguished; when a step merely breaks a description into parts, those parts get fresh names of their own and need not carry the whole lineage. Confusing the two produces either unmanageable names or a tree you cannot navigate.

What most repays keeping the tree is the discovery that the relation between description and implementation is many-to-many in both directions. One description has many valid implementations, which everyone expects. Less expected, and more useful: one implementation frequently satisfies several different descriptions, including ones written later and under weaker assumptions than the code was originally built for. A component written for a quiet single-threaded world can turn out to meet a specification that tolerates concurrent disturbance, with no change to its text — you discover this by checking, not by rewriting. Keeping the tree is what makes such reuse visible, because the several descriptions are all still there to check against.

**Source:** [Development Methods for Computer Programs including a Notion of Interference](../works/development-methods-for-computer-programs-including-a-notion-of-interference.md) — the naming subsection of the data-refinement chapter, which introduces a suffix scheme for alternative refinements and multi-level designs and notes that decomposed sub-operations take new names rather than carrying the numbering; the examples chapter's development diagrams, which show several alternative multi-stage developments from a single specification; and the equivalence-relation development, where one root-finding routine is shown to satisfy three successively weaker-assumption specifications and earlier sequential code is found to satisfy the specifications of the parallel design unchanged.
