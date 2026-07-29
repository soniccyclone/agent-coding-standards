---
type: lesson
title: "Make the rest of the computation an argument"
figure: strachey
works: [continuations-a-mathematical-semantics-for-handling-full-jumps]
axes: [expressiveness, verifiability, primitive-count]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Make the rest of the computation an argument

When a compositional account of a system breaks down, the usual instinct is to patch the composition rule with cases: this piece behaves normally, that piece might bail out, so split the program into regions where the tidy rule is safe and stitch the regions together by hand. Strachey and Wadsworth show that the case analysis is a symptom, not a fix. The real trouble is that each fragment was being described in isolation, as if its effect could be settled without reference to what follows it — and no such description exists once a fragment is permitted to decline to hand control onward. The repair is to stop describing fragments in isolation and instead describe each one as a function of its successor: give every piece the whole remainder of the computation as an explicit argument, and let the piece decide whether to use it.

The payoff is that abnormal control stops being abnormal. A construct that transfers control elsewhere is simply one that ignores the successor it was handed and applies a different one; a construct that returns a value early is one that reinstates a successor stashed earlier. What had needed a separate mechanism per escape — jumping out, breaking a loop, returning a result, resuming a suspended evaluation — collapses into one mechanism used differently, and the sequencing rule that failed before now needs no exceptions at all. Reifying the successor also makes it storable, computable and nameable, which is why the same account extends to control transfers that ordinary reasoning finds perverse, such as re-entering an evaluation that was abandoned.

The habit generalises far past language semantics. Any time a component's behaviour cannot be pinned down because it might not return to its caller — error paths, cancellation, retries, protocol handoffs, callbacks — the productive move is to find the implicit "and then" that the design assumed and make it a value the component receives. A programmer who thinks this way stops writing special-case machinery for each way control can leave a region, because once the continuation is a parameter, leaving is just choosing a different parameter. A programmer who does not think this way accumulates one bespoke escape mechanism per situation and a reasoning rule riddled with caveats about which fragments are well-behaved.

**Source:** [Continuations: A Mathematical Semantics for Handling Full Jumps](../works/continuations-a-mathematical-semantics-for-handling-full-jumps.md) — the diagnosis in the section on the problem of jumps, where composing state transformations fails because a fragment's jump-freedom cannot be determined, followed by the reformulation that hands each command the state transformation for everything after it.
