---
type: lesson
title: "When features serve disjoint audiences, the system has already split"
figure: stonebraker
works: [one-size-fits-all]
axes: [primitive-count, cognitive-load]
subdomains: [software-engineering-and-architecture, databases-and-data-management]
tags: [lesson]
---
# When features serve disjoint audiences, the system has already split

There is a recognizable late stage in a general-purpose system's life where its feature list stops being a list of capabilities and becomes two lists interleaved. One index structure is right for one class of user and useless to the other; one view mechanism helps here and never there; one storage encoding pays off in one regime and is pure loss in the other. Each addition was individually justified, so nobody notices that the union no longer describes a single system. The unity that remains is the entry surface — one language, one installer, one name — while behind it two engines with disjoint mechanisms coexist.

Recognizing that state matters because a shared surface is very effective at concealing it. As long as users write against the same interface, the system can be described, sold, and reasoned about as one thing, and the internal split reads as breadth rather than as fracture. The concealment is not free: every mechanism admitted for one audience is carried, tested, documented, and reasoned about by everyone, including the half of the user base that can never benefit. The maintenance burden scales with the number of internal regimes even when the external count stays at one, which is exactly the accounting error that makes a merged system look cheaper than two honest ones.

The practical discipline is to audit features by audience rather than by merit. For each mechanism, ask which class of workload it serves and which class it is dead weight for; then look at whether those classes partition. If they do, you are maintaining several systems and hiding the fact from yourself. Sometimes preserving the common surface is still the right call — a shared front end is real value for users who straddle both regimes — but that decision should be made knowingly, as a choice to pay for a compatibility layer, not held as a belief that the system is still singular. And when the divergence reaches the point where even the surface cannot be shared, the merge has nothing left to defend it.

**Source:** ["One Size Fits All": An Idea Whose Time Has Come and Gone](../works/one-size-fits-all.md) — the early argument that mainstream products already contain distinct transactional and analytical engines joined only by a common parser, and that each market keeps demanding features worthless to the other.
