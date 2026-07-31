---
type: lesson
title: "Prefer the class closed under composition over the simpler class inside it"
figure: scott
works: [data-types-as-lattices]
axes: [expressiveness, cognitive-load, verifiability]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# Prefer the class closed under composition over the simpler class inside it

**Lesson:** When you are choosing which functions to admit, there is usually an obvious restrictive class whose members are individually easier to understand, sitting inside a wider class whose members are individually stranger. The wider class is normally the right choice, and the deciding property is not elegance but closure under the operations you build with. A class whose members you can describe crisply but which loses a member as soon as you substitute one variable for another is not an abstraction level at all; every construction you perform has to be accompanied by a check that you are still inside it, and eventually you leave. Scott's concrete instance: functions determined by their behavior on single elements of an argument are simpler to state and to compute with than functions determined by behavior on finite subsets, but the simpler class is not closed under substitution — identifying two arguments of a well-behaved two-place function of the simple kind yields a one-place function of the general kind, and no amount of care avoids this.

The wider notion also turns out to have the better intuitive reading, once you look for it. Restricting to single elements says each element of an input contributes independently. Admitting finite subsets says the elements of an input may cooperate in determining an output, subject to the constraint that no output can depend on more than finitely much of the input. That constraint is the real content of the requirement, and it is exactly the condition an implementation must satisfy: an answer has to be committed after finitely many observations of an argument that may be infinite. So the wider class is not a technical concession forced by closure; it is the class that correctly expresses what a finite mechanism can do, and the narrow class was an unmotivated additional restriction that happened to be easier to describe.

The habit to carry away is to test any proposed restriction against the operations you intend to use, before adopting it, rather than after. Ask what happens under composition, under substitution of one variable for another, under taking limits, under whatever your combining forms are. A restriction that survives all of them is a genuine abstraction and you can stop checking. One that does not is a promise you will spend the rest of the project failing to keep, and the honest move is to widen the class until it closes, even if the resulting members are harder to picture.

**Source:** [Data Types as Lattices](../works/data-types-as-lattices.md) — Section 1's substitution theorem establishing closure of continuous functions under substitution, the Section 2 reading of continuity as finitary cooperation among the elements of an argument, and the Appendix's discussion for Section 2, which contrasts distributive with continuous functions, shows that a distributive function of two variables becomes non-distributive when its arguments are identified, and gives this failure of closure under substitution as a reason continuous functions are the better class.
