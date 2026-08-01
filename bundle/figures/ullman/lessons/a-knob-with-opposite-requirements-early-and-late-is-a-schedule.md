---
type: lesson
title: "A knob with opposite requirements early and late is a schedule, not a value"
figure: ullman
works: [mining-of-massive-datasets]
axes: [cognitive-load, verifiability]
subdomains: [algorithms-and-complexity, distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---
# A knob with opposite requirements early and late is a schedule, not a value

**Lesson:** Some tuning parameters resist tuning in a characteristic way: every argument for raising them is sound and every argument for lowering them is also sound. Set the step of an iterative refinement too small and it takes forever to get anywhere; set it too large and it overshoots and never settles. Someone in this position starts hunting for the value that balances the two complaints, and can spend a long time hunting, because there frequently is no such value. The complaints are not in balance, they are attached to different phases of the run. Far from the answer, only speed matters and precision is meaningless. Near the answer, only precision matters and speed is wasted. A single number is being asked to serve two regimes with opposite needs, and the reason it feels impossible to choose is that it is.

The recognition to make is that a symmetric pair of failure modes with a phase structure is a signal to replace the constant with a rule that varies. The rule can be very crude and still beat any constant: start at the value the early phase wants, shrink toward the value the late phase wants as the run proceeds, stop shrinking at some floor. Two or three parameters have replaced one, which sounds like a loss, but they are far less delicate than the one they replaced, because none of them is being asked to do two jobs. Getting the decay roughly right is enough, whereas getting a single constant roughly right is not.

The same shape shows up well outside numerical optimisation. Retry intervals want to be short while a failure might be transient and long once it clearly is not. Cache lifetimes want to be short while a workload is unfamiliar and long once it is characterised. Sampling rates want to be high while a distribution is unknown and low once it is pinned down. Batch sizes want to be small while feedback is valuable and large once it is not. In each case the standard advice is to find the right constant, and in each case the arguments on both sides remain valid at that constant, which is the tell.

Two cautions keep this from becoming a reflex. First, a schedule is a commitment to a story about how the run proceeds, and if the story is wrong — the situation is not converging, the workload is not stabilising — the schedule will confidently move the knob in the wrong direction and there is no feedback loop to notice. Where a cheap signal about the current phase exists, driving the knob off the signal is better than driving it off elapsed time. Second, a schedule makes runs no longer comparable to one another unless the schedule is held fixed, so it has to be recorded as part of the configuration rather than treated as an implementation detail of the loop.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 13's treatment of the learning rate in the gradient-descent section, which notes that too small a value means convergence may take a very large number of iterations while too large a value may cause the parameters to oscillate and never converge, concedes that choosing it is usually a matter of trial and error, and then describes the common practice of starting from an initial rate and multiplying it by a factor below one at each iteration until it reaches a sufficiently low value.
