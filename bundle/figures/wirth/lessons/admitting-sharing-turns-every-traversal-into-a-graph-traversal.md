---
type: lesson
title: "Admitting sharing turns every traversal into a graph traversal, so give the traversal an identity"
figure: wirth
works: [project-oberon]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [programming-environments-and-object-systems, algorithms-and-complexity]
tags: [lesson]
---
# Admitting sharing turns every traversal into a graph traversal, so give the traversal an identity

**Lesson:** A containment structure starts as a tree because that is what containment naturally is, and every operation written against it silently assumes the tree property: a walk reaches each member exactly once, so anything the walk does per member happens once. Then a feature arrives that lets one member appear beneath two containers — a view of a view, an alias, a shared component, a symbolic link. The feature looks local and its cost looks like one extra pointer. It is not. It converts every existing traversal from a tree walk into a graph walk, and the operations that were correct only because of the once-per-member property become wrong all at once, in a way that produces no error and no crash. An operation that duplicates produces two copies of the shared part instead of one. An operation that counts overcounts. An operation that mutates applies twice.

The failure is worth understanding precisely because it is not a bug in any of those operations. Each is still correct on its own terms; what changed is a global property they all relied on and none of them stated. So the fix has to be global too, and the useful form is to give the traversal itself an identity and require every member to reject a second arrival of the same one. Notice where the state lives in that arrangement: the identity travels on the moving thing, and each member remembers only the most recent identity it has seen. Nothing needs clearing between traversals, because the next traversal simply carries a different identity and every stale remembered value automatically fails to match. Compare the obvious alternative — a visited flag per member — which is correct but obliges every traversal to be bracketed by a reset sweep, an obligation that is easy to forget, expensive on large structures, and impossible to honour if two traversals can overlap.

The transferable rule has two halves. First, whenever you relax a structural invariant to allow sharing, enumerate the operations that were written under the old invariant rather than assuming they are unaffected; the ones at risk are exactly those whose result depends on how many times a member is reached, and that set is usually larger than expected. Second, when you need per-run bookkeeping across a shared structure, prefer a generation stamp carried by the run over a boolean owned by the members. The stamp costs one field and no reset; the boolean costs one field and a sweep you will eventually skip.

The residue is honest to admit: identity comparison only detects repeats, it does not decide what should happen instead. Whether the second arrival should be dropped, merged, or counted is a semantic question per operation, and the mechanism only guarantees that the question gets asked.

**Source:** [Project Oberon](../works/project-oberon.md) — appendix A.2's observation that allowing views of views means paths may join in the display space so its tree structure can no longer be asserted, that in combination with a context-oriented forwarding strategy this may cause undetected multiple arrivals of one message at the same object, illustrated by a copy message arriving twice at a shared component and producing two different copies of it; and the remedy that messages are time-stamped and recipients are required to detect multiple arrivals by comparing time-stamps, realized in the handler sketch by each frame backing up the timestamp of the message it has just accepted and comparing an incoming message's stamp against that backup before processing.
