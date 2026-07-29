---
type: lesson
title: "Put the variety in the joints between programs, not inside them"
figure: thompson
works: [the-unix-time-sharing-system]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Put the variety in the joints between programs, not inside them

**Lesson:** There are two places the variety a user wants can live: inside each program as a growing set of options, or outside all of them in the way their inputs and outputs are wired together. The first place is the obvious one and it is a trap, because the number of option combinations grows multiplicatively with the number of programs while nobody is willing to implement more than a handful per program. The second place is cheap, because if every program agrees to take a stream in and put a stream out, and something else decides where those streams come from and go, then n programs give you n-squared behaviors for free and none of them had to be anticipated.

What makes this work is that the agreement has to be almost content-free. The programs share a convention about a couple of already-open channels and nothing else; a program cannot tell whether the thing on the other end is a terminal, a stored file, or another program running concurrently, and it is specifically not allowed to care. The redirection notation never reaches the program at all — it is consumed by the thing doing the wiring. That asymmetry is the whole design: the composing layer knows about plumbing, the composed programs know about their own job, and neither leaks into the other. A separate but load-bearing choice is that the composing layer is itself an ordinary program rather than part of the privileged core, so making it more powerful costs nothing structurally and invites experimentation with alternative wirings.

A programmer who believes this stops treating feature requests as requests for features. When someone asks a tool to also paginate, or also sort, or also write somewhere else, the response is to check whether the tool's output can be handed to something that already does that, and if the handoff is awkward, to fix the handoff rather than absorb the feature. It changes what counts as a design win: not a rich program, but a boring program with an interface so plain that other people can build things with it that its author never considered. It also predicts where a system will rot — every option flag that exists only because two programs could not be connected is a piece of evidence that the connective tissue is too weak.

**Source:** [The UNIX Time-Sharing System](../works/the-unix-time-sharing-system.md) — the argument in the shell sections about standard I/O, redirection, and filters, which explicitly contrasts composing small programs against the alternative of building pagination and spooling options into a directory-listing command, and the closing retrospective on why those facilities were trivial to implement.
