---
type: lesson
title: "Where a mechanism lends its authority, its inputs become the security perimeter"
figure: ritchie
works: [on-the-security-of-unix]
axes: [verifiability, primitive-count, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Where a mechanism lends its authority, its inputs become the security perimeter

The mechanism Ritchie spends most of the memo circling lets a program run with the privileges of its owner rather than its invoker. The intent is narrow and reasonable: let one program be the sole custodian of data nobody else may touch directly, the score file for a game being the canonical illustration. The consequence is that every argument such a program accepts is now an instruction issued at elevated privilege. His escalation walkthrough — a privileged delivery program willing to append caller-supplied text to a caller-nominated path, aimed via a link at the account database — never breaks any access check. Each check passes. The authority was simply spent on a target the caller chose.

The general shape is that privilege attaches to a *code path*, but the effect is determined by *data*. So the boundary you must reason about is not the module's source but the closure of everything its parameters can name or become. Ritchie makes the same point from three directions: a privileged binary that is itself writable is not a program but a slot anyone can fill; a filesystem a user is allowed to attach is metadata the kernel will read as truth, so an ordinary user who can mount can hand the system ownership records and device entries of his own manufacture; and the all-powerful account, which he calls a blemish on any protection scheme, is the limiting case where lent authority is total and no input can be safely interpreted at all. The kernel's checks are correct in every one of these; the trust was misplaced one level below them.

Why it holds: an access-control decision is only as meaningful as the binding between the name checked and the object eventually acted on. Anything that can be interposed in that binding — a link, a mount, a writable path, a rewritable executable — moves the decision out from under the checker without contradicting it. Correct enforcement of a rule about names says nothing about objects if names are attacker-controlled.

A programmer who believes this stops asking "does this code check permissions" and starts asking "what is the set of objects this code can be aimed at, and who controls the aiming." They keep the privileged surface small enough to enumerate that set by hand, treat any privileged component's input validation as part of the kernel's trust base rather than as application hygiene, and are suspicious of convenience features that widen what a privileged path will accept. Ritchie's own proposed mitigations follow that logic exactly: either withdraw the dangerous capability from unprivileged users, or make the privileged path inspect what it is being handed before it agrees to act.

**Source:** [On the Security of UNIX](../works/on-the-security-of-unix.md) — the sections defining the set-UID/set-GID mechanism and then dismantling it: the writable privileged binary, the mail-to-a-link escalation, the super-user caveat, and the closing discussion of user-performed mounts.
