---
type: lesson
title: "Size each description to what a reader can hold at once, and exempt the pieces that get reused everywhere"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Size each description to what a reader can hold at once, and exempt the pieces that get reused everywhere

**Lesson:** Decomposition advice usually stops at "make the pieces small," which gives no guidance about when to stop splitting and no defence against the opposite failure of shattering a system into fragments too numerous to relate. A sharper version sets the target from a property of the reader rather than of the system: a description should hold about as many participants as a person can keep in mind simultaneously, roughly seven give or take two. Above that range, look for a sub-phenomenon to factor out. *Below* it, consider merging — a swarm of two-participant descriptions is its own comprehension problem, and the advice cuts in both directions rather than only licensing further division.

The part that makes this more than numerology is the exception. Very small descriptions are exactly right when they are used many times: a two-participant client-and-server arrangement is below the merge threshold and should nonetheless stay separate, because it will be composed into many different larger descriptions and each of those compositions is where its value is realized. So the rule is not really about size at all — it is about how many times a reader will have to load the thing. A piece read once in one context should be sized to fill a mind comfortably; a piece read in twenty contexts should be small enough that recognizing it is instant.

The second trigger for splitting is structural rather than numeric: when the same shape appears repeatedly inside one description, that repetition is the thing to extract, independent of how many participants the description has. And the whole business is explicitly iterative rather than a decision made once — split what grew too big, merge what fragmented too far, and expect to do both more than once, because the right boundaries are discovered rather than designed.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 3's guidelines for finding models, which set 7±2 roles from short-term memory limits, recommend merging models under five roles, name repeated internal patterns as a second factoring trigger, and carve out heavily-reused two-role models such as client-server as the standing exception.
