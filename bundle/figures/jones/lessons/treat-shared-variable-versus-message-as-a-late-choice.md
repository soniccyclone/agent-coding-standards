---
type: lesson
title: "Treat shared memory and message passing as alternative realizations of one abstraction, chosen late"
figure: jones
works: [tentative-steps-toward-a-development-method-for-interfering-programs]
axes: [expressiveness, parallelizability, hardware-affinity]
subdomains: [distributed-systems-and-concurrency, programming-languages-and-semantics]
tags: [lesson]
---
# Treat shared memory and message passing as alternative realizations of one abstraction, chosen late

**Lesson:** Arguments about whether concurrent programs should communicate through shared state or through messages are usually conducted as if the answer determined how you may think about the problem. It does not have to. A quantity that several activities need to read and update is a coherent design object whose meaning is fixed by what may be observed of it and how it is allowed to change; whether that object is finally realized as a memory cell with disciplined access or as a value held privately by a server that answers requests is a decision about mechanism. Carry the abstraction as far down as it stays useful, and pick the mechanism when you know which one the target actually supports. The design above that point is unaffected either way, and the same design can be finished both ways.

Doing it in this order also explains what synchronization mechanisms are for. If a design has arrived at a point where some participant must make a change that its neighbours' assumptions cannot tolerate at arbitrary moments, the mechanism you reach for is whatever makes that change atomic from the outside — a lock, a monitor, a guarded server, a rendezvous. Choosing it is answering a question the design has already posed precisely, instead of picking a concurrency style up front and then discovering which of your intentions it cannot express. The mechanism is downstream of the obligations, not upstream of them.

There is a corollary about language design worth stating separately. Once interference is something you specify rather than something you hope about, the value of a language feature is measured by how well it lets you bound and localize interference — which parts of the state a construct can possibly touch, and what an outside observer can possibly catch mid-flight. A language whose constructs make those bounds visible lets a designer discharge obligations by inspection; one that does not forces every obligation to be argued from scratch over the whole program. That is a sharper criterion for judging concurrency features than expressive convenience, and it points the same way regardless of which mechanism a given program ends up using.

**Source:** [Tentative Steps Toward a Development Method for Interfering Programs](../works/tentative-steps-toward-a-development-method-for-interfering-programs.md) — the maximally-parallel search development, which carries a shared bound through several design steps and only at the last moment realizes it as a value held behind a rendezvous-style guarded task, contrasted with the sibling development that keeps genuine shared variables; and the closing discussion point that this work exerts strong pressure toward language features making the degree of interference controllable.
