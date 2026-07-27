---
type: lesson
title: "Refuse to specify the things you do not want depended on, even when every implementation agrees on them"
figure: steele
works: [the-revised-report-on-scheme, the-java-language-specification]
axes: [parallelizability, hardware-affinity, verifiability]
subdomains: [programming-languages-and-semantics, distributed-systems-and-concurrency]
tags: [lesson]
---
# Refuse to specify the things you do not want depended on, even when every implementation agrees on them

**Lesson:** The report makes a decision that looks perverse until you see what it buys. Every existing implementation of the language evaluated the parts of a call in a fixed left-to-right order, and the report says so — and then declines to promise it, stating outright that programs must not depend on the order. Silence here is not an oversight or a deferral; it is the primary design act. A specification is a contract in both directions, and whatever it fixes becomes something implementations may never change and programs will inevitably come to rely on. So the specifier's real question is not "what does the system do?" but "what am I willing to be held to forever?"

What the withheld promise pays for is visible immediately. The report notes that an implementation might reasonably want to evaluate a call's parts right-to-left in order to build them up in the order the machine wants them, and freedom of order is what leaves that available. The same freedom is the precondition for evaluating parts concurrently at all — order-independence is not an optimization applied to a specified order, it is what you have left when you never specified one. The report then carries the discipline through consistently: the bindings of a simultaneous-binding form may be computed in any order, the stepping expressions of a loop may be computed in any order, and an assignment to a loop variable is explicitly not promised to survive into the next iteration. Each of these is a place where a more generous specification would have closed off a class of implementations.

The cost is shown honestly rather than hidden. The report walks through a destructive list-reversal idiom that works in the sibling dialect precisely because that dialect committed to an order, and demonstrates that the same code is not valid here, then rewrites it so that the sequencing it needs is stated explicitly instead of inherited from the evaluator. That is the tell for the whole approach: a program that needs an order must say so in its own text, using the construct that means order, rather than borrowing an order the language happened to have.

A programmer with this instinct writes interfaces that promise the minimum their callers actually need, and treats every incidental observable — iteration order of a collection, timing, the exact text of an error, whether two calls happen to be serialized — as a liability until deliberately promised. They also read other people's specifications the opposite way round from most people, hunting for what is conspicuously *not* guaranteed, because that is where the implementation retains room to move underneath them and where their own code is quietly accumulating dependence on an accident.

**Source:** [The Revised Report on Scheme: A Dialect of LISP](../works/the-revised-report-on-scheme.md) — the four numbered points about how a call is evaluated, and the treatment of the loop form's initialization and stepping expressions together with the reworked destructive-reversal example.
