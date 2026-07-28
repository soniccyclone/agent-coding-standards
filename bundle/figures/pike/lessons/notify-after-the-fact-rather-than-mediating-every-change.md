---
type: lesson
title: "Notify after the fact rather than mediating every change"
figure: pike
works: [acme-a-user-interface-for-programmers]
axes: [cognitive-load, parallelizability, expressiveness]
subdomains: [programming-environments-and-object-systems, distributed-systems-and-concurrency]
tags: [lesson]
---
# Notify after the fact rather than mediating every change

There are two ways to wire a component to the thing that changes its data. In the
mediating arrangement, the component is informed of each intended change and is
responsible for carrying it out: it hears that a key was pressed and must decide
what to display. In the notifying arrangement, the change has already been applied,
and the component learns of it afterward and may respond or ignore it. This work
chooses the second, and the reason it gives is structural rather than stylistic:
many independent agents can modify the same text — a keyboard, a pointer, an
external program writing into it — so there is no single stream of intents to
mediate in the first place. Once multiple writers are real, "consult me before
anything changes" stops being implementable.

The notifying arrangement pays off immediately in how little most clients have to
do. A program that composes a message does not track each edit; it lets the edits
happen and reads the final contents when told to send. That is not laziness, it is a
consequence of the notification being about facts rather than requests: a client
with no opinion about intermediate states simply has no code for them. The mediating
design forces every client to have an opinion about every keystroke whether it has
one or not, which is why such clients are large.

The cost is stated plainly in the work and belongs in the lesson: because
characters reach the display before any program has a say, a client cannot suppress
them. Nothing stands between the input and the screen, so hiding typed input is
impossible. That is a real capability lost, and it is the general shape of the
trade — a system built on notification cannot offer veto, and any behavior needing
veto must be rebuilt some other way or abandoned. Choose the side deliberately,
because the choice fixes what every future client can and cannot do, and reversing
it later means rewriting the contract with all of them.

**Source:** [Acme: A User Interface for Programmers](../works/acme-a-user-interface-for-programmers.md) — the section on the event interface for external programs, which notes that changes are communicated after they occur, explains the multiple-writer model motivating it, and names the loss of input suppression as the price.
