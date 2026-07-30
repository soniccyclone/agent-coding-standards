---
type: lesson
title: "Whoever saves your state holds your secrets, so look for leaks in the suspend mechanism and not in the interface"
figure: wilkes
works: [cambridge-cap-computer-and-its-operating-system]
axes: [verifiability, parallelizability]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# Whoever saves your state holds your secrets, so look for leaks in the suspend mechanism and not in the interface

**Lesson:** A component can have a perfectly tight interface — every operation checked, every result filtered, nothing exposed that the designer did not choose to expose — and still leak everything, because something else in the system is entitled to stop it mid-computation and write its working state somewhere. Whatever suspends and resumes a computation must record enough to resume it, and that record contains the computation's private contents at an arbitrary moment. If the place that record is written is readable by a party the computation does not trust, the interface is irrelevant: the attacker never calls the operation improperly, they just arrange to be the one who saves it, and read the residue after each interruption.

Two things follow. First, the search for information flows has to include the mechanisms that were not designed to move information at all — checkpointing, suspension, logging, crash dumps, migration, anything that must capture state in order to restore it. These are usually treated as infrastructure rather than as interfaces, so they get none of the scrutiny the interfaces get, while carrying strictly more than any interface does. Second, this makes an apparently attractive structural idea impossible: you cannot both delegate scheduling authority downward and preserve confidentiality upward, because the delegate necessarily becomes the keeper of its subjects' state. The only way out is to store that state somewhere neither party controls, which means the delegation was never real — a single central custodian was doing the work all along.

The style of the discovery is worth as much as the finding. The leak was not visible from the protection rules; it emerged from tracing what physically has to be written down when an interruption occurs, and asking who can read that place. Any argument that a component is sealed should be checked the same way: not against the operations it offers, but against the list of things that can stop it and what they must retain to start it again.

**Source:** [The Cambridge CAP Computer and Its Operating System](../works/cambridge-cap-computer-and-its-operating-system.md) — Chapter 5's analysis of why passing an entry authority across the boundary of a coordination domain destroys protection, since an arbitrary external interrupt causes the subordinate's coordinator to dump the interrupted computation's state — possibly confidential to the entered procedure — into space the superior can read, with the worked scenario of a user writing their own coordinator to harvest that residue, and the conclusion that storing status centrally is the only remedy.
