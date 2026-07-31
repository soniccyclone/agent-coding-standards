---
type: lesson
title: "Ask the population instead of maintaining a registry"
figure: wirth
works: [project-oberon]
axes: [cognitive-load, primitive-count]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Ask the population instead of maintaining a registry

**Lesson:** Two components need to reach each other: a producer of change and whoever cares about it, or a questioner and whoever holds the answer. The reflexive design is a registry — interested parties sign up, the other side keeps the list, and delivery walks the list. It works, and it costs more than it appears to. The list is state that must be correct: entries added on creation, removed on destruction, and removed reliably even when destruction happens abnormally, or the list retains references to things that no longer exist. Worse, the party keeping the list now depends on the type of the parties in it, which is a dependency in exactly the direction you did not want — the thing being observed knowing about its observers.

The alternative is available whenever the system already maintains an enumerable collection of the candidates for some other reason. Then you do not need a second list; you need a traversal. Send the notice, or the question, to everyone in the existing structure and let each recipient decide whether it is concerned. Nothing registers, nothing deregisters, nothing goes stale, and the sender needs to know only the common base type of the recipients — which it already knows, because the structure holding them is typed that way. The dependency inverts: recipients know about the notice, the sender knows about nobody.

The same move works for retrieval and not only for notification, which is the less obvious half. Instead of maintaining a variable naming the currently distinguished participant — the one holding the selection, the focus, the most recent whatever — send a query to all of them, have each fill in its own answer only if its answer is better than the one already in the message by some ordering carried in the message itself, such as a timestamp, and read the result out when the traversal ends. The distinguished participant is then a derived fact recomputed on demand rather than a maintained fact that every participant must remember to update. The class of bugs where the pointer names something stale or destroyed disappears, because there is no pointer.

The trade is cost proportional to the size of the population per event, against correctness that is structural rather than protocol-dependent. Take the traversal when the population is small enough that walking it is unremarkable and its membership already changes for other reasons; take the registry when the population is large, the events are frequent, or the interested subset is a small fraction of the whole. The mistake is not choosing either one — it is reaching for the registry by default, and paying for a second, redundant, hand-maintained copy of a structure you were already keeping.

**Source:** [Project Oberon](../works/project-oberon.md) — section 4.2's note that broadcasting messages from a document to the entirety of its potential views is an implementation of the model-view-controller pattern which dispenses models from knowing, that is registering, their views; section 3.3.2's implementation of the retrieval of the most recent text selection as a broadcast of a selection message carrying a time stamp to all viewers, with the answer read out of the message after the broadcast rather than from a maintained global variable; sections 3.3.3 and 3.3.4's use of the same mechanism for copy-over and for cloning, where receivers interpret the request individually; and section 4.2's listing of the four categories of universal message together with the remark that generic operations, meaning those interpretable individually by any recipient whose exact identity is unknown to the sender, are the key to extensibility.
