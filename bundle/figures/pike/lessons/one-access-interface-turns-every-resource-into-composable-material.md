---
type: lesson
title: "One access interface turns every resource into composable material"
figure: pike
works: [the-use-of-name-spaces-in-plan-9]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# One access interface turns every resource into composable material

The usual instinct when a new kind of resource appears — a process table, a
display, a network stack, a backup archive — is to give it its own vocabulary:
a system call, an ioctl, a library, a daemon with a bespoke wire format. Each
one is locally reasonable and collectively catastrophic, because none of them
compose. Ten resources with ten interfaces give you no way to point a tool at a
resource it wasn't written for. This work takes the opposite bet: pick one
interface — a hierarchy of names, plus attach, read, and write — and force every
resource in the system through it, including the ones for which it is a slightly
awkward fit.

The payoff is not tidiness, it is leverage that arrives unplanned. Once
processes are named files, an existing text-search tool becomes a debugger's
instrument and a two-line script becomes a process lister. Once yesterday's
filesystem image is reachable by name, "when did this bug get fixed" is a
question you ask with the tool you already have rather than a feature someone
has to build into a backup product. Once network connections are named and
written to as text, a login service is a handful of shell lines and a protocol
gateway is one command. None of these were designed; they are consequences of
having refused to invent a second vocabulary.

The discipline this demands is real: choosing the uniform interface means
accepting that some resources will be expressed a little clumsily through it,
and resisting the pressure to add a special mechanism each time that clumsiness
shows. The trade is a small, permanent cost per resource against an open-ended
gain in what can be combined with what. A programmer who has internalized this
stops asking "what API does this thing need" and starts asking "what does this
thing look like in the vocabulary the rest of the system already speaks" — and
treats a resource that cannot be expressed there as a design question, not as a
licence to add a primitive.

Also notice the choice of textual, self-describing content over packed binary
records. That is the same instinct applied one level down: representation that
any tool can read and any human can inspect keeps byte order, word size, and
machine architecture from leaking into the interface at all.

**Source:** [The Use of Name Spaces in Plan 9](../works/the-use-of-name-spaces-in-plan-9.md) — the file-protocol argument and the long tour of non-storage "file systems" (process, console, bitmap, network devices, the dated backup roots), where each example exists to show ordinary commands doing work that elsewhere needs a special mechanism.
