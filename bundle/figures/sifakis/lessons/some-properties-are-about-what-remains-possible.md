---
type: lesson
title: "The claim you most need about a running system is that a way forward still exists"
figure: sifakis
works: [cesar-1982]
axes: [expressiveness, verifiability]
subdomains: [formal-methods-and-verification, distributed-systems-and-concurrency]
tags: [lesson]
---
# The claim you most need about a running system is that a way forward still exists

**Lesson:** Say what freedom from deadlock actually asserts: from every state the system can reach, there is at least one continuation along which some action of interest becomes available again. That is a statement about the existence of a future, not about all futures, and no amount of reasoning restricted to "along every execution, this holds" will produce it. A vocabulary that can only quantify universally over runs pushes you into stating something adjacent that you can say, and the substitution is easy to miss because the adjacent claim also sounds like liveness. Being able to say "possibly" as well as "necessarily" is not decoration; it is the difference between expressing the property and approximating it.

Once both are available, response properties come in two strengths and the gap between them is the real content. After some action occurs, it may be that a matching action merely becomes reachable — the channel is not permanently closed — or that it becomes unavoidable — every continuation gets there. The first is a claim that the system has not painted itself into a corner; the second is a commitment about progress. Real specifications need both, applied to different pairs of actions, and conflating them either overstates what the design guarantees or demands more than the design was ever meant to provide.

There is a companion habit here: state each property at the weakest strength that would still catch the failure you fear, and only strengthen with a reason. The weak forms are cheaper to establish, they fail loudly on gross defects, and having the whole family written down lets you see what each stronger claim is actually buying over its predecessor. A specification that is a flat list of maximally strong assertions hides that structure and is harder both to check and to read.

**Source:** [Specification and Verification of Concurrent Systems in CESAR](../works/cesar-1982.md) — the branching-time operators for potential and inevitable reachability in section 3.1, and the graded families of liveness and response properties, from absence of deadlock through liveness of a single action to inevitable response, in section 3.2.
