---
type: lesson
title: "Extensibility is what you add when the core is too slow"
figure: pike
works: [the-text-editor-sam]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Extensibility is what you add when the core is too slow

**Lesson:** Treat a demand for a macro facility, a plugin API, or a user-scripting layer as evidence about the tool underneath it rather than as a feature request in its own right. People write shorthands for actions that are tedious to perform directly. If the direct action costs one gesture and returns its answer immediately, almost nobody bothers to name it, parameterize it, and store it somewhere for reuse — the abbreviation would cost more than the thing it abbreviates. So the volume of scripting a tool accumulates is a rough measurement of how much friction its primitive operations carry. Reading it that way inverts the usual response: instead of building the extension mechanism, go find the operations whose expense made it necessary.

This holds because an extension layer is a second, weaker interface to the same capability. It duplicates the semantics of the primitives, adds a naming and binding scheme, and introduces state that persists between sessions — so the tool no longer behaves identically each time you sit down at it, and every user's version diverges. The cost is paid permanently, by everyone, including the people who never write a script. Meanwhile the underlying friction remains: users have merely arranged to encounter it less often. Fixing the primitive removes the friction for everyone at once and leaves nothing extra to maintain, learn, or debug. The trade only favors extensibility when the space of things people want is genuinely open-ended and the primitives are already cheap — which is rarer than the request rate suggests.

There is a companion move that makes the argument work in practice: make the invocation surface itself editable, so repeating and varying a command needs no stored abbreviation. If the last thing you asked for is still sitting there as ordinary material you can adjust and re-run, the main practical benefit of a macro — not retyping — arrives without any macro machinery. A programmer who believes this responds to "can we add hooks/config/a DSL for this?" by asking which specific interaction was painful enough to prompt it, fixes that, and checks whether the request survives. Often it doesn't.

**Source:** [The Text Editor sam](../works/the-text-editor-sam.md) — the Reflections section, where the author answers why the editor was deliberately not made programmable, and the related discussion of why the command window is itself editable text.
