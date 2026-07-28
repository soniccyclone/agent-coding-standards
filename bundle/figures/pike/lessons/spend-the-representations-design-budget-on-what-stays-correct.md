---
type: lesson
title: "Spend a representation's design budget on what stays correct"
figure: pike
works: [hello-world]
axes: [hardware-affinity, cognitive-load, verifiability]
subdomains: [operating-systems-and-systems-programming, programming-languages-and-semantics]
tags: [lesson]
---
# Spend a representation's design budget on what stays correct

When a representation used by everything has to change, the temptation is to
pick the cleanest new representation and pay the conversion cost everywhere. This
work rejects the clean choice — fixed-width units for every character — with an
argument worth remembering: a uniform wide representation is perfectly workable
inside a single program that controls all of its own input and output, and simply
impossible across a network of independently written programs exchanging streams.
The clean design is clean only at a scale you do not have.

So the encoding is chosen by working backwards from the invariants that
surrounding code silently depends on. Bytes in the legacy range must mean exactly
what they always meant. No legacy byte may appear as a fragment of a longer
sequence, so anything scanning for a delimiter keeps working, and a filename with
a foreign character cannot accidentally contain a path separator. The order
produced by naive byte comparison must match the order of the character values,
so existing sorting stays right. The stream must carry no byte-order state, so
pipes do not need a header. Each of these is not elegance, it is a specific
promise that a specific class of existing program keeps working untouched. The
measured result is the point: of about 170 utilities, only a couple of dozen ever
needed to mention the new character type at all.

The deeper structural move that makes any of this possible is separating the set
of abstract values from the way they travel as bytes. Once those are distinct, the
transport encoding becomes a replaceable detail, and the authors demonstrate
exactly that — they later swapped the encoding for an incompatible one, and the
work was rewriting one library, mechanically re-encoding the data files, and
recompiling. An evening and an afternoon. Their own conclusion is the useful one:
the choice of encoding was the shallow decision; committing to a large value space
and to a byte-stream representation were the deep ones.

The habit to take away is to evaluate a candidate representation not by how nice
it looks in isolation, but by enumerating what currently-correct code it keeps
correct — and to treat a large count of untouched call sites as the actual
success metric of the migration.

**Source:** [Hello World or Καλημέρα κόσμε or こんにちは 世界](../works/hello-world.md) — the Standards section, which rejects fixed-width units and lists the properties of the chosen byte encoding, and the end of the tools-conversion section, which reports how little work the later change of encoding required.
