---
type: lesson
title: "Scrutiny held collectively is held by nobody, so partition it and keep a check on the partition"
figure: parnas
works: [active-design-reviews-principles-and-practices]
axes: [parallelizability, cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Scrutiny held collectively is held by nobody, so partition it and keep a check on the partition

**Lesson:** Assigning a whole artifact to a whole group produces less examination than assigning pieces of it to individuals, and the reason is structural rather than motivational. When everyone is nominally responsible for everything, each person's attention spreads thin over the same surface, nobody's judgment is individually attributable, and the parts that look boring get skimmed by all of them identically. The group's aggregate scrutiny is not the sum of its members; it is closer to the maximum of any single member, minus the confidence lost to diffusion. The fix is the same move that makes systems maintainable: divide the work so that each piece has exactly one owner, and make the pieces small enough that owning one is a real commitment rather than a gesture.

Once responsibility is partitioned this way, several other properties follow for free. The examinations become independent, so they run concurrently instead of serially through one meeting's speaking order — and a meeting is a serial resource whose cost grows with attendance while its yield does not. Interaction shrinks to small conversations between the person who made a decision and the one person questioning it, which is where the difficult objections actually get raised; the objection that never survives a room of twelve gets stated plainly to an audience of one. And because each participant's output is a written answer attached to their name, absence of effort becomes visible rather than inferable.

But the partition itself is now the weak link, and this is the part usually missed. If scrutiny is delivered entirely through a fixed set of narrow assignments, then anything nobody thought to assign is guaranteed to pass. The narrower and more disciplined your decomposition of the reviewing job, the more completely a gap in that decomposition hides. So the discipline needs a deliberately unfocused complement: a small number of people asked for an unstructured look at the whole, whose function is not to answer your questions but to notice which question you failed to ask. A programmer who internalizes this treats any checking regime — review assignments, test suites, monitoring dashboards, audit checklists — as having two failure modes, one inside the checks and one in the enumeration of them, and refuses to let the first crowd out the second.

**Source:** [Active Design Reviews: Principles and Practices](../works/active-design-reviews-principles-and-practices.md) — drawn from the critique of conventional reviews (collective responsibility with no part receiving concentrated examination, large meetings suppressing detailed pursuit of specific issues) and the countermeasure of independent, parallel, individually-assigned reviews plus a few deliberately broad ones held in reserve against unposed questions.
