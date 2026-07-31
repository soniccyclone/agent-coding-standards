---
type: lesson
title: "Wrapping a function optimizes only the calls that go through the wrapper, which the inner calls usually do not"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [hardware-affinity, verifiability]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Wrapping a function optimizes only the calls that go through the wrapper, which the inner calls usually do not

**Lesson:** Memoization turns the exponential Fibonacci procedure into a linear one, which is the headline. The instructive part is the question attached to it: would the scheme still work if the memoized procedure were simply built by wrapping the original? It would not, and the reason is exact. The wrapper caches only the calls that pass through it. Inside the original procedure, the recursive calls name the original directly, so they never touch the table, and the whole exponential tree is regenerated beneath the one call the wrapper saw. What you have built is a cache on repeated top-level queries, not a change to the algorithm's growth.

The general shape is that a decoration applies to a boundary, not to a function, and self-reference by name is what determines whether the boundary is on the recursive path. Wrapping something whose recursion goes through the same name it was bound to catches every level; wrapping something whose recursion is internal or captured at definition time catches only the outermost. Nothing about the code you can see tells you which — it depends on where the recursive reference resolves, and the difference between the two versions in the text is invisible at the call site.

This generalizes to every wrapper anyone reaches for. Retry logic, instrumentation, rate limiting, authorization, tracing, transaction wrapping, a caching decorator on a service client: each covers exactly the calls routed through it, and each silently misses the internal path if the component calls itself or its own siblings directly. The failure mode is uniform and nasty, because the wrapper *appears* to be working — metrics appear, the cache fills, the retry fires, and it is all happening only at the outermost layer while the interesting traffic goes around it. The absence is invisible from the outside.

Two consequences follow. First, when you add a wrapper, trace one representative call all the way down and confirm the wrapper appears where you expected rather than only at the top; the version that works and the version that does nothing are separated by a name-resolution detail. Second, in a design where the wrapping matters, arrange for internal calls to go through the same indirection as external ones — self-reference through the bound name, dispatch through the same table, a component calling its own public interface. That is not indirection for its own sake; it is what makes cross-cutting behaviour actually cut across.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) - Exercise 3.27 in chapter 3 section 3.3.3, which describes memoization as recording previously computed values in a local table keyed by the arguments that produced them, gives a memoize procedure holding a local table and consulting it before calling the underlying procedure, applies it to a Fibonacci definition whose recursive calls name the memoized binding rather than the raw one, asks the reader to explain why the result computes the nth Fibonacci number in a number of steps proportional to n, and closes by asking whether the scheme would still work if the memoized procedure had simply been defined by memoizing the original Fibonacci procedure.
