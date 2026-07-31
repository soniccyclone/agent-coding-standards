---
type: lesson
title: "When you know a generalization is coming, refuse to state the laws it will break"
figure: hoare
works: [communicating-sequential-processes-book]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# When you know a generalization is coming, refuse to state the laws it will break

**Lesson:** You are developing a theory of a restricted case and you already know the restriction will later be lifted. Some of the facts available to you now hold *because* of the restriction and will become false when it goes. They are true today, they are true of everything currently in the system, and stating them would make the present exposition shorter and slicker. Refuse to state them. Publish only the facts that will survive the generalization. What that buys is that everything anyone learns, quotes or builds upon remains valid across the transition — the generalization becomes an extension rather than a revision, and no work done in the meantime has to be re-audited when it lands.

The cost is real but bounded and lands on you. You forgo convenient reasoning in the restricted setting and occasionally take a longer route to a result the doomed law would have given in one step, and you pay that once, during construction. The alternative cost is unbounded, lands on everyone else, and is denominated in the worst currency available: rules that used to be true. Someone who has internalized a rule does not re-derive it when the system grows; they apply it, and it silently yields wrong conclusions in exactly the new situations the generalization was introduced to accommodate. Withdrawing a fact is far harder than withdrawing a feature, because facts have no call sites to grep for and no deprecation warning to emit — they live in people's heads and in old proofs that still look fine.

The discipline that makes this workable is not to throw the doomed laws away but to segregate them and stamp each with the restriction it depends on, and to publish the exception list explicitly rather than leaving readers to discover it. Being able to say "this holds only while X" is worth more than either quoting it bare or suppressing it, because the set of facts that hold only under X is the sharpest available description of how the two theories differ — often the single most useful document about a generalization. The habit transfers well beyond formal work. An interface guarantee that a planned change will invalidate should not be written as a guarantee. A performance property that holds only in the single-node case should never appear without its condition attached. An invariant that depends on one component being the sole writer should name that dependency where it is asserted, not in a design document nobody reads at the moment they rely on it.

**Source:** [Communicating Sequential Processes](../works/communicating-sequential-processes-book.md) — the mathematical-theory section closing the concurrency chapter, which notes that the definition of a process given there is not yet adequate because it cannot represent nondeterminism, that all laws for the general case hold in the restricted one but the restricted case obeys extra laws such as the idempotence of parallel composition, that such laws have deliberately been left unquoted throughout the book so that everything quoted may safely be applied in the general case, and which then lists by number the small set of laws that do become false once the chaotic process is admitted.
