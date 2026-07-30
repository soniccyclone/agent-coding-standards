---
type: lesson
title: "There is no best reuse mechanism — match it to the layer, and expect the crude one to win somewhere"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [expressiveness, primitive-count]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# There is no best reuse mechanism — match it to the layer, and expect the crude one to win somewhere

**Lesson:** Discussions of code reuse normally proceed as if the mechanisms were competitors and one of them were correct — inheritance against composition, frameworks against generators, libraries against templates. Having mapped an industry's software production onto six populations with different competences and different jobs, this team then selected a reuse technique for each population separately, and reported the outcome as a pleasant surprise: every technique they had catalogued turned out to be the right answer somewhere. That result reframes the whole argument. The mechanisms are not rivals but a menu indexed by who is doing the reusing, and a fight over which is best is a symptom of having only one population in view.

Two things make the selection criterion concrete rather than a shrug. The relevant variable is the consumer's competence and interest, not the elegance of the mechanism, so the technique appropriate for people building substrate components is not the one appropriate for a consultant configuring a system for a specific customer, even when both are formally "reuse." And the author attaches a warning to the selection step: be open-minded, because plain duplication of a working master object may be more appropriate than sophisticated machinery like automatic program generators. That is not a concession to the unskilled. Duplication is inspectable, has no build-time indirection, fails locally, and requires nothing of its user beyond reading what they copied — properties that a generator trades away for leverage that only pays off at volume, in the hands of someone who will maintain the generator.

The reason to keep this as a reflex is that the pressure runs the other way. Sophisticated reuse machinery is what an engineer wants to build and what looks like progress in a review, so the crude option loses on the criteria people actually apply. Making the choice explicitly per population, and asking what the population's competence supports rather than what the mechanism can do, is what keeps a technique from being adopted at the layer where its cost lands on someone who did not choose it.

The wider form applies to any decision about a mechanism serving several distinct audiences: stop looking for the single right answer, enumerate the audiences, and let the answer differ. And treat a mechanism that turns out to be right for every audience with suspicion, because that is more often evidence that the audiences have not been distinguished than evidence of a universal solution.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 10 sections 10.1 and 10.2: the Intelligent Network study identified six actors with very different competence and outlook, selected appropriate technologies for each layer, and found "every one of the reuse technologies described in chapters 5 and 11 was applicable on at least one layer"; and the instruction, when selecting technology per layer, to be open-minded because a simple duplication of master objects may be more appropriate than sophisticated technology such as automatic program generators.
