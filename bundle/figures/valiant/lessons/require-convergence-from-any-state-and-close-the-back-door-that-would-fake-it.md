---
type: lesson
title: "Require convergence from any starting state, then close the back door that would let a single step fake a restart"
figure: valiant
works: [evolvability]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Require convergence from any starting state, then close the back door that would let a single step fake a restart

**Lesson:** There are two very different guarantees an incremental process can offer. The weak one is that it converges from a designated initial state — a clean install, a fresh cache, a zeroed accumulator. The strong one is that it converges from *any* state it might find itself in, with no step ever giving up more than a bounded amount of ground. The gap between them is much larger than it looks, and it is exactly the gap that decides whether the process composes with itself. If convergence needs a designated start, then arriving at that start from wherever you happen to be is an unanalyzed move that can cost arbitrarily much, and a system built from several such processes in sequence has an unquantified hole between every pair of stages. If convergence works from anywhere, the finished state of one stage is a legal starting state for the next, and stages chain without any interstitial reset.

The subtle part is that the strong guarantee is easy to lose by accident, because a parameter meant for something else can smuggle a restart back in. The relevant parameter here is the threshold that decides whether a candidate step counts as acceptable: a step is taken if it does not lose more than that much ground. Left unbounded above, that single threshold lets one step discard an arbitrary amount of accumulated quality, which is a reinitialization wearing the costume of an ordinary move. So the definition has to be pinned from *both* ends — the threshold must be at least something, so that real improvements are distinguishable from noise, and at most something, so that no single step can wipe the slate. Bounding it above is not fussiness; without it the whole start-anywhere requirement is vacuous, and everything the theory then proves is a statement about a weaker model than the one written down.

The transferable habit is to read every definition and every configuration knob for the maximum damage one application of it can do, not just the intended use. Any knob whose extreme setting reproduces a capability you deliberately excluded has re-admitted that capability, and your guarantee has quietly become conditional on people not turning it that far. The general form of the audit: for each parameter, ask what the process can do at the parameter's limit, and check that the answer is still inside the model you claim to be working in. When it isn't, bound the parameter in the definition rather than in a comment.

**Source:** [Evolvability](../works/evolvability.md) — the insistence in section 2 that convergence hold from any starting representation because a permitted reinitialization step could otherwise incur an arbitrarily large performance loss, together with section 3's discussion of why the tolerance is constrained between two polynomially related bounds: an unbounded tolerance would supply initialization by a back door, and start-anywhere convergence is what allows successive phases with different targets to be chained without a drop at any step.
