---
type: lesson
title: "When you borrow a mechanism, permit it less than its source did"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [primitive-count, verifiability]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# When you borrow a mechanism, permit it less than its source did

**Lesson:** Inheritance in programming languages serves two unrelated purposes that happen to share one syntax. Sometimes you derive from something because the derived thing genuinely *is* a special case of it, and the relationship carries meaning a reader can rely on. Other times you derive from it because it contains code you want, with no claim that the concepts are related at all — the classic example being a set built on a general collection, inheriting most of the collection's machinery while having to prohibit the indexed access that machinery offers, because indexing an unordered thing is meaningless. Both uses are legitimate. The second is defensible as long as everyone is clear that is what is happening.

The instructive move is what you do when designing your *own* composition mechanism with that history in front of you. The tempting choice is to allow both uses, since both proved useful. The better choice can be to permit only one and say so: this mechanism exists for building concepts, and using it merely because the ingredient contains something handy is out of bounds — even though nothing in the mechanism's implementation would stop you. You are deliberately declining half of what your inspiration supported.

The reasoning generalizes past inheritance. A mechanism's value depends on what a reader can infer from seeing it used, and every additional purpose you permit erodes that inference. If a construct can mean either "this is a kind of that" or "this borrows code from that," then encountering it tells a reader almost nothing and they must go read the details. Narrowing the permitted uses is how you buy back the inference — the same discipline that makes a restricted control-flow construct more informative than a jump. So when you adopt a mechanism from elsewhere, treat its full generality as a menu rather than a specification, and be explicit about which items you are refusing and why, because an unstated restriction gets violated by the next person and a stated one becomes a reviewable rule.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 3's distinction between subclassing for concept building and subclassing for code sharing, including the collection-and-set example where inherited indexed access must be prohibited, followed by the explicit insistence that the book's own synthesis operation is reserved for concept building alone.
