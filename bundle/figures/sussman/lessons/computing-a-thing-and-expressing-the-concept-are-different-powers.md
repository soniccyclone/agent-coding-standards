---
type: lesson
title: "Being able to compute a thing and being able to express the concept are different powers"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Being able to compute a thing and being able to express the concept are different powers

**Lesson:** You can always write the multiplication out rather than naming the operation, and everything you could compute before you can still compute. What you lose is stated exactly: your programs remain able to compute cubes, while your *language* loses the ability to express the concept of cubing. Nothing about the achievable outputs changed; something about the achievable thoughts did.

That distinction is worth carrying because it is invisible to the usual way of evaluating a tool. Ask what a system can compute and two systems look equivalent. Ask what a system can *name* and they come apart, because naming is what lets a concept be referred to, reasoned about, passed around and generalized. Without a name for summation you can write any particular sum; with one you can state results about summation itself, independent of which series is being summed. The mathematicians' sigma notation is the same move and bought the same thing.

The practical consequence is that anyone restricted to expressing only instances is forced to work permanently at the level of whatever operations happen to be primitive in their tool. Their programs will be correct and their vocabulary will be their vendor's. Every recurring idea in their domain either gets rewritten at each use or gets a name only in comments and conversation, which is to say in places the system cannot act on.

So when evaluating any notation -- a language, a query dialect, a configuration format, an interface -- the question is not what it can accomplish but which of your domain's recurring concepts it lets you name and then manipulate as things. Concepts you can only spell out are concepts you cannot build on, and the cost appears not as a missing feature but as an absence in what the users of that system are able to think about.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) - chapter 1 section 1.3's opening, which observes that one could get along without defining `cube` by always writing the multiplication out, and that doing so would force working at the level of whatever operations happen to be primitive -- programs able to compute cubes, in a language lacking the ability to express the concept of cubing -- with the parallel to sigma notation, whose power is that it permits dealing with the concept of summation itself rather than only with particular sums.
