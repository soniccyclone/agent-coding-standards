---
type: lesson
title: "Generality and flexibility are two different purchases, paid for at different times"
figure: parnas
works: [designing-software-for-ease-of-extension-and-contraction]
axes: [expressiveness, cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Generality and flexibility are two different purchases, paid for at different times

Two responses to an uncertain future get filed under the same heading and are not the same thing. One is building something that copes with many situations without being touched; the other is building something that is cheap to alter into whatever the situation turns out to need. Parnas separates them by where the bill arrives. The first is paid continuously at run time, in the resources spent carrying machinery that any single deployment does not use. The second is paid once, up front, in design effort — and skilled designers can get a great deal of it without a run-time penalty at all, which is why the two are worth keeping apart in your head instead of collapsing into a vague preference for "adaptable" code.

Parnas traces the confusion to a borrowed instinct. For a mathematician, a more general result strictly dominates a narrower one — there is no cost to proving the stronger theorem, so generalizing is always progress. Engineers of physical things know better, because their generality shows up as a larger, more expensive product nobody wants: a receiver that decodes every broadcast convention on earth has a market of almost nobody. Programmers, working on abstract objects and taught by mathematicians, inherited the mathematician's reflex and apply it to artifacts that behave like the engineer's. Specialization is not a failure of ambition; it is what makes the thing affordable, and the general interface can coexist with narrow, cheap contents behind it.

Neither purchase is wrong. An organization with resources to spare, weak facilities for pushing changes into the field, or a real horror of maintaining many divergent versions may quite rationally choose to pay at run time and ship one general artifact. The failure mode Parnas names is not choosing badly but not choosing — the decision usually just *happens*, as a byproduct of whatever each contributor found natural, rather than being made once, deliberately, with the recovery of the investment in mind.

The programmer who has absorbed this asks two questions of every parameter, hook, and configuration point: which currency am I spending, and do I expect to earn it back? Design-time cost is only justified by changes you actually anticipate making; run-time cost is only justified by variety you actually intend to serve simultaneously. And nobody can hand you the right ratio — the point is that the ratio should be a position you hold, not a residue of a thousand unexamined local decisions.

**Source:** [Designing Software for Ease of Extension and Contraction](../works/designing-software-for-ease-of-extension-and-contraction.md) — The contrast between the mathematician's and the engineer's notions of generality in the discussion of module definition, developed into an explicit cost comparison in the closing summary.
