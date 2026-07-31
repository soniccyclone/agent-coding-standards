---
type: lesson
title: "Deferring a decision and turning it into data are different moves, and the second costs you self-evident meaning"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [expressiveness, primitive-count]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Deferring a decision and turning it into data are different moves, and the second costs you self-evident meaning

**Lesson:** The authors read data abstraction as an application of least commitment: the barrier lets you postpone choosing a concrete representation until the last possible moment, which preserves freedom in the design. Then they push the principle past where it usually stops. You need not postpone the choice — you can decline to make it, keep both representations, and let each value say which one it is. That is a categorically different move from deferral, and it is worth separating them in your head, because the second is available in situations where "decide later" has run out of road.

Deferral has a deadline. Somebody eventually picks, and everything downstream inherits the pick. Converting the decision into data has no deadline, because the decision is now made per value rather than per program, and the answer can differ between two objects of the same type sitting next to each other. Anywhere you find yourself trying to choose one configuration, one policy, one strategy for a whole system, the question to ask is whether the choice can instead ride along with the individual thing it governs — at which point the argument about which one is right stops needing to be settled.

The price is stated in the same passage and is easy to underrate. A pair of numbers is a perfectly good rectangular complex number and an equally good polar one; asked for the magnitude of that pair, there is no fact of the matter. Once two interpretations share a shape, the shape has stopped determining the meaning, and the meaning has to be carried explicitly or it is simply gone. This is what a type tag is: not bookkeeping, not overhead you might optimize away, but the restoration of information that admitting a second representation destroyed. Any system with plural representations owes this, whether it discharges it with a tag field, a wrapper, a vtable pointer, or a schema version — and one that does not is relying on some convention outside the data, which is a bet that every future reader knows something the value does not say.

There is a mundane corollary the passage does not skip: once two independently designed implementations are to live in the same program, their names collide, and somebody has to systematically qualify them. That is the first, smallest instance of the general problem — coexistence is not free, and the costs it imposes are exactly the ones that a single global choice was implicitly paying for you.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) - the opening of chapter 2 section 2.4.2, which describes data abstraction as an application of the principle of least commitment permitting the concrete representation to be deferred to the last possible moment, then carries the principle further by keeping both the rectangular and polar representations in one system, argues that a distinction is then needed because otherwise the magnitude of the pair (3, 4) has two defensible answers, introduces the type tag attached to each value with its attach-tag / type-tag / contents interface, and notes that the two authors must also keep their procedure names from conflicting by suffixing them.
