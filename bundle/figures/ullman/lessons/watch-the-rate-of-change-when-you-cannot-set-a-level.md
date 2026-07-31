---
type: lesson
title: "When you cannot justify a level, watch the rate of change instead"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# When you cannot justify a level, watch the rate of change instead

**Lesson:** Plenty of decisions come down to a threshold nobody can defend. How large is too large, how diffuse is too diffuse, how many is enough — asked in absolute terms these have no principled answer, because the right value depends on units, scale, and domain specifics that vary between datasets and drift over time. A threshold picked anyway will be wrong somewhere and will need retuning forever. The escape is to stop asking about the level and start asking about the increment. Track how much the quantity moves at each step of the process. While the process is doing something sensible, the increments are small and roughly uniform. When it crosses a structural boundary, the increment jumps, often by more than the accumulated total of everything before it. That jump is the signal, and it is scale-free in a way the level is not.

The reason this works is worth understanding, because it tells you when it will not. A quantity that grows smoothly under legitimate operations and abruptly under illegitimate ones is reflecting a real discontinuity in the data — the boundary between things that genuinely belong together and things that do not. If your process has no such boundary to cross, or if the underlying structure is itself gradual, there is no jump to find and the derivative view will mislead you exactly as badly as the level view. So the check to run first is whether you expect a discontinuity at all, not whether you can compute one.

There is a practical dividend beyond avoiding a magic number: the criterion is self-calibrating against each dataset. The comparison is between one step and the previous steps of the same run, so a dataset with different units, different density, or different scale gets a different effective threshold for free, without anyone reconfiguring anything. That is the property that makes the technique worth reaching for in systems that will run on inputs you have not seen.

The failure mode to guard against is that having detected the jump, you have already taken the step that caused it. The correct behaviour is to undo it and report the state before, which means the process needs to be able to roll back one step, or to look one step ahead before committing. Designing that in is cheap when you know you will need it and awkward when you discover it afterwards, so decide up front whether your process is speculative or committed.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the stopping-criteria discussion of the clustering chapter, which tracks the average diameter across merges, notes that it rises slowly while merges are legitimate and jumps almost as much in one bad merge as in all nine previous ones, and concludes that the last merge should be rolled back.
