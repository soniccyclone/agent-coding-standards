---
type: lesson
title: "Price a restriction instead of judging how restrictive it feels"
figure: chaitin
works: [on-the-length-of-programs-for-computing-finite-binary-sequences]
axes: [hardware-affinity, primitive-count, expressiveness]
subdomains: [foundations-of-computation, software-engineering-and-architecture]
tags: [lesson]
---
# Price a restriction instead of judging how restrictive it feels

**Lesson:** Chaitin took a general computing model and imposed what sounds like a crippling constraint: control can only transfer a bounded distance, so no instruction may jump further than a fixed number of steps from itself. Intuition says this destroys generality. It does not. Choose the bound large enough to hold an interpreter for the unrestricted model and the restricted machines can do everything the unrestricted ones can, at a cost in program size that is a constant factor rather than a change of kind. Meanwhile every program in the restricted model becomes position independent, since all its transfers are relative, which means programs can be built by concatenating pieces without patching addresses.

The habit worth taking from this is to evaluate a discipline by pricing it rather than by feeling its bite. The question is never whether the restriction removes something you can imagine wanting, because it always does. The question is what the restriction costs on the measure you care about, and what it buys. Here the cost is a constant and the purchase is composability, which is close to the best trade available. That same shape recurs: structured control flow, immutability, single ownership, pure functions, and bounded resource use all feel like losses of power and mostly cost a constant while making assembly and reasoning cheap.

There is a second effect in Chaitin's construction that is easy to miss. Because transfers became relative, absolute addresses vanished from the encoding, so the restriction did not merely cost nothing, it removed redundancy that a more permissive design was carrying. Constraints sometimes pay for themselves in representation size, because a smaller space of legal programs needs fewer symbols to name a program within it. Worth checking for whenever a restriction is on the table.

**Source:** [On the Length of Programs for Computing Finite Binary Sequences](../works/on-the-length-of-programs-for-computing-finite-binary-sequences.md) - Part 2, which introduces bounded-transfer machines, argues in two independent ways that a sufficiently large bound preserves full computing power, and notes that the resulting programs are instantly relocatable and convenient to assemble from subroutines.
