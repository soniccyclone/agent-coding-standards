---
type: lesson
title: "Put the fix where it belongs, even if that means owning more"
figure: pike
works: [plan-9-from-bell-labs]
axes: [cognitive-load, primitive-count, hardware-affinity]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Put the fix where it belongs, even if that means owning more

Every practicing engineer knows the compromise where a problem gets solved in
the wrong component because that is the component you are allowed to change.
Terminal handling ends up in the kernel because the kernel is yours and the
window system isn't. A workaround lands in the application because the library
is frozen. Each such displacement is invisible in isolation and, accumulated,
is most of what makes an old system unpleasant: the layer boundaries no longer
correspond to the structure of the problems. This work's stance is that the
boundary between kernel, library, and application is an artifact of interest to
the implementors and of no interest to the user, and that what matters is where
the functionality actually belongs.

Acting on that stance has a price, and the price is scope. To move terminal
behavior out of the kernel and into the window system, you have to be able to
change both. To make heterogeneous architectures a non-issue you have to touch
the compilers, the build conventions, the naming of resources, and the
environment at once, because the problem genuinely spans all of them and any
single-component fix is a patch. The corresponding freedom is what makes the
right placement possible: compatibility is treated as a nice-to-have rather
than a constraint, so an interface whose semantics changed gets a new name
instead of a subtly overloaded old one, and the compatibility layer for foreign
software is kept as a deliberate side road rather than allowed to shape the
main system.

The same instinct shows up as a refusal to keep privileged shortcuts. There is
no distinguished "native" compile — every compilation is a cross-compilation,
so the general path is also the only path and therefore the tested one. There is
no all-powerful administrative account; the administrative user's powers are
scoped to a machine's own housekeeping and stop short of reading anyone's files.
A privileged special case is a second implementation of the general mechanism
that nobody maintains, and it will rot exactly where you rely on it.

You cannot always take the scope. What you can always do is name the
displacement honestly: know which component the problem belongs to, know that
you are patching elsewhere, and keep that debt visible rather than convincing
yourself the patch is the design. The habit worth taking is to ask, before
reaching for the local workaround, which layer the problem is actually about —
and how much of the stack you would need to influence to fix it there.

**Source:** [Plan 9 from Bell Labs](../works/plan-9-from-bell-labs.md) — the Motivation section's argument for building an all-new system rather than adapting an old one, and the Discussion section's account of problems whose solutions span several components at once and of interfaces renamed rather than reused when their meaning changed.
