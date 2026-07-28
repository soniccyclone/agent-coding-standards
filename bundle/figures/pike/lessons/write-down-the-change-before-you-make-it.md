---
type: lesson
title: "Write down the change before you make it"
figure: pike
works: [the-text-editor-sam]
axes: [verifiability, cognitive-load]
subdomains: [programming-environments-and-object-systems, databases-and-data-management]
tags: [lesson]
---
# Write down the change before you make it

The obvious way to implement editing is to edit: compute a modification, apply it, repeat.
Pike declines this and interposes a record. A command's effects are accumulated as a
sequence of described edits against the state as it was when the command began, and only
after the whole command has been described is the description played against the real
data. The indirection looks like pure overhead until you count what it buys, at which
point it turns out to be the cheapest structure in the program.

Three separate problems dissolve at once. Edits inside one command cannot perturb each
other, so a search that runs early cannot trip over a replacement that ran earlier still
— the semantics become "everything happened simultaneously," which is a rule you can
state in one sentence instead of a folklore of ordering dependencies. An error partway
through a complicated command leaves nothing half-applied, because you abandon the
description rather than repair the data. And undo requires almost no new machinery: a
description of a change can be inverted, so the log that made the change possible is also
the log that takes it back, and accumulating logs gives you unbounded history rather than
the single self-inverting step that ad-hoc implementations settle for. One structural
decision, three properties that are each individually expensive to retrofit.

The reflection Pike draws is the part to carry forward: reversibility is nearly free if
designed in at the start and effectively unobtainable if not, and it is precisely what
licenses a system to be powerful. Users will only experiment with an unfamiliar and
sharp-edged facility if mistakes are cheap; a reliable undo is what lets you hand people
a capability they do not yet fully understand, and it is why the design can skip the
confirmation prompts that otherwise accumulate around every destructive operation. So when
you find yourself about to mutate state directly, ask what a description of the mutation
would cost, and what else it would give you.

**Source:** [The Text Editor sam](../works/the-text-editor-sam.md) — the two-pass
"doing and undoing" scheme that treats each file as a database with changes registered as
transactions, together with the retrospective assessment of undo in the closing
discussion.
