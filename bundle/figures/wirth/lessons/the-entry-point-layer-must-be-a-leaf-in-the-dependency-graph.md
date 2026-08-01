---
type: lesson
title: "The entry-point layer must be a leaf in the dependency graph"
figure: wirth
works: [project-oberon]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# The entry-point layer must be a leaf in the dependency graph

**Lesson:** The layer where a user's request arrives — the thing that scans a command line, extracts parameters, checks them and calls something — should have no clients at all, and this gives a mechanical test for a common structural error. If another component finds it needs to call into your entry-point layer, then something that belongs further down has been implemented up there, and the right response is to move it, not to export it. The test is cheap to apply because it does not require judgement about what "belongs" where: just look at who imports the entry-point unit. In a healthy structure the answer is nobody. Every other consumer of the system reaches past it to the layers it also calls.

The reason this matters is that entry points multiply and the core must not. A second way of driving the same functionality — a different front end, an editor that integrates several kinds of content, a batch driver, a test harness — is a normal thing to want, and it is only cheap if all of them are siblings sitting on the same core rather than a chain in which each new one wraps the previous one. Chains form when the first entry point accreted logic that had nowhere else to live, so the second one has to go through it to get at that logic, and now the first one's argument parsing and its user-facing assumptions are load-bearing for a caller that has neither.

Keeping the layer a leaf also settles what it is allowed to contain, which is the same thing said from the other side: scanning, validating, and dispatching, and nothing whose value would be missed by a caller that does not have a command line. Validation is worth keeping there rather than pushing down, because it is where untrusted input arrives and the lower layers should be entitled to assume well-formed arguments. What must not stay there is anything that constitutes an operation on the system's actual subject matter, however convenient it was to write it next to the parsing that discovered its arguments.

**Source:** [Project Oberon](../works/project-oberon.md) — section 13.8.1's characterization of module `Draw` as a typical command module whose task is to scan the command text for parameters, check their validity, and activate the corresponding procedures contained in `Graphics` and `GraphicFrames`; and the accompanying emphasis that graphic frames may be opened and manipulated by other modules as well, so that a document editor integrating texts and graphics would refer to `Graphics` and `GraphicFrames` directly and not to `Draw`, which as a command module should not have clients.
