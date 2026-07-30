---
type: lesson
title: "A state is not its observable values: keep the worlds nobody believes in, drop the facts that hold everywhere"
figure: vardi
works: [reasoning-about-knowledge]
axes: [cognitive-load, verifiability, primitive-count]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# A state is not its observable values: keep the worlds nobody believes in, drop the facts that hold everywhere

**Lesson:** Two situations in which every observable quantity has the same value can still be genuinely different situations, because who can distinguish what differs between them. Vardi's model makes this explicit and it is easy to get wrong: the temptation is to deduplicate — same values, same state, merge them — and merging destroys the very distinction the model exists to capture, since in one of the merged situations a participant has an alternative in view that in the other it does not. The identity of a state includes its position in the web of indistinguishability, not just its contents. The same trap appears in any system whose behaviour depends on what observers can tell apart: interned values, canonicalized records, memoization keyed on payload.

The complementary error is pruning by impossibility. There are worlds in the model that no participant considers possible and that could never occur — and they still have to be there, because someone considers it possible that someone else considers them possible. Depth of nesting, not one-step reachability, decides what has to be represented. Any argument of the form "this cannot happen, so leave it out" is only valid to the depth at which your reasoning stops, and reasoning about what others believe about others never stops at depth one.

Pointing the other way, there is a clean rule for what to leave out: anything true in every situation under consideration. If a fact holds at all the alternatives, adding it to each state description gains nothing — it belongs to the frame of the model rather than to any particular state. That is the useful sense in which shared background assumptions simplify a design, and also the warning attached to it: the moment a background assumption might fail, or might be doubted by someone, it stops being background and has to enter the state. So the discipline is to put into a state exactly what varies across the possibilities you need to distinguish, no less and no more, and to keep worlds in the model based on nested reachability rather than plausibility.

**Source:** [Reasoning About Knowledge](../works/reasoning-about-knowledge.md) — chapter two's warning that a state is not characterized by the truth values of its propositions because the possibility relation matters too, illustrated by two worlds agreeing on the only proposition yet differing in what is known; the card-game example arguing that worlds a participant knows to be impossible must still appear in the structure because they are reachable through another participant's uncertainty; and the discussion of the muddy children model on which facts can be omitted because they hold at every world, together with the note that if there were doubt about whether a child could see, that information would have to enter the state description.
