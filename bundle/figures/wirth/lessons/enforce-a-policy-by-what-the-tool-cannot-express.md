---
type: lesson
title: "Enforce a policy by what the tool cannot express"
figure: wirth
works: [project-oberon]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Enforce a policy by what the tool cannot express

**Lesson:** A policy stated as a rule that people are asked to follow decays: it has to be taught, remembered, and checked, and every check is a thing someone can skip. A policy that follows from a tool's inability to express the forbidden thing does not decay, because there is no moment at which anyone could violate it. So when you find yourself writing a guideline about where some capability may be used, look first for a way to make the guideline a consequence rather than an instruction — typically by *removing* something from the tool that grants the capability, rather than by adding a checker beside it. Omission is a stronger enforcement mechanism than inspection, and it is cheaper, since the thing you build is smaller rather than larger.

The instance worth generalizing is a lower-level tool that deliberately declines to support declaring dependence on other components. Nothing needs to say that the low-level escape may only be used at the bottom of the system: a component written with that tool cannot name anything else, so it is a leaf by construction, and the escape hatch is confined to the leaves without a rule about it. Note that the omitted feature is not one anybody would have designed away for its own sake — declaring dependence is useful — and that is exactly the sign of a good structural constraint: a capability withheld from one tool because withholding it makes a boundary self-enforcing.

The constraint also has to be the *right* one, and the argument for that is separate and should be made. Here it happens that the benefit of dropping to the lower level comes from control over a small set of machine resources, and that control pays off in procedures that do not call outward, since those are the ones whose resource use is entirely local. So the tool's limitation and the reason for using the tool point at the same population, and the constraint costs nothing anybody wanted. That coincidence is what to look for before adopting this technique: check that the code which genuinely needs the capability is the same code the restriction still admits. A limitation that enforces a boundary but also excludes a legitimate use is not self-enforcing policy, it is an obstacle, and people will route around it in ways you will like less than the rule you were trying to avoid writing.

**Source:** [Project Oberon](../works/project-oberon.md) — section 8.4's remark, made in passing while introducing the assembler-coded kernel, that only base modules can be written in assembler because the assembler purposely does not accept the specification of imports; the accompanying reasoning that the prime justification for assembler coding is efficiency, obtained largely through judicious use of the few available registers, that efficiency matters primarily in leaf procedures which do not call upon others, and that it is therefore appropriate to restrict assembler use to leaf modules; together with the surrounding explanation that the kernel exists because the processor's supervisor mode is needed to protect the resource allocation tables whose corruption would be disastrous, and that the language provides no facility for handling the trap by which supervisor mode is entered.
