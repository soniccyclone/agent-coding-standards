---
type: lesson
title: "A shared base is the intersection of its uses, not their union — if you forbid subsets you must make it small"
figure: hoare
works: [the-emperors-old-clothes]
axes: [primitive-count, cognitive-load, hardware-affinity]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# A shared base is the intersection of its uses, not their union — if you forbid subsets you must make it small

**Lesson:** Two policies about a shared foundation are each reasonable and together impossible: that everyone must use all of it, no subsetting permitted, and that it must serve every application area and every deployment target. The first is a demand for uniformity, motivated by portability and by the wish that any two practitioners can read each other's work. The second is a demand for coverage. Holding both forces the foundation to be the union of everyone's needs while obliging everyone to carry the union, which is a guarantee of exactly the situation the no-subsets rule was meant to prevent: a thing too large for any single practitioner to be responsible for. The contradiction resolves in one direction only. If subsets are forbidden, the base must be small.

Small means chosen by intersection, and the criterion is worth stating as a test applied to each candidate feature: is it needed by every application of this foundation, and is it appropriate on every configuration where the foundation is implemented? Anything failing either half does not belong in the base — not because it is bad, but because it belongs in an extension, designed later for the specific hardware or the specific application area that needs it, and carried only by those who need it. Note what this buys the extensions: a base with few features and no need for subsets is strong enough to support several specialized dialects that all remain recognizably the same thing, whereas a base that already contains everything has no room left to be extended and can only be cut down, differently by each user, into mutually unintelligible fragments.

The counterintuitive part is that the intersection discipline is what produces power, not what limits it. A designer under pressure to prove the foundation is capable will add, since every addition is a demonstrable capability while every omission looks like a gap. The result is a plethora of features and notational conventions in place of the original objectives — often the very objectives, reliability and readability and simplicity, that motivated a new foundation at all. When you see those goals traded away for capability, the trade is not a compromise between equals: capability can be recovered by extension later, and the traded goals cannot be recovered at all.

**Source:** [The Emperor's Old Clothes](../works/the-emperors-old-clothes.md) — the closing argument about Ada, where the sponsors' declaration that there shall be no subsets is called the strangest paradox of the project, followed by the rule that a base should include only what is needed for every single application and appropriate for every single hardware configuration with extensions designed specially where needed, and the citation of Pascal's few unnecessary features as the reason it could support specialized extensions for real-time work, simulation and microprocessor workstations; also the earlier note that the language's original objectives of reliability, readability, formality and simplicity were gradually sacrificed in favor of supposed power.
