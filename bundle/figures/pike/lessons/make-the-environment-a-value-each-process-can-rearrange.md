---
type: lesson
title: "Make the environment a value each process can rearrange"
figure: pike
works: [the-use-of-name-spaces-in-plan-9]
axes: [expressiveness, cognitive-load, verifiability]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# Make the environment a value each process can rearrange

Most systems treat the mapping from names to things as global truth: one file
tree, one set of library locations, one meaning for a given path. Because that
global map cannot be varied, every situation needing a *different* map gets its
own patch — a search-path variable, an override flag, a preload hook, a
container image, kernel code that quietly reinterprets one magic path per
process. This work's move is to relocate that mapping into the process itself
and give it operations. The map becomes a mutable, inheritable, per-process
value; a child can share its parent's map or take a private copy and edit it.

What this buys is that a whole class of problems collapses into one mechanism.
Running the right binaries on a heterogeneous fleet stops being a path-search
convention and becomes a binding. Testing whether last week's library caused
today's bug stops being a build-system exercise and becomes a binding.
Sandboxing, remote device access, protocol gatewaying, and interposing a
measurement layer between a program and everything it touches are all the same
operation applied at different points. A window system can hand each client its
own meaning for the console rather than requiring the kernel to special-case one
name — the general mechanism does what a pile of special cases did before, and
does it in cases nobody anticipated.

The subtle part is that local maps do not abolish convention, they depend on it.
Programs remain writable only because everyone agrees roughly what lives where;
what varies is which concrete thing that agreed name resolves to. That is the
actual design shape worth stealing: keep the *names* conventional and stable so
code can be written against them, and make the *bindings* late, private, and
first-class so the same code can be aimed at different realities. A programmer
who works this way stops adding a configuration knob per situation and starts
asking which layer of indirection already exists and could simply be rebound.

**Source:** [The Use of Name Spaces in Plan 9](../works/the-use-of-name-spaces-in-plan-9.md) — the mount/bind/rfork discussion and its follow-on examples, particularly the argument against a global name space and the pointed comparison of architecture bindings against a search-path variable, and of per-client console files against kernel special-casing.
