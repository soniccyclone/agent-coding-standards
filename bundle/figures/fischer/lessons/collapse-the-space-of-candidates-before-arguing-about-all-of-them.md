---
type: lesson
title: "Before reasoning about every possible implementation, collapse them into one canonical form"
figure: fischer
works: [a-lower-bound-for-the-time-to-assure-interactive-consistency]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [formal-methods-and-verification, distributed-systems-and-concurrency]
tags: [lesson]
---

# Before reasoning about every possible implementation, collapse them into one canonical form

**Lesson:** A claim about every possible program is unmanageable if taken literally, because the space of programs is vast and mostly irrelevant. The move that makes such claims tractable is to prove first that the space folds. Show that any implementation meeting the requirement can be converted, without cost in the resource you are measuring, into one drawn from a much smaller normalized family. From then on the argument only has to defeat the normalized family, and the conclusion still binds everything, because the conversion was lossless in the dimension that matters.

Two folds are performed before the actual bound is attempted. The first says that if only elapsed rounds are being counted, there is no advantage in cleverness about what to transmit: a component may as well relay everything it knows on every round. Withholding cannot help, since a recipient can always recompute a smaller message from a larger one, and there is no point withholding from a broken component either, because a broken component was free to fabricate the missing content anyway. This kills the entire dimension of message-design cleverness in a paragraph. It also collapses history into a single object, because a component that always relays everything and includes itself among the recipients can be treated as if its whole decision were a function of the final round's arrivals alone. The second fold says the components may as well all run identical code, because any disagreement between two components on an observation both could plausibly have is already excluded by the agreement requirement itself, given enough honest participants to witness the substitution.

Each fold consumes an assumption, and those side conditions are the interesting part, because they say which resource the eventual bound actually constrains. Relaying everything is free when rounds are the only ledger, and ruinous the moment traffic is on the ledger too — so the same normalization that is legitimate for a latency bound is illegitimate for a bandwidth one. Running identical code everywhere needs enough honest participants that two situations can be pinned together by a shared witness. A reduction is not a bookkeeping preliminary; it is where the scope of the theorem is decided.

What is striking is how much of the real work happens in these reductions rather than in the theorem. Once every candidate is a single function over final-round observations, the remaining argument is short: order the possible observation patterns, walk from an all-low pattern to an all-high one, and note that adjacent patterns are covered by a common scenario. The reductions bought a setting in which that walk is even expressible. Without them there is no single function to walk over, only a fog of possible protocols.

A programmer meets the same situation whenever a claim has to hold across an open-ended set of cases: all callers, all configurations, all input schemas, all scheduling orders. The productive question is not "how do I test all of these" but "what is the quotient". Find the transformation that maps every case to a representative without changing the property in question, argue about the representatives, and state the transformation explicitly, since it is now carrying the generality of the whole result. The same reflex read backward is a debugging tool: when a reduction like this fails to go through, the thing that blocks it is usually exactly the asymmetry the real system depends on.

**Source:** [A Lower Bound for the Time to Assure Interactive Consistency](../works/a-lower-bound-for-the-time-to-assure-interactive-consistency.md) — the motivation section's argument that relaying maximal information loses nothing when rounds are the only cost, together with the following section's reduction showing that a protocol running identical code everywhere exists whenever any protocol does.
