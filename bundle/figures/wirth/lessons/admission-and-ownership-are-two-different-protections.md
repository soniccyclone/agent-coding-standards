---
type: lesson
title: "Admission and ownership are two different protections, and only one of them changes the data model"
figure: wirth
works: [project-oberon]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [operating-systems-and-systems-programming, databases-and-data-management]
tags: [lesson]
---
# Admission and ownership are two different protections, and only one of them changes the data model

**Lesson:** "Protect the system" is two requirements wearing one word, and they have very different costs. The first is keeping outsiders out: deciding whether a request comes from anyone entitled to use this facility at all. It is a single predicate over the requester, its answer does not depend on what is being asked for, and it can be added to an existing system without touching any of the data — one check at the entrance, and everything behind the entrance is unchanged. The second is keeping insiders apart: deciding whether this particular requester may touch this particular thing. That one cannot be answered from the requester alone, because it is a question about a relation between requester and object, and if the objects do not record who they belong to, the question has no answer at any price.

Recognising which you are being asked for is therefore the first thing to settle, because it determines whether you are adding a guard or changing a representation. Admission is cheap and can be retrofitted. Ownership is a modelling decision: every protected object must carry, or be reachable from, the identity it is associated with, and the naming scheme must make that association reliable rather than conventional. Systems that decide late that they want the second usually discover that their objects are addressed in a way that has no room for the association, and the retrofit is a migration rather than a feature.

Two consequences are worth keeping in view. Once identities are recorded per object they must be stable and unique in a way that mere admission never demanded, which is what forces a registry of participants into existence and gives the registry an owner, a lifecycle, and a durability requirement of its own — an administrative apparatus that is a cost of the second protection, not of the first. And a system that has admission only should say so, plainly, rather than allowing its users to infer separation from the presence of a login. Users assume that if they had to identify themselves, their things are their own. If that is not true, the assumption is the more dangerous for having been invited.

**Source:** [Project Oberon](../works/project-oberon.md) — section 11.5's distinction between two kinds of protection: that of the server's resources in general, for which some validation of a user's identification might suffice, and that of individual users' resources from being accessed by others, which is said to require the association of personal resources with user names; together with the section's statement that the central server must in any case store data for each registered user and be able to check the admissibility of a request against it, and its opening remark that centralization inevitably calls for an administration whose typical duties are accounting and protection against misuse.
