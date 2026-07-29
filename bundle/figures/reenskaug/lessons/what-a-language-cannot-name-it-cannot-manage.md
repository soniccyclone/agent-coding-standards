---
type: lesson
title: "What a language has no word for, its programs cannot govern"
figure: reenskaug
works: [a-dci-execution-model]
axes: [expressiveness, primitive-count]
subdomains: [programming-environments-and-object-systems, programming-languages-and-semantics]
tags: [lesson]
---
# What a language has no word for, its programs cannot govern

Reenskaug's audit of what a machine actually does yields three capabilities, not two: it changes data, it keeps data, and it moves data between parts. Programming languages historically grew constructs for the first two — expression and statement forms for transformation, declaration forms for storage — while the third was handed off to libraries and treated as peripheral I/O. The consequence is not that communication stops happening. It happens constantly, and it happens in a medium the language cannot see, which means no compiler checks it, no name refers to it, and no reader can find it in one place. The traffic pattern of a running system becomes the one thing about the system that exists only as an emergent side effect of scattered call sites.

The argument generalizes past its object-oriented setting. Every construct a language offers is also a claim about what deserves to be a unit of thought, and every capability a language declines to name gets encoded implicitly, redundantly, and inconsistently in whatever primitives are available. The test is whether you can point at a thing: if the structure of who talks to whom is real enough that programmers argue about it in meetings and draw it on whiteboards, but there is no textual artifact you can open and read that structure off of, the language has a hole in exactly the place your design lives.

A programmer who accepts this stops treating missing vocabulary as a stylistic gap to be papered over with conventions and naming discipline. Instead the missing thing gets promoted into a first-class construct with its own declaration, its own scope, its own lifetime, and its own runtime representation — and the cost of that promotion is paid honestly, in extra machinery, rather than avoided by pretending the concept was never needed. The relevant question when facing recurring accidental complexity is which real concept the notation refuses to admit exists.

**Source:** [A DCI Execution Model](../works/a-dci-execution-model.md) — the opening argument on the three services a computer provides and why the third lacked language support, and the closing three-layer restatement that puts communication alongside transformation and storage as a basic capability of computing.
