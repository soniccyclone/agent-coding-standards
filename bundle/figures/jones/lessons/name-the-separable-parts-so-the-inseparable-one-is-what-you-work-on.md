---
type: lesson
title: "Name the separable parts explicitly, so that what remains is the coupling you actually have to solve"
figure: jones
works: [software-development-a-rigorous-approach]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, algorithms-and-complexity]
tags: [lesson]
---
# Name the separable parts explicitly, so that what remains is the coupling you actually have to solve

**Lesson:** Any design problem of real size arrives as a tangle, and the productive first move is not to start solving it but to sort its parts into two piles. Some sub-problems are separable: they have a statable interface, they can be handed to someone else or postponed to a later step, and nothing about how they are solved changes anything above them. Others are not separable, and they are not separable for a specific reason — two requirements are pulling on the same structure at once, and no amount of decomposition makes that go away.

The discipline is to do the sorting out loud. Say, for each part you are setting aside, that it is being set aside and what its interface is. This looks like bookkeeping and is not, for two reasons. It stops a reader from mistaking omission for oversight — a design that simply does not mention how items are located in an ordered collection is indistinguishable from one whose author forgot, unless the author says which. And it prevents the far more common failure of solving the easy separable parts first because they are tractable, running out of budget, and discovering the genuine conflict last, when everything has been built around one arbitrary resolution of it.

What is left after the sorting is the actual content of the design step, and it is usually small and specific. Information must be reachable by two different keys, and one arrangement can only serve one of them; that is a real conflict between two requirements over one structure, and it is resolved by a real decision — keep a second arrangement that indexes into the first, and pay for it in update cost and space. Notice the shape: the inseparable part is where you spend a resource to buy back a property you could not have for free, and it is the only place in the design where that kind of trade is being made. Everything else was delegation.

The habit generalizes past data structures. In front of any hard design question, ask what the irreducible conflict is, and check that you can state it as two things wanting the same resource. If you cannot state it, you have probably not found it yet, and you are about to spend your effort on the parts that were never going to be the problem.

**Source:** [Software Development: A Rigorous Approach](../works/software-development-a-rigorous-approach.md) — chapter 14's inverted-file development of the telephone directory problem: the survey of arrangements for locating information by key and the explicit statement that the actual method of locating items in an ordered list is not covered, that this is not an oversight but an important part of the general method being proposed, namely that separable problems should be separated and this one is certainly separable; the immediately following identification of what cannot be separated, that two different keys are required for locating information and a list cannot be kept in two orders at once; and the resolution by a secondary index, a second ordered list whose items locate entries in the first, with the accompanying note that where the secondary key is used infrequently the auxiliary structures may sacrifice speed to economize on storage.
