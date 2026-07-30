---
type: lesson
title: "Split a two-party protocol at the ownership boundary so each side's policy lives in the object it owns"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [expressiveness, parallelizability]
subdomains: [distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---
# Split a two-party protocol at the ownership boundary so each side's policy lives in the object it owns

**Lesson:** Establishing a connection between two parties is naturally modelled as one operation — one initiator, one procedure, one outcome. This implementation instead splits it in two: a calling-side component responsible for the originating end, and a called-side component responsible for the receiving end. The mechanical consequence, stated plainly, is that the choice belonging to the caller is made by an object owned by the caller, and the choice belonging to the recipient is made by an object owned by the recipient. Each party's policy lives on their own side of the line.

What this buys is that the recipient acquires real discretion without the initiator knowing anything about it. The receiving component can refuse the request, accept it, redirect it to a different party entirely, or select among several destinations by conditions the recipient configured — time of day, day of week, working hours — with the rules tested in order and a default if none applies. None of that is visible to or encoded in the calling side, which asks only for a connection to a party and does not learn how the party chose to route it. Had the operation stayed unified, every one of those policies would have had to be either a parameter the caller supplies or a lookup the caller performs, and adding a new kind of recipient policy would mean changing the caller.

The general principle is that a protocol's decomposition should follow the boundary of authority rather than the flow of control. Control flows through the interaction once; authority is a standing fact about who is entitled to decide what, and it is the thing that must be respected on every future extension. When the split matches authority, each side's rules can grow independently and neither side's changes are visible to the other. When it does not — when one participant executes the whole interaction and the other is merely an address — every capability the second party should own arrives as a parameter, a callback, or a configuration lookup performed on their behalf, which is why such systems accumulate options rather than capabilities.

The practical test, for any interaction between parties with distinct interests, is to list the decisions the interaction makes and mark each with the party who ought to own it. If decisions marked with different owners are being made in the same component, that component is the reason the other party's policies keep arriving as feature requests.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 12 section 12.1, which separates Plain Old Telephone Service into a calling-end service and a called-end service specifically so the called party can reject, accept, forward to another user, or route to one of several telephones; notes explicitly that the choice of calling service was made in an object belonging to A while the choice of called service was made in an object owned by B, permitting detailed customization to different users' preferences; and describes the called-end component as initialized with any number of selectors, each pairing a condition on time of day or day of week with an action, tested sequentially with a default telephone if none is satisfied.
