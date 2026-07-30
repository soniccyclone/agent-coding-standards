---
type: lesson
title: "Model a type with exactly the distinctions its operations can observe, and no more"
figure: jones
works: [development-methods-for-computer-programs-including-a-notion-of-interference]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# Model a type with exactly the distinctions its operations can observe, and no more

**Lesson:** When you describe a type by giving a concrete structure and defining its operations over that structure, you get a definition that is easy to write, easy to check by reading, and easy to be subtly wrong in one specific way: the structure may draw distinctions that no operation can detect. Describe a set by a sequence and two orderings of the same elements are different values that behave identically. That redundancy is not a cosmetic flaw. It biases the type toward implementations shaped like the structure you happened to pick, because an implementation that also carries the invisible distinction is easy to match up with your definition while one that does not is hard. You have accidentally specified a representation while believing you specified behaviour.

The test is mechanical and worth applying to every model you write: can two distinct values of the structure be told apart by some sequence of the type's own operations? If not, the model is biased and the extra structure must go. There is a positive form of the same check that is usually easier — try to write an equality test using nothing but the type's operations. If you can, the model is clean; if you cannot, either your model carries invisible detail or the operation set is too weak to pin down what you claimed. Note the sensitivity to the operation set: remove an observer from the interface and a previously clean model becomes biased, because what counts as an observable distinction is defined by the interface, not by the data.

Two refinements follow. First, when several unbiased models exist they are interchangeable in principle, so choose among them by the complexity of the constraints each needs to rule out nonsense values — a model requiring an elaborate side condition to stay legal is a worse starting point than an equivalent one that is legal by construction. Second, unbiasedness is a property demanded of specifications, not of implementations. A design deliberately introduces redundancy the moment maintaining a canonical form gets too expensive, and that is entirely legitimate; what matters is knowing which artifact you are writing. Redundancy in the thing you are building is an engineering decision. Redundancy in the thing you are building it against is a mistake that will make every future implementation harder to justify.

**Source:** [Development Methods for Computer Programs including a Notion of Interference](../works/development-methods-for-computer-programs-including-a-notion-of-interference.md) — the implementation-bias subsection of the specification chapter: the list-as-set example, the definition of bias as indistinguishability of carrier elements by any term of the operations, the equality-function test and how it degrades as operations are removed, the preference for carriers with simpler invariants among isomorphic models, the buffer-with-counters case found in the literature; and the design subsection of the data-refinement chapter, where bias and complex invariants are said to arise legitimately during design.
