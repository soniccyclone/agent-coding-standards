---
type: lesson
title: "Extending one part alone is meaningless; extend the arrangement"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Extending one part alone is meaningless; extend the arrangement

Reenskaug makes a small observation with large consequences: there is no point in deriving a specialized version of a component that adds a capability unless you are simultaneously deriving whatever will use that capability. A new ability nobody exercises changes nothing about how the system behaves. So specialization is never really an operation on one component — it is an operation on a group of components, of which the conventional mechanism happens to let you write down only one at a time.

Once seen, this explains why single-component specialization is so often unsatisfying in practice. The mechanism records that a part gained something, and says nothing about the collaboration that gained a new capacity, which is the change anyone actually cares about. The story of what the extension is for lives in the relationship between the extended part and its counterparts, and that relationship has no textual home, so it survives as tribal knowledge and gets rediscovered by whoever maintains it next. Extension also drifts toward being justified by convenient code sharing rather than by any conceptual relationship, and while sharing code is a legitimate motive, conflating it with conceptual specialization means the structure can no longer be read as an argument about the domain.

The lift Reenskaug proposes is to make the whole arrangement the unit that gets specialized: a derived arrangement takes on the participants, the connections, and the behavior of the arrangement it derives from, and adds participants or extends behavior across several of them at once. Reuse then delivers a working story rather than a bag of capabilities, and the specialization relationship carries its own explanation, since you can see what the added capability is for by looking at who now uses it.

A programmer holding this distrusts any extension point that can only describe one participant, and when specializing a component asks which counterpart must change with it — treating the answer as part of the same change rather than as follow-on work. The reusable asset worth building is the smallest complete arrangement that does something, not the most capable individual part.

**Source:** [Working with Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — the comparison-with-other-methods discussion of why inheritance must apply to whole models, together with the technology overview's treatment of synthesis as inheritance lifted from the individual component to the collaboration.
