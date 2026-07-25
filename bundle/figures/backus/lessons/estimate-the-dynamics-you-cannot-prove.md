---
type: lesson
title: "When the right static decision depends on unknowable dynamics, estimate the dynamics instead of assuming them away"
figure: backus
works: [the-fortran-automatic-coding-system, the-history-of-fortran-i-ii-and-iii]
axes: [verifiability, hardware-affinity]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# When the right static decision depends on unknowable dynamics, estimate the dynamics instead of assuming them away

**Lesson:** Deciding which values should occupy a scarce set of physical registers is a static decision whose correct answer depends on facts that only exist at run time: which paths through the program are hot and which are barely taken. The standard responses are to pretend the question does not matter, apply a uniform heuristic, or wait for a theory. A third response is to estimate. Simulate the program's execution, resolve each conditional branch with a weighted random draw, count how often each straight-line block is entered, and use those counts to decide. The costly operations of saving and restoring registers can then be pushed out of the frequently executed paths and into the rare ones, which is where the entire benefit lives.

Two supporting ideas make this more than a trick. First, the simulation needs a distribution, and some of what determines it is knowledge only the program's author has. So give the author a channel to declare expected relative frequencies of branches and loops, treated as input to the optimizer rather than as part of the program's meaning. Design for the case where the tool is missing information a human already possesses, instead of pretending the tool can derive everything. Second, be exact about the epistemic status of the result. No procedure was known to be optimal for general programs with loops; what the team had was a policy with convincing arguments behind it that empirically appeared to produce code that was very hard to improve, and whose straight-line behavior was only later shown, elsewhere, to coincide with a provably optimal replacement policy. Shipping on empirical adequacy while being clear that it is not proof is a defensible position; confusing the two is not.

A practitioner who internalizes this stops treating "we cannot know the runtime behavior statically" as a reason to ignore runtime behavior. Measure it, simulate it, or ask the author for it, and let the estimate drive the decision. The corresponding discipline is to keep the estimate's role visible, so that when the estimate is wrong the failure is a bad guess in a known place rather than a mystery in the output.

**Source:** [The FORTRAN Automatic Coding System](../works/the-fortran-automatic-coding-system.md) — the flow-analysis stage that derives block frequencies by simulated execution with weighted random branch outcomes, and the following stage that uses them to place register loads and stores in the least-frequent paths. Also [The History of FORTRAN I, II, and III](../works/the-history-of-fortran-i-ii-and-iii.md) — the narration of that design choice, the author-supplied frequency declarations that feed it, and the frank note that no provably optimal allocation was known while the shipped policy nevertheless appeared optimal in practice.
