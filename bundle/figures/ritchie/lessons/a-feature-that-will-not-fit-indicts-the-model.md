---
type: lesson
title: "A feature that will not fit is evidence against your model, not a case for a special rule"
figure: ritchie
works: [the-development-of-the-c-language]
axes: [expressiveness, hardware-affinity, primitive-count]
subdomains: [programming-languages-and-semantics, operating-systems-and-systems-programming]
tags: [lesson]
---
# A feature that will not fit is evidence against your model, not a case for a special rule

**Lesson:** Ritchie identifies one specific moment as the decisive break between the typeless ancestor and the typed language. He had inherited a model in which declaring an array allocated a named cell, allocated the elements, and stored the address of the first element into the cell — a pointer that physically exists in memory. Adding record types broke it. If a record contained an array, where would the compiler put that materialized pointer? Worse, and this is the part that mattered, he insisted a record should describe not merely an abstract object but an actual pattern of bits that could be read straight off the disk, such as a directory entry. There is no room in that pattern for a hidden pointer. Even granting some way to hide it, initializing the hidden pointers of records containing arrays containing records to arbitrary depth was a problem with no clean answer.

The escape was not a special rule for arrays inside records. It was to change what an array is: stop storing the pointer at all, and generate it at the moment the array's name appears in an expression. That single redefinition let records be laid out as pure data, kept nearly all existing code working, and opened the way to composing types generally. The obstruction had been telling him the representation was wrong, and the payoff came from believing it.

Two things generalize. First, when a new capability cannot be fitted into a design, the honest reading is usually that the design encodes a mistaken commitment, and the productive move is to go find which one rather than to carve out an exception. Exceptions cost less today and compound; re-derivations cost more today and simplify. Second, the discipline that forced the issue was refusing to let the abstraction float free of the bytes it had to describe. Had records been allowed to be merely abstract, the hidden pointer would have been tolerable and the flawed model would have survived. Requiring a data type to name real external layout is a constraint that catches representational errors nothing else catches.

A programmer who believes this treats "we cannot express X without a special case" as a diagnostic to be chased, not an obstacle to be routed around. They ask what the model currently insists on that makes X impossible, and whether that insistence was ever load-bearing. And they deliberately hold their data models against the external formats they must interoperate with, because that is the test that exposes representations quietly carrying invisible extra state.

**Source:** [The Development of the C Language](../works/the-development-of-the-c-language.md) — the "Embryonic C" section, where attempting to add structured types to the intermediate language exposes the impossibility of a stored array pointer and leads to the rule that array values become pointers when mentioned in expressions.
