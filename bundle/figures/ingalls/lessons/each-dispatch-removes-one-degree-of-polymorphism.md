---
type: lesson
title: "Treat a dispatch as one degree of type-uncertainty removed, and chain as many as the problem has variable terms"
figure: ingalls
works: [a-simple-technique-for-handling-multiple-polymorphism]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
tags: [lesson]
---
# Treat a dispatch as one degree of type-uncertainty removed, and chain as many as the problem has variable terms

**Lesson:** A dynamic dispatch is best understood not as "calling a method" but as an operation that converts exactly one unknown runtime type into a known one. Once you hold that view, the standard complaint that single dispatch cannot express behavior depending on two independently varying operands stops being a language deficiency and becomes an arithmetic mismatch: the problem had two degrees of type freedom and you spent one dispatch on it. Spend a second and the mismatch is gone. The mechanism for spending it is to have the first dispatch's method — which now knows its own type with certainty — send a message whose *name* encodes that certainty, and send it to the still-polymorphic operand. Knowledge gained by a dispatch is carried forward in the selector, not in a variable, which is why no type test and no language extension are required.

The move generalizes past two. Each additional message send in the chain retires one more degree, and the count of chained sends is a direct measure of how many things about the situation were genuinely unknown at the call site. Which operand relays to which is not forced by the technique — both orderings give the same freedom from case analysis — so it is settled on other grounds: whichever family of classes is the more natural home for the final implementations, and which direction of extension you expect to happen more often. That is a design decision the technique surfaces rather than one it makes for you.

The disciplinary value is the diagnostic it supplies. When code in a language with dynamic dispatch starts explicitly interrogating an argument's type, that is almost never evidence the language is too weak; it is evidence a dispatch is missing, and the type test is a hand-rolled, non-extensible substitute for the one the language would have performed for free. A hand-rolled test buries the whole N-dimensional case matrix in one place, so every new kind of participant means editing code that already works — the exact failure that the message paradigm was introduced to eliminate. The correct reflex on seeing a type test is to ask which dispatch it is standing in for.

**Source:** [A Simple Technique for Handling Multiple Polymorphism](../works/a-simple-technique-for-handling-multiple-polymorphism.md) — the solution section, where message transmission is characterized as reducing a polymorphic variable to a monomorphic one, the relay methods introduce a new selector family to preserve what the first dispatch established, and the closing remarks on reversing the relay direction and on retiring higher degrees one send at a time.
