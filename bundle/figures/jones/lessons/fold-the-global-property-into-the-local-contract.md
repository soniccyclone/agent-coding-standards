---
type: lesson
title: "Fold the awkward global property into what 'meets its description' locally means, and composition stops charging you for it"
figure: jones
works: [software-development-a-rigorous-approach]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Fold the awkward global property into what 'meets its description' locally means, and composition stops charging you for it

**Lesson:** Some properties of a system are naturally whole-system properties — it finishes, it never deadlocks, it never leaks a handle — and the instinct is to argue about them at the top, over the assembled thing. That is the expensive place to argue. A whole-system argument has to look at everything at once, has to be redone whenever anything is rearranged, and is exactly the argument nobody gets around to. The alternative is to push the property down into the definition of what it means for a *part* to satisfy its description, and then check that the ways you glue parts together preserve it. When that works, the global property stops being a separate thing you prove and becomes a thing you cannot lose.

Termination is the clean case. Define "this piece meets its description" to mean it delivers the promised outcome *and finishes*, whenever it is used within the assumptions it stated. Now consider putting two such pieces one after the other. Each one finishes; therefore the pair finishes; there is nothing to prove. Same for a branch: whichever arm runs, it finishes. Same for calling out to a component you did not write, provided its description carries the same meaning. Across the entire vocabulary of ways to combine things, exactly one construct can actually fail to finish, and it is the one that repeats. So an obligation that would otherwise hang over every line of the system has been localized to a single construct, and everywhere else the corresponding check is not merely easy — it does not exist.

Contrast the arrangement where the local notion of correctness is weaker: *if* it finishes, it delivers the right answer. Now every part is silent about finishing, no composition rule can give you what the parts never had, and termination has to come back as a separate pass over the whole program. Two passes, two chances to skip one, and the second pass has to reconstruct structure the first pass already knew. The weaker local contract did not save work; it deferred it and made it worse.

The generalizable move is to notice that you get to choose how strong "done" is, and to choose it by looking at what the composition rules would then owe you. A slightly stronger obligation on each part, if it is the kind of obligation that composition preserves, converts a global proof into no proof at all. This is the same reason a stated restriction on inputs pays for itself: it is a local, checkable thing that makes a family of global questions go away. Look for properties with this shape — preserved by sequencing, preserved by choice, threatened only by repetition or by sharing — and pay for them once, locally, rather than repeatedly and at the top.

**Source:** [Software Development: A Rigorous Approach](../works/software-development-a-rigorous-approach.md) — chapter 5, the "Sequential Statements" section: the reading given to a three-part specification, that for every state satisfying the stated assumption the operation both terminates and produces a state satisfying the required relation; and the remark following the three rules for sequential composition that although termination is handled at every development step, the sequencing rule itself carries no termination obligation, because each sub-operation is guaranteed to terminate on states meeting its assumption and therefore so must their composition.
