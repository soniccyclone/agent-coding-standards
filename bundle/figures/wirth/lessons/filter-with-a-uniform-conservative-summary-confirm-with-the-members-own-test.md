---
type: lesson
title: "Filter with a uniform conservative summary, confirm with the member's own test"
figure: wirth
works: [project-oberon]
axes: [expressiveness, cognitive-load, hardware-affinity]
subdomains: [programming-environments-and-object-systems, algorithms-and-complexity]
tags: [lesson]
---
# Filter with a uniform conservative summary, confirm with the member's own test

**Lesson:** A container that holds members of kinds it deliberately does not know about still has to answer questions about them — which member is at this point, which members fall entirely inside this region, which are affected by this change. There are two ways to get an answer and the good design uses both in a fixed order. Require every member, as a condition of admission, to publish a small summary of itself in a uniform format the container understands — an extent, a range, a key interval — chosen so it is *conservative*: it never excludes a member that might qualify. The container can then scan the whole collection and decide most questions arithmetically, with no dispatch and no knowledge of what any member actually is. Where the conservative answer is not good enough, ask the member itself through its own operation, which knows its true shape.

The ordering matters because it is what keeps the two costs in their proper places. The uniform test is cheap and runs over everything; the exact test is expensive, possibly indirect, and runs only over the survivors. Getting this backwards — dispatching to every member first and using the summary as a late refinement — costs the same correctness and much more time, and it also forfeits the structural benefit: with the summary in the base record, the container's search code is written once and never revised when a new kind of member is invented. That is what makes an extensible collection genuinely extensible. If the container had to understand each member to locate it, every new kind would edit the container.

The obligation this imposes is worth stating to whoever adds a member kind, because it is easy to get subtly wrong in a way nothing detects. The summary must be maintained in step with the member's real state, and it must err only in the direction of over-inclusion; a summary that is too tight silently loses members from queries, and the failure appears as an object that cannot be selected rather than as a crash. So the rule to write into the base type's contract is not "each member records where it is" but "each member records a region it is guaranteed to lie within", and the difference between those two sentences is the whole of the correctness argument.

**Source:** [Project Oberon](../works/project-oberon.md) — section 13.3's rule that every graphic object records not only its position x, y but also the width and height of the rectangle within which it lies, so that testing whether a point identifies an object or whether an object lies wholly inside a selection rectangle is a search through the linked list using only base-type fields; together with the `selectable` procedure in the per-type method record, which lets an individual object type decide the exact question — and the macro convention by which only a designated sensitive corner counts as a hit.
