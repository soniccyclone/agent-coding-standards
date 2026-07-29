---
type: lesson
title: "If the seed object needs privileges the others lack, the mechanism is not uniform yet"
figure: ungar
works: [self-the-power-of-simplicity]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
tags: [lesson]
---
# If the seed object needs privileges the others lack, the mechanism is not uniform yet

Uniformity claims fail at the bootstrap. A design says "everything is one kind of thing, created one way," and then there is the first thing — the origin, the template, the root — which had to come from somewhere else, and which therefore quietly needs a second creation path, a second lookup rule, or a special status the ordinary cases do not have. The moment that second path exists, the uniformity is rhetoric: users now have to know which case they are in before they can predict behavior, which is exactly the burden the uniform mechanism was supposed to remove.

The fix is not to hide the special case but to restructure so the seed genuinely has no privileges. If a template must be indistinguishable from what is made from it, then whatever makes the template *a template* has to be factored out of the template itself and into something both it and its offspring reference equally. Then the origin object is a peer, not a parent-in-disguise, and there is once again one creation operation with no branch in it. The design pressure runs backwards from a test you can actually apply: point at the most privileged object in the system and ask whether a user could have built it with the ordinary tools. If not, look for what to lift out of it.

Note what this costs and what it buys. It costs an extra indirection and an extra object that has no counterpart in the naive design — the split feels like added structure at the moment you make it. What it buys is the elimination of an entire category of exception from every rule downstream, which is why it pays. Special cases are not local; a privileged seed forces conditionals into every piece of code that might encounter one, and into every explanation of how the system works. Removing the privilege removes all of those at once, and it also kills the infinite-regress problem where each describing thing needs its own describer.

A programmer who takes this seriously treats bootstrap asymmetry as a design smell rather than an inevitability. When the framework's own base configuration cannot be expressed in the configuration language, when the metaobject needs a metametaobject, when the "default instance" is reachable only through a back door — these are not the unavoidable price of getting started. They are signals that some role got fused into an object that should have been holding only one.

**Source:** [Self: The Power of Simplicity](../works/self-the-power-of-simplicity.md) — the argument in the prototypes discussion that placing shared behavior in the prototype itself would force two distinct creation operations and make prototypes "not prototypical at all," resolved by moving shared behavior into a separate peer-parent; connected to the same section's disposal of the metaclass regress.
