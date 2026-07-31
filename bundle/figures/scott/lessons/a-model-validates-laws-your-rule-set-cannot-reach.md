---
type: lesson
title: "A model validates laws your rule set cannot reach, and those are the rules you are missing"
figure: scott
works: [data-types-as-lattices]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# A model validates laws your rule set cannot reach, and those are the rules you are missing

**Lesson:** The usual reason given for constructing a model of a formal system is defensive: it shows the rules are consistent, that they do not prove everything. That is the smaller half of what a model is for. The larger half is that the model has structure the rules never mentioned, and that extra structure proves things. Scott closes his development of the language by producing an equation that is stated entirely in the system's own notation, is true in the model, and cannot be derived by the system's ordinary rewriting rules. He does not treat this as an embarrassment for either side. He treats it as evidence that the rule set is incomplete with respect to its intended meaning, remarks that there must be many more such equations, and leaves them as work to be done. The gap between what is true of your semantics and what your rules can derive is a to-do list, not a nuisance.

The shape of the argument that gets him there is worth taking as a technique on its own. The rules can only push terms around; they have no notion of one term being an approximation of another. The model does, and it characterizes the recursion operator as producing the *least* solution of an equation. So to prove two terms equal he shows each one satisfies the equation whose least solution the other is, concluding each lies below the other, and then closes by antisymmetry. Ordering plus minimality does in a few lines what no amount of rewriting will do, because the fact being used — that this is the smallest thing with the property, not merely a thing with the property — is not something the rewriting rules can express. Whenever your reasoning leans on minimality, uniqueness, or "nothing else has this property," check whether your mechanical rules can even state that; if they cannot, no tool implementing them will ever confirm your argument.

Two working consequences. First, when a proof assistant or a rewriting engine cannot discharge something you are certain of, the honest diagnosis is not always that you are wrong or that the tool is weak — it may be that the property you are relying on lives in the semantics and was never encoded into the rules, and the fix is to add it as a rule with the semantic argument as its justification. Second, in the other direction, when you extend a rule set on the strength of a model, you have decided that this model is the one that matters; anything else that was also a model of the old rules is now excluded. That is a real commitment and is best made knowingly, since the rule you gain and the models you lose are two descriptions of the same change.

**Source:** [Data Types as Lattices](../works/data-types-as-lattices.md) — the closing paragraphs of Section 2, which present an equation about the recursion combinator that holds in the model, is expressible in the pure calculus, and cannot be proved by ordinary reduction; the two-sided argument that establishes it by using the least-fixed-point property of each side against the other and concluding equality from mutual containment; and the remark that many other such equations must exist.
