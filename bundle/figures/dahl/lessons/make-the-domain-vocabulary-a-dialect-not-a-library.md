---
type: lesson
title: "Resolve the pull between a general language and a problem-shaped one by making the general language a substrate for dialects"
figure: dahl
works: [simula-67-common-base-language, class-and-subclass-declarations]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Resolve the pull between a general language and a problem-shaped one by making the general language a substrate for dialects

**Lesson:** Two desires pull against each other and both are legitimate. People working in a field want to write in the concepts and words of that field, which argues for many specialized languages. Everyone else wants few languages, because each new one costs compilers, portability, tooling, and training. The resolution proposed here is to stop treating them as a choice: design one general language whose extension mechanism is strong enough that a domain vocabulary built in it is not a set of calls but an environment you write inside. Prefix a program with a class and its concepts become the concepts available in that program. Someone working in the domain need not know the whole base language; someone who does know it can add to the domain vocabulary without touching a compiler.

The proof that the mechanism is strong enough is that the language's own flagship capability is delivered this way. Simulation, the thing the language is named for, is a class written in the language: it defines the time axis, the queue structures, and the notion of an entity whose activity phases are ordered by that axis. Nothing in the base grammar knows about simulation. A user who wants job-shop analysis writes a further class prefixed by the simulation class and hands his colleagues a job-shop dialect, which they enter the same way. Domain vocabulary and language vocabulary end up at the same level, which is the property that matters: there is no ceiling where library-provided concepts start feeling second-class next to built-in ones, and no incentive to petition the language designers for a feature you could have built.

The consequences for how you judge a language are not obvious ones. Feature richness becomes a weak signal, since a built-in feature is evidence the extension mechanism was too weak to express it. A layer that ships with the language becomes interesting mainly as a demonstration that a user could have written the same layer. And stability of the core becomes more valuable than growth of the core, because every dialect built on it inherits its portability and every change to it breaks dialects that were fine.

A programmer working this way asks, before adding the fortieth utility function to a domain module, whether the module should instead define the vocabulary that the domain's programs are written inside, so that the domain's rules are structural rather than remembered. The test to apply: does using this abstraction feel like calling into someone else's code, or like working in a language that happens to know about my problem? The second is achievable far more often than most codebases assume, and it is what makes a domain layer teach a newcomer instead of merely serving one.

**Source:** [SIMULA 67 Common Base Language](../works/simula-67-common-base-language.md) — the introduction's argument for a general language as substrate for application languages, followed by the application-language-capability section, which shows the simulation and job-shop layering and states that a user may restrict himself to the aggregated concepts without knowing the full base language. Also [Class and Subclass Declarations](../works/class-and-subclass-declarations.md), whose prefixed-block extension and closing remarks identify protecting whole families of data, procedures, and subordinate classes as a way of defining dialects aimed at particular problem areas.
