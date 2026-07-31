---
type: lesson
title: "Move the side condition inside the claim, and instantiation can no longer produce a falsehood"
figure: reynolds
works: [the-craft-of-programming]
axes: [verifiability, expressiveness]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Move the side condition inside the claim, and instantiation can no longer produce a falsehood

**Lesson:** A statement with a caveat attached to it — "this holds, provided the two names refer to different things" — is two artifacts in different notations: a formal claim, and an informal fence around it that no mechanism enforces. The fence is where the failures live, because every time the claim is reused the fence has to be re-checked by hand, and the reuse that breaks it is precisely the one that made the two names coincide. The repair is to stop having a fence. Make the proviso a hypothesis of the claim itself, expressed in the same language, so that the whole thing is one statement whose truth is unconditional.

What that buys is closure under substitution, and it is worth seeing exactly how it works. Take a claim that is true only under a separation assumption and instantiate it by identifying the two names: the claim becomes flatly false, and nothing in the artifact records that you have done something illegitimate. Take the version with the assumption folded in as a hypothesis, and apply the same instantiation: the hypothesis instantiates too, into something self-evidently unsatisfiable, so the whole implication remains true — vacuously, which is the correct outcome. The bad instantiation cannot generate a falsehood; it can only generate a statement whose antecedent nobody can discharge. You have converted an obligation on the *user* of the rule into a fact about the rule.

This changes what "reusable" means for a piece of stated knowledge. A claim that is unconditionally true can be handed to any consumer, substituted into blindly, composed with others, and mechanically checked, because its own text contains everything needed to know when it applies. A claim with an external proviso can only be used by someone who has read the prose and understood the reasoning behind it. Aim for the first: whenever you find yourself writing "assuming," ask what it would take to say that assumption inside the statement, and pay the notational cost of making it sayable. The measure of a specification language is whether the conditions your rules depend on can be expressed in it at all, since anything that cannot be said there will end up as a comment nobody enforces.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 3.3.2 on universal specifications, which observes that because of interference there are hardly any universal specifications of the ordinary precondition-statement-postcondition form and that obtaining them requires radically enlarging the specification language, introduces an explicit non-interference specification and an implication between specifications, exhibits an assignment rule made universal by taking non-interference as its antecedent, and then argues that universality is preserved by substitution by contrasting the substitution that identifies two identifiers applied to the bare rule, which yields a patently false statement, against the same substitution applied to the guarded rule, which yields a true one because its antecedent has become false.
