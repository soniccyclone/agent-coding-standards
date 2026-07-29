---
type: lesson
title: "Permission belongs to the relationship, not to the interface"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [verifiability, expressiveness]
subdomains: [software-engineering-and-architecture, distributed-systems-and-concurrency]
tags: [lesson]
---
# Permission belongs to the relationship, not to the interface

An interface answers what a component will respond to. Reenskaug points out that this is only half of what a design usually intends, and the missing half is who is entitled to ask. In his notation the permitted requests are attached to the connection between two participants rather than to either participant alone, so a request can be legal from one counterpart and not merely discouraged but undeclared from another. A component understanding a request and a given caller being allowed to issue it become separate facts, which is what most designs assume informally and no interface can express.

The examples show why the distinction is not pedantic. In a purchasing arrangement, the bank on the paying side accepts payment instructions, but only from the participant occupying the buyer's position; nothing else in the arrangement may issue one, and the declaration says so rather than leaving it to be enforced by hope. Likewise a supplier plainly knows its own bank in reality, and within this particular arrangement there is deliberately no connection between them, because the concern being described does not include that conversation. Absence of a connection is positive information: it states that this collaboration does not involve that path, so a reader need not wonder and a checker can object.

The wider point is about where a design's real constraints live. Reachability is usually the loosest thing about a system and the least examined — anything holding a reference may call anything the reference exposes, and the resulting call graph is far denser than any intended design. Declaring authority per relationship narrows the possible call graph to the intended one and makes an unintended path a statable violation rather than an undiscovered fact. The narrowing also localizes reasoning: to know what can arrive at a participant, you read its incoming connections instead of searching everything that can reach it.

A programmer holding this specifies not just the operations a component offers but the counterparts entitled to invoke each, and treats a broadly reachable capability as an unstated risk even when every present caller behaves. A design where every participant may address every other has, in effect, declined to say what its structure is.

**Source:** [Working with Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — the collaboration and interface views in the role modeling chapter, where permitted messages are attached to the ports on each collaboration relationship, together with the purchasing example's explicit marking of participants that do not know one another within the concern being modeled.
