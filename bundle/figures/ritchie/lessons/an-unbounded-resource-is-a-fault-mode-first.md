---
type: lesson
title: "An unbounded resource is a fault mode before it is an attack, so audit for missing limits rather than for attackers"
figure: ritchie
works: [on-the-security-of-unix]
axes: [verifiability, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# An unbounded resource is a fault mode before it is an attack, so audit for missing limits rather than for attackers

Ritchie's account of where Unix was weakest does not begin with adversaries. It begins with the observation that nothing in the system counted anything: no ceiling on blocks consumed, on directory entries created, on live process slots. From that single structural absence he derives both a four-line shell loop that halts the machine and the ordinary case of a buggy program that halts it by accident. The two are the same defect encountered by different people with different intentions. Malice only shortens the time to discovery.

This reframes how to look for this class of problem. Hunting for attacks means enumerating clever sequences, which is unbounded work and depends on how inventive you happen to feel. Hunting for unmetered resources is a finite audit: list every pool the system hands out, ask what happens when the last unit is taken, and note which pools have no accounting at all. The answer for a pool with no limit is always the same, so the question is worth asking mechanically. Ritchie's process-table example also shows why the audit has to include *release* paths, not just acquisition — the slot stayed occupied until someone waited on it, so a resource that was returned promptly in intent leaked in practice because reclamation depended on a caller doing something optional.

The honest second half is that he does not claim a fix. He says the system is essentially defenseless here, that no easy repair exists, and that what actually kept the group safe was a comfortable resource margin plus users who were not trying to hurt anyone. That is worth imitating: separating "this defect is closed" from "our operating conditions have kept this defect from mattering" prevents the second from being mistaken for the first. Conditions change; the code does not notice.

A programmer who holds this view treats every allocation without a quota as an outage waiting for a trigger, whether or not a threat model mentions it. They also make detection and attribution a design requirement when prevention is genuinely out of reach — Ritchie's consolation was that when disaster struck it was easy to see what had happened and who had done it, which is the fallback posture when a limit cannot be retrofitted.

**Source:** [On the Security of UNIX](../works/on-the-security-of-unix.md) — the memo's opening section on crashing and crippling the system, where disk, inode, process-table and swap exhaustion are treated as one structural gap rather than as separate exploits.
