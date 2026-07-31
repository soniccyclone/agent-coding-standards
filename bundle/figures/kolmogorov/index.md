---
type: figure
title: Andrey Kolmogorov
description: 1903-1987, Moscow State University. Defined algorithmic/descriptive complexity as shortest-program length - reducing information content to a computability-theoretic primitive.
status: accepted
layer: design-thought
subdomains: [foundations-of-computation]
tags: [figure, accepted]
---

# Andrey Kolmogorov

**Dates:** 1903-1987. Soviet mathematician, Moscow State University; polymath across probability, turbulence, and logic.

## Why a candidate
Independently of Solomonoff and shortly before Chaitin, defined the descriptive/algorithmic complexity of an object as the length of the shortest program (on a fixed minimal machine) that produces it. Boundary case flagged: most of his career (probability axiomatization, turbulence) is outside this subdomain — only a thin slice is squarely relevant.

## Top 10 most influential works
1. "Three Approaches to the Quantitative Definition of Information" (1965) — `paywalled`/`uncertain`
2. "Logical Basis for Information Theory and Probability Theory" (1968, IEEE Trans. Info. Theory) — `paywalled`
3. Kolmogorov & Uspensky, "On the Definition of an Algorithm" (1958) — `uncertain`
4. *Grundbegriffe der Wahrscheinlichkeitsrechnung* (1933, adjacent, not core) — `uncertain`

## Lessons
Kolmogorov's method is to find the level of description at which a question becomes answerable, and to be ruthless about what that choice costs. When no formula is available, he defines a thing by the constraint every observation of it must satisfy; when a quantity resists computation he defines it anyway, on the grounds that being uncomputable is not the same as being meaningless. Founding a new subject on an existing theory means first stripping that theory of the setting it was born in, and then — the step usually skipped — naming the specialization that makes it generative, because reduction to a general framework explains nothing by itself. His discipline about assumptions is severe and worth copying: put the one you cannot justify in a single named place, introduced only where it is needed; find out which hypotheses a result actually rests on, since inherited machinery quietly narrows where it applies; and treat a sufficient condition as unfinished until you have tried to weaken it and failed on purpose. Several lessons are about scope confusion — a guarantee about one trial says nothing about many and vice versa, checking every pair is not checking the whole, and a relation between two systems holds only at some resolution and dies when either is refined. The unifying instinct is that an arbitrary choice stops mattering once you can bound its effect, after which you may claim exactly what the bound leaves and nothing more.
