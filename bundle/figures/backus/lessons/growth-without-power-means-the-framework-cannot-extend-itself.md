---
type: lesson
title: "Growth without added power is evidence that the framework cannot be extended from inside it"
figure: backus
works: [can-programming-be-liberated-from-the-von-neumann-style, the-history-of-fortran-i-ii-and-iii]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Growth without added power is evidence that the framework cannot be extended from inside it

**Lesson:** Split any system into its fixed framework and its user-supplied parts. The framework states the rules everything obeys; the supplied parts are the things the rules anticipate but do not specify. A system's health can then be read off a single ratio: how much capability can arrive as a supplied part versus how much has to be cut into the framework itself. Nobody would legislate a hundred complicated features into the permanent rules if those features could have been defined later within them, so the sheer bulk of a framework is an admission, not an achievement. This gives a diagnostic that requires no taste: if successive versions get larger without getting stronger, the framework's definitional capability is the thing that failed, and adding version N+1's features will not fix it.

Two mechanisms decide the ratio. First, how tightly meaning is bound to state — if every step of a computation must be described as an effect on the state, then every anticipated need must be provided for in the state and its transition rules in advance, and the framework has to be exhaustive by construction. Second, whether the system's own combining machinery applies to everything it contains. Anything the framework can only mention but not manipulate becomes a dead end where composition stops. Names are the standard example: if names and functions are disjoint categories, if names cannot be applied, combined, or passed around like ordinary values, then each new naming discipline is a framework change rather than a definition. The alternative is to make the objects the system computes over able to stand for the system's own operators, at which point new ways of combining programs are introduced by writing ordinary definitions instead of by amending the language.

A designer who believes this measures a proposed feature by whether accepting it enlarges the permanent rules. Features that can be expressed within the existing rules cost nothing structural, however many there are. Features that cannot are expensive out of all proportion to their apparent size, because each one has to be accounted for by every later part of the framework and by everyone who reads the manual. When you find yourself about to build a special case into the foundation, the more valuable question is which missing definitional power made the special case necessary.

**Source:** [Can Programming Be Liberated from the von Neumann Style?](../works/can-programming-be-liberated-from-the-von-neumann-style.md) — the middle sections distinguishing a language's framework from its changeable parts and arguing that weak changeable parts force a bloated framework, together with the later treatment of representing operators as ordinary objects and of naming as an ordinary function. Also [The History of FORTRAN I, II, and III](../works/the-history-of-fortran-i-ii-and-iii.md) — the concluding comments, which read the size of contemporary languages as proof that their features could not have been defined rather than built in.
