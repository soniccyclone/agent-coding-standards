---
type: lesson
title: "The loop you write silently chooses the data's shape"
figure: pike
works: [the-text-editor-sam]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [programming-environments-and-object-systems, programming-languages-and-semantics]
tags: [lesson]
---
# The loop you write silently chooses the data's shape

Every iteration construct carries a hidden claim about how the data is divided. A tool
that loops over lines has decided, without ever saying so, that its subject is an array
of lines; a tool that loops over records has decided the same thing about records. The
decision feels like plumbing rather than semantics, so nobody argues about it, and then
every capability the tool grows inherits that partition. Whole classes of problem become
awkward not because the operations are missing but because the units are wrong.

The move Pike makes is to notice the hidden claim and promote it to an argument. Once
the description of the units is supplied by the caller — a pattern that says what a
chunk *is* rather than a predicate that says which chunks to keep — the loop stops
assuming a shape and starts accepting one. The same small operator set then reaches
multi-line records, newline-free text, identifiers inside source code, and things nobody
anticipated, because the part that used to be baked in is now something you write. This
is why the language stays small while its reach grows: generality came from removing a
commitment, not from adding features.

A programmer who has internalized this reads their own code for undeclared partitions.
Where does this system decide what an item is? Is that decision in the same place as the
operations, and does it have to be? If splitting and acting are fused, the fusion is
usually load-bearing in the worst way: it will be the reason the next requirement needs
a new subsystem rather than a new argument. Separating "what counts as a unit" from
"what to do with a unit" is often the cheapest generalization available, and it tends to
shrink the primitive count rather than grow it.

**Source:** [The Text Editor sam](../works/the-text-editor-sam.md) — the treatment of
regular expressions as descriptions of a file's structure rather than as filters on
pre-cut lines, and the retrospective remark that its line-editor predecessor had been
imposing an array-of-lines model through its looping command all along.
