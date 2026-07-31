---
type: lesson
title: "Compare the artifact, not the meaning — and check which way the test errs"
figure: wirth
works: [project-oberon]
axes: [verifiability, cognitive-load, hardware-affinity]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Compare the artifact, not the meaning — and check which way the test errs

**Lesson:** Deciding whether a published description has changed since last time looks like a question about meaning: are the two versions equivalent in what they promise to anyone depending on them? Answering it that way means defining equivalence, walking both structures, and deciding for every kind of element which differences matter — a body of code with its own bugs, whose defects are exactly the ones that produce silent inconsistency. The alternative is to compare the two generated artifacts as opaque sequences of bytes and treat any difference as a change. It is crude, it can be written in a few lines, and it has one property that the sophisticated test struggles to guarantee.

That property is the direction of its errors. Provided generation is a function of its input — the same description always produces the same bytes — a byte comparison cannot report "unchanged" for something that changed. It can report "changed" for something that did not, when some incidental detail of emission shifted, and the price of that mistake is wasted work: dependents get rebuilt unnecessarily. The price of the opposite mistake is a system whose parts disagree about a shared description and no indication that anything is wrong. When the two error directions differ that sharply in cost, a test that is wrong only in the cheap direction beats a more accurate test that can be wrong in the expensive one. Notice that the whole argument rests on determinism of the producer, which is therefore a property to establish deliberately rather than assume — any nondeterminism there converts the crude test from conservative to merely noisy.

The corollary concerns the action taken on a positive result. Replacing the published description is not a private act; it invalidates everyone holding the old one. An operation whose consequences land outside the system performing it should not happen as an automatic side effect of a routine run — it should require an affirmative request from someone in a position to know that the invalidation is acceptable. The detection can be automatic and conservative; the destruction should be requested.

**Source:** [Project Oberon](../works/project-oberon.md) — the end of section 12.6, which states that after a symbol file is generated it is compared with the file from a previous compilation of the same module, that the old file is replaced only if the two differ and the compiler's s-option is enabled, that the comparison is made byte after byte without consideration of the file's structure, and that this somewhat crude approach was chosen for its simplicity and yielded good results in practice; together with section 12.4's note that the s-option enables overwriting an existing symbol file, thereby invalidating clients.
