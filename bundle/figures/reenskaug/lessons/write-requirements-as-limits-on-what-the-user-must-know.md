---
type: lesson
title: "Write requirements as limits on what the user is permitted to have to know"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Write requirements as limits on what the user is permitted to have to know

**Lesson:** Requirements for a reusable component are conventionally written as capabilities: it shall do this, it shall support that. A specification written that way is satisfiable by something nobody can use, because every capability can be delivered as one more thing the caller must understand and drive correctly. The alternative on display here is to phrase the requirement as a bound on the consumer's knowledge — this mechanism shall not need to be part of their working repertoire; they shall only ever have to think in one frame of reference; this behavior they shall always get and never construct.

Three properties make these better requirements than the capability form. They are falsifiable by observation rather than by argument: hand the component to someone and see what they had to learn, which is a cheaper and less disputable test than assessing whether an interface is elegant. They constrain the implementation in the direction that actually matters, since "the caller must not have to know X" forbids every design that exposes X, including the ones that would otherwise pass review by being technically complete. And they are stable under implementation change, because the internals can be rewritten freely so long as the knowledge bound holds, which is precisely the invariant a consumer depends on and the one that capability lists fail to protect.

The strongest of the three forms is the pairing of "always get it" with "never construct it," which is a decision rule and not just a wish. Take any facility that is intricate to build and is wanted essentially every time: those two properties together say it must be internal and automatic, not offered. Offering it as an option means every consumer pays the cost of the decision and some fraction get the construction wrong, in exchange for a configurability nearly nobody exercises. Conversely, a facility that is intricate but rarely wanted should not be internalized, because it will load every consumer with a model of something they never use. The pair of questions — how hard, how often — sorts a candidate feature into internal, exposed, or omitted, and it produces answers where "should this be configurable" produces debate.

Held as a habit, this reverses the usual direction of specification work. Instead of enumerating what the thing does and hoping usability follows, enumerate what the user is allowed to be ignorant of and let that dictate what the thing must do.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 9 section 9.4's technical requirements for the Tool framework, three of which are phrased as knowledge bounds: that the changed-update intricacies shall not need to be part of the application programmer's active competence, that programmers shall only be required to think in the application's coordinate system because thinking in several simultaneously is hard, and that scrolling shall be internal so programmers can always get it and never need to construct it.
