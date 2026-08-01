---
type: lesson
title: "An action spread over many events needs a named in-progress state, and every intervening action owes it a reset"
figure: wirth
works: [project-oberon]
axes: [cognitive-load, verifiability]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# An action spread over many events needs a named in-progress state, and every intervening action owes it a reset

**Lesson:** Some things a user or a caller means as one act arrive at the system as a long run of separate events — one per keystroke, one per packet, one per row. The system has no event that means "the act", only events that mean "another piece of it", and it cannot tell from the current event whether the piece extends the previous act or begins a new one. The only way to know is to keep a variable that says which act, if any, is currently open. That variable is not an implementation detail to be hidden or apologised for; it is the act itself, promoted from something implicit in a sequence to something explicit in the store, and it should be named for what it holds rather than for the mechanism that maintains it.

The obligation it creates is the part that gets missed. Between two pieces of the same act, arbitrary other things can happen, because nothing in the system suspends the world while an act is half-built. Each of those other things has to be classified: does it leave the open act open, or does it end it? Moving the insertion point ends it; scrolling does not. The set of actions that invalidate the state has to be enumerated deliberately and each one has to clear the variable, and this is a global obligation rather than a local one — a new command added later is a new chance to leave a stale act open and have the next piece attach itself to something the user stopped meaning several minutes ago. Writing the reset set down next to the variable is the cheapest defence, because it converts an invisible cross-cutting duty into a list somebody can check a new command against.

The second move is to keep the open state small enough that it is a single object rather than an accumulated history, and the way to do that is to restrict what may vary within one act. If every piece of a composite is required to carry the same attributes, the open state is one object with one set of attributes and the incremental update is a single append. Allow the attributes to change mid-act and the open state becomes a sequence of runs, every incremental update becomes a structural edit, and the invalidation logic has to reason about which run it is in. That restriction is a real loss of expressiveness for the user, and it is worth taking anyway when the alternative is complexity in a mechanism that is already awkward for reasons that cannot be removed. Pay for an unavoidable complication by narrowing what it has to handle, not by making the mechanism cleverer.

**Source:** [Project Oberon](../works/project-oberon.md) — section 13.8.2's account of caption creation, where the input process consists of as many user actions as there are characters and other actions may intervene between the typing, making it unavoidable to record an insertion state in the global variable `newcap`, which is reset to NIL when the caret is repositioned; together with the accompanying restriction, adopted to avoid further complexity, that all characters of one caption use the same font and colour.
