---
type: figure
title: Richard Rashid
description: b. 1949, CMU. Led the Mach microkernel project - its IPC/VM architecture underlies NeXTSTEP and macOS/iOS's XNU kernel.
status: accepted
layer: implementation-mapping
subdomains: [operating-systems-and-systems-programming]
tags: [figure, accepted]
---

# Richard Rashid

**Dates:** b. 1949. American computer scientist, Carnegie Mellon University; later founded Microsoft Research.

## Why a candidate
Led design and implementation of Mach, whose IPC/virtual-memory architecture underlies NeXTSTEP and macOS/iOS's XNU kernel and shaped the microkernel research line running through L4/seL4.

## Top 10 most influential works
1. "Mach: A New Kernel Foundation for UNIX Development" (1986, with Accetta et al.) — `public` (widely mirrored in course archives)
2. "Accent: A Communication Oriented Network Operating System Kernel" (1981, with Robertson, Mach's direct predecessor) — `uncertain`

Bibliography beyond the Mach team papers is thin — not padded further.

## Lessons

Across three generations of the same kernel lineage, Rashid teaches a single
discipline applied relentlessly: decide what the smallest set of things a
system must name is, make every capability an instance of naming one of them,
and then treat everything else — where the named thing lives, who currently
implements it, whether it is privileged, whether it is on this machine — as
information the caller is structurally unable to depend on. The twelve lessons
here divide into three moves. The first is representational: a reference should
be opaque, unforgeable, and denote a role rather than an implementor, because
that one choice simultaneously buys protection, failure notification,
relocation, interposition, and a communication graph the system itself can see
— and its absence produces a defect list that looks like four independent
problems. The second is about where decisions live: a privileged or foundational
core should hold mechanism only, so that the identity of the system moves into
replaceable components, and a machine-facing layer should own no authoritative
state so it can be discarded and rebuilt per architecture. The third is the
part most designers skip: the honest accounting of cost. Rashid's argument for
strong semantics — a transfer really means a private copy — rests on making it
cheap through address-translation tricks rather than on hoping nobody notices;
his answer to "message passing is slow" is to decompose the claim into what the
abstraction costs versus what the hardware was never tuned to support; and his
successor systems are smaller than their predecessors in specific places
because three years of measurement said which mechanisms nobody used. Running
underneath all of it is a view of durability that has little to do with
elegance: primitives survive when they correspond one-to-one with the physical
structures machines are built from, and a design survives only if it can host
the software that already exists.
