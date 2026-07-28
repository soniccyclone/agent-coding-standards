---
type: lesson
title: "Privacy is a runtime invariant to maintain, not a lexical fact to read off the text"
figure: milner
works: [a-calculus-of-mobile-processes]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, programming-languages-and-semantics]
tags: [lesson]
---
# Privacy is a runtime invariant to maintain, not a lexical fact to read off the text

**Lesson:** In a language with static scope, "who can see this name" is settled by the program text and never changes while the program runs. That reading survives only as long as names cannot be communicated. Once a private name can be sent in a message, the set of parties who hold it grows during execution, and the boundary that made it private has to grow with it — otherwise either the recipient holds a name it cannot use, or the name silently merges with an unrelated name the recipient already had. The design consequence is to stop treating a scope boundary as a fixed region of text and start treating it as something that moves, with the guarantee it enforces — this name is distinct from every other name in play — as an invariant the semantics is obliged to preserve across every step.

Two symmetrical hazards fall out, and both must be handled explicitly rather than assumed away. Sending a private name outward requires the enclosing boundary to expand to cover the recipient. Sending any name inward, toward a party that happens to hold a private name spelled the same way, requires that party's private name to be renamed first, because the coincidence of spelling is an accident. The formal machinery for this is precisely the bound-variable hygiene of the lambda calculus, transplanted from a static rewriting setting into a running system: renaming stops being a convenience of proof presentation and becomes an operational obligation.

The alternative was available and is argued against on purpose. Sending the text of a component rather than a reference to it means the component's free names get reinterpreted wherever it lands — dynamic binding, in the sense of the earliest treatment of function parameters in LISP. That is simpler to define, and it destroys the guarantee: a link that was private between sender and a neighbour is broken by transmission, and may silently reconnect to a same-named link at the destination. The harder rules are adopted because they are the ones that keep privacy meaning something.

A programmer who holds this view stops trusting textual encapsulation the moment references cross a boundary. Handing out an identifier for something private is an act that must either extend the private region or be forbidden; a system that has no representation for that extension has no way to state, let alone check, that its secrets stayed secret. Capability leaks, aliasing bugs, and tokens that turn out to be guessable are all the same failure — a static reading of a boundary that the runtime moved.

**Source:** [A Calculus of Mobile Processes, I and II](../works/a-calculus-of-mobile-processes.md) — Part I's basic examples of a private link's scope being intruded and extruded by communication, and Part II's transition rules that open a restriction into an action and re-close it around sender and receiver, together with the argument for static over dynamic binding when passing components.
