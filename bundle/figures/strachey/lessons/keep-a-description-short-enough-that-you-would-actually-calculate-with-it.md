---
type: lesson
title: "Keep a description short enough that you would actually calculate with it"
figure: strachey
works: [toward-a-mathematical-semantics-for-computer-languages]
axes: [cognitive-load, verifiability, primitive-count]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# Keep a description short enough that you would actually calculate with it

Having written a clause dense enough that they expect the reader to recoil, Scott and Strachey defend it on a ground that has nothing to do with elegance. Condensing each clause to a line or two is an advantage, they say, because someone who can write the equations out in full has a chance of proving something about them — and that chance improves as the equations get shorter. Length is being treated as a capability constraint. A description exists to be manipulated: substituted into, rearranged, inducted over, ground down until two things turn out to be equal. Past a certain size nobody performs that manipulation, not from laziness but because the number of steps and the opportunities for error grow past what a person will sustain. So a formal description that is correct but bulky is not a slightly worse version of a compact one; it is an artifact of a different kind, useful for reference and useless for reasoning.

This gives a criterion for the operators you build to write such descriptions with, and the criterion is what they conceal. Their combining forms absorb the routine plumbing — the threading of state, the pairing and projecting, the order of composition — so that what survives on the page is the structure of the construct and the order in which its parts happen. The intended reading is that a good abstraction here is judged by what it makes invisible, since anything left visible competes for the same scarce attention as the part you actually need to reason about. Naming operations that carry the bookkeeping is not decoration; it is how the equation gets short enough to be worked with.

There is a real trade being made, and they name it: the notation looks forbidding at first encounter. That cost is paid once, by each reader, on the way in. The benefit is paid every time anyone calculates with the equations, which for a description that is going to be used is many more times than once. The usual instinct inverts this, optimising for the first reading and producing a form that is welcoming and unusable. They also hold the claim honestly, admitting they do not know whether the method stays tractable for a full-sized language — which is the right register for a claim about scaling that has not yet been tested.

The transferable habit is to ask what you intend to do with a description before choosing its form. If the answer is only that people will read it, verbosity is cheap. If the answer is that you or a tool will reason over it — derive, check, transform, prove equivalence — then its size is the property that decides whether that ever happens, and the work of finding combining forms that swallow the incidental is the work of making the reasoning possible at all.

**Source:** [Toward a Mathematical Semantics for Computer Languages](../works/toward-a-mathematical-semantics-for-computer-languages.md) — the remarks following the semantic clause for recursive command declarations in the section on identifiers and environments, which defend the operators on the grounds that they conceal the right material while leaving structure and sequencing visible, argue that condensing clauses improves one's chances of proving a theorem, and concede that the method's practicality for more complex languages remains to be seen.
