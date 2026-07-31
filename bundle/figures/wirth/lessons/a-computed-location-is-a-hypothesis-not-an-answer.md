---
type: lesson
title: "A computed location is a hypothesis, not an answer"
figure: wirth
works: [algorithms-and-data-structures]
axes: [expressiveness, verifiability, primitive-count]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# A computed location is a hypothesis, not an answer

**Lesson:** Retrieval problems are easier to think about once you state what they are asking for rather than how you have been solving them. Everything ultimately reaches its data by naming a place, so the problem is to find a mapping from identifiers to places — and every structure built to support search, however elaborate, is one implementation of that mapping. Stating it that way is not pedantry; it is what makes visible the option of computing the place arithmetically from the identifier instead of navigating to it, which is a completely different family of solutions that a navigation-shaped statement of the problem hides. Whenever you find yourself comparing variants within a family, try restating the problem as the relation it must implement, and check whether the family you are in is the only one that implements it.

Once the mapping is computed, an unavoidable consequence follows from counting. The set of possible identifiers is enormously larger than the set of available places, so no such mapping can be one-to-one; many identifiers must share a destination. Therefore the location the computation yields is not an answer but a proposal, and the design owes two things it would not have owed otherwise. It must verify — compare the identifier actually stored at the proposed place against the one sought — because a computation that cannot distinguish two identifiers cannot be trusted to have found the right one. And it must have a policy for what to do when verification fails, producing a further place to try, deterministically, so that the same identifier always follows the same trail.

Recognizing this pattern is worth more than the particular case, because a lossy computation followed by a confirming check is a shape that recurs everywhere something is looked up by a summary of itself. The rule to carry: whenever a value is used to compute a location, ask whether the computation can collide, and if it can, the design has three parts and not one — the computation, the verification, and the resolution — and omitting either of the last two does not simplify the design, it converts a slow answer into a wrong one. The failure is also easy to miss in testing, since a collision-free test set exercises only the first part.

**Source:** [Algorithms and Data Structures](../works/algorithms-and-data-structures.md) — section 5.1's restatement of the retrieval problem as finding an appropriate mapping of keys into addresses, with the note that the list and tree search algorithms of the preceding chapter were implementations of that mapping over different underlying data organizations; the observation that the set of possible key values is much larger than the set of available store addresses, illustrated by the count of possible sixteen-letter names against a thousand table positions, so that the function is necessarily many-to-one; and the consequent statement that retrieval has a first step computing the index and a second, explicitly necessary step verifying that the item at that index really carries the sought key, together with the definition of a collision and the requirement that the generation of alternative indices be deterministic so the probe sequence for a given key is always the same.
