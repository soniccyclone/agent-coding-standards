---
type: lesson
title: "Give each construct a meaning of its own instead of explaining the whole by translating it away"
figure: scott
works: [toward-a-mathematical-semantics-for-computer-languages]
axes: [cognitive-load, verifiability, expressiveness]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Give each construct a meaning of its own instead of explaining the whole by translating it away

**Lesson:** There are two ways to say what a notation means. One is to translate it wholesale into something else — an abstract machine, an intermediate form, a reference implementation — and let the target's behavior stand as the explanation. The other is to give each construct, one grammar clause at a time, a meaning built from the meanings of its parts. The two are not equally useful even when both are technically complete. Translation makes the meaning of any single feature inaccessible: to find out what one construct does you must understand the target machine and then locate your construct's contribution inside a global process. The clause-by-clause account lets you stop at each construct, understand it in isolation, and move on.

The property that makes this work is that the meaning of a compound depends only on the meanings of its components, with the grammar's structure supplying the connection. That is a strong constraint and it is what buys the locality: because nothing about a subexpression's context can reach into its meaning, you can reason about a piece and reuse the reasoning wherever the piece appears. It also has a striking side effect on how much apparatus you need. Symbol tables, identifier lists, and bookkeeping structures that a translation-based definition must formalize before it can say anything simply do not appear, because they were artifacts of the explanation strategy rather than features of the thing being explained.

A subtlety worth carrying: since the meaning of a compound is assembled by following the grammar, meaning attaches to the parse structure, not to the character string. If the grammar is ambiguous, a string has as many meanings as it has derivations, and this is the honest answer rather than a defect to be papered over — how a thing is read determines what it means. The corresponding discipline for ordinary systems: prefer specifications that assign each construct or component a self-contained meaning over specifications that only say what the assembled system does. The first kind survives having a piece replaced. The second has to be re-established from scratch.

**Source:** [Toward a Mathematical Semantics for Computer Languages](../works/toward-a-mathematical-semantics-for-computer-languages.md) — the syntax-directed structure of the semantic equations for commands and expressions, the closing comparison with translation into an abstract machine which makes it hard to discuss features of the original language in isolation, the claim that the method needs no formalized bookkeeping or symbol tables, and the treatment of semantic functions as defined on annotated derivation trees rather than on expressions alone.
