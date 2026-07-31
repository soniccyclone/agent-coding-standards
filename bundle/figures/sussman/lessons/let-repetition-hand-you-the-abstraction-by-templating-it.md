---
type: lesson
title: "When you see the same shape three times, write the template and turn its holes into parameters"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [expressiveness, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# When you see the same shape three times, write the template and turn its holes into parameters

**Lesson:** Three procedures sum different quantities over a range. Set side by side they are for the most part identical, differing in the name, in the function computing each term, and in the function producing the next index. The authors treat that as evidence rather than as an aesthetic complaint -- the presence of a common pattern is strong evidence that a useful abstraction is waiting to be brought to the surface -- and then give a mechanical procedure for surfacing it.

That procedure is what makes this more than an exhortation against repetition. Write the shared shape down as a template with explicit holes where the instances differ. Then convert each hole into a formal parameter. The abstraction is not invented, it is *read off*: whatever varies becomes an argument, whatever is constant becomes the body, and the result is guaranteed to cover exactly the cases you started from because it was derived from them.

Two properties recommend this over designing an abstraction up front. It cannot over-generalize, because the parameters come from observed rather than anticipated variation, so you get exactly the degrees of freedom the evidence supports. And it makes the result checkable: each original should reappear as a short call, and if one will not fit, that instance is telling you the pattern was less shared than it looked, which is information you want before committing.

The step people skip is writing the template down explicitly. Comparing implementations in your head yields a vague sense that they are similar; writing the shape with its holes marked forces precision about *which* parts vary, and that precision is the entire content of the resulting design. When the holes turn out to be numerous or oddly shaped, that is the signal to stop -- the cases are less alike than they appeared, and the abstraction would cost more in parameters than the duplication costs in lines.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) - chapter 1 section 1.3.1, which places three summation procedures side by side, notes they are for the most part identical apart from the name, the term function and the next-index function, states that such a common pattern is strong evidence of a useful abstraction waiting to be surfaced, shows the shared template with bracketed slots, and obtains the general `sum` procedure by transforming those slots into formal parameters -- after which each original is redefined as a one-line call.
