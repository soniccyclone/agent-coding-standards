---
type: lesson
title: "Permission to depend has to be earned in both directions"
figure: parnas
works: [designing-software-for-ease-of-extension-and-contraction]
axes: [cognitive-load, verifiability, primitive-count]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Permission to depend has to be earned in both directions

Most projects treat a dependency as something a programmer takes when it helps. Parnas treats it as something the design grants, subject to a test with four conditions, and the shape of that test is more instructive than the conditions themselves. Two of them are about complexity and they run in opposite directions: the upper party must come out genuinely simpler for leaning on the lower one, and the lower party must not be made appreciably more complicated by being forbidden to lean back. The second half is the one nobody checks. A dependency edge is not free for the thing at the bottom of it; being pinned beneath something costs it the facilities above, and if that cost is large the edge is wrong even when the party asking for it benefits enormously.

The other two conditions are not about complexity at all, which is what makes the test unusual. They ask what configurations the edge creates and destroys. An edge is admissible only if some worthwhile system contains the lower part without the upper one, and only if no worthwhile system could contain the upper part without the lower one. Read together, those two say a dependency is legitimate exactly when it matches a real cut in the space of systems you might want to deliver. If you can picture a useful configuration that includes the caller but not the callee, then the edge silently forecloses that configuration, and the honest conclusion is not that the configuration is unimportant but that the structure is wrong.

Adopting this changes what a design review of dependencies looks like. The question stops being whether the reference is reasonable and becomes four separate questions, each of which can be answered wrongly on its own: is the client actually simpler, is the supplier actually unharmed by the ordering, does a subset exist below the edge, and is there no subset that wants the top without the bottom. Notice also what supplies the answers to the last two — the catalogue of reduced systems you decided you wanted before the design began. Without that catalogue the test has no content, which is the mechanism by which "we never worked out what subsets matter" turns into "any dependency is as good as any other."

**Source:** [Designing Software for Ease of Extension and Contraction](../works/designing-software-for-ease-of-extension-and-contraction.md) — the four conditions proposed for allowing one program to use another, in the section on criteria for the uses structure.
