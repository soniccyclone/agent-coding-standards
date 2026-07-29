---
type: lesson
title: "Make formation total and judge acceptability separately, because what you forbid you can never explain"
figure: curry
works: [grundlagen-der-kombinatorischen-logik]
axes: [expressiveness, verifiability, cognitive-load, primitive-count]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# Make formation total and judge acceptability separately, because what you forbid you can never explain

**Lesson:** The standard response to terms that misbehave is to make them unformable: stratify the universe, restrict what may be applied to what, and declare the offending expressions to be not merely false but meaningless. Curry rejects the move on the grounds that it purchases safety with abdication. The contradictions do not live in those terms; they live in the properties someone wanted to attribute to them — a self-applied predicate is harmless until you insist the result is a proposition, a largest cardinal is harmless until you insist it is a cardinal. A discipline that forbids forming them avoids the contradictions at the price of never accounting for them, and a theory of reasoning that has to exclude some reasoning from its scope has failed at its own job.

His alternative is to take a single base category of things that can be identified and told apart, make application total on it — for any two things there is a thing that is the first applied to the second, no side condition — and then treat "which of these are acceptable" as a further question asked about terms, not a gate that decides whether terms exist. Two payoffs follow immediately, and Curry states both. Introducing new objects no longer requires reasoning about domains, because there is nowhere for an application to fail to land. And the rules of the system can be stated as unrestricted universals, which means they need no case analysis over sorts of thing; the entire frame gets smaller because generality in the rules is cheaper than a taxonomy the rules must respect. He is explicit that the price is real and that paying it is the point: sorting the acceptable from the unacceptable becomes the central problem of the theory rather than an assumption of it.

There is a methodological claim underneath. A prohibition defended in advance, on the grounds that violating it must produce nonsense, cannot be argued with — the only refutation available is to build a coherent theory that violates it. Curry notes that the usual a priori defence proves too much: the same argument that forbids quantifying over all propositions because doing so creates new ones would forbid quantifying over all oranges because new oranges keep being grown. General judgements are grasped through the character of the property, not by surveying a completed collection, so no completed collection needs to exist.

A programmer who works this way separates the layer that builds things from the layer that approves them. Parsers accept, checkers reject. Representations are total, with validity as a predicate you can query, log, and refine — instead of a constructor that throws and thereby destroys the evidence. Type systems sit on top of an untyped substrate rather than being welded into term formation, so an unassignable term is still a term you can inspect, reduce, and diagnose. The habit generalizes past logic: any system that makes bad states unrepresentable also makes them undiagnosable, and when one shows up in production anyway, you will have no vocabulary for it.

**Source:** [Grundlagen der kombinatorischen Logik](../works/grundlagen-der-kombinatorischen-logik.md) — the philosophical chapter's discussion of allegedly meaningless notions and of unrestricted universals, together with the primitive frame that follows from them: one base category, a total application operation, and rules stated without restriction on their subjects.
