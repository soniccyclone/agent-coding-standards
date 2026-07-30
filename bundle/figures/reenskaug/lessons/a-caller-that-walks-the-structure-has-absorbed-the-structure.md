---
type: lesson
title: "A caller that walks the structure to reach a service has absorbed the structure"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# A caller that walks the structure to reach a service has absorbed the structure

**Lesson:** Reviewing his own working code, the author traces one initialization sequence and finds a single object performing a three-step hop: ask a neighbor for its root, ask that root for its input device, ask the device for a specialized instance. Everything works. The verdict is still negative, and the reasoning is precise — the initiating object now knows a great deal about the complete structure of objects, which makes the structure hard to change. His preferred design has the object make one request of its immediate neighbor and let that request propagate along the containment chain to whoever can satisfy it.

The diagnostic is worth extracting on its own, because it turns a stylistic complaint into a countable one. The number of intermediaries a caller names is the number of structural facts it has committed to, and every one of them is a place the caller breaks when the structure is rearranged. That reframes the cost: it is not that the chained call is ugly, it is that the caller has silently taken on maintenance obligations proportional to the length of the chain, and taken them on invisibly, since nothing in its interface declares the dependency. Delegating instead — one request to one neighbor, forwarded until answerable — costs a forwarding method per level and buys the freedom to reorganize everything above the first hop.

There is a second, sharper observation in the same passage. The temporary handles the caller obtained mid-traversal were held in local variables rather than fields, and the author insists they must still be drawn as connections in the collaboration model, because messages are sent through them. This closes the escape route that makes chained navigation look harmless. A dependency does not become smaller by being short-lived; the coupling is created by the message being sent, not by where the reference is stored, so "it's just a local" is not a defense. That is exactly why chained navigation escapes review in practice — it adds no fields, no imports, no obvious surface, and so leaves no trace in the places reviewers look.

The habit, then, is to count hops in the code and treat every hop beyond the first as a structural assumption requiring justification, while refusing the storage-lifetime excuse. Where an object needs something it cannot reach directly, the request should travel the structure rather than the requester.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 9 section 9.3.3, where the TranslatingSensor initialization scenario shows the Controller obtaining the view's topComponent, then that window's sensor, then a new translatingSensor; the author remarks the Controller knows a great deal about the complete structure, calls this generally not a good idea because it makes the structure hard to change, says he would have preferred the request to pass up the Container-Component chain, and notes that the Controller's temporary variables must still be shown as ports because messages are sent through them.
