---
type: lesson
title: "A construct that silently bundles two decisions makes every case that wants them apart into a fight"
figure: ungar
works: [organizing-programs-without-classes]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# A construct that silently bundles two decisions makes every case that wants them apart into a fight

Some abstractions are hard to use not because they lack power but because they decide two things at once and only let you speak about one of them. A single construct that records both "what state does this thing carry" and "what behavior do things like this share" reads as an economy — one declaration, both jobs done — right up until you meet a case where the two answers should differ. Then there is no way to say so, because the notation never gave the two decisions separate names. You get a hierarchy where the specialized case must carry the general case's storage whether it wants it or not, and a family of workarounds — an extra empty layer inserted purely to have somewhere to put behavior without storage, accessor wrappers written to reach state the layering has now hidden, guidance that only the leaves of a hierarchy may be concrete.

Look closely at those workarounds. Each one is a hand-built approximation of the separation the construct refused to make. That is the diagnostic: when the recommended style for using an abstraction consists of instructions for neutralizing half of what it does, the abstraction has fused something. The repair is to split the roles into distinct entities and let a user reference each independently. Then "share the behavior and also the storage" and "share the behavior but not the storage" are both ordinary things to write, differing only in whether one reference is present, and neither needs a rule about where in the hierarchy it is allowed to appear.

The split has a second payoff that is easy to miss: it lets the notation express distinctions it previously could not even state. Once behavior-sharing and representation are separate objects, a purely abstract thing is simply the first without the second, and a thing with exactly one instance is the two collapsed into one object. Those aren't new features; they are configurations that become sayable as soon as the fusion is undone. The same is true of the classic multiple-inheritance ambiguity about whether two same-named fields merge or stay distinct — a question that only needs a language rule because the representation was being computed implicitly rather than written down.

For a working programmer this generalizes past language design to every schema, interface, and framework abstraction. When users keep hitting the same wall, do not ask what feature is missing. Ask which two independent decisions your construct is answering with one word, and give each its own word. The result usually has fewer rules than the version with an escape hatch bolted on, because the escape hatch existed to undo the coupling you just removed.

**Source:** [Organizing Programs Without Classes](../works/organizing-programs-without-classes.md) — the sequence of sections on representation sharing and representation modification, especially the worked contrast between a subtype that should extend its parent's representation and one that should replace it, and the awkward layering that a representation-fused construct forces on the latter.
