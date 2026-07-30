---
type: lesson
title: "An investment you cannot price needs a decider who has done both jobs, not a better formula"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# An investment you cannot price needs a decider who has done both jobs, not a better formula

**Lesson:** Choosing between a contract with a known cash flow and building infrastructure invisible to both management and customers is a resource allocation problem with no computable answer. The author says so plainly — it would be nice to have a formula for return on a proposed investment in reusable assets, they do not have one, and their allocations rest more on intuition than on calculation. He supports the admission with the evidence that makes it credible rather than merely modest: components that were built and never used once, and one occasion of coming precariously close to total system collapse. Failures in both directions, from the same team, reported.

What is valuable is that the response to an unpriceable decision is not to keep hunting for the metric. It is a structural claim about who is fit to decide, and it is arrived at by elimination — three funding arrangements are ruled out, each for a distinct reason. Infrastructure work cannot be folded into delivery work, because the goals and timescales are irreconcilable and the near deadline always wins. It cannot be a separate insulated function, because insulated from the consequences of its choices it drifts onto a tangent and optimizes for its own interests. And it cannot be commissioned and paid for by delivery, because delivery's horizon is exactly the horizon that this class of investment must outlast, so making delivery the customer imports the short view through the funding channel. That third exclusion is the counterintuitive one, since "let the users of the platform pay for it" sounds like sound discipline and is a common arrangement; the objection is that it converts a long-term decision into a sum of short-term ones.

What remains is people who alternate between both activities: the ones who have felt what inadequate tooling costs under deadline and who also know what the reusable stock could become. They are not better forecasters. They hold both cost functions in a form no report conveys, which is the only substitute available when the quantity is genuinely not measurable.

The residual work is honest about its own incompleteness: keep searching for processes that make good assets' benefits more visible and that quantify the cost of the difficulties inadequate tooling causes — attacking the measurement problem without pretending it is solved — and meanwhile circulate every outcome, favorable and not, so the organization's intuition is trained on real cases rather than on the ones that flattered someone.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 10 section 10.3's management-challenge discussion, which admits to having no good formula for return on investment in reusables and to deciding by intuition, cites reusable components never used and one near-total system collapse, argues that creating reusables cannot be part of production (clashing goals and schedules), cannot be isolated (it takes off on a tangent), and cannot be controlled or paid for by production (losing the long-term view), and concludes that decisions are dominated by people who alternate between both types of activity.
