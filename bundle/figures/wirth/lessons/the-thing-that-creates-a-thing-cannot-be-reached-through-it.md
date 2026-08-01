---
type: lesson
title: "The operation that creates a thing cannot be reached through the thing"
figure: wirth
works: [project-oberon]
axes: [expressiveness, cognitive-load, verifiability]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# The operation that creates a thing cannot be reached through the thing

**Lesson:** A design that attaches every operation to the object it acts on will get all the way to the end and then discover one operation that cannot be attached: the one that brings the object into existence. Reconstructing a stored object requires knowing its kind before there is any object to ask, so the creating operation cannot live in the object's own operation table, and no amount of rearrangement fixes this — it is a consequence of the ordering, not of the encoding. The gap has to be closed by something outside the object, and the honest way to close it is to record, in the stored form, a *name* that the surrounding environment can resolve into the creating operation. Everything else about the scheme can stay decoupled; this one link cannot be removed, only made explicit.

The consequences of choosing a name are worth accepting deliberately rather than stumbling into. A name resolved at load time is late binding of the strongest kind: the reader contains no list of kinds, so a stored artifact may name a kind that did not exist when the reader was written, and the environment can locate and load the implementing unit on demand. That is exactly the property that makes a format outlive its readers and makes new kinds installable without touching anything already built. The price is that the name has become part of the stored format's contract. Whatever supplies the namespace — module names, a registry, a package path — is now a compatibility surface, and renaming the implementing unit silently invalidates every artifact that mentions it. If you would not accept that constraint on the name, do not use it as the link.

Note also the division of labour in reconstruction, which falls out of the same asymmetry. The environment resolves the name and invokes the creator, which allocates an instance and installs its operations; the common attributes shared by every kind are then read by generic code; and only the kind-specific remainder is read by the newly attached operation. Three distinct actors, in a fixed order, because each is the earliest one that can possibly do its part. Getting this order explicit in the design is what prevents the recurring bug where reading begins before the reader knows what it is reading into.

**Source:** [Project Oberon](../works/project-oberon.md) — section 13.7's account of object classes, in which each class is a module, the method suite is assigned at creation, and the one unavoidable remaining link is described: because the object does not yet exist when its attribute values are being read, the generating procedure cannot be a member of the method suite, so every object's class is identified by its module name, the allocator by a command name, and loading proceeds via `Modules.ThisMod` — which may load the class module on demand — then `Modules.ThisCommand`, then the base type's data, then the extension's data through the class's own `read` method.
