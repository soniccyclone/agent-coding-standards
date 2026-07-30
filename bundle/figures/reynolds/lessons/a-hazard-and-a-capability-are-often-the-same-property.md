---
type: lesson
title: "A mechanism's hazard and its expressive power are often the same property seen twice"
figure: reynolds
works: [the-craft-of-programming]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# A mechanism's hazard and its expressive power are often the same property seen twice

**Lesson:** Two properties of textual argument substitution are usually written up as defects. An argument gets re-evaluated every time the body mentions it, which is wasteful and surprising. And an argument can overlap with something else the body touches, so that changing one changes the other, which quietly breaks components written on the assumption that their arguments are independent. Both complaints are correct. But put them together deliberately — pass a variable that the body will assign to, and separately pass an expression built from that same variable — and you have a general summation operator: each time round, the body advances the variable, and each time round the expression means something different because it depends on the variable. The two "defects" are what make it possible to parameterize an iteration by the term to be accumulated, in a language with no other way to say that.

The lesson is not that the hazards are secretly fine. It is that a property is not a defect or a feature in itself; it becomes one when combined with an intention, and the same property serves both. Before eliminating a hazard wholesale, work out what capability disappears with it, and decide whether you have another way to get that capability. If you do, remove the hazard without regret. If you do not, you are trading a class of bugs for a class of things nobody can express, and that trade should be made knowingly rather than as a hygiene measure.

The mature resolution is usually not to choose but to stratify. Keep the general mechanism as the definition, because it is the one everything else can be explained in terms of, then define restricted forms on top of it — copy the argument in on entry, copy the result out on exit — that mechanically eliminate the overlap and the repeated evaluation, and make those restricted forms the default that people reach for. The general form remains available for the few cases that need it, including the case where an argument must not be evaluated at all unless another argument permits it. What you must not do is delete the general mechanism because the restricted one covers the common case; the definition is what the restricted forms are explained by, and losing it costs you the ability to say what they mean.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 3.1.5, which presents call by value and result as a transformation into local variables that eliminates interference and repeated evaluation, notes that call by name nonetheless remains conceptually more fundamental since the others are defined in terms of it, gives the case where an argument must go unevaluated to avoid a subscript error, and then presents Jensen's device, which turns repeated evaluation and interference into advantages by making a summation procedure whose accumulated term is supplied as an expression depending on the loop variable passed alongside it.
