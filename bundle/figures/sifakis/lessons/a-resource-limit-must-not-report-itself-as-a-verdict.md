---
type: lesson
title: "Give an analysis a third answer: yes, no, and I ran out of budget"
figure: sifakis
works: [cesar-1982]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Give an analysis a third answer: yes, no, and I ran out of budget

**Lesson:** The iteration at the heart of this method converges, but there is no useful bound in advance on how many rounds it will take. Rather than let that become an unbounded wait, the user sets a ceiling on iterations. The important design decision is what happens when the ceiling is hit: the analyzer reports that it has no answer. It does not report failure of the property, and it does not report success on the partial result it has accumulated. Exhausting a budget is a fact about the run, not a fact about the system, and the tool refuses to launder one into the other.

That distinction is worth being severe about, because the ways of getting it wrong are all tempting and all quiet. Returning the partial fixed point as though it were the limit reports a property as violated when it may hold. Returning success on timeout ships a false guarantee. Even a warning attached to an otherwise ordinary verdict tends to disappear, because everything downstream is written to consume the verdict. The only robust arrangement is a distinct outcome that no consumer can accidentally treat as either answer.

The general form: any procedure that terminates on a resource limit rather than on a decision needs its answer type widened to admit that case. This applies to solvers with timeouts, static analyses with widening thresholds, retries with deadlines, sampling with a cap. It is also a spec-level point about honesty on the boundaries of a method — the paper is equally direct that the whole approach is limited by which variable domains can be handled at all, and a tool that states its limits is a tool whose successes mean something.

**Source:** [Specification and Verification of Concurrent Systems in CESAR](../works/cesar-1982.md) — the user-imposed bound on iterations and the analyzer's explicit failure-to-answer outcome in section 4.2, together with the conclusion's statement of the method's limitations on variable types and complexity.
