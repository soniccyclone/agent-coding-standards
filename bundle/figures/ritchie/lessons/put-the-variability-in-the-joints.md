---
type: lesson
title: "Put the variability in the joints between components, not inside the components"
figure: ritchie
works: [unix-time-sharing-system]
axes: [expressiveness, primitive-count, parallelizability, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Put the variability in the joints between components, not inside the components

**Lesson:** Every program has a demand queue of options attached to it: send the output somewhere else, paginate it, format it in columns, hand it to a printer, run it without blocking. Satisfying those demands inside each program is the obvious move and it is a trap, because the options multiply per program and nothing learned by one is available to another. The alternative Ritchie and Thompson took is to give each program a fixed, dumb attachment point — a numbered input and output it uses unconditionally — and let a separate coordinating program rebind those attachments before the program starts. The redirection notation never reaches the command at all; the command contains no code for it and cannot tell the difference. Chaining two commands so one feeds the other is then the same idea again, with a channel substituted for a file, and running the stages concurrently costs nothing extra because separate stages were already separate processes.

The reason this works is that a joint is a single place where N components meet, so a feature implemented at the joint is implemented N times over for the price of one, while a feature implemented in a component stays there forever. It requires a discipline, though: the attachment point has to be genuinely uniform, which means the component must not be allowed to inspect what it is attached to. The moment a program behaves differently because its output is a terminal rather than a channel, the joint has leaked into the component and the multiplication stops.

There is a second, subtler dividend. Once composition lives outside the components, the composing program is itself just another component and can be composed the same way — invoked recursively, fed from a file of commands, or replaced entirely by a different interface for a class of users. The coordinator gets to be as elaborate as anyone wants precisely because it holds no privileged position in the system.

A programmer who believes this stops answering feature requests by adding flags. They look for the seam the request is really about, ask what would have to be true for the seam to carry the feature for every participant, and spend the effort there. They also treat "this composition was awkward" as a defect in the connective tissue rather than a missing option on a leaf.

**Source:** [The UNIX Time-Sharing System](../works/unix-time-sharing-system.md) — the shell sections on standard I/O, filters, background execution, and the implementation sketch showing that redirection reduces to rearranging inherited descriptors between fork and execute.
