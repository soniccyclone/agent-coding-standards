---
type: lesson
title: "To state a constraint that spans two structures, build the single structure that contains both"
figure: vardi
works: [on-the-semantics-of-updates-in-databases]
axes: [expressiveness, verifiability, primitive-count]
subdomains: [databases-and-data-management, formal-methods-and-verification]
tags: [lesson]
---
# To state a constraint that spans two structures, build the single structure that contains both

**Lesson:** A relation between two things cannot be stated inside either one of them, which is what tempts people to invent a second mechanism for it — a meta-language, a special operator, a side channel. The cheaper move is to enlarge the object of discourse until the relation becomes an ordinary internal constraint. Vardi's paper does this twice with two apparently unrelated problems, which is what marks it as a technique rather than a trick. To relate a derived presentation to the data it comes from, he considers the structure holding both at once; the defining relationship is then just a sentence that structure satisfies, in the same language as everything else. To handle rules about which transitions are permitted rather than which states are legal, he considers the structure holding the current and next states at once; a rule about change becomes a rule about a single wider state, with the added requirement that an update leave the part representing the past alone.

The gain is not merely notational. Once the relation lives inside a single structure, every tool you already had for reasoning about that structure applies to it — the same solver, the same constraint checker, the same minimality criterion, the same priority ordering. A separate mechanism for temporal rules would need its own semantics, its own proof rules, and its own interactions with everything else; the widened state needs none, because it introduces no new kind of thing. This is the concrete payoff of keeping the primitive count low: not elegance, but the reuse of all existing machinery on a problem the machinery was not designed for.

The same instinct handles "hold this part constant while changing that part." Rather than adding an operator meaning do-not-disturb, record the information to be preserved as ordinary content at the highest standing, and the existing minimal-change rule will protect it automatically. The general pattern to look for: when a requirement seems to need a new construct because it is about your data rather than in it, ask what larger state would make it an ordinary fact. Snapshots plus deltas, before-and-after pairs, request-plus-context, effect-plus-capability — all are cases of paying a little representational width to avoid a whole second formalism.

**Source:** [On the Semantics of Updates in Databases](../works/on-the-semantics-of-updates-in-databases.md) — section four's construction of an extended structure containing both the base relation and the view so that the view definition is a sentence satisfied by it; the later treatment of preserving complementary information by adding it to the store at the highest priority instead of introducing a preservation operator; and the concluding remarks' handling of transition laws by lumping present and next states into one extended database in which the transition laws become ordinary state laws.
