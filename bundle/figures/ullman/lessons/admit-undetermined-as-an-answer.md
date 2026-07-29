---
type: lesson
title: "Admitting 'undetermined' as an answer buys you a total, computable definition"
figure: ullman
works: [assigning-an-appropriate-meaning-to-database-logic-with-negation]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [databases-and-data-management, formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# Admitting 'undetermined' as an answer buys you a total, computable definition

Insisting that every question have a yes-or-no answer feels like rigour and often
costs you both totality and tractability. Ullman's comparison of the two rival
treatments of recursive negation is a clean demonstration. The approach that keeps
a strict two-valued discipline gives no verdict at all on some programs — a
preferred reading may fail to exist, or several may exist with nothing to choose
between them — and determining whether one exists at all is beyond polynomial
reach. The approach that admits a third status, neither established nor refuted,
is always defined and computable in time polynomial in the data. Weakening the
demand on the answer is what made the answer obtainable.

The third value is not a fudge, because it names something real. In the circuit
reading Ullman uses, the propositions that come back undetermined are exactly the
terminals whose value the circuit does not fix: mutually dependent gates that will
settle one way or the other according to physics the model does not describe. In
the game reading, the undetermined positions are exactly the draws. In both cases
the honest structure of the problem has three outcomes, and a two-valued
formalism was mismodelling it — being forced either to invent a verdict or to fall
silent. The two approaches also agree wherever agreement is possible: on the
programs where everything does come out determinate, they coincide, so the third
value costs nothing on the easy cases and only pays out on the hard ones.

Which points at a general design instinct: when a definition or an analysis keeps
failing to be total, check whether you have demanded a binary verdict from a
situation with three outcomes. Type checkers that answer "cannot prove either
way," schedulers that report "no ordering is forced," reachability analyses that
distinguish unreachable from unknown, and health checks that separate failing from
not-yet-determined are all the same manoeuvre, and each one converts a
partial-or-intractable procedure into one that always terminates with information
you can act on. There is a real cost — every consumer downstream now has a third
branch to handle — but the alternative is worse: a total-looking answer that
fabricated a verdict, or a procedure whose running time you cannot bound. The
choice between two competing semantics is often really a choice about how much you
insist on knowing, and the community that prizes being able to answer at all will
pick differently from the one that prizes the answer's philosophical purity.

**Source:** [Assigning an Appropriate Meaning to Database Logic with Negation](../works/assigning-an-appropriate-meaning-to-database-logic-with-negation.md) — the sections developing three-valued well-founded semantics against two-valued stable models, including the two circuit examples where undetermined terminals correspond to unmodelled races, the game rule whose draws are undetermined, and the closing note on the tractability gap between the two.
