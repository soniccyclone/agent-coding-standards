---
type: lesson
title: "A proof step that refuses to fire is usually reporting a weak specification, not an inadequate rule"
figure: reynolds
works: [separation-logic-a-logic-for-shared-mutable-data-structures]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# A proof step that refuses to fire is usually reporting a weak specification, not an inadequate rule

**Lesson:** One routine can satisfy several specifications of different strength, and which one you adopt is not a matter of taste — it determines whether the composition steps you need are available. A copying routine that works on unshared structures also works, unchanged, on structures with sharing, and both claims are true. But the proof that goes through easily for the unshared case stalls for the shared one, at exactly the point where a recursive call has to be lifted into the surrounding context, because the pieces being recursed over are no longer separate and the rule that lifts local claims requires separateness. The productive reading of that stall is not that the rule is too restrictive. It is that the stated claim about the routine genuinely fails to say something the argument needs — nothing in it promises that a call working on one part leaves the shared remainder undisturbed — and a rule that fired anyway would be unsound. A concrete counterexample is constructible: a routine meeting the weaker claim is permitted to rearrange the shared portion, invalidating the sibling's description.

So when a step you expected to work refuses, run the diagnosis in this order. Ask what the step would have needed to be true, ask whether your hypothesis actually entails it, and only if it does should you suspect the rule. Most of the time the hypothesis does not entail it, the block is genuine information arriving early, and a rule generalized to let the step through would have been unsound in cases you had not thought of. This is the same reflex as trusting a type error over your intuition about the code, applied to proof rules.

The repair is instructive in itself. What was missing was a promise of non-disturbance, and enumerating the specific things preserved does not scale — you cannot list the properties of a structure you do not know the shape of. The move that works is to quantify over descriptions: take an arbitrary property of the resource as a parameter of the specification, and assert it still holds afterward. The claim becomes "whatever was true of this beforehand remains true", which is both stronger than any enumeration and shorter. Where a language cannot express that kind of quantification, the specification vocabulary needs extending rather than the property weakening — which is the honest general form of the point: preservation is naturally stated by quantifying over assertions, and a formalism admitting only concrete assertions will keep producing specifications too weak to compose.

**Source:** [Separation Logic: A Logic for Shared Mutable Data Structures](../works/separation-logic-a-logic-for-shared-mutable-data-structures.md) — section 6's treatment of the tree-copying procedure, which satisfies both an unshared and a shared-input specification but whose proof for the latter cannot apply the frame rule, together with the exhibited state change permitted by the weaker recursion hypothesis and the repair that introduces an assertion variable to state that every property holding of the heap beforehand still holds afterward.
