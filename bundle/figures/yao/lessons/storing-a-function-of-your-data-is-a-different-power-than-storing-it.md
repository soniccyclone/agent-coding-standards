---
type: lesson
title: "Permission to store a function of your data is a different power from permission to store the data"
figure: yao
works: [should-tables-be-sorted]
axes: [expressiveness, hardware-affinity]
subdomains: [databases-and-data-management, algorithms-and-complexity]
tags: [lesson]
---
# Permission to store a function of your data is a different power from permission to store the data

**Lesson:** Two capabilities get confused whenever people reason about data layout. One is freedom in *where* things go — computing an address from the item you are looking for, following links, choosing an arrangement per input set. The other is freedom in *what* the storage may hold — a value that is not one of the items at all, but something derived from the whole collection. The first is what a random-access machine gives you and what every familiar structure exploits; ordering, hashing, and link-chasing all differ only in how they compute positions. The second is a strictly larger power, and the gap between them is not a constant factor. Grant only address freedom and, once the value space is wide enough relative to the collection, no arrangement beats the obvious ordered one: the number of lookups must grow with the collection. Grant the second freedom — even a single extra location holding one derived value — and the cost collapses to a fixed couple of lookups regardless of size.

The mechanism is worth understanding because it recurs. A derived value can act as a selector: it names, out of a prearranged catalogue of ways the collection might have been distributed, the one actually used, and that name is enough to send every subsequent lookup straight to the only place its target could be. The catalogue is the real object being designed, and the derived cell is a pointer into it. So the design question is not "which layout" but "how much of the answer can be precomputed into a value that is not itself part of the data." Note also which side of the line the classic structures sit on. They are all on the weak side, which is why they cluster around the same cost and why the feeling that nothing better exists is well-founded — inside that model.

Two habits follow. When a bound tells you your data structure cannot improve, read the model for the capability it withheld rather than accepting the bound as a fact about the problem; the withheld capability is usually the cheapest thing in the system to add. And when you do add derived state, be honest that you have changed the model, not merely optimized within it: derived state must be recomputed when the collection changes, which is precisely the cost the weak model was avoiding. The trade is not layout against layout, it is maintenance of a derived summary against per-query work.

**Source:** [Should Tables Be Sorted?](../works/should-tables-be-sorted.md) — the contrast between the paper's general lower bound, proved in a model where the storage may hold only the given items and pointers among them and therefore covering ordering, hashing, lists and trees alike, and the later two-probe result showing that permitting one additional cell to hold an arbitrary derived value drops the cost to a constant; together with the conclusions section, which separates the addressing power of a random-access machine from the encoding power that arbitrary contents provide.
