---
type: lesson
title: "Grouping erases where a value came from, so make origin part of the value"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, verifiability, primitive-count]
subdomains: [databases-and-data-management, distributed-systems-and-concurrency]
tags: [lesson]
---
# Grouping erases where a value came from, so make origin part of the value

**Lesson:** Any mechanism that collects things by a key is, by construction, an information-destroying step: it tells the consumer what values share a key and deliberately forgets everything about how they arrived. That is exactly what you want for a sum or a count, where the answer is a function of the multiset alone. It is fatal for any question whose answer depends on provenance — was this item present in both inputs, or only one; did it come from the side we are subtracting or the side we are keeping; is this pair an inner join partner or two rows of the same table. Once the collection has happened, the distinction is not recoverable by any amount of cleverness in the consumer. The information was thrown away one stage earlier.

The fix is unglamorous and worth internalising as a reflex: if the downstream answer distinguishes sources, promote the source into the payload before the merge, so that grouping preserves it as ordinary data instead of destroying it as metadata. And the payload should carry the smallest thing that restores the distinction — a tag, a bit, a discriminant — not a copy of the source it names. This is the difference between a design that scales and one that ships an entire relation alongside each row because someone reasoned "the consumer needs to know which relation this is." Set difference, intersection, join, and outer join all fall out of the same one-bit trick applied to the same key-grouping primitive; what varies between them is only what the consumer does when it inspects the tags on a key's value list.

The wider habit is to look at every place your data merges and ask what the merge is quietly discarding. Union types collapsed into a common shape, events from different producers appended to one log, results from several services concatenated into one array, rows loaded from several files into one table — each is a grouping step, and each will eventually be followed by a question that needed the distinction. It is cheap to carry a discriminant from the start and free to ignore it; it is often impossible to reconstruct one later, because the reconstruction requires rerunning the producers. Deciding *at the merge* what the merged form must still be able to answer is a design step, not an afterthought.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the MapReduce implementations of the relational operators, particularly the contrast between union and intersection (which need only the length of a key's value list) and difference and natural join (which require each mapped value to carry a bit naming its originating relation), plus the explicit warning that the tag should be a bit, not the relation itself.
