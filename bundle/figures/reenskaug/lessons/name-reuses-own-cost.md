---
type: lesson
title: "Reuse costs you the fresh look, and the person advocating it should be the one to say so"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Reuse costs you the fresh look, and the person advocating it should be the one to say so

**Lesson:** The case for reusing proven descriptions is easy to make and largely correct: it cuts development cost and elapsed time, it raises quality because the reused piece has already been exercised, and it lets you protect something delicate by forcing all access through a validated intermediary. What is unusual is to see that case immediately followed, by its own advocate, with the principal cost — that building on established descriptions encourages you to keep building on them, and the habit quietly removes the fresh outlook that discovering something new requires. Reuse is a bet that the existing decomposition of the problem is still the right one. Every time the bet pays off it becomes harder to notice when it stops paying.

That framing is worth more than the individual trade-off, because it is a template for how to hold any practice you are advocating. A technique presented with only its benefits gives a reader nothing to reason with; the reader must either accept it wholesale or reject it wholesale. A technique presented with the specific mechanism by which it degrades gives the reader a test they can apply to their own situation — here, "am I reaching for the existing model because it fits, or because it exists?" The cost is not a disclaimer bolted on for balance; it is the part that makes the advice usable.

For a programmer the practical residue is to keep the question live rather than settled. Before composing from what you have, spend a moment asking what a person who had never seen these pieces would build, and treat a large gap between that answer and your assembly as information rather than noise. Sometimes the gap means your library is good and the newcomer would waste effort. Sometimes it means the problem has moved and your pieces are now the wrong shape, which is precisely the thing reuse is structurally unable to tell you.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 3's summary of why models are composed rather than extended, which lists reduced cost, increased quality through tested components, and integrity protection via mandatory validated access, then names blindly building on old models and the consequent loss of fresh outlook as the main disadvantage.
