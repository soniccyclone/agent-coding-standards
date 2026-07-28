---
type: lesson
title: "Find the smallest thing that could possibly run, and treat that as a requirement"
figure: parnas
works: [designing-software-for-ease-of-extension-and-contraction]
axes: [primitive-count, cognitive-load]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Find the smallest thing that could possibly run, and treat that as a requirement

Parnas puts a question at the front of design that almost nobody asks there: what is the least this system could do and still be worth anything, and what are the smallest steps by which it grows from there? This is not a design activity that follows requirements gathering — he argues it is *part* of determining requirements, and that a buyer forbidden from dictating how a contractor works can still legitimately demand that particular reduced configurations exist, because their existence is an observable property of the delivered software.

The hard part is that you cannot get the answer by asking. Users overstate what they need, and their answers describe only the reductions someone happens to want today, not the ones that will be wanted later. Worse, the truly minimal configuration is usually a system no customer would ever order — useful as scaffolding and as a target during development and testing, not as a product. So identifying it is a demanding act of imagination rather than a survey, and the payoff comes from pushing the increments smaller than any user would think to ask for, because a finer set of increments is a broader space of deliverable systems.

There is a second, sharper consequence: it invalidates the usual way of drawing a system's core. If you decide what belongs at the center by asking which services are essential or which programs are critical, you have frozen exactly those things into every configuration forever, and you will find later that some perfectly reasonable reduction is unobtainable without major surgery — or that users route around your core to get at hardware you claimed for it. Parnas's alternative is to let the core be whatever falls out of the dependency ordering, and to distrust the word "almost" wherever it appears: two capabilities that are *almost* always used together are capabilities that are sometimes not, and that is the case your structure has to admit.

A programmer who works this way gets something valuable beyond flexibility — a schedule that can degrade gracefully. If the system was built as an ordered series of working subsets, then falling behind means shipping less rather than shipping nothing, and there is never a stage where the answer to "does it run yet" is that nothing runs until everything runs.

**Source:** [Designing Software for Ease of Extension and Contraction](../works/designing-software-for-ease-of-extension-and-contraction.md) — Argued in the step on identifying subsets during requirements definition, and again in the closing comparison against kernel- and nucleus-centered operating system design.
