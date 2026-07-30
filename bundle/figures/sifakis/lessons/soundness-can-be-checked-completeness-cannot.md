---
type: lesson
title: "Automation covers whether your requirements are consistent, never whether they are all there"
figure: sifakis
works: [turing-lecture-2009]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Automation covers whether your requirements are consistent, never whether they are all there

**Lesson:** A set of stated requirements has two independent quality properties, and tooling is wildly asymmetric across them. That the set is satisfiable at all — that you have not demanded something no system could exhibit — is well understood and can be settled by decision procedures. That the set says everything that matters has no agreed definition, no procedure, and in the exact sense (the specification pins the system down completely) is both uninteresting and unreachable for anything real. So the half of specification quality that can be mechanized is the half that is rarely where projects go wrong, and the half that dominates real failure is left entirely to judgment.

The practical consequence is where to spend review attention. A green check from any verification pipeline is a statement about stated properties only, and carries no information at all about the property nobody wrote down. Elaborate machinery aimed at the formalized requirements can generate confidence that runs well ahead of the evidence, because the machinery is silent on the failure mode that actually bites. Reviewing the requirement list for omissions is unglamorous, unautomatable work that no amount of downstream rigor substitutes for.

The gap widens as you move away from functional behavior. The available formalisms were built to describe what a system computes and in what order, and there is far less to work with for the properties that increasingly decide whether a system is acceptable — confidentiality and privacy, whether an optional feature can interfere with the rest of the system when enabled, tolerances on service quality like timing variance. Any of those left unstated is not conservatively assumed by the checker; it is simply absent from the analysis, and absence looks exactly like success.

**Source:** [Model Checking: Algorithmic Verification and Debugging](../works/turing-lecture-2009.md) — Sifakis's section on requirements specification: soundness as automatable versus the absence of any consensus on completeness, and the observation that existing formalisms address mainly functional requirements.
