---
type: lesson
title: "Top-down refinement is not strictly top-down: name the part whose specification lives downstream and leave it empty"
figure: reynolds
works: [the-craft-of-programming]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Top-down refinement is not strictly top-down: name the part whose specification lives downstream and leave it empty

**Lesson:** Decomposing from the top implies you can specify each piece as you introduce it, and that is nearly true — but some pieces exist only to agree with a decision that has not been made yet. A part that produces the framing for output cannot be written before the output is designed; a part that reserves capacity cannot be sized before the thing it holds is chosen. Trying to write such a part at the moment you name it means inventing the downstream decision under pressure, in the wrong context, and then treating it as fixed for the rest of the derivation. That is how a passing detail at the top of a decomposition ends up dictating the shape of everything under it.

The technique is to name the part and leave the body empty, with an explicit note that it is waiting on something specific. Naming it costs nothing and keeps the structure at the current level complete and readable; refusing to fill it keeps the decision where it belongs. When the sibling subtree is elaborated and the decision falls out naturally, come back and write the deferred part against what actually got built. Some sequencing of this kind is unavoidable in any decomposition, so the useful skill is noticing which parts are in this category as you introduce them, rather than discovering it when the derivation stalls.

Recognising these parts also tells you something worth knowing about the design. A deferred part is one whose content is determined elsewhere, which means the two are coupled — a change to the format the deep code produces silently invalidates the shallow code that frames it, and nothing structural connects them. Once you have that in view you can decide what to do about it: derive both from one shared description, or check the agreement mechanically, or accept the coupling and record it. What you should not do is leave the dependency implicit merely because the order you wrote things in happened to make it work the first time.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Appendix C.3's top-down construction of a complete test program, where a step to print a heading is introduced in the outermost refinement but deliberately left unexpanded, with the details postponed until the per-case output has been designed; the heading is filled in last, with its spacing chosen to line up its column labels with the values printed by the per-case code, and the invalid-input message spaced to align with the values printed in the valid case.
