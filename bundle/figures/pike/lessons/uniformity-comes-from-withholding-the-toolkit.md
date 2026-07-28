---
type: lesson
title: "Uniformity comes from withholding the toolkit, not shipping one"
figure: pike
works: [acme-a-user-interface-for-programmers]
axes: [cognitive-load, primitive-count, expressiveness]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Uniformity comes from withholding the toolkit, not shipping one

The standard way to make many programs behave alike is to give their authors a
library of ready-made interface pieces and hope they use it consistently. They
don't, because the library is optional, extensible, and cheaper to bypass than to
learn. This work does the opposite: the shared component provides one fixed
interaction model and a few conventions, and client programs get no way to invent
their own. Consistency stops being a matter of author discipline and becomes a
structural property, because no program is in a position to be inconsistent.

The economics of this are the interesting part. If the shared component owns the
interaction rather than merely offering it, then all the effort that would have
been spread thinly across every application can be concentrated in one place and
spent lavishly — on placement heuristics rewritten several times until they feel
right, on moving the pointer to where it will next be needed, on inferring what a
single click meant from the text around it. Every client inherits that work for
free. Meanwhile the clients collapse: a terminal-emulator equivalent is a few
hundred lines with no display code in it at all, a mail reader's only difficult
parts are the external mail protocols, and neither contains anything about
keyboards, redrawing, or selection. Work removed from many places and done well
once is the whole trade.

The corresponding constraint has to be accepted honestly. A fixed interface means
some things clients elsewhere take for granted are simply not available, and the
work says so. If the shared component owns the model, a client cannot opt out of
it. That is the cost of the guarantee, and it is only a good trade when the fixed
model is genuinely good enough — which is exactly why the concentrated effort
matters. A programmer who believes this stops treating "we published a component
library" as a consistency strategy, and asks instead which behaviors could be
removed from clients entirely.

**Source:** [Acme: A User Interface for Programmers](../works/acme-a-user-interface-for-programmers.md) — the abstract's contrast between offering libraries of interface elements and providing a fixed interface with conventions, developed through the nuances section on placement and pointing heuristics and the reported sizes of the terminal and mail clients.
