---
type: lesson
title: "Label the seam where your formalism meets the informal thing it stands for: inside is proof, across is hypothesis"
figure: kleene
works: [recursive-predicates-and-quantifiers]
axes: [verifiability, expressiveness]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Label the seam where your formalism meets the informal thing it stands for: inside is proof, across is hypothesis

**Lesson:** Recognizing that some procedure really does settle a question in finitely many steps is a judgment a person makes, not a fact a formalism delivers. So when a precisely defined class is put forward as capturing that judgment, the identification is doing double duty and the two duties must not be confused. Read one way, it is a definition: it fixes the meaning of the informal phrase so a mathematical theory can be built, and nothing about the theory is in doubt. Read the other way — the way that matters, because everyone already has the informal notion — it is a hypothesis about whether the theory applies to what you meant, and it is supported only by accumulated evidence: every procedure anyone has recognized as effective and then examined has landed inside the class. Compelling, but an entirely different kind of support than a proof.

The same bookkeeping applies wherever a structural stand-in replaces an informal ambition. Identifying "has a formal deductive system" with "provability takes the shape of an existential claim over a decidable check" is a bridge hypothesis; so is identifying "constructively proves that every input has an output" with "exhibits a computable witness function." In each case a converse is available — anything of the stated shape can be realized as a system of the informal kind — which is what makes the identification feel definitional rather than arbitrary. Naming the two readings separately is not pedantry; it tells you exactly what would count as a refutation and exactly what would not.

The payoff for being explicit is enormous and easy to miss. Because the bridge is stated structurally, in terms of the shape of the guarantee rather than any particular system's rules, the limitation it yields is not a construction performed against one system after the fact. It applies in advance to every system anyone will ever build, and the awkward properties can be exhibited as values of one fixed, pre-announced family. Trading a per-instance argument for a universal one is entirely the work of having stated the bridge as a general structural claim.

For anyone writing specifications this is the whole shape of the specification-versus-intent problem, and it argues for a habit rather than a technique. Everything you prove is proved about the model. The claim that the model is the requirement sits outside the proof system, is supported by review, by convergent independent formulations, and by the continued failure of counterexamples to appear, and is never itself established by more internal rigor. So mark that seam in the artifact, and aim scrutiny at it, because piling more verification on the interior does nothing to strengthen the one claim most likely to be wrong.

**Source:** [Recursive Predicates and Quantifiers](../works/recursive-predicates-and-quantifiers.md) — the Part III passages introducing the three theses, which explicitly separate the definitional reading from the hypothesis reading, note that the recognition of effectiveness is a subjective act, and observe that stating the provability bridge structurally is what lets one preassigned family of propositions defeat every possible system rather than one system at a time.
