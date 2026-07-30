---
type: lesson
title: "Formalize the property that carries the weight, not the one that happens to be true"
figure: scott
works: [logic-and-programming-languages]
axes: [cognitive-load, expressiveness]
subdomains: [foundations-of-computation, software-engineering-and-architecture]
tags: [lesson]
---
# Formalize the property that carries the weight, not the one that happens to be true

**Lesson:** Every real machine has finitely many states, so a finite-state model of it is accurate. It is also, past a point, superficial — because finiteness is not the feature that explains anything interesting about what the machine does, and a formalism built on the wrong distinguishing property yields results that are technically correct and practically inert. The failure mode is subtle precisely because the premise is unimpeachable. Accuracy is cheap; the real question about a chosen abstraction is whether the property it makes central is the property the phenomena actually turn on. Choose wrong and you get a well-developed theory that keeps not connecting to the problems you care about, and the diagnosis is a lot harder than noticing an error.

Two further symptoms are worth learning to recognize. One is a classification that runs out: a hierarchy whose first couple of levels are genuinely illuminating and then has no clear continuation is telling you the organizing principle was local, not structural — an abundance of alternative families with no order among them is chaos wearing a taxonomy. The other is generality reached too early. A sufficiently abstract framework may well lead somewhere good, but adopting it before the concrete cases have taught you what the structure is makes the work harder to understand without making it more true, and the fact that the abstraction is available is not an argument that now is when to use it. Both symptoms are the same error at different times: committing to an organizing idea before the material has shown you which idea is load-bearing.

The practical discipline is to keep asking what the abstraction is *for* while you build it, and to treat persistent failure to connect as evidence about the abstraction rather than about the difficulty of the domain. Complexity you find displeasing rather than illuminating is a signal worth acting on — being unable to see where to turn next in a formalism is often the formalism's fault. And the cure is usually not more machinery on top; it is going back to find the property that the interesting cases actually share and rebuilding around that, even at the cost of abandoning a body of work that was perfectly rigorous on the wrong foundation.

**Source:** [Logic and Programming Languages](../works/logic-and-programming-languages.md) — the judgment that finiteness is not the important feature of physical machines and the automaton viewpoint is often superficial, the assessment of the language hierarchy as ultimately disappointing for having no clear continuation past its early levels, and the opinion that categorical machinery used too early only makes things harder to understand.
