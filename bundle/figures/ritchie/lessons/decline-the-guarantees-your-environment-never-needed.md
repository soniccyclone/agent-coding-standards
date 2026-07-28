---
type: lesson
title: "Decline the guarantees your actual environment never asks for, and be explicit about which ones you kept"
figure: ritchie
works: [unix-time-sharing-system]
axes: [verifiability, primitive-count, cognitive-load]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# Decline the guarantees your actual environment never asks for, and be explicit about which ones you kept

**Lesson:** Concurrent write access to shared storage is exactly the situation textbooks answer with locking, and Ritchie and Thompson simply refused. Their system exposes no locks and imposes no limit on simultaneous writers, and the stated reasoning has two halves that are worth separating. Unnecessary: the workloads they actually had were not large shared databases tended by independent processes, so the interference the mechanism prevents was not interference they experienced. Insufficient: even a working reader-writer lock fails to prevent the confusion it was invoked for, because the editor of the day copies the file it edits, so two people can trample each other's work without ever holding the file open at the same moment. A mechanism that neither addresses your observed problem nor solves the problem it claims to is a mechanism you can drop.

What makes this a discipline rather than an excuse is the second half of the same passage: internal interlocks are present and non-negotiable, so the system's own structural consistency survives concurrent writes to a file, concurrent creation in a directory, or one user deleting another's open file. The distinction is between invariants the implementation must preserve because nothing above can repair them, and policies about user-level interference that the environment can be allowed to handle socially. Collapsing those two categories is how systems end up with mechanisms that are simultaneously expensive and inadequate.

The general move is to derive your guarantee set from the failures you can actually observe and from an honest account of what a candidate mechanism would and would not prevent, rather than from the list of features comparable systems advertise. It is also a claim with an expiry date, and Ritchie's phrasing concedes as much by scoping it to "our environment" — the argument was about a particular workload, and a different workload revokes it.

A programmer who believes this treats every proposed safety mechanism to two questions before building it: which observed failure does this remove, and does it actually remove that failure end to end, including the paths the users take rather than the paths the design assumes. When either answer is weak, they leave the mechanism out and write down the workload assumption that justified leaving it out, so the omission can be revisited when the assumption breaks rather than being discovered as a mystery later.

**Source:** [The UNIX Time-Sharing System](../works/unix-time-sharing-system.md) — the passage in the I/O calls section explaining why no user-visible locks exist, immediately followed by its statement that internal interlocks do maintain file-system consistency under concurrent use.
