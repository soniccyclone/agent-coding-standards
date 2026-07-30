---
type: lesson
title: "Delivery adds entropy and generalization removes it; each has a visible failure signature when it dominates"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Delivery adds entropy and generalization removes it; each has a visible failure signature when it dominates

**Lesson:** Two kinds of work go on in any organization that ships software from a stock of reusable parts, and the sharpest framing here is thermodynamic. Meeting a specific customer requirement adds special cases, adds volume, and adds coupling — it is entropy-increasing by nature, not by sloppiness, and no amount of care converts it into the other kind. Going back over what shipped, finding the generalization, and folding it into the reusable stock is entropy-decreasing. Both are necessary. What makes the framing useful rather than a slogan is that each direction, allowed to dominate, fails in a specific and recognizable way.

Delivery unchecked ends in collapse under accumulated weight, and the author names the signature: a sharp and rising bug rate. The second-order effect is what makes it a genuine threshold rather than a gradual decline — past a certain complexity, fixing one bug reliably introduces two more, so the usual response of allocating more effort to defects actively accelerates the failure. That is worth holding as a diagnostic, because it means a team whose bug backlog grows while it works harder on bugs is not under-resourced; it has crossed into a regime where the corrective action is to reduce complexity rather than to fix faster.

Generalization unchecked fails in the mirror image and is much harder to see from inside, since every local sign is good: the code is clean, the abstractions are satisfying, the engineers are enjoying themselves. The author's line about that state — nice and clean, programmers having great fun, revenue stream drying out — records the specific danger, which is that this failure produces no internal complaint. Delivery failure announces itself through defects; investment failure announces itself only through the market, i.e. too late and through a channel engineers do not watch.

The pair yields a habit that neither exhortation alone provides. Instead of asking whether a team is doing enough refactoring in the abstract, ask which failure signature is currently visible: rising defects with rising effort means the entropy-increasing side has been dominant too long, while a clean codebase with no recent shipped capability means the other. Both directions are real risks, both come from doing something genuinely valuable too exclusively, and the honest description of the second failure — as pleasant, and therefore self-sustaining — is the part most treatments omit.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 10 section 10.3's Fountain Model discussion, which calls production an entropy-increasing activity that risks the system collapsing under its own weight, manifest as a sharp and increasing rate of bugs where complexity makes it humanly impossible to fix one bug without introducing two new ones; and calls experience collection an entropy-reducing investment which, if allowed to dominate, leaves functionality inadequate and the revenue stream dry — "a sad situation even if the system is nice and clean and the programmers are having great fun."
