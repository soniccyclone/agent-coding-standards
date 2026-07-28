---
type: lesson
title: "Sugar cannot break a law, so a broken law is proof that an addition is genuinely primitive"
figure: landin
works: [generalization-of-jumps-and-labels]
axes: [primitive-count, verifiability]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Sugar cannot break a law, so a broken law is proof that an addition is genuinely primitive

**Lesson:** Claims that a feature is "just sugar" or "not expressible here" are usually settled by whoever is more confident, because both sound unfalsifiable. Landin shows they are not. Anything introduced purely by definition on top of an existing system inherits that system's equivalences: it is built out of pieces that already obey them, so it cannot make a previously valid interchange invalid. Turn that around and you have a test with real teeth. Exhibit an equivalence that holds throughout the host system, then exhibit two programs in the extended system that the equivalence says are interchangeable and that observably are not. You have proved, not asserted, that the extension is a new irreducible ingredient and no amount of cleverness with definitions will reach it.

He runs the test twice. For a mutable store, the law he picks is that taking a compound thing apart and putting it straight back together must yield something indistinguishable from the original — a law that survives every definition you could write, and that a store destroys the moment two names can refer to the same mutable cell. For his own control operator, the law is substitution: a definition with no free variables, used only inside an inner scope, can be moved into that inner scope without changing anything. He gives two programs differing only in where such a definition sits and notes that with his operator present they behave differently, because what the operator captures is precisely the surrounding situation that moving the definition changed. In one stroke that shows the operator is not definable in the purely functional host, and also shows exactly which property of the host it destroys.

The cost side is stated with unusual candour. Because the new operator depends on the machine's notion of a suspended situation rather than on the abstract things expressions denote, he can no longer define meaning by a function from expressions to values as he had before; the semantics has to be given in terms of the machine's step-by-step behavior instead. That is a substantial retreat, and he takes it openly. The lesson embedded in the retreat is that irreducibility is not a badge of honour. A feature that cannot be defined away is a feature that has to be built into whatever you reason with, so the abstraction level at which you can explain your system drops to accommodate it.

The working habit this produces is to demand a witness rather than an argument. When someone says a library or a language extension adds nothing fundamental, ask which existing law it would have to break to be adding something, and go look for a program pair that breaks it — usually built around aliasing, ordering, identity, or capture of surrounding context. When someone says a feature is essential, run the same test in reverse: if no law breaks, the feature is convenience, and convenience belongs in a layer that cannot complicate the core. Either way the argument ends with a program you can run instead of two opinions.

**Source:** [A Generalization of Jumps and Labels](../works/generalization-of-jumps-and-labels.md) — the remark proving that a mutable store cannot be introduced into a purely functional system by definition because no definition can disturb take-apart-and-reassemble interchangeability, the paired programs showing the new control operator defying the substitution rules with the irreducibility corollary drawn from them, and the accompanying admission that meaning must now be specified via the abstract machine.
