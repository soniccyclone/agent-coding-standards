---
type: lesson
title: "A component's interface is defined by what it cannot refuse, not by what it chooses to accept"
figure: lynch
works: [an-introduction-to-input-output-automata]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# A component's interface is defined by what it cannot refuse, not by what it chooses to accept

**Lesson:** The I/O automaton model makes exactly one distinction its foundation, and it is not the distinction most programmers reach for. It does not partition a component's vocabulary by data type, direction of information flow, or layer. It partitions by control: which occurrences does this component get to decide the timing of, and which does the outside world impose on it? Everything a component emits or does privately is under its own authority, and it may hold that action back until a condition of its choosing holds. Everything arriving from outside is not negotiable — the model requires that every incoming action be possible in every state. A component may not decline.

That constraint looks like a limitation and is actually the model's sharpest tool, because it forbids the most common self-deception in interface design. When a component can refuse input, designers use refusal for two incompatible jobs: throttling a peer that is going too fast, and ruling out inputs that "cannot happen." The second use is where systems rot, because the ruled-out input eventually arrives and there is no defined behavior for it. Forbid refusal and both jobs have to be done honestly. Flow control becomes something the protocol arranges explicitly. Bad inputs become something you either respond to with a defined error or explicitly declare yourself unconstrained by — and either way the assumption is written down where a reader can see it.

The reframing this produces is that correctness statements for open components are naturally conditional. Not "this component behaves well," but "given that its environment respects these restrictions, this component behaves well." Once you accept input-enabledness, that shape is forced rather than optional, and the environment's obligations stop being folklore. It also means the interface is total: a reviewer can ask, for every incoming action and every internal state, what happens, and the model guarantees the question has an answer.

A programmer working this way stops writing handlers that assume ordering, arrival, or absence, and starts asking of every boundary: what does the caller control, what do I control, and what is my defined response to the message I was sure could never show up here? The messages you were sure could never show up are the ones production sends.

**Source:** [An Introduction to Input/Output Automata](../works/an-introduction-to-input-output-automata.md) — the model overview's argument for classifying actions by who controls their timing, and its explicit contrast with formalisms that let a process block its inputs.
