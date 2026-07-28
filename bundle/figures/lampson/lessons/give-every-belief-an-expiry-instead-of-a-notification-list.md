---
type: lesson
title: "Withdrawing a fact by notifying everyone who holds it is a distributed problem you cannot win; give the fact an expiry and make withdrawal a refusal to renew"
figure: lampson
works: [authentication-in-distributed-systems-theory-and-practice]
axes: [verifiability, parallelizability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
tags: [lesson]
---
# Withdrawing a fact by notifying everyone who holds it is a distributed problem you cannot win; give the fact an expiry and make withdrawal a refusal to renew

**Lesson:** Any system that lets derived conclusions be copied around eventually faces the question of how to take one back. The obvious design is bookkeeping: remember every place a conclusion was sent, and when it stops holding, tell them all. This looks correct and is quietly unimplementable at scale. It taxes the cheap operation (recording a copy) to make the rare one possible, the list of holders is itself state that can be lost, and the whole scheme depends on being able to reach every holder at exactly the moment you have the least reason to expect cooperation. Worse, it inverts the direction of the dependency: the authority now needs the recipients to be available, instead of the recipients needing the authority.

The inversion to make is to attach a bounded lifetime to the conclusion itself and require holders to come back and re-derive it. Withdrawal then costs nothing and requires no communication with anybody — you simply decline to reissue. What was a correctness problem with an unbounded failure mode becomes a single tunable number trading refresh traffic against how stale a withdrawn conclusion may remain. It also makes every holder's copy a pure cache in the strong sense: droppable at any instant with no consequence beyond a later re-derivation, which means no deadlock from cache exhaustion, no pinned memory, no invalidation protocol, no orphan entries after a crash.

The cost is that renewal makes the authority a liveness dependency, and there is a real tension between an authority that is highly secure and one that is highly available — the properties pull in opposite directions, since the way to make something hard to subvert is to keep it offline and rarely touched. The resolution generalizes well beyond security: split the authority into a durable, seldom-consulted issuer with long-lived statements and a cheap, always-reachable co-signer with short-lived ones, and require both before a conclusion counts. Now the slow, well-protected half decides *what* may ever be true, and the fast, exposed half decides *whether it still is*. Compromising the exposed half delays withdrawal but cannot manufacture authority. A designer who has absorbed this stops asking "how do I invalidate" and starts asking "what is the shortest lifetime I can afford, and which half of the authority is allowed to be online" — and, having done so, gets to treat every derived fact in the system as freely discardable.

**Source:** [Authentication in Distributed Systems: Theory and Practice](../works/authentication-in-distributed-systems-theory-and-practice.md) — the caching discussion in the concepts section, where notification-based invalidation is rejected in favor of limited lifetimes, and the joint-authority construction later used to pair a long-lived offline issuer with a short-lived online countersigner.
