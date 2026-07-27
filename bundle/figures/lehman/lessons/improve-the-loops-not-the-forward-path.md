---
type: lesson
title: "If a process is a feedback system, improving its forward path barely moves the outcome — the loops set the behavior"
figure: lehman
works: [metrics-and-laws-of-software-evolution-the-nineties-view]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# If a process is a feedback system, improving its forward path barely moves the outcome — the loops set the behavior

**Lesson:** Decades of genuine advances — better languages, more formality, mechanized support, new paradigms — bought real but incremental improvement while the large-scale record of software projects stayed stubbornly poor. The explanation that survives scrutiny is not that the advances were fake but that they all improved the forward path of a system whose behavior is set by its loops. Real development and evolution is a multi-level, multi-loop, multi-agent feedback arrangement: many inputs, many outputs, and a great many paths by which information about outcomes comes back around to change what happens next. Systems of that shape develop their own dynamics and their own global stability, and stability is exactly the property that absorbs perturbations — including well-meant improvements applied at one point. To change the behavior you have to change loops, which means first finding them.

Some of the loops are obvious: users ask for more, so the system grows; growth raises complexity, which slows comprehension and raises error rates, which diverts effort from growth to repair, which slows growth. Positive influence pushing outward, negative influence pulling back, and the visible ripple on a growth curve is the trace those two leave. But most of the loops are neither designed nor even noticed. They pass through people who observe, interpret, communicate, decide, and abstain, on the basis of instructions, experience, and biases they may not be able to articulate, which makes much of the control unplanned and part of it irreducibly stochastic.

The consequence for method is that this class of system will not yield to the analytic tools one would reach for first. With loops numbering in the tens or hundreds, and with agents inside the system carrying implicit models of the system itself — the self-reference that makes exact treatment hopeless in principle — simulation and modelling of behavior beat closed-form analysis. The workable program is to attack from two sides: treat the process as a black box and hunt in its measured history for the fingerprints of feedback control, and separately build explicit models of the internal loop structure and run them to see whether they reproduce what the history shows. Neither alone is convincing; agreement between them is.

A programmer or manager who has internalized this stops expecting a new tool, language, or methodology to transform project outcomes, and stops blaming individual failures on individual causes when the same failures recur across unrelated organizations. Instead they ask what feedback path produced the behavior and whether it can be observed, measured, and acted on — accepting that the answer usually requires expertise beyond software technology itself, in how organizations and people actually regulate their own work.

**Source:** [Metrics and Laws of Software Evolution - The Nineties View](../works/metrics-and-laws-of-software-evolution-the-nineties-view.md) — the statement of the feedback-system law and the FEAST hypothesis, together with the discussion of why investigating it is hard: hundreds of loops, human and partly unconscious control, self-modelling elements, and the resulting choice of simulation plus paired black-box and white-box study.
