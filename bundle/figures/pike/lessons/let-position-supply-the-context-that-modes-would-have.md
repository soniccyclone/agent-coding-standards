---
type: lesson
title: "Let position supply the context that modes would have"
figure: pike
works: [acme-a-user-interface-for-programmers]
axes: [cognitive-load, expressiveness, primitive-count]
subdomains: [programming-environments-and-object-systems, operating-systems-and-systems-programming]
tags: [lesson]
---
# Let position supply the context that modes would have

Systems accumulate hidden state that changes what an action means: a current
directory, a current mode, a selected target, a focused pane. Each such variable is
a thing the user must track and the system must display, and every bug of the form
"that did the wrong thing because I was in the wrong state" comes from one. The
move made here is to delete the global state and let the location of the text
supply the missing context instead. There is no single current directory; a command
or file name is resolved relative to the label of the window that physically
contains it. Nothing to set, nothing to remember, nothing to get wrong — the
context is visible on screen next to the thing it governs.

Once context comes from position, a very small set of gestures covers a large set
of jobs, because the same gesture can resolve differently depending on what it
lands on. One button means "execute this," whether the text is a built-in word, a
program in the containing directory, or a command the user just typed into a
scratch space. Another means "take me to this," and it resolves to opening a file,
jumping to an address inside a file, or searching for literal text, chosen by
examining what is actually there. This is overloading, and it works — where
overloading usually confuses — because the resolution rule is derived from
inspectable local evidence rather than from invisible state. The user can always
see why it did what it did.

There is a real design cost, and the work is candid about it: making this feel
right takes work that has no elegant closed form. The placement rules were
rewritten several times. Determining what a bare click meant requires guessing at
word boundaries, checking whether a candidate name exists, and falling back to
plain text. Heuristics are not beautiful, and the system will occasionally be
wrong. The judgment being made is that a system which infers well from context is
worth far more than one which is principled and demands you maintain its state for
it — and that when you take on inference, you commit to tuning it against real use
rather than reasoning about it once.

**Source:** [Acme: A User Interface for Programmers](../works/acme-a-user-interface-for-programmers.md) — the user interface section's replacement of a current directory with per-window context, and the nuances section's rules for expanding a bare click into an intended target.
