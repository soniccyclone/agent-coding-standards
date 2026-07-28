---
type: lesson
title: "Independence of failure is something you build, not a number you pick"
figure: liskov
works: [practical-byzantine-fault-tolerance]
axes: [verifiability, hardware-affinity, cognitive-load]
subdomains: [distributed-systems-and-concurrency, software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Independence of failure is something you build, not a number you pick

**Lesson:** Every replication argument has the same shape: so long as no more than some fraction of the participants are broken at once, the healthy majority outvotes the broken minority. The fraction is arithmetic and easy to reason about. The premise underneath it — that the participants break independently — is an empirical claim about the deployment, and it is the part that quietly fails. Copies running the same build, on the same operating system, administered by the same person with the same credentials, are one participant wearing several costumes. The arithmetic still holds; it just no longer describes anything.

So independence is a property to engineer deliberately, along each axis that could correlate: different implementations of the service, different underlying systems, separate administrative control and separate credentials. That is expensive and awkward and is exactly why it gets skipped, and skipping it converts a carefully proved tolerance threshold into decoration. The point generalizes past replication — any argument of the form "all of these would have to fail together" is only as good as the work done to make together unlikely.

The payoff for taking it seriously is larger than it first looks, because a fault model general enough to cover arbitrary misbehavior does not care whether the misbehavior is hostile. A participant corrupted by an attacker and one that hit a bug in its own code look the same from outside: both produce output that is simply wrong in an unconstrained way. So genuinely independent copies mask defects, not just intrusions — particularly the intermittent kind that depend on timing or ordering and therefore do not reproduce across differently built copies. A defect present in every copy is untouched by any amount of replication, which is precisely why the diversity is the mechanism rather than the count.

A programmer who believes this reads a stated tolerance as a conditional promise and immediately asks what makes the condition true here. Before adding copies, they look for the shared thing every copy depends on — one image, one deploy pipeline, one credential, one clock source — because that shared thing, not the arithmetic, sets the real bound. When diversity is genuinely unaffordable they say so and stop claiming the tolerance, rather than quietly inheriting a proof whose premise does not hold.

**Source:** [Practical Byzantine Fault Tolerance](../works/practical-byzantine-fault-tolerance.md) — the system-model section's discussion of steps required to make independent node failure a realistic assumption, together with the conclusion's observation that the same technique masks nondeterministic software defects but not defects shared by all copies.
