---
type: lesson
title: "Take the choice of input away from whoever benefits from choosing it"
figure: rabin
works: [digitalized-signatures-and-public-key-functions-as-intractable-as-factorization]
axes: [verifiability]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Take the choice of input away from whoever benefits from choosing it

**Lesson:** A component that performs a privileged operation on request is exposed in a way that has nothing to do with whether its logic is correct: the requester picks the operand. If some operands leak more than others, or land in a weak corner of the operation's behavior, then the requester's freedom to choose is itself the vulnerability. This work handles that directly. Before the privileged operation is applied to a caller-supplied value, the value is combined with a freshly drawn random component that the caller does not control, and only the combination is operated on. The caller can still get its request served, but it can no longer aim.

The quantitative form is what makes this more than hygiene. With a random component of modest size, the number of distinct values the privileged operation might actually be applied to for a given request is astronomically large, so no requester can steer the operation toward any particular one, and repeated requests for the same nominal item do not repeat the same underlying computation. This has a second effect that shows up in the same design: because not every value is even usable by the operation, the random component doubles as the retry knob — redraw until the operation applies, with a small expected number of draws. One mechanism buys both unpredictability and a way out of the unusable cases.

The habit to carry forward is to look at every interface where an untrusted party's input reaches a sensitive operation and ask what freedom that gives them beyond the intended request. Then remove the freedom rather than trying to enumerate its consequences. Salting, per-request nonces, randomized identifiers, jittered timing, randomized iteration order in anything whose order is not part of the contract — all the same move. Each replaces a claim you cannot verify ("no chosen input causes trouble") with one you can ("the input the sensitive step sees is not chosen by them").

Notice the epistemic modesty in it, too. This work does not claim the direct attack would have worked; it says it does not look like a serious threat, and adds the randomization anyway because the cost is negligible and the argument becomes unnecessary. That is the right calculus for a defense whose price is a few bytes and a redraw: pay it and delete the reasoning obligation, rather than keeping the reasoning obligation alive for everyone who later modifies the code.

**Source:** [Digitalized Signatures and Public-Key Functions as Intractable as Factorization](../works/digitalized-signatures-and-public-key-functions-as-intractable-as-factorization.md) — the signing section, where a randomly chosen suffix is appended before hashing both to make the required congruence solvable after a few attempts and to deny an adversary control over which value the private operation is applied to.
