---
type: lesson
title: "Turn the machinery the implementation passes behind your back into an ordinary argument, then hide it again in the notation"
figure: sussman
works: [lambda-the-ultimate-imperative]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [programming-languages-and-semantics]
tags: [lesson]
---
# Turn the machinery the implementation passes behind your back into an ordinary argument, then hide it again in the notation

**Lesson:** Every runtime hands each procedure things the source text never mentions: where to send the answer, and the ambient context that determines what free names mean. Those are the two implicit arguments hiding inside a conventional call. The productive move is to write them down as real parameters. Once "where the answer goes" is an argument, escapes and early exits are not a new control feature but a second, alternative destination that some branch chooses instead of the default one. Once the ambient context is an argument, caller-determined variable lookup stops being a consequence of some closure-capture policy baked into the evaluator and becomes a data structure you build and extend yourself, which is what lets a procedure have one name resolved where it was written and another resolved where it was called — something no single global choice of capture rule can deliver.

Reification also composes in a way that hidden machinery cannot. Represent the ambient context not as a table plus a lookup routine but as the lookup procedure itself, closing over the bindings it knows and delegating what it does not, and it becomes the same kind of thing as the answer-destination: a procedure taking one argument. Two mechanisms that had nothing structurally in common are now the same mechanism, so they can be merged into one object that responds to several requests — return this value, resolve this name, assign this name, print how we got here. The debugging facility that seemed to require special interpreter support is just another message. Choosing a procedural representation for what looked like a data structure is what made the unification available.

The cost, of course, is that every call site now mentions plumbing it does not care about. That is where the second half of the discipline comes in, and the authors state it as a general criterion for judging any language: a good notation lets you leave out what carries little information. Make the hidden thing explicit to gain power at the semantic level, then arrange that the surface syntax omits it uniformly, so the notation says only what varies. Both halves are required. Keep the machinery implicit and you cannot express things the designer did not anticipate; make it explicit and stop there, and you have bought expressiveness with clutter at every call. The pair — reify, then suppress — is how a small core supports features that look like they need special support.

**Source:** [Lambda: The Ultimate Imperative](../works/lambda-the-ultimate-imperative.md) — the escape-expression section reframing an escape as an alternate destination for the answer; the dynamic-scoping section that threads an explicit environment argument through every call, states the suppress-what-carries-little-information criterion for languages, then reworks that environment from an association list into a delegating lookup procedure and merges it with the answer-destination into a single message-taking object.
