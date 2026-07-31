---
type: lesson
title: "Recursion forces you to write the contract before you can check the body"
figure: reynolds
works: [the-craft-of-programming]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Recursion forces you to write the contract before you can check the body

**Lesson:** For a component that calls nothing of its own, you can work bottom-up: examine the body, find out what it happens to guarantee, and let the interface be a summary written afterwards. The contract is discovered. That order is available to you only because nothing inside the body depends on the contract. Introduce a call from the body back to itself and the order collapses — you cannot get through the body without a statement about what its own calls achieve, and that statement is the contract you were hoping to derive. Discovery is no longer possible; the contract has to exist before the check begins.

This is not a quirk of one proof system, it is what self-reference costs, and the constructive reading is that self-referential code has to be *declared*. The statement of what a call accomplishes, the conditions the caller must establish, the quantity that shrinks — these must be written down at the declaration as a hypothesis you are permitted to use inside, and the body's job is then to justify that hypothesis under the assumption that its own inner calls already satisfy it. A declaration carrying enough of this is not documentation; it is the input to the check. A recursive procedure whose interface is undocumented cannot be checked by anyone, including its author, without first reconstructing the missing statement by guesswork.

The transferable habit is to notice which of your components sit on a cycle — direct self-calls, mutual recursion, callbacks that route back in, a service that reenters itself through a queue — and to treat those specifically as requiring a written contract, while accepting that a leaf component's contract can be summarized after the fact. This is also a reason to prefer breaking cycles where you can: each cycle converts an obligation you could have discovered into one you must invent up front, and inventing it is the hard part. And when the cycle spans several components rather than one, the same argument still works in principle but the bookkeeping grows fast enough to be worth avoiding rather than solving.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — the strengthening described in Section 3.3.8 whereby the procedure assumptions must be added to the premiss about the body so that the same assumptions can be made about calls from within the body as from elsewhere in its scope; and Section 3.3.9's second example, which states that with a recursive procedure one cannot first prove a specification of the body and then match it to determine the assumptions, since the assumptions are needed while proving the body, and observes that an adequately commented procedure declaration contains enough information to determine the replacements, alongside the summary that the basic method of reasoning about recursion is to assume, while showing the body correct, that recursive calls behave correctly; together with the remark that extending the rule to groups of mutually recursive procedures is conceptually straightforward but yields a rule too complicated to formulate.
