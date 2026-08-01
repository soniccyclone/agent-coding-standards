---
type: lesson
title: "Tell the reader what is load-bearing and what is only provenance"
figure: ullman
works: [mining-of-massive-datasets]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Tell the reader what is load-bearing and what is only provenance

**Lesson:** An explanation of any depth contains material of two kinds. Some of it is required: later parts do not make sense without it, and a reader who skims it will be lost in ten minutes without knowing why. The rest is provenance — where a name came from, what earlier idea this resembles, why the notation looks like that — and it exists because it satisfies a real curiosity and because a reader who has met the ancestor will otherwise wonder about the connection. Both kinds are worth writing. The failure is presenting them in the same voice, so the reader cannot tell which is which and has to grant equal attention to everything or gamble on skipping.

The remedy is one sentence at the top of the optional part saying that it is optional and naming what, if anything, depends on it. This costs the author nothing and changes the economics for every reader. The reader who wants the origin story reads it with the pressure off, knowing nothing downstream is at stake. The reader on a deadline skips it and knows the skip is safe rather than merely convenient, which is the difference between moving on and carrying a quiet debt. What makes this work is that the dependency information is the author's to give: only the person who wrote the whole thing knows what actually gets used later, and reconstructing that from the outside requires reading everything, which is precisely what the reader was trying to avoid.

The same declaration is worth making in the opposite direction, on material that is easy to mistake for practice. Explanatory material often walks a reader through a hand-built version of something that in reality is never hand-built, because constructing it by hand is how anyone comes to understand what the automatic version produces. That is a good device, and it is dangerous unattended: some readers will carry the exercise back to their work as a method. A short note saying that this is done here for understanding and not done this way in practice repairs it entirely.

Generalised past prose, this is a claim about metadata on any body of material a person has to consume selectively. Reference documentation, runbooks, comments in a long file, a suite of tests: each has parts that must be understood before anything else works and parts that are context, and the consumer cannot distinguish them without doing the full read. Marking the distinction is a cheap, unglamorous act by whoever has the knowledge, and it compounds over every future reader. It also has an effect on the author, which is that a section nobody depends on and which explains nothing anybody asked about becomes visible as a candidate for deletion once it has to be labelled.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the opening sentences of chapter 13's subsection on convolution and cross-correlation, which announce the subsection as a short detour explaining the origin of a name and state that it is not a prerequisite for any other material in the chapter, together with the footnote attached to a later exercise noting that the networks the reader is being asked to design by hand are, like any neural network, to be learned from data rather than designed that way.
