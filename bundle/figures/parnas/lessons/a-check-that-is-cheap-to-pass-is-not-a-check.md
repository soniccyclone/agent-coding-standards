---
type: lesson
title: "A check that can be passed without doing the work is not a check"
figure: parnas
works: [active-design-reviews-principles-and-practices]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# A check that can be passed without doing the work is not a check

**Lesson:** Any verification performed by a person has a cheapest passing state,
and people find it. Invite someone to raise concerns about a design and the
cheapest response is silence, which is indistinguishable from approval and carries
no risk of looking foolish. Ask whether a justifying assumption exists and the
cheapest response is "yes," which is also what a careful reader would say, so the
answer carries no information. The defect is not in the reviewer's diligence; it is
in a request whose satisfying answer costs nothing to produce. Under that design,
the more intimidated or overloaded the reviewer, the more the process converges on
producing approvals — precisely inverted from what you wanted.

The repair is to demand output that cannot be manufactured without engaging the
artifact. Instead of asking whether a claim is supported, ask which specific
statements support it, so the answer is a citation that either exists or does not.
Instead of soliciting defects, require positive assertions the reviewer must stand
behind and may be asked to defend, so that endorsing something becomes an act with
a cost attached rather than the default. In the strongest form, make the check
require actually using the thing: have the reviewer write code against the
interface being specified, since attempting to use a description is how its gaps
become visible in a way that reading never achieves. Notice how fine-grained this
gets — the difference between two phrasings of the same question decides whether
the whole exercise means anything.

The transferable habit is to evaluate any verification step by what its passing
signal costs to emit, not by whether the step exists. A green tick that a broken
system would also produce, a sign-off nobody can be asked to justify, an approval
whose cheapest path is inaction — these consume schedule and return confidence
without evidence, which is worse than having no step at all, because now everyone
believes the design was examined. A programmer who takes this seriously designs the
question before recruiting the answerer, and treats "could someone answer this
convincingly without having read the thing?" as the test the check itself must pass.

**Source:** [Active Design Reviews: Principles and Practices](../works/active-design-reviews-principles-and-practices.md)
— the diagnosis of why conventional reviews produce silence from under-briefed
reviewers, and the questionnaire-design discussion contrasting an active phrasing
that demands a citation with a passive one that is too easy to affirm.
