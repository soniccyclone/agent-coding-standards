---
type: lesson
title: "Give failure a single unwind ladder whose rungs are named for what they undo"
figure: torvalds
works: [linux-kernel-coding-style]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Give failure a single unwind ladder whose rungs are named for what they undo

**Lesson:** In a language without automatic cleanup, the naive way to handle failure is to release whatever you acquired at each point where you might bail out. The style guide rejects this and defends the construct most style guides ban, on grounds that are entirely about maintenance arithmetic. If cleanup is duplicated at every exit, then acquiring one more resource means finding and correctly amending every existing exit — a task whose difficulty grows with the number of exits and whose failure mode is a leak on the one path you missed. Route all failures instead into a single ordered sequence of release steps, each entered at the point corresponding to how far acquisition had progressed, and adding a resource means adding one rung. Correctness stops depending on your ability to enumerate exits.

The naming rule is where the idea sharpens from a code-shape preference into a verification technique. Sequential labels carry no information: they must be renumbered when a step is inserted, and worse, they make it impossible to check the code by reading it, because nothing about the label says what state the program is supposed to be in when control arrives there. Name each rung for the specific undoing it performs, and every jump becomes a locally checkable assertion — you can read a single jump and ask whether exactly that much had been acquired at that point, without simulating the whole function. The document's own illustration of the bug this prevents is instructive: collapsing several distinct partial states into one shared cleanup block produces code that releases something that was never acquired, and that mistake is invisible when the label is a number and glaring when the label names the resource.

The structure works because it encodes a real property of resource acquisition: it is a monotone sequence, and any failure leaves you at some prefix of it. The unwind ladder is the mirror of that sequence, so the correspondence between "where I failed" and "what I must release" becomes positional rather than something reconstructed by hand at each site. Secondary benefits fall out — nesting stays shallow, and the alternative of expressing the same thing with nested conditionals pushes the interesting code rightward and makes the common path harder to see than the exceptional ones. The document is also honest about the residual risk, and prescribes deliberately inducing failures to exercise every rung, since these paths are exactly the ones normal use never visits.

A programmer who believes this stops treating error handling as an obligation discharged locally and starts treating it as a structure with its own invariant. They build the ladder as soon as a function acquires its second resource, name every rung after the thing it releases, and consider a function's error paths untested until they have forced each one to run.

**Source:** [Linux Kernel Coding Style](../works/linux-kernel-coding-style.md) — the chapter on centralized exiting, with its rationale for a single jump-based cleanup path, its insistence on labels named for the undoing they perform rather than numbered, its worked example of the bug produced by merging distinct partial states, and its closing advice to simulate failures to reach every exit.
