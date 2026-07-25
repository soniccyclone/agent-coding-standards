---
type: lesson
title: "When a class of mistakes needs a name to happen, remove the ability to name it"
figure: brinch-hansen
works: [monitors-and-concurrent-pascal-a-personal-history, the-programming-language-concurrent-pascal]
axes: [verifiability, primitive-count, cognitive-load]
subdomains: [programming-languages-and-semantics, distributed-systems-and-concurrency]
tags: [lesson]
---
# When a class of mistakes needs a name to happen, remove the ability to name it

**Lesson:** Some families of bug share a precondition that is easy to overlook: they require the program to be able to refer to something. A coordinator that wakes a specific participant needs to hold that participant's identity, and the moment identity is a value that can be stored, copied, and passed, the program can name a participant that has departed, one that was never waiting, or one that is waiting for something else entirely. No amount of care at the call sites eliminates that possibility, and no checking discipline can validate such a reference in general. The productive response is not to check the references more carefully but to redesign so the reference does not exist. Attach the waiting places to the shared state itself, and let a coordinator speak only of the caller in front of it and of whoever happens to be waiting in a particular place. Nothing then holds an identity, so nothing can hold a stale one.

Once you see the shape of the move you can apply it deliberately. The design work is to find the *smallest* naming power that still expresses what you need, then remove the rest — and to close the remaining escape routes, since a construct that cannot be assigned to, cannot be passed as an argument, and starts out empty simply has no way to acquire a bad value. Notice that this is a stronger result than validation would have given: the erroneous state is not detected, it is unconstructible, which costs nothing at run time and requires no error path.

The general principle worth carrying is that an error class is not always best attacked at the point where it manifests. Ask what capability the error depends on, and whether that capability is actually load-bearing or merely inherited from a more permissive design. Programmers reach reflexively for validation because it is local and additive, while removing expressive power is global and feels like a loss. The trade is often strongly in favor of the removal, and the way to tell is to write the programs you care about in the reduced language and see whether you miss it. In this case the answer was that a coordinator never needed to think about which participant it was dealing with, only about the role that participant was playing.

**Source:** [Monitors and Concurrent Pascal: A Personal History](../works/monitors-and-concurrent-pascal-a-personal-history.md) — the abandoned-attempts and waiting-game sections, which identify process references as the flaw in the earlier proposals and then describe attaching waiting places to shared state so no identity type is needed, with the dangling-reference problem eliminated by making those places initially empty and not assignable. Also [The Programming Language Concurrent Pascal](../works/the-programming-language-concurrent-pascal.md) — the queue rules that carry the same restriction into the language proper.
