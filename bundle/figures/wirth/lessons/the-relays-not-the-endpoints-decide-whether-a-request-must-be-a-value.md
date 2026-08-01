---
type: lesson
title: "The relays, not the endpoints, decide whether a request must be a value"
figure: wirth
works: [project-oberon]
axes: [expressiveness, primitive-count, verifiability]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# The relays, not the endpoints, decide whether a request must be a value

**Lesson:** The argument about whether a component's interface should be a fixed set of named operations or a single entry point taking an open-ended request is usually conducted between the two parties who care — the caller and the callee — and framed as a question about how likely the operation set is to grow. That framing omits the party that actually settles it. If a request travels from its sender to its recipient through intermediaries that are involved in neither end of it, then those intermediaries must be able to accept, carry, and often inspect a request whose kind they have never heard of. A fixed operation set makes that impossible: every relay would have to name every operation it might forward, so introducing one new kind of request anywhere would mean editing and recompiling every relay on every path. The requirement for an open, self-describing request comes from the transit, not from the destination.

This is worth separating because the two ends can be entirely closed and the conclusion still holds. A component may understand a small, permanently fixed set of requests and still be unreachable by direct call, because the only way to reach it is down a path of containers written by other people at other times. Conversely, an endpoint with a wildly open operation set that its callers address directly has no such requirement — it can expose whatever it likes, because nobody in between has to survive contact with it. So the question to ask when choosing the form of a request is not "will the set of operations grow" but "who has to handle this request besides the two parties who understand it", and if the answer is anyone at all, the request has to be a value with a common ancestor rather than a name in a signature.

The relays impose one further demand that a purely opaque payload would not satisfy. They do not only forward: they preprocess, contributing their own share of context, deciding routing, sometimes declining to propagate. So the request must be inspectable enough that an ignorant relay can do its part — read the routing fields, add to the accumulated context, compare an identity stamp — while remaining unintelligible in its specific content. That is a real design constraint, and it says the request wants a small common head that everyone understands and an arbitrary tail that only the endpoints do. Getting that division wrong in either direction hurts: put too little in the common head and relays cannot do their job; put too much in it and the head becomes the shared declaration whose growth you were trying to avoid.

The general shape: before fixing the representation of anything that moves between components, draw the whole path it travels and identify every party that must touch it without understanding it. Those parties, not the ones with the requirements, determine how much of it has to be self-describing.

**Source:** [Project Oberon](../works/project-oberon.md) — appendix A.2's closing observation returning to an earlier remark on the value of open object interfaces, that any context-oriented forwarding strategy in fact requires them because intermediate stations on a message's path must be able to pass through and even preprocess messages of a possibly unknown type, instanced by update-view requests for exotic components; read together with the same section's handler sketch in which each intermediate frame reads and updates the message's context pointer, timestamp and accumulated coordinates before propagating it.
