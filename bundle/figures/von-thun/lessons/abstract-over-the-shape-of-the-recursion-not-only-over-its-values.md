---
type: lesson
title: "Abstract over the shape of the recursion, not only over its values"
figure: von-thun
works: [joy-forths-functional-cousin]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [programming-languages-and-semantics, algorithms-and-complexity]
tags: [lesson]
---
# Abstract over the shape of the recursion, not only over its values

Parameterizing over data is second nature; parameterizing over control structure
is not, and that asymmetry is a habit rather than a necessity. Von Thun's
observation is that a large fraction of recursive definitions differ only in
their fillings, not their skeletons: there is a test for the base case, an answer
for the base case, a step that produces the smaller problem, and a step that
combines the result back up. Once that skeleton is captured as a single
operator, the individual functions that used to be written recursively become
four small pieces handed to it, and the recursion itself is written once and for
all rather than re-derived each time.

The payoff is not only brevity. Von Thun points out that recursion is one of the
few genuinely forcing reasons to give a function a name — you cannot call
yourself without a way to refer to yourself — and he treats this as an
irritation imposed by the notation rather than a fact about the computation. When
the recursive shape lives in the operator, the recursive function no longer needs
to exist as a named entity at all, and can be written inline exactly where it is
used, including as an argument to something else. A requirement that looked
structural dissolves once you notice it was serving the mechanism rather than the
problem.

The classification also does real conceptual work. Distinguishing linear from
binary recursion is not bookkeeping; it separates the family containing
accumulate-style traversals from the family containing quicksort and the
naive Fibonacci, and the family a problem belongs to is what determines its cost
profile and how it might be transformed. Making that distinction explicit in the
vocabulary means the shape of a computation is stated rather than inferred by
squinting at a definition body, which is exactly the information a reader or an
optimizer wants first.

A programmer who works this way looks at a set of similar recursive or looping
functions and asks what varies rather than writing each one out. They reach for a
traversal skeleton rather than hand-rolling the walk, and they name the pattern
of control in their vocabulary — fold, unfold, linear, tree-shaped — so that the
structure of a computation is visible from its call rather than reconstructed from
its body. The failure mode this guards against is a codebase where twenty
functions each re-implement the same descent, differing only in the two lines
that matter.

**Source:** [Joy: Forth's Functional Cousin](../works/joy-forths-functional-cousin.md) — the recursive-combinators section, which motivates the pattern-capturing operators by noting the nuisance of having to define a function explicitly only because it happens to be recursive, then distinguishes the linear from the binary recursion pattern.
