---
type: lesson
title: "Let each authority bind the parameters it alone knows and pass the artifact on still open"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [expressiveness, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Let each authority bind the parameters it alone knows and pass the artifact on still open

**Lesson:** A configuration passes through four parties before it runs, and each one settles exactly the part it is competent to settle. The first defines which configurations are possible at all. The second creates an instance and fixes the commercial terms. The third copies that and fixes what applies to their population. The last copies again and fixes the remaining details, which only they can know — where a call should go today. At every step the artifact is a partially bound thing carried forward, and what makes it work as a carrier is that it remembers the values already set, so no party has to be told what the earlier ones decided.

The reason to name this as a pattern is that it answers a question usually answered badly. Faced with a value that different parties know at different times, the standard options are to hard-code it (wrong for anyone but the author), to expose everything as runtime configuration (correct but hands every decision to whoever is last, who is least equipped for most of them), or to build a separate interface per party (which duplicates the model four times and lets the copies drift). Staged binding along a chain of authority is a fourth answer: one artifact, one vocabulary, and each parameter closed at the first point where somebody actually knows its value.

Two properties do the work. Binding is monotone — a decision, once made, is not revisited downstream, so nobody below has to understand or second-guess the terms set above them, and each party's cognitive load is only the parameters still open when the thing reaches them. And what remains open at each stage is itself a design decision, which is where the real expressiveness lives: choosing what to leave unbound for the next party is choosing how much discretion they have. That choice is normally made accidentally, by whatever happened to be easy to parameterize.

The transferable question, for any setting that varies, is not "should this be configurable" but "who is the first party in the chain who knows this value, and does the artifact reach them still open at that point?" Values bound too early remove authority from the only party with the information. Values left open too long arrive at someone who must guess. Both failures are invisible in a flat configuration file, which flattens a chain of decisions into one undifferentiated surface and thereby loses the record of who was entitled to decide what.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 12 section 12.5, which notes that objects are eminently suitable as information carriers on the upper four layers because they remember specific values set for service parameters, and enumerates the staging: the Service Creator specifies the schema defining all permissible variants, the Service Provider instantiates objects and sets certain parameters, the Subscriber duplicates them and binds further parameters, and the User duplicates them and binds the remaining parameters before installing for execution — with section 12.2 noting that remaining open parameters, such as the number to receive a forwarded call, must be bound before execution.
