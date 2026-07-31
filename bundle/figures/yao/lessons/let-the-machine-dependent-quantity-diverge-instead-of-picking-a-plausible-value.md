---
type: lesson
title: "To get a claim that outlives the hardware, let the machine-dependent quantity diverge instead of fixing a plausible value"
figure: yao
works: [should-tables-be-sorted]
axes: [hardware-affinity, verifiability]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# To get a claim that outlives the hardware, let the machine-dependent quantity diverge instead of fixing a plausible value

**Lesson:** Cost models smuggle in machine parameters, and the most common smuggler is the unit of work. Charging one unit per inspection of a storage cell is only meaningful once you say how much a cell can hold, because a cell wide enough to hold anything is a cell that can be made to carry an arbitrary amount of precomputed reasoning. Two responses are available. You can pin the parameter at whatever today's machines provide, which yields a result that is accurate now, silently expires later, and cannot distinguish an advantage that comes from the problem's structure from one borrowed from the current word size. Or you can let the parameter run to infinity and ask what remains true. The second is the one that produces claims about the problem rather than about the installed base.

Taking the limit does specific work; it is not just asymptotic reflex. Letting the space of possible values grow without bound kills every technique whose advantage came from the values being few enough to serve as addresses — collisions become unavoidable, so any scheme whose speed rested on computing a position from the value being sought loses that footing. What survives the limit is structural, and what dies in the limit was borrowed. That is a diagnostic no amount of benchmarking on fixed hardware can give you, because on fixed hardware the two are indistinguishable by construction. The same limit also cleanly separates families of model that otherwise blur: charging per bit examined and charging per cell examined are different theories with different answers, and the difference only becomes visible when cell width is a free parameter rather than a constant.

The trade is real and should be stated rather than hidden. Results proved in the limit often bite only past sizes nobody will reach, so they answer "is this advantage fundamental" while declining to answer "does this help me." Both questions are legitimate; the mistake is expecting one framework to serve both, or reporting a limit result as operational guidance. The practical arrangement is to keep the two analyses side by side — the limit result to tell you which mechanism your speed genuinely comes from, and a bounded-parameter result to tell you what happens at the sizes you ship — and to be suspicious of any performance argument that has never been run through the limit, because that is precisely the argument that could be resting entirely on a number the hardware happens to supply this decade.

**Source:** [Should Tables Be Sorted?](../works/should-tables-be-sorted.md) — the conclusions section, which names a word-length-independent framework obtained by letting the value space grow without bound as a main theme of the work and lists open problems in that framework; together with the introduction's motivation for studying models equipped with address-computing power, and the bibliographic note contrasting earlier bit-access cost models with the word-access models used here.
