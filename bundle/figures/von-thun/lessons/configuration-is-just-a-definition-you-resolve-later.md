---
type: lesson
title: "Configuration is just a definition you resolve later"
figure: von-thun
works: [the-prototype-implementation-of-joy]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [programming-environments-and-object-systems, programming-languages-and-semantics]
tags: [lesson]
---
# Configuration is just a definition you resolve later

The implementation has no configuration format, no settings syntax, no options parser. What it has is a rule: on startup, look in the working directory for a file with a known name and read it as ordinary program text. Everything a site or a person wants to customise is expressed as definitions in the language itself, and the customary content of that file is a single directive to load the shared library — so the user file's real job is to establish an environment before the common code arrives. Loading is a stack of nested inclusions, so an environment can be layered as deeply as it needs to be, and the mechanism that builds it is the same mechanism that runs everything else.

The payoff shows in von Thun's small example of editing a file from inside the system. The shared library defines the editing action in terms of a symbol it never defines: the name of the editor. Each user's own startup file supplies that name. One reader wants a screen editor, another wants something else entirely, and the shared definition is identical for both and never has to change. The extension point is not a hook, a plugin API, or a variable looked up in a table — it is a name the shared code leaves for someone else to bind, resolved by load order. Nothing was designed as configurable; the dictionary simply is the configuration, because unresolved names are the natural place where a decision can be deferred.

The reason this stays simple is that no second language was introduced. A dedicated configuration format arrives with its own grammar, its own errors, its own type coercions, its own escaping rules, and eventually its own conditionals and interpolation as people discover it needs to compute things — reinventing, badly, the language sitting right next to it. If your system already evaluates a language and already has a namespace, the cheapest configuration mechanism is a file of definitions loaded early, and the cheapest extension point is a name you decline to bind. A programmer who takes this seriously reaches for a settings format last rather than first, and asks what the equivalent of "a definition supplied before the shared code loads" is in whatever system they are actually working in.

**Source:** [The Prototype Implementation of Joy](../works/the-prototype-implementation-of-joy.md) — the session-initiation and input/output sections describing the startup search for a user file and the stack of inclusions, together with the closing example where a shared definition of an editing command depends on an editor name that each user's own file supplies.
