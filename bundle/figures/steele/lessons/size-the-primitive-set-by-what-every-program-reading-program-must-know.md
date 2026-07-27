---
type: lesson
title: "Count your primitives by asking how much every tool that reads programs will be forced to hardcode"
figure: steele
works: [common-lisp-the-language-2nd-edition]
axes: [primitive-count, cognitive-load, verifiability]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
tags: [lesson]
---
# Count your primitives by asking how much every tool that reads programs will be forced to hardcode

**Lesson:** This specification gives an unusual justification for keeping its set of irreducible constructs small, and the justification is better than the aesthetic one. It is not that fewer constructs are more elegant, nor that they are easier to prove things about. It is that every program which analyses programs — the compiler, the code walker, the optimiser, the editor that indents, the tool that instruments — must contain special-case knowledge of each irreducible construct, and nothing can spare it that work. The size of the irreducible set is therefore not a property of the language alone; it is a fixed tax levied on every tool anyone will ever write for the language, forever.

The corollary is what makes the idea productive: constructs that reduce to others are *free* by this measure, because an analyser can expand them and then analyse the result with machinery it already has. A language can consequently carry an enormous amount of derived vocabulary without imposing any additional burden on tooling, provided the reductions are mechanical and available to the tools rather than lying only in the specification's prose. The document takes this seriously enough to spell out the protocol an analyser should follow — recognise the constructs you know, otherwise try to expand, otherwise treat it as an ordinary call — and to recommend that library-supplied expansions avoid leaning on implementation-private constructs, precisely so that a tool written against the standard can still walk them. It also concedes both directions of the freedom this creates: an implementation may realise a derived construct primitively for speed, or realise a nominal primitive as a reduction, and a tool must be prepared for either.

The reframing is that low primitive count buys *ecosystem* leverage rather than conceptual purity. The cost of a new irreducible construct is paid not once by the designer but N times by everyone downstream who has to understand programs mechanically, and those costs are invisible at design time because the tools do not exist yet. This also explains why an extension mechanism that produces reducible constructs is categorically different from one that produces new primitives: the first grows the language for free, the second taxes the whole ecosystem.

A designer who has absorbed this asks of every proposed addition whether it can be expressed as a transformation into what already exists, and treats an affirmative answer as a strong reason to ship it that way even when a direct implementation would be faster — then makes the transformation programmatically available, not merely documented. The same instinct applies well outside language design: any construct that tools must special-case (a new node type in an IR, a new message kind in a protocol, a new resource shape in a config schema) should be counted against the tooling budget, not the feature budget.

**Source:** [Common Lisp the Language, 2nd Edition](../works/common-lisp-the-language-2nd-edition.md) — the discussion in the program-structure chapter explaining why the set of special forms is deliberately fixed and small, together with the recommended processing order for program-analysing programs and the implementation note on keeping macro expansions free of implementation-private constructs.
