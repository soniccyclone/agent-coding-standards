---
type: lesson
title: "Let a program do the organising, and hardware only what a program cannot"
figure: strachey
works: [time-sharing-in-large-fast-computers]
axes: [primitive-count, hardware-affinity, expressiveness]
subdomains: [operating-systems-and-systems-programming]
tags: [lesson]
---
# Let a program do the organising, and hardware only what a program cannot

Faced with a machine that must juggle many devices and many jobs, the obvious response is to build the juggling into the apparatus: give every peripheral its own controller, its own buffer, its own little brain, and let each one manage its own affairs. Strachey's objection to this is not aesthetic but structural. The work those controllers do is logically intricate while being arithmetically trivial, and intricacy is what dominates the cost of a special-purpose device — so you end up paying repeatedly, in dedicated hardware, for exactly the kind of bookkeeping the general machine was built to do well. Worse, each controller is only as capable as the day it was fixed in metal, so situations slightly outside its design (an error partway through a transfer, an unusual retry policy) become impossible rather than merely awkward.

The inversion he proposes is to strip the special-purpose units down to the minimum that must be physical, and move the organising intelligence into an ordinary program that the machine runs on their behalf. That program is not a component of the application; it is a resident authority that the machine enters whenever something outside asks for attention. Everything about how the resources are apportioned — which job runs, how much store it gets, when it is judged to have failed — becomes a matter of text you can rewrite rather than circuits you must re-fabricate. The payoff Strachey names last is the one that matters most in the long run: you can try a completely different arrangement of the machine by rewriting one program.

What must stay in hardware is then a short and principled list: exactly those things a program cannot establish for itself. A program cannot make its own authority unforgeable, cannot guarantee it will regain control from code that has stopped cooperating, and cannot observe an address before the store responds to it. So the machine supplies a signal that seizes control, a boundary check that happens alongside the memory access rather than after it, and a class of instructions reachable only from where the trusted program lives. That is the whole hardware contribution. A designer who thinks this way asks of every proposed piece of mechanism whether software could have done it, and treats a yes as a reason to remove the mechanism — reserving silicon for the properties that software is logically incapable of asserting about itself.

**Source:** [Time Sharing in Large Fast Computers](../works/time-sharing-in-large-fast-computers.md) — The argument runs from the economic critique of autonomous peripheral units through the proposal of a resident supervisory program, and closes with the minimal set of privileged facilities that program needs from the machine.
