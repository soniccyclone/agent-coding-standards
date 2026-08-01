---
type: lesson
title: "Ask whether the arrangement already determines the attribute"
figure: wirth
works: [project-oberon]
axes: [cognitive-load, hardware-affinity, verifiability]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Ask whether the arrangement already determines the attribute

**Lesson:** Before deciding how much a member of a collection must carry, ask which of its attributes are implied by the collection's arrangement and which are not. In a sequence, where each member follows a determinate predecessor, an attribute like position is a function of the predecessor's and can be recomputed on every traversal, so it need never be stored; membership itself supplies it. In a set, where no member stands in any relation to another, the same attribute is independent for each one and must be recorded explicitly. The two designs read almost identically in the source and differ substantially in what they cost: the sequence pays time on each traversal and nothing per member, the set pays storage per member and less time. Moving a design from an ordered domain to an unordered one therefore carries a cost that is invisible at the level of the code and shows up only in the size of the store.

The reason to ask the question in this form is that it also settles the status of the attribute when you do store it. If the arrangement determines it, then a stored copy is a cache and inherits every obligation a cache has — it can disagree with the truth, something must re-establish it after every structural change, and the definition of correct is "equal to what recomputation would yield". If the arrangement does not determine it, then the stored value *is* the truth, and there is nothing to be consistent with. Designs get into trouble by storing a derivable attribute without noticing they have created the first situation, and by hunting for an authority to reconcile against in the second, where none exists.

The subordination is worth keeping straight, though. Storage economy is real but it is not what picks the representation. What picks it is the kinds of things to be held and the operations demanded of the collection — insert, search, delete, or traverse-and-transform — and the derivability question refines a choice already narrowed by those. Answering it first produces the classic error of a structure that is beautifully compact and cannot support the one operation the system exists to perform.

**Source:** [Project Oberon](../works/project-oberon.md) — the opening of section 13.3, contrasting a text, whose elements form a sequence so that an element's position is recomputed from its predecessor's each time it is needed and never stored, with a graphic, whose objects form an unordered set so that each must carry its position explicitly, at a substantially larger storage cost for an equal number of elements; and the immediately following remark that the primary determinants of the representation are nonetheless the kinds of objects to be held and the operations to be applied to them.
