---
type: lesson
title: "Judge a design by which programs it has ruled out, not by whether it looks tasteful"
figure: parnas
works: [on-the-design-and-development-of-program-families]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Judge a design by which programs it has ruled out, not by whether it looks tasteful

**Lesson:** Structural quality is normally assessed by consulting someone respected and asking whether they like it. That is not a standard, it is deference, and it leaves practitioners with no way to argue and no way to improve except by imitation. There is an alternative that admits an actual answer. Any precise description of a partially completed design — a refinement with holes in it, a set of external descriptions of parts, or a mixture — determines a set of programs consistent with it. Every decision made shrinks that set. So you can ask of any point in a development: which programs have been excluded so far, and which remain? Now there is something to inspect.

The criterion follows immediately. A development is going well if the decisions taken early exclude only programs that are uninteresting, undesirable, or unnecessary, and if every decision that would exclude a program someone might want is either postponed or sealed inside a boundary where reversing it touches nothing else. Criticism becomes concrete in the same motion: the complaint is that a particular assumption, one with a real chance of changing, has influenced too much of the code — either because it was taken too early or because it was never confined to a single keeper. That is a claim about a design that another person can check and dispute, unlike a claim about elegance.

Two honesties keep this from becoming its own dogma. First, this is not the only thing worth measuring. Ease of understanding and ease of verification matter too, there is reason to think they are correlated with this measure, and no reason to assume they agree; the difference is that ease measures are relative to whoever is doing the understanding, while the set of excluded programs can be examined without reference to a particular reader. That is exactly why it is worth having in the toolkit — not because it is the whole of quality, but because it is the part that does not depend on who is looking. Second, applying it still needs judgment: which assumptions are likely to move is a matter of experience, and no formalism supplies that. It is, though, a far more tractable thing to argue about over a table than whether a structure is beautiful.

The habit this produces is small and worth adopting directly. At any point in a design, be able to say what has been ruled out. If you cannot, you do not know what you have decided.

**Source:** [On the Design and Development of Program Families](../works/on-the-design-and-development-of-program-families.md) — the concluding remarks, which contrast asking a famous practitioner for a verdict on taste with asking which programs a family description excludes, state the criterion for a good development, and qualify it against clarity and verification as independent measures.
