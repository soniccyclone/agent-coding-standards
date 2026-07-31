---
type: lesson
title: "Read your proof rule off the construction, and do not settle for its convenient instances"
figure: scott
works: [a-type-theoretical-alternative-to-iswim-cuch-owhy]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# Read your proof rule off the construction, and do not settle for its convenient instances

**Lesson:** When you have built an object as the limit of an iteration — start from nothing, apply the step, repeat, take the limit — the reasoning principle for that object is already determined, and you get it by transcribing the construction into a rule. Show the property holds of the starting point; show the step preserves it; conclude it holds of the limit. Nothing about this is specific to arithmetic, and the rule should be stated without mentioning integers, even though counting is what justifies it in the background argument. That separation matters: the induction lives in the shape of the construction, not in the index set used to describe it, and a rule phrased abstractly applies to every domain built that way rather than only to the ones you can number.

The rule, not the theorems it easily yields, is the asset. Two facts about a least fixed point fall out of such a rule almost immediately — that it really is a fixed point, and that it is below every other one — and it is tempting to bank those two as axioms and drop the rule that produced them. Scott judged this insufficient and gave the reason: there are ordinary facts about fixed points he could see no way to prove except by the general rule. That is the test to apply whenever a general principle looks heavier than its popular corollaries. Corollaries are what you needed last week. A principle is what answers next week's question, and once it has been replaced by its instances that capability is gone silently, because nothing announces the theorem you can no longer reach.

The same logic runs in the other direction and is worth exploiting: if the abstract rule is available, the concrete ones can be *derived* rather than assumed. Ordinary mathematical induction over the integers need not be a separate axiom at all if the integers have been characterized by equations that define them as a fixed point, because then integer induction is just the general rule specialized to that fixed point. A framework organized this way has one reasoning principle where the naive version has several, and the specialized forms arrive with proofs instead of on faith.

**Source:** [A Type-Theoretical Alternative to ISWIM, CUCH, OWHY](../works/a-type-theoretical-alternative-to-iswim-cuch-owhy.md) — Section 3's induction rule and the semantic argument for its validity by iterating the step from the undefined element and passing to the limit, its derivation of the fixed-point and minimality properties as first examples, the remark that the two instances are not the whole story and that a composition theorem about fixed points seemed provable only from the full rule, and Section 4's derivation of integer induction from the recursion equation characterizing the integers.
