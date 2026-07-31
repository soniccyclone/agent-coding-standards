---
type: lesson
title: "Judge a system by its primitives, its means of combination, and its means of abstraction"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [expressiveness, primitive-count]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Judge a system by its primitives, its means of combination, and its means of abstraction

**Lesson:** A language is not mainly a way to instruct a machine; it is the framework within which its users organize their thinking about a domain. That reframing produces a specific evaluative instrument, and the instrument is what makes it useful rather than merely inspiring. Ask three questions of any system. What are its primitive expressions — the simplest things it can talk about at all? What are its means of combination — how are compound things assembled from simpler ones? What are its means of abstraction — how does a compound thing get named and thereafter handled as a unit?

The three are not a taxonomy to fill in but a diagnostic, because weakness in any one of them is a different disease with a different cure. Impoverished primitives mean the system cannot express its domain and users will smuggle in an escape hatch. Weak combination means everything must be written out at full size and there is no way to build the large from the small. Weak abstraction is the subtlest and the most common: users can build the compound thing but cannot name it, so the same construction is reassembled everywhere and the system's real vocabulary never grows beyond what its designer shipped.

The framing generalizes far past programming languages, which is why it is worth carrying. Configuration formats, query languages, build systems, APIs and schema languages are all evaluated this way, and the question people usually ask instead — what features does it have — is a poor substitute, because a feature list conflates the three and hides which one is missing. A system with rich primitives and no abstraction looks impressive in a demo and produces enormous unmaintainable artifacts in practice.

The corollary worth stating is that the same triple applies to the two categories a system manipulates. Both the operations and the data want primitives, combination and abstraction, and a system that supplies all three for one and only some for the other will bend everything it touches toward the half it supports properly.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) — chapter 1's opening statement of the framework: a powerful language serves as the framework within which we organize our ideas about processes, and every powerful language provides primitive expressions, means of combination and means of abstraction — applied to both procedures and data.
