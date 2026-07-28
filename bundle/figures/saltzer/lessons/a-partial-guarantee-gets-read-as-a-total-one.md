---
type: lesson
title: "A partial guarantee gets read as a total one"
figure: saltzer
works: [end-to-end-arguments-in-system-design]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, distributed-systems-and-concurrency]
tags: [lesson]
---
# A partial guarantee gets read as a total one

**Lesson:** When a layer advertises that it protects against some hazard, the
people building above it do not carry forward the qualifier. They remember "this is
handled" and drop the scope. This is not carelessness on their part so much as an
inevitable consequence of abstraction working as intended: the whole point of a
layer boundary is that you stop thinking about what is behind it, and a guarantee
stated at that boundary is exactly the kind of thing you are supposed to be able to
stop thinking about. So a mechanism that covers the transmission but not the
buffering, or the storage but not the copy into and out of storage, will be
consumed as though it covered everything, and the gaps will go undefended by anyone.

That makes a partially protective lower layer worse than an openly unprotective
one, which is a genuinely uncomfortable conclusion. An unreliable layer that admits
it prompts every client to build its own check. A mostly-reliable layer suppresses
that instinct while leaving the residual failures live, and the residual failures
are now rare enough to escape testing and to look like something other than what
they are when they finally surface. Rare corruption arriving through a channel
everyone believes is verified gets diagnosed as anything but the channel.

The practical consequence is a rule about how you state what you provide, and a
rule about how you read what others provide. When you build a layer, describe the
hazard boundary in terms of where the protection stops rather than what it covers,
because the former is what a client actually needs to reason about. When you build
on someone's layer, treat every guarantee you did not derive yourself as covering
strictly less than its name suggests, and place your own check at the point where
you can see the result you actually care about. The end-to-end check is cheap
insurance precisely because it does not need to know which of the intervening
mechanisms is lying.

**Source:** [End-to-End Arguments in System Design](../works/end-to-end-arguments-in-system-design.md)
— the short "too-real example" section, where a per-hop check led application
programmers to treat the network as trustworthy while data sat unprotected inside
intermediate nodes, and a low-rate byte-swapping fault silently corrupted files over
a long period.
