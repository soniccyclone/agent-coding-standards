---
type: lesson
title: "Two specifications can be identical and still want different answers"
figure: ullman
works: [assigning-an-appropriate-meaning-to-database-logic-with-negation]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [databases-and-data-management, formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# Two specifications can be identical and still want different answers

The hope behind any search for the right semantics is that meaning is recoverable
from the text: given the rules and the data, a sufficiently clever definition will
produce what the author intended. Ullman closes his survey by reporting the
counterexample that undermines it. A rule set describing which board positions are
wins, and a rule set describing where in a complex of buildings to place cafeterias
and lounges, are the same program up to renaming. They want different answers. The
game wants the single determinate reading, with draws left undetermined. The
building layout wants the whole family of alternative determinate readings, because
each one is a legitimate plan and the point is to enumerate the options. No
definition operating on the text can serve both, since the text is the same.

The reason is that the two problems ask different questions of the identical
structure. One asks what is forced; the other asks what is possible. Those are
distinct queries, and the ambiguity that is a defect in the first case — several
consistent readings, none forced — is exactly the deliverable in the second. This
is why the search for a single universally correct interpretation stalls, and
Ullman is candid that his own prior confidence in one answer did not survive the
anomalies. The later generalization he describes, which lets a reader choose which
negative assumptions to commit to and leave the rest open rather than treating all
of them uniformly, is a concession to the same fact: the parameter that resolves
the ambiguity is not in the program.

The habit to carry away is to stop treating interpretive ambiguity as a bug to be
eliminated by a better default and start treating the choice of resolution as an
input the author has to supply. A constraint system, a package resolver, a
scheduler, a planner and a policy engine all sit on structures that admit multiple
solutions, and whether the correct output is the one forced solution, the set of
all solutions, or an arbitrary member of that set depends on what the caller is
doing — not on the constraints, which are identical in all three cases. Designs
that hard-code one of those readings will be wrong for real users of the other
kind, and the wrongness will be invisible in the specification, because the
specification looks exactly the same either way.

**Source:** [Assigning an Appropriate Meaning to Database Logic with Negation](../works/assigning-an-appropriate-meaning-to-database-logic-with-negation.md) — the closing section on the limits of well-founded and stable models, built around the pairing of the game rule with the structurally identical cafeteria-placement program whose intended answer is the family of alternative solutions, and the subsequent generalization allowing selective negative assumptions.
