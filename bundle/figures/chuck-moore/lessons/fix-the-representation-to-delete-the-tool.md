---
type: lesson
title: "Change what the input looks like and the machinery that interprets it can be thrown away"
figure: chuck-moore
works: [colorforth-documentation]
axes: [primitive-count, cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
tags: [lesson]
---
# Change what the input looks like and the machinery that interprets it can be thrown away

**Lesson:** A large part of any language processor exists to recover, from a flat stream of characters, information the author knew perfectly well while typing. Where a name ends, whether a word is being defined or invoked or merely commented, whether a token is meant as a value: all of this is present in the writer's intent, discarded by the storage format, and then laboriously reconstructed by a parser using punctuation as evidence. Store the intent instead of the punctuation and the reconstruction step ceases to exist. If each word in the stored form carries a small tag saying what kind of thing it is, the processor reads the tag rather than deducing it, and the syntax whose only job was to make that deduction possible can be deleted from the language.

The consequences run in several directions at once, which is what makes the trade a good one rather than merely clever. The compiler shrinks, because it has less to figure out. The writer types fewer marks whose purpose is to inform the machine rather than the reader. And the display becomes unambiguous about interpretation, since the same tag that guides the processor can be rendered visibly, so a reader sees how each word will be treated rather than inferring it from surrounding marks. The representation is also free to be efficient in ways plain text is not, since it is no longer obliged to be a character sequence at all; encoding names in fewer bits than characters would take and storing numbers already converted are natural once the format is designed for the machine's use.

Fixing the representation this way has a second consequence for what the system needs to keep. When producing executable form from source costs no noticeable time, compiled output stops being worth preserving, and the entire apparatus of object libraries and their maintenance can be dropped: source becomes the only artifact, and everything else is regenerated on demand. The cost of the whole approach is that the format is no longer ordinary text, so an editor that understands it becomes mandatory rather than optional, and interchange requires a conversion step. A programmer who thinks this way treats the input format as a design variable rather than a given, and asks which components of a toolchain exist only to compensate for a representation that threw information away.

**Source:** [colorForth: Programming Language and Operating System](../works/colorforth-documentation.md) — the sections on source and on the use of color, which replace the defining and compiling punctuation of classic Forth with per-word tags, describe the pre-parsed word format and its bit-level encoding, credit the arrangement with reducing syntax and simplifying the compiler, and explain why an object library becomes unnecessary once recompilation is instantaneous. The companion primer's compiler section restates the tag scheme as the whole of the language's grammar.
