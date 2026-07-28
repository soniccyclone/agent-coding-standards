---
type: lesson
title: "Measuring what exists is not designing what could"
figure: pike
works: [systems-software-research-is-irrelevant]
axes: [verifiability, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Measuring what exists is not designing what could

**Lesson:** Measurement feels like rigor, so it becomes the default activity of anyone who wants to be taken seriously — benchmark the two candidates, chart the latencies, publish the comparison. But every number you produce is a fact about designs someone else already committed to. A comparison ranks the options on the table; it cannot put a new option on the table. A practice that measures exclusively will therefore converge on ever-finer knowledge of a fixed option set, and mistake that convergence for progress, because each individual study is defensible and each one is genuinely about something real.

The reason the substitution is so easy to make is that measurement has a cheap and universally recognized success criterion while design does not. You always know whether you got the numbers; you often cannot tell for years whether a design was worth building. Under any pressure toward legible short-term results — a review cycle, a funding horizon, a quarterly plan — the activity with the crisp criterion crowds out the one without it. The output is not wrong, it is just not the thing anyone actually needed, and no individual decision in the chain looks like the mistake.

The counterweight is to insist that some fraction of effort produce a thing that did not previously exist and can be shown working, and to judge that fraction by whether the machine now feels different rather than by whether a chart moved. Note the asymmetry: a new design can be measured afterwards, but no amount of measurement retroactively generates the design. A programmer who believes this notices when a team's entire output for a quarter is knowledge about other people's systems, treats the profiling-and-comparison reflex as a signal to ask what would be worth building instead, and accepts a weaker success criterion in exchange for the possibility of a new option.

**Source:** [Systems Software Research is Irrelevant](../works/systems-software-research-is-irrelevant.md) — the slide diagnosing the field as too much phenomenology, where observation is said to have displaced invention, together with the closing advice to work on how systems behave rather than only how they compare.
