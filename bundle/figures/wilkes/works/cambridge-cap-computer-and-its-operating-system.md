---
type: work
title: "The Cambridge CAP Computer and Its Operating System"
figure: wilkes
description: The full account, co-written with Roger Needham, of the CAP machine's capability-based protection architecture and the operating system built on top of it. It covers the hardware representation of capabilities, how protected procedures use them to enforce access control without a trusted supervisor mediating every call, and what it took to get a working system running on real hardware rather than in a simulator. CAP was the first working hardware implementation of capability-based addressing, and this book is the primary source for how it actually worked.
subdomains: [operating-systems-and-systems-programming]
year: 1979
url: https://www.cl.cam.ac.uk/events/50+5/assets/pdf/cap.pdf
extraction: complete
survey_pages: 177
survey_text_layer: full
survey_fetch_mb: 7
access: public
host: institutional
tags: [work]
---

# The Cambridge CAP Computer and Its Operating System

**Author(s):** Maurice V. Wilkes, Roger M. Needham
**Venue/year:** Operating and Programming Systems Series (Peter J. Denning, ed.), North-Holland, 1979.
**Source:** https://www.cl.cam.ac.uk/events/50+5/assets/pdf/cap.pdf — full scan hosted by the University of Cambridge Computer Laboratory (Wilkes's and Needham's own department) for a departmental anniversary event; originally listed as `paywalled` (the printed book is out of print and not otherwise freely available) but this institutional copy resolves and was visually verified (cover page, title page, and series listing all confirm the match).

## Lessons
- [To control an operation, guard the values it accepts instead of the actors allowed to perform it](../lessons/guard-the-value-not-only-the-actor.md)
- [Hierarchy is right for organizing control and wrong for organizing authority](../lessons/hierarchy-fits-control-flow-not-authority.md)
- [Prefer restrictions that make the forbidden thing unnameable over restrictions that merely catch the attempt](../lessons/make-the-forbidden-unnameable.md)
- [The return on minimum privilege is inspectable blast radius, and it is paid mostly in development and change](../lessons/least-privilege-pays-in-inspectability.md)
- [A design principle earns its keep by settling the hundreds of small decisions nobody could argue individually](../lessons/a-principle-that-settles-the-arbitrary-cases.md)
- [Let the requirement for privilege, not functional cohesion, draw your module boundaries](../lessons/let-the-privilege-requirement-draw-the-boundary.md)
- [A structural property decays through additions that individually violate nothing, so audit the property rather than the changes](../lessons/a-structural-property-decays-by-accretion.md)
- [Count the problems a design makes impossible to state, not just the features it provides](../lessons/count-the-problems-your-design-cannot-have.md)
- [Whoever saves your state holds your secrets, so look for leaks in the suspend mechanism and not in the interface](../lessons/whoever-saves-your-state-holds-your-secrets.md)
- [Price the generality you add for elegance by asking what the structure would actually change](../lessons/price-the-generality-you-add-for-elegance.md)
- [A service that both a layer and its clients require cannot live in either, and that is a verdict on the layering](../lessons/a-service-both-sides-need-belongs-to-neither.md)
- [Specify what a component requires from its environment, not only what it offers, and the call-versus-message choice becomes reversible](../lessons/specify-the-environment-a-component-needs.md)
- [The cost of crossing a boundary decides how much ends up inside it](../lessons/the-cost-of-crossing-decides-what-ends-up-inside.md)
- [Let a fixed core enforce distinctions whose meaning it cannot interpret](../lessons/enforce-distinctions-you-cannot-interpret.md)
- [State crash safety as ordering invariants, then defer every write the invariants do not pin down](../lessons/state-the-ordering-invariants-then-defer-freely.md)
- [Trade repeated work for the absence of state: abandon and retry instead of recursing](../lessons/trade-repeated-work-for-the-absence-of-state.md)
- [A uniform rule about failure doubles as a complexity budget you did not have to argue for](../lessons/a-uniform-failure-rule-is-a-complexity-budget.md)
- [Let a request escalate along the call chain until it meets enough authority, instead of asking who has it](../lessons/let-a-request-escalate-until-it-meets-authority.md)
- [Two mechanisms maintained for different reasons that must agree somewhere give you a free oracle](../lessons/two-mechanisms-that-must-agree-are-an-oracle.md)
- [Leaving a rule unenforced needs an argument about who could break it, not about how likely breakage is](../lessons/an-unenforced-rule-needs-a-bounded-set-of-violators.md)
- [The metaphor you adopt for a primitive fixes which operations are cheap and which become impossible](../lessons/the-metaphor-you-pick-fixes-what-is-affordable.md)
- [Choose a representation by what the management operations must iterate over, not by which is conceptually cleaner](../lessons/keep-together-what-must-be-managed-together.md)
- [Test a candidate architecture against the controlled exceptions experience says you will need](../lessons/test-an-architecture-against-the-exceptions-you-know-you-need.md)
- [When accountability fights speed, split the mechanism at the frequency boundary rather than picking one policy](../lessons/split-a-mechanism-at-the-frequency-boundary.md)
- [A convenience pool of ambient authority is invisible overprivilege, and its harmlessness is relative to a model you may change](../lessons/ambient-convenience-authority-is-invisible-overprivilege.md)
