---
type: work
title: "Distributed Snapshots: Determining Global States of a Distributed System"
figure: lamport
description: Gives the Chandy-Lamport algorithm for capturing a consistent snapshot of an entire distributed system's state — every process's local state plus every in-transit message — while the system keeps running. Does this with lightweight marker messages instead of stopping the world, so the snapshot doesn't distort the computation it's observing. Underpins later checkpointing, recovery, and distributed-debugging protocols that need a consistent global view without pausing everything.
subdomains: [distributed-systems-and-concurrency]
year: 1985
url: https://lamport.azurewebsites.net/pubs/chandy.pdf
access: public
host: self-archived
tags: [work]
---

# Distributed Snapshots: Determining Global States of a Distributed System

**Author(s):** with K. Mani Chandy
**Venue/year:** ACM Transactions on Computer Systems 3(1), February 1985
**Source:** https://lamport.azurewebsites.net/pubs/chandy.pdf — self-archived PDF on Lamport's own site, live and directly downloadable (HTTP 200).

## Lessons
_(empty)_
