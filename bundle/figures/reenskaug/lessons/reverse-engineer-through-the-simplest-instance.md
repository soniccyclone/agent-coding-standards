---
type: lesson
title: "To understand a mechanism, dissect its simplest instance, not its most representative one"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# To understand a mechanism, dissect its simplest instance, not its most representative one

**Lesson:** Wanting to learn how a system's windowing machinery worked, the authors first opened a code browser — a rich, real, thoroughly representative example — and found it far too complex to learn from. They switched to the system transcript, the simplest window in the environment, on the grounds that it still contains every mechanism they cared about. That substitution is the whole technique, and it runs against the instinct to study something important enough to be worth understanding.

The reasoning is that a mechanism's *presence* and its *prominence* are different things. A general mechanism appears in the trivial case as fully as in the elaborate one, just with less surrounding noise, so the trivial case has a strictly better signal-to-noise ratio for the thing you are trying to learn. Choosing the important example instead means paying in confusion for realism you did not need — and the failure is quiet, because you will still learn things, just slowly and with less confidence about which parts were essential.

The rest of the method is worth stealing too, because it is empirical rather than documentary: run the simple instance, interrupt it, and inspect the live object graph rather than reading source. That yields the actual structure, at which point the recurring shapes become visible — in their case the same container-and-part relationship appearing ten separate times inside one modest window, and a model-view-controller triad appearing five times. Those repetitions are the mechanisms, and their multiplicity inside one small example is exactly why the small example was sufficient. A programmer approaching unfamiliar machinery can therefore ask: what is the least impressive thing that still exhibits this behaviour, and can I catch it running?

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 9's reverse-engineering step, which reports abandoning the Browser as far too complex and selecting the System Transcript as the simplest window of all, then activating it, interrupting the program, inspecting its object structure, and identifying ten instances of the Container-Component relation and five instances of the Model-View-Controller triad within it.
