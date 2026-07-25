---
type: lesson
title: "A practice is a fit to conditions, and the conditions move"
figure: boehm
works: [a-view-of-20th-and-21st-century-software-engineering]
axes: [hardware-affinity, cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# A practice is a fit to conditions, and the conditions move

**Lesson:** Boehm reads five decades of his field as a repeating cycle: a position, a reaction against its real failures, then a hybrid that keeps what the reaction discarded too eagerly. What makes this more than a tidy narrative is the mechanism he attaches to it. Each generation's remedy is calibrated to the cost structure of its moment, and each remedy generates the pathology the next generation reacts to. Machine time vastly more expensive than programmer time produced habits of hand-checking before submitting a run, and those habits were correct. When the ratio inverted, the same habits became waste, and the instinct to save microseconds outlived the economics that justified it. Cheap modification of software relative to hardware produced a change-freely culture, which produced unmaintainable tangles, which produced heavy sequential discipline, which produced document-bound slowness, which produced the reaction against it. Nobody in that chain was stupid. Each was solving the problem in front of them with the constraints they had.

The practical discipline that follows is to treat any inherited practice as a compressed answer to a question you can no longer see, and to go recover the question. What was scarce when this rule was made? Is it still scarce? A rule whose enabling condition has expired does not announce itself; it persists as professionalism, and it is defended on aesthetic grounds long after its economic basis is gone. This is why Boehm bothers to separate, decade by decade, the principles that survive the shift in conditions from the practices that were correct only under conditions now gone. He also inverts the usual admonition about history: repeating the past is fatal in a regime that changes underneath you, and repeatability as a virtue deserves suspicion for exactly that reason.

Note that this cuts against the newest thing as well as the oldest. He is explicit that slogans get adopted as identity and applied past their range, including the slogans of the movements he is otherwise sympathetic to. A practice adopted because it signals membership is no better grounded than one retained out of habit.

A programmer who thinks this way asks of every convention what resource it was rationing, and re-derives rather than inherits. When they see a benchmark, a coding rule, or an architectural taboo, they look for the hardware and cost regime it was tuned against, and they accept that some of their own hard-won instincts have an expiry date they will not be notified about.

**Source:** [A View of 20th and 21st Century Software Engineering](../works/a-view-of-20th-and-21st-century-software-engineering.md) — the framing of the field's history as a thesis-antithesis-synthesis chain, the machine-time-versus-programmer-time anecdote and cost-crossover data driving it, and the closing separation of timeless principles from aging practices decade by decade.
