---
type: lesson
title: "Bound an accumulating structure from both sides, and you have characterised a family of algorithms rather than checked one"
figure: jones
works: [software-development-a-rigorous-approach]
axes: [verifiability, cognitive-load, parallelizability]
subdomains: [algorithms-and-complexity, formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Bound an accumulating structure from both sides, and you have characterised a family of algorithms rather than checked one

**Lesson:** When an algorithm works by building up a store of intermediate findings and then reading an answer off it, the temptation is to explain the store by explaining the procedure that fills it. Say the other thing instead: state two constraints on the store's contents that make no reference to how it got filled. The upper bound says nothing in it is unjustified — every entry corresponds to something genuinely true of the input. The lower bound says nothing is missing — every fact of a certain shape that holds of the input is present. Neither bound alone is worth much. Together they are a complete account.

The payoff is where the final answer comes from. With the upper bound in hand, a positive answer read off the store cannot be a false alarm; with the lower bound, a negative answer cannot be an oversight. That the concluding test is right stops being something you argue and becomes something you see, because the test is just an instance of one bound and the absence of a mistake is an instance of the other. Compare this with tracing the procedure: there, the test's correctness depends on every step having done its part, and the argument is as long as the algorithm.

The more valuable consequence is what the bounds *fail* to determine. Two constraints on contents say nothing about order of insertion, about which entries are derived from which, about whether the work is done in one pass or many, sequentially or concurrently. Any procedure whose result lands between the bounds is correct, so you have described a family and not a member. That is the right shape for a design record: the bounds are the part that must not change, and everything the bounds leave open is explicitly declared to be a free choice, which is where the performance work and the parallelisation both live. If you find your characterisation pins down exactly one algorithm, you have written down more than correctness required and you have quietly forbidden alternatives you may want later.

One caveat about when this is available. The two-sided characterisation is usually not something you can pull out of the air; it comes from an established body of theory about the problem area, and where no such theory exists you will have to fall back on the chain of small justified steps from the description down to the code. The chain always works. The direct argument is shorter when the domain has been studied enough to supply the vocabulary, and noticing that it has is worth the check.

**Source:** [Software Development: A Rigorous Approach](../works/software-development-a-rigorous-approach.md) — chapter 18's "*Alternative Proof" section for Earley's recognizer, which having justified the algorithm by a chain of argument from the specification observes that because the problem area has a well-developed theory a more direct proof is possible; its plan of stating constraints on the contents of the status structure so that the final test's correctness is obvious and the algorithm is easily seen to satisfy them; the explicit remark that this is only one algorithm with the property and that the constraint leaves much freedom; and the constraint's construction as an upper bound requiring every recorded item to be a valid item for its position together with lower bounds requiring the initial item and every derivable item to be present.
