---
type: lesson
title: "Responsibility Belongs Where the Information Is"
figure: corbato
works: [introduction-and-overview-of-the-multics-system]
axes: [cognitive-load, verifiability]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture, databases-and-data-management]
tags: [lesson]
---
# Responsibility Belongs Where the Information Is

**Lesson:** The 1965 Multics paper makes the same argument twice about two unrelated duties, and the shared shape of the argument is the lesson. On overlapping computation with input and output, Corbató observes that an individual user cannot do this well for his own program: one program's demands are not balanced against themselves, and the person lacks the live picture of what else is happening. Averaged over many users the same erratic demand becomes smooth and schedulable, and the averaging only has to be written once, in one place. On backup of stored information, he notes something sharper — the more reliable storage becomes, the less any individual can justify the trouble of preparing for the rare catastrophic loss, so leaving the duty with the user guarantees it will not be done.

Both cases resolve to one test. Ask which level of the system holds the information needed to discharge a duty correctly, and which level can spread its cost across enough instances to make it worth paying, and put the duty there. The uncomfortable corollary is about incentives rather than capability: a responsibility assigned to a level where the payoff does not reach will be performed badly regardless of how clearly it is documented or how sincerely it is promised. Corbató's word for what the file system actually provides is insurance, which is exactly right — the value of insurance is that it pools an event too rare for any one participant to rationally prepare for.

Someone reasoning this way stops asking who *ought* to handle a concern and starts asking who can see enough to handle it and who can amortize it. The answers frequently disagree with the organizational chart or the API boundary, and when they do, the boundary is what should move. Note also the direction Corbató does *not* go: he is not centralizing for its own sake, since the same paper delegates resource authority as far down as it can. The rule picks a level, and sometimes that level is low.

**Source:** [Introduction and Overview of the Multics System](../works/introduction-and-overview-of-the-multics-system.md) — the fourth item in the system requirements discussion, on why individual users cannot multiprogram their own work, together with the file system section's justification for providing backup at system level and describing it as insurance.
