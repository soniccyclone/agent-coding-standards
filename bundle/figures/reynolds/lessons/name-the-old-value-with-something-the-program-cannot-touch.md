---
type: lesson
title: "To say anything about change, name the old value with something the program cannot touch"
figure: reynolds
works: [the-craft-of-programming]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# To say anything about change, name the old value with something the program cannot touch

**Lesson:** A condition about the state describes one moment. It has no vocabulary for two. So the instant a requirement is genuinely about change — this ended up smaller than it started, that was consumed, the balance moved by exactly the amount withdrawn — the condition language runs out, and no amount of cleverness inside a single-state assertion recovers it. The fix is not a richer assertion language but an extra name: introduce an identifier that stands for the value at the earlier moment, and require that the program contain no way to refer to it. Because it is unreachable from the code, it cannot drift, and every later condition can quote it freely as a fixed point of comparison.

The cost of a component that overwrites its own input is now visible rather than merely felt. A component that leaves its inputs alone can be specified entirely in the ordinary vocabulary, because the earlier value is still sitting there under its own name at the end. A component that destroys its inputs forces the reader to carry a phantom name through the whole argument. That is not a moral failing, and for small values the price of preserving inputs is low enough that preservation is simply the better default; but for large aggregates it may not be affordable, and the honest move is to accept the phantom rather than to pretend the specification is simpler than it is. Either way, the specification-language cost is a real design input, not an afterthought.

The general shape recurs far from proofs. Any time a claim spans two moments — a migration's before-and-after, an audit trail, a test that checks a delta rather than a value — the same device is what makes the claim expressible at all: pin one side under a name whose defining property is that the running system has no handle on it. What makes the device work is exactly the inaccessibility. A snapshot the program can still write to proves nothing, because the comparison is then between the state and itself.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — the integer-division example where deleting the input-preserving assignment makes the specification unstatable, and the introduction of ghost identifiers as names occurring in the specification but never in the program, together with the surrounding discussion of why input-preserving programs are cheaper to specify.
