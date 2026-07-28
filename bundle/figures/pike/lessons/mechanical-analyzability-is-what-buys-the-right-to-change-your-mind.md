---
type: lesson
title: "Mechanical analyzability is what buys the right to change your mind"
figure: pike
works: [go-at-google]
axes: [verifiability, cognitive-load, parallelizability]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Mechanical analyzability is what buys the right to change your mind

**Lesson:** Whether a design mistake is permanent has almost nothing to do with how bad it is and everything to do with whether a program can find and rewrite every place it appears. If the notation can only be understood by resolving names and types across the whole world, then correcting an early error means asking thousands of people to each edit their own code, which means the old form must be supported indefinitely and both forms will exist forever. If instead the notation can be parsed and reconstructed by a modest program, one person can perform the correction everywhere at once and the old form can simply stop existing.

That reframes surface-level decisions usually dismissed as taste. How regular the grammar is, whether meaning depends on context a parser would have to accumulate, whether presentation is canonical rather than a matter of individual preference — these determine the cost of every future automated change. Canonical presentation matters more than it looks: when everything is already laid out the one way, a rewriting program's output differs from its input only where meaning changed, so its diffs are reviewable and its blast radius is legible. Without that, every mechanical edit drowns in incidental reformatting and nobody can tell what was actually done.

There is a second-order effect worth planning for. Once the parsing machinery is a normal, available part of the environment rather than a specialized project, people build transformations the designers never anticipated: cross-cutting migrations, documentation extraction, compatibility audits. That ecosystem is a consequence of design choices about the notation, not of anybody's tooling roadmap, and it accrues to whoever made the notation tractable.

The practical stance: when choosing a representation — a language surface, a config format, an interface description — score it on how cheaply a program can rewrite it correctly, and pay real design cost for that property even when it makes the human-facing form slightly more verbose. Then use the capability. Migrate call sites mechanically rather than deprecating and waiting, so that only one version of anything is ever in service, and the accumulation of compatibility debt never starts.

**Source:** [Go at Google: Language Design in the Service of Software Engineering](../works/go-at-google.md) — the syntax section's emphasis on a grammar parseable without type information, and the tools section on canonical formatting, tree-rewriting migrations, and fleet-wide API updates.
