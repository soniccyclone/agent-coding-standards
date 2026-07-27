---
type: lesson
title: "When a system's real specification is other people's software, running that software unmodified is the only acceptance test that counts"
figure: torvalds
works: [comp-os-minix-original-announcement]
axes: [verifiability, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# When a system's real specification is other people's software, running that software unmodified is the only acceptance test that counts

**Lesson:** The evidence the announcement offers that the project is real is not a feature list or a design document. It is that a shell and a compiler — programs written by other people, for another system, with no knowledge of this one — had been brought up and appeared to work. That is a deliberate choice of proof obligation, and it reflects something true about the class of artifact being built. A kernel has no interesting behavior of its own; its entire contract is the environment it presents to software it did not write. The specification of that contract does not live in prose, it lives distributed across every existing binary that depends on it, most of it undocumented and much of it accidental.

Once you accept that, the verification strategy follows. You cannot check conformance against a document, because the document is not where the truth is; you check it by running the real corpus and watching for divergence. A large third-party program exercises system calls in combinations, orders, and edge conditions no author of a self-test would think to try, and it does so without the sympathetic bias of a test written by the implementer. Getting a compiler to compile itself on your kernel is a shockingly dense correctness signal per unit of effort — it touches process creation, file semantics, memory growth, and signal delivery, and it fails loudly.

The uncomfortable consequence, which this project internalized more thoroughly than almost any other, is that once real software depends on your behavior, that behavior is the specification whether you like it or not — including the parts you consider bugs. A programmer who believes this stops asking "does my implementation match my intent" and starts asking "does the software that matters still work," treats a passing real-world workload as a stronger claim than a passing unit test, and builds the corpus of external programs into the development loop early, because each one added is a permanent tripwire over a region of the interface no hand-written test covers.

**Source:** [Original Usenet Announcement, comp.os.minix](../works/comp-os-minix-original-announcement.md) — the progress report itself, where the milestone claimed is that a ported shell and compiler run, and the note that the filesystem's on-disk layout was kept compatible with the incumbent for practical reasons rather than redesigned.
