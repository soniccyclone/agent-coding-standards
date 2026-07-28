---
type: lesson
title: "The trusted region grows for reasons unrelated to trust"
figure: saltzer
works: [protection-and-the-control-of-information-sharing-in-multics]
axes: [verifiability, primitive-count, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# The trusted region grows for reasons unrelated to trust

**Lesson:** Ask why a given piece of code sits inside the part of a system that
everything else depends on, and the answer is usually not that it needs to be there.
It is there because crossing the boundary was expensive when it was written, or because
a deadline made the shortcut irresistible, or because it arrived as part of a larger
component that nobody took the time to split into the part that needed privilege and
the part that merely came along. None of those reasons is about trust. All of them
survive long after the circumstance that produced them has passed, because nothing ever
prompts a re-examination — the code works, and its location is invisible in normal
operation.

The important consequence is that the size of a trusted region is not evidence of how
much trust the system actually requires. It is an accumulated record of past
convenience, which means it is compressible, often dramatically, by exactly the analysis
nobody did the first time: for each resident, name the reason it is inside, and check
whether that reason still holds. A region that grew this way is not merely bloated; it
is uninspectable, and it is uninspectable in the one place where inspection is the only
available means of confidence. So the measurement — how much is in here, and why — is
the whole intervention. Once each entry has an attributed reason, the ones with stale
reasons become obvious, and shrinking becomes ordinary refactoring rather than a
research problem.

Two of the three causes deserve particular suspicion because they masquerade as
engineering. The performance argument for putting something inside is often a fossil:
it was measured against a cost that later designs eliminated, and it never got
re-measured. The decomposition failure is the one that hides best, because from the
outside a coarse component looks like a single thing that needs what it needs, and only
someone willing to open it up can discover that nine tenths of it is ordinary code
riding along on the privileges of the other tenth.

A programmer who internalizes this keeps an explicit inventory of whatever their system
treats as trusted — the privileged service, the shared library everything links, the
process that runs as root, the module with the database credentials — with a stated
reason per entry and a habit of periodically re-asking whether the reason survives.
The alternative is the normal outcome, where the trusted region only ever grows and
nobody can say what would happen if any part of it were wrong.

**Source:** [Protection and the Control of Information Sharing in Multics](../works/protection-and-the-control-of-information-sharing-in-multics.md)
— the first of the two major weaknesses the paper reports on itself, counting the
fraction of modules residing in the most protected area and attributing that residency
to design-time economics, schedule pressure, and insufficiently fine analysis of
composite subsystems, with the assessment that restructuring could shrink it by roughly
an order of magnitude.
