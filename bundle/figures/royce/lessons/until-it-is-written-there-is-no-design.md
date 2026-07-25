---
type: lesson
title: "Until the design is externalized, there is no design"
figure: royce
works: [managing-the-development-of-large-software-systems]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Until the design is externalized, there is no design

**Lesson:** The easiest way to misread Royce's documentation argument is as ordinary advocacy for writing things down. His actual claim is stronger and more interesting: in the period before code exists, the documentation, the specification and the design are not three things related to each other, they are one object under three names. There is nowhere else the design lives. Bad writing therefore means a bad design rather than a well-understood design poorly described, and absent writing means no design at all, only people thinking and talking about one, which he allows has some value but not much. Writing is the medium the design is made of, not a record kept alongside it.

Two consequences he draws are sharper than the usual case for documentation. First, an unequivocal written position can be checked and a verbal one cannot, which is why written work destroys the perpetual "ninety percent finished" report: a document either states the interface or it does not, and its state is inspectable by someone other than its author. Externalization is what makes progress a fact instead of a claim. Second, the ability to hand work to somebody who did not build it is a property of the artifact, not of the staffing plan. He applies this ruthlessly. If the argument against having specialists test a module is that only its author understands it, that argument is evidence the module was never properly externalized. If a system can only be operated by the people who built it, operations are worse and the software gets blamed first with nothing available to answer the accusation. If the design cannot be found, then even a modest later change means discarding the whole existing framework rather than modifying it.

What holds the whole chain together is transferability. A design that exists only as accumulated context in one person's head cannot be reviewed, cannot be tested independently, cannot be operated by anyone else, and cannot be modified after the person leaves. Each of those is a downstream cost, and all four have the same upstream cause.

A programmer who believes this measures a design by what a competent stranger can do with its written form alone, and reads "only one person understands that part" as a defect report about the code rather than a fact about the person. The disproportion Royce notes between hardware and software specification volume is the same observation from another angle: a software design has vastly more decisions in it that exist nowhere physically, so vastly more of it has to be deliberately externalized or it is simply lost.

**Source:** [Managing the Development of Large Software Systems](../works/managing-the-development-of-large-software-systems.md) — the "document the design" corrective, in particular the identification of documentation with specification and design during early development, and the three downstream situations (testing, operations, later modification) used to argue the value.
