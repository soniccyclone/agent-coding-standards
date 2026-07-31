---
type: lesson
title: "The escape must not travel the path it is escaping"
figure: wirth
works: [project-oberon]
axes: [verifiability, hardware-affinity, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# The escape must not travel the path it is escaping

**Lesson:** Every system that can get stuck needs a way for a person outside it to say stop, and the recurring mistake is to deliver that message through the same machinery that is stuck. If the abort request is queued behind the work, it waits for the work. If it is handled by the loop that is not terminating, it is never handled. If it is dropped when the buffer is full — and a buffer fills precisely because nothing is draining it, which is what being stuck looks like from the outside — then the escape is unavailable in exactly the situation it exists for. The property you need is not that the escape is fast or high-priority; it is that its delivery shares no resource whose exhaustion or blockage is the condition being escaped from.

That turns a vague reliability wish into a checkable structural claim. Trace the escape signal from the moment it is produced to the moment it takes effect and list every queue, lock, allocation, scheduler decision and cooperative yield it passes through. Each one is a place where the failure you are trying to survive can also stop the cure. The remedy is usually not more mechanism but an earlier decision point: recognise the escape at the very first place it becomes distinguishable — before the enqueue, before the dispatch, before anything that could be full or busy — and let it act there. Handling it early also has the pleasant property of making the escape immune to a large class of corruption downstream, because none of that code runs.

Two consequences follow that are easy to get wrong. First, the escape's effect must be something the stuck component cannot decline; asking a wedged computation to please unwind at its next convenient point is asking the failure to cooperate in its own removal. The effect has to be imposed from a layer the component does not control. Second, generosity about what else gets the same privilege is fatal — if every urgent-looking message is allowed onto the reserved path, the path acquires its own congestion and its own queue, and you are back where you began. The escape route stays reliable only while it is nearly empty, which means the design must be stingy about what is admitted to it. One signal, one meaning, no capacity to fill.

**Source:** [Project Oberon](../works/project-oberon.md) — the commentary on module `Input` in section 9.2, where the keyboard interrupt handler inspects each received character for the abort code and induces a trap immediately, explicitly so the operator can interrupt a computation that appears not to terminate, while the circular keyboard buffer's stated overflow policy is to ignore incoming characters when full, with the abort character named as the sole exception.
