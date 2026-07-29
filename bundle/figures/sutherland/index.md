---
type: figure
title: Ivan Sutherland
description: b. 1938, MIT/Harvard/Caltech. Sketchpad (1963) - earliest master/instance object system with interactive direct manipulation. Turing Award 1988.
status: accepted
layer: implementation-mapping
subdomains: [programming-environments-and-object-systems]
tags: [figure, accepted]
---

# Ivan Sutherland

**Dates:** b. 1938. Computer scientist, PhD MIT under Claude Shannon, later professor at Harvard, Caltech, Portland State.

## Why a candidate
Sketchpad (1963) is the earliest system to use "master/instance" objects with inherited properties and interactive, on-screen direct manipulation — widely credited by Kay and others as the conceptual ancestor of both object-oriented modeling and live graphical environments, predating both Simula's formalization and Smalltalk's message-passing model.

## Top 10 most influential works
Direct bibliographic footprint in this subdomain is narrow — Sketchpad is the load-bearing work:
1. "Sketchpad: A Man-Machine Graphical Communication System" (1963 PhD thesis) — `public` (multiple mirrors, incl. Cambridge tech-report reprint)
2. "Sketchpad" (1963, AFIPS conference version) — `paywalled` (ACM DL; content duplicates the free thesis)
3. "The Ultimate Display" (1965, IFIP) — `public` (frequently mirrored)
4. "A Head-Mounted Three Dimensional Display" (1968, AFIPS, tangential) — `public` (widely mirrored)

## Lessons
Sutherland's recurring move is to keep the structure that generated an artifact rather than the artifact, then make that structure something a person can point at, so the machine holds the model and the human holds the intent. From that one commitment the rest follows: relations are stated as a measurement of how wrong things currently are rather than as procedures for fixing them, type-specific knowledge is pushed into the data so the programs above it stay general, and an invariant is only maintainable if it can be displayed, indicated and deleted like anything else. He is relentless about collapsing accumulated special cases into the single operation that generates them, reaching intermediate designs by composing the extremes instead of parameterizing them, choosing representations where the degenerate case is just another ordinary value, and keeping a slow but reliable general method underneath the fast special one that usually wins. The hardware work adds a physical realism to the same habit of mind: find which variables the result is genuinely a function of and stop measuring the rest, derive a component's required precision from the error already present in the chain, trade unstructured noise for an ambiguity you can compute away, let stages negotiate locally rather than be scheduled globally, and rank candidate methods by how they grow instead of how they look at today's problem size — while remembering that computation the apparatus performs for free is also a dependency on that apparatus. Around all of it sits his method for choosing what to build at all: state the asymptote so essential limits can be told from current ones, mechanize a medium only where the model gives back more than the output would have, treat familiarity as something manufacturable rather than something to imitate from the physical world, and accept that what an observer can reach bounds what a representation can say — which is why every projection must carry the way back to the node that produced it, why input should be snapped onto the model's vocabulary at the boundary, why the interesting search is often for an evaluation order rather than an answer, and why you sometimes have to build the thing before the abstraction the old medium was hiding becomes visible.
