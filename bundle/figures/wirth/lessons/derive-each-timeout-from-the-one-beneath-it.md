---
type: lesson
title: "Derive each timeout from the one beneath it, and stay until the other side can no longer ask"
figure: wirth
works: [project-oberon]
axes: [verifiability, parallelizability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
tags: [lesson]
---
# Derive each timeout from the one beneath it, and stay until the other side can no longer ask

**Lesson:** A system with more than one waiting point acquires more than one deadline, and the usual practice is to pick each of them separately by feel. That is how you get a design whose durations contradict each other: an outer wait that expires while the inner one is still legitimately retrying, so a healthy exchange is abandoned as failed; or an outer wait so much longer than necessary that a genuinely dead counterpart holds a resource for minutes. Neither symptom points at its cause, because each individual number looks defensible. The error is not in any of the values but in the fact that they were chosen independently when they are not independent quantities.

The relation between them is arithmetic and worth writing down explicitly. The innermost deadline is the only one anchored in physical reality: it should be some comfortable multiple of the time the underlying operation actually takes, and that measurement is the one empirical input the whole scheme needs. Every deadline above it is then a consequence — a wait that encloses a bounded number of retries at the level below must be at least that count times the lower deadline, or it is asserting that the retry policy it contains is not permitted to run. Expressing the outer values as products rather than as literals makes the dependency visible, and means that recalibrating the one measured quantity corrects the whole hierarchy instead of leaving a set of numbers that were consistent once.

The same arithmetic governs the end of an exchange, which is where it is most often forgotten. When one party decides it is finished, the other may still be inside its retry window, and a request sent into a conversation that has already been dismantled produces either a lost operation or — worse — a stray message that arrives during someone else's exchange. So finishing has a duration too: the departing party must remain able to respond until the counterpart's last possible retry has expired, which is again a quantity derived from the deadlines below rather than a fresh guess. Treat teardown as a phase with its own timing obligation rather than as the absence of activity, and a whole family of intermittent failures that appear only under retry simply never arises.

**Source:** [Project Oberon](../works/project-oberon.md) — section 10.4's account of the two timeout constants in the network module: the limit for receiving the next data packet, stated to correspond to about a second against a maximum-length packet transmission time of about sixteen milliseconds, and the limit for receiving the next request, described as roughly the former multiplied by the maximum number of possible retransmissions; together with the accompanying statement that, before disengaging itself from a transaction, the sender of data waits until no further retransmission requests can be expected to arrive.
