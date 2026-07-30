---
type: lesson
title: "Spend the confidence a better method buys you on making the same systems safer, not on attempting harder ones"
figure: jones
works: [systematic-software-development-using-vdm]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Spend the confidence a better method buys you on making the same systems safer, not on attempting harder ones

**Lesson:** A discipline that genuinely raises your confidence in what you build hands you a surplus, and there are two things to do with it. Point it at the class of problems you were already attempting by looser means, and those systems come out markedly safer. Treat it instead as a licence to attempt systems whose complexity was previously beyond reach, and you end up exactly where you started — the same residual doubt, now attached to something with more capacity to hurt. Nothing in the method decides which happens; that is a choice made by the people using it, usually implicitly, usually without noticing they made it. Anyone advocating a stronger method owes an explicit answer, because the advocacy is what creates the appetite that then gets spent one way or the other.

There is a boundary the surplus never crosses, and honesty about it is part of the same obligation. What someone actually needs is not a formal object, so nothing can be proved about the fit between a description and a need. Precision buys you something real but different: a description sharp enough to be contradicted, which you can then attack the way a scientific claim is attacked, by hunting for the case that refutes it. The proofs you construct against a precise description are on your side of the gap only; the gap itself stays open. The working conclusion is not to give up but to carry a standing assumption on every project that the mismatch is present and has not yet been found.

The same modesty applies one level down. Even a machine-checked argument moves a probability rather than reaching certainty — as is true of anything physical you might build — so the real engineering judgement is comparative: which subsystem is most likely to be the one that fails, and is effort better spent there than on the one you can most easily reason about. That reframing is more useful than it sounds, because the parts amenable to proof and the parts most likely to be wrong are frequently not the same parts, and a discipline that only reports on the former can quietly redirect attention away from the latter. Do not oversell what the method delivers, to others or to yourself; overselling is how a genuine improvement in confidence turns into a net increase in exposure.

**Source:** [Systematic Software Development Using VDM](../works/systematic-software-development-using-vdm.md) — the postscript: the stated personal responsibility not to oversell the ideas, the concession that proving properties of a specification can never establish a match with inherently informal requirements together with the appeal to refutability as what formality on the specification side actually buys, the insistence that nothing can ever provide absolute certainty and that designing a system means comparing probabilities of error across subsystems, and the closing warning that improved methods applied to the problems previously handled by ad hoc means make systems far safer while the same methods used to justify attempting greater complexity leave no progress at all.
