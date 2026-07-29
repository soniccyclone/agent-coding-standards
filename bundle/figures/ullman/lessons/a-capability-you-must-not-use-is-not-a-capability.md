---
type: lesson
title: "A capability you have to avoid using is not a capability"
figure: ullman
works: [a-comparison-between-deductive-and-object-oriented-database-systems]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# A capability you have to avoid using is not a capability

The sharpest move in this paper is a test, not a claim. When someone answers a criticism by saying "our system supports that too," Ullman asks whether the two supported things survive being used at the same time. His running example is a system that offers both the freedom to introduce new kinds of data whenever you like and the ability to pose short unplanned questions over whatever data exists. Each is genuinely present. But exercising the first one strands the second, because a freshly-introduced kind of data has no operations defined over it yet, so asking anything about it means stopping to write code — and the whole point of the unplanned question was that you did not have to.

He names the pattern with a piece of Vietnam-era gallows humor about having to destroy a village in order to save it. The feature is preserved exactly as long as nobody exercises it. That reframing matters because feature lists are checked for presence, never for compatibility-in-use, and the space of pairwise interactions is where systems actually fail. A capability that only works while a neighboring capability sits idle should be recorded on the list of things the system cannot do.

Notice this is not the same as a tradeoff dial, and confusing the two is what makes the failure hard to see. A dial you can set anywhere on the range and live at the setting. What Ullman is describing is a pair of properties where the useful region is at the ends: you get the dynamic vocabulary or you get the ad-hoc interrogation, and every intermediate position gives you a system where both features exist and neither pays off. The honest design move is picking an end and building for it, rather than shipping the middle and letting users discover the interference.

The habit this builds is to interrogate any claimed superset. When a design claims to subsume an older, more restrictive one, look for the restriction that the older design was actually exploiting. Restrictions are what let a system make promises about things it has not seen yet — closure of an operation set over all producible values, uniform access to any result, a fixed meaning for a name. Removing the restriction removes the promise, and the promise was usually the reason the old design was worth copying.

**Source:** [A Comparison Between Deductive and Object-Oriented Database Systems](../works/a-comparison-between-deductive-and-object-oriented-database-systems.md) — the dynamic typing and ad-hoc query discussion in the "why the two don't mix" section, and the reprise of the same argument at the end of the declarativeness section.
