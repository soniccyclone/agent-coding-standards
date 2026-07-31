---
type: lesson
title: "Decide whether an operation needs the value or the place, and let the interface say which"
figure: wirth
works: [algorithms-and-data-structures]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Decide whether an operation needs the value or the place, and let the interface say which

**Lesson:** Two operations on the same structure can look identical at the call site and differ completely in what they need from the caller. One only wants to know which part of the structure to work on; it reads, computes, descends, and finishes. The other has to be able to replace what is there, which means it does not want the designation of a part — it wants the slot that holds the designation, so that assigning through it changes the structure as seen by everyone else. This is the distinction between being handed a value and being handed a place, and it is not a performance detail. Handing over a place is granting write authority over the caller's variable, and handing over a value is withholding it.

Read the choice as a statement rather than a mechanism, because that is how it should be made. Passing a designation by value says the relevant entity is the thing designated, and asserts that whatever the procedure does internally, the caller's own variable is not at risk of being changed underneath it — a guarantee the caller can rely on when reasoning about its own code. Passing the location says the opposite: that this call may replace what the caller was holding, and that the caller is expected to see the result. In a structure built out of links, this is precisely what distinguishes traversal from growth. You can walk a structure knowing only where you currently are; you cannot attach anything to it unless you hold the field that will point at the new part, because attaching means writing that field.

The design rule that follows is to let the mode of every parameter be chosen by which of the two an operation genuinely requires, and never by convenience or uniformity. Choosing the permissive mode everywhere costs nothing at runtime and costs a great deal in reasoning, because every call becomes a possible mutation of the caller's state, and nothing in the code distinguishes the calls that really do it from the ones that do not. Choosing the restrictive mode where mutation is needed does not fail quietly; it fails by making the operation impossible to write, which is the good kind of failure. The broader habit: whenever an interface can express a restriction that is true, express it, because the value of the restriction is entirely in what a reader may conclude from seeing it — and the reader loses that conclusion the moment the restriction is applied inconsistently.

**Source:** [Algorithms and Data Structures](../works/algorithms-and-data-structures.md) — section 4.4.2's remark that in the three traversal procedures the tree pointer is passed as a value parameter, which expresses that the relevant entity is the reference to the subtree and not the variable holding that reference, which could be changed were it passed as a variable parameter; contrasted with section 4.4.3's note that the search-with-insertion procedure takes its pointer as a variable parameter, essential because insertion must assign a new pointer value to the variable that previously held the empty-subtree value.
