---
type: lesson
title: "Observation of a running system yields a state that never occurred, and that can be enough"
figure: lamport
works: [distributed-snapshots-determining-global-states-of-a-distributed-system]
axes: [parallelizability, verifiability]
subdomains: [distributed-systems-and-concurrency]
tags: [lesson]
---

# Observation of a running system yields a state that never occurred, and that can be enough

**Lesson:** A process in a distributed system can record its own state and nothing else, so "the global state right now" is unobservable in principle: there is no instant shared by all recorders, and stopping the world to create one would destroy the very computation being observed. The mature response is to lower the demand. Instead of asking for a state the system actually passed through, ask for a state the system could have passed through — one reachable from where observation began, and from which the state at observation's end is reachable. Piecemeal local recordings, coordinated only by markers flowing through the ordinary channels, can be assembled into exactly such a state, even though the assembled picture may correspond to no moment that ever existed.

Why is a fictional state useful? Because the questions worth asking of a running system are often stable properties, predicates that once true stay true: the computation has terminated, a deadlock exists, a token has vanished. For such a property, truth in the possible-state implies truth now, and falsehood in the possible-state implies falsehood at observation start. The fiction answers the real question. This is the deeper move: define what "meaningful observation" requires relative to the property being detected, rather than chasing an absolute notion of accuracy that physics denies you. Careful reasoning about the relationship between local states, channel contents, and reachability is also exactly what earlier, incorrect detection algorithms lacked; the published record of broken deadlock detectors is what happens when that relationship is left to intuition.

A programmer who absorbs this stops trying to build the impossible instantaneous view (or, worse, believing a naively assembled one) and instead designs monitoring, checkpointing, and debugging around consistency: cuts that respect message causality, observation protocols that ride the normal channels without perturbing the computation, and claims about the observed picture scoped to the class of properties the picture can actually support.

**Source:** [Distributed Snapshots: Determining Global States of a Distributed System](../works/distributed-snapshots-determining-global-states-of-a-distributed-system.md) — the opening constraint that a process can record only its own state, the marker algorithm, the theorem that the recorded state is reachability-equivalent to the actual run via permuting pre- and post-recording events, and the stability-detection section that scopes what the snapshot can answer.
