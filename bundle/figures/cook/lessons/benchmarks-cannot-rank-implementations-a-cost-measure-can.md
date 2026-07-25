---
type: lesson
title: "Performance on examples cannot rank competing implementations — define a cost measure parameterized on the dimension that actually drives the work"
figure: cook
works: [the-complexity-of-theorem-proving-procedures]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Performance on examples cannot rank competing implementations — define a cost measure parameterized on the dimension that actually drives the work

**Lesson:** A field can accumulate dozens of competing implementations of the same task and still have no way to say which is better. Running each on a pile of examples gives you something, and it is not worthless, but it cannot answer the question, because a fast time on the cases someone chose to try tells you nothing about the fundamental limits of the approach. What the comparison needs is a cost measure: a function saying how much work the procedure does as the difficulty of the instance grows. Absent that, "which of these is the better method" is not a question with an answer, only a question with opinions and demo timings.

The hard part is deciding what to measure the growth against, and this is where most attempts quietly fail. The obvious knob — the size of the input — is often the wrong one, because it does not track what makes an instance hard. The productive choice is a parameter that measures the intrinsic difficulty of the instance for the class of procedures under study: how much intermediate material has to be generated before the answer becomes forced. Choosing that parameter has consequences you can check in advance. Parameterize on the wrong quantity, and proving a bound on your procedure collapses into some other open question you have no purchase on, so the whole exercise becomes vacuous. Parameterize well, and modest theorems become provable and the boundaries of the approach become visible. Checking which of these you have chosen, before you start proving anything, is part of the work.

Two pieces of intellectual honesty go with this. First, the measure should be admitted to be crude when it is: reducing a procedure's behavior to a single scalar in a single parameter throws away real structure, and a better measure would probably take several parameters — how much material was generated, how much of it turned out to be needed. Publishing the crude version anyway, labeled as crude and offered as a basis for discussion, is more useful than waiting for the ideal measure. Second, the payoff being sought is not a scoreboard but a boundary. A good complexity criterion tells you what a whole family of procedures fundamentally cannot do, which redirects effort toward goals that are not already ruled out. That is a different and better purpose than deciding who wins.

A programmer who takes this seriously treats a benchmark suite as evidence about the cases in the suite and nothing more. Before comparing two implementations, they ask what parameter of the input actually drives the cost, whether their measurements vary that parameter, and whether the resulting picture would still hold on instances nobody has tried. When a component's cost depends on something the benchmark holds fixed, the benchmark is measuring the fixture.

**Source:** [The Complexity of Theorem Proving Procedures](../works/the-complexity-of-theorem-proving-procedures.md) — the sections after the completeness results, which set up an efficiency criterion for mechanical theorem provers by bounding run time as a function of how many ordered substitution instances are needed to force a contradiction, explain why measuring against formula length instead would make the resulting bound equivalent to an already-open question, and close by arguing that the field needs a theoretical criterion rather than example runs while conceding the proposed one is probably too coarse.
