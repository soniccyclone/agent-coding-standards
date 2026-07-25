---
type: lesson
title: "When code moves, move its environment with it, because the worst failure is the one that succeeds with the wrong meaning"
figure: cardelli
works: [a-language-with-distributed-scope]
axes: [cognitive-load, verifiability]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
tags: [lesson]
---
# When code moves, move its environment with it, because the worst failure is the one that succeeds with the wrong meaning

**Lesson:** Sending program text somewhere to be executed looks like the simplest possible form of mobility and is the most dangerous. Text has no attachments: every name in it that was not defined inside it will be resolved against whatever the destination happens to have. Sometimes that means an error, which is survivable. Sometimes it means the name resolves to a different thing of the same name, the computation completes, and the wrong state is updated in the wrong place with no indication that anything went wrong. Shipping text silently converts a design where names mean what they say into one where names mean whatever is lying around at the destination, which is a property nobody would choose deliberately.

The fix is to ship the computation with its bindings rather than its source: a package containing the code together with values for the names it did not define. There is an efficiency argument for this shape, since only the bindings the code actually needs travel rather than an entire evaluation context, but the real argument is meaning preservation. Two useful consequences follow. First, remote execution becomes something you can reason about, since the free names are exactly the ties back to the origin and the code's behaviour at the destination is the behaviour it would have had at home. Second, the set of unbound names becomes a specification of connectivity: a package with none is genuinely autonomous and can run while the origin is offline, one with a few maintains a thin tether, and one with many will chatter across the network. That is a design dial the programmer can see and choose, rather than a property discovered from traffic graphs.

The habit generalizes to anything migratory: serialized closures, deployed configuration, templates, queries assembled in one context and run in another. Ask what will be resolved at the destination, and either carry the resolution along or accept that the meaning is now determined by the destination's contents. The second option is occasionally what you want, and it should be a decision rather than an accident of the transport format.

**Source:** [A Language with Distributed Scope](../works/a-language-with-distributed-scope.md) — the language overview's argument that transmitting program text implies a complete disconnect from the originating computation and yields unpredictable resolution of free names, the closure-transmission mechanism described in the distributed semantics section, and the compute server and agent examples where the free-name set determines how tethered a mobile computation is.
