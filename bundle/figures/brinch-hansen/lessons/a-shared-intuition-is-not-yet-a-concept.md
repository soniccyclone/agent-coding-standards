---
type: lesson
title: "A shared intuition is not yet a concept; force it into a definition and then allow yourself no other tool"
figure: brinch-hansen
works: [monitors-and-concurrent-pascal-a-personal-history]
axes: [expressiveness, primitive-count]
subdomains: [programming-languages-and-semantics, distributed-systems-and-concurrency]
tags: [lesson]
---
# A shared intuition is not yet a concept; force it into a definition and then allow yourself no other tool

**Lesson:** There is a moment in the life of an idea when several capable people can describe it to each other, agree that they mean the same thing, and feel that the work is done. It is not. The account of how monitors came to exist is largely an account of the distance between that moment and a usable concept: three researchers had a common verbal picture, and what remained undone was the scheduling mechanism, the notation, and an implementation. Each of those turned out to be hard, and the first serious attempts at notation were abandoned because they made process identity into something programs could hold and pass, which reintroduced exactly the class of error the idea was supposed to remove. The distance between an intuition and a definition is not a writing-up exercise. It is where you find out whether the intuition was right.

Two habits follow. The first is that the way to close the distance is to define the thing precisely, with its restrictions stated, in a form something mechanical must accept — which is why embedding an idea in a language beats promoting it as a style. A style is never pinned down, so its rules get bent silently, mixed with other half-stated ideas, and never tested against a boundary. Precision is a constraint you impose on yourself to make disagreement possible. The second habit is stranger and more valuable: once the concept is defined, deliberately allow yourself no alternative. Brinch Hansen made monitors the only communication mechanism in the language specifically so that the concept's limitations would have nowhere to hide. If you keep an escape hatch, every place the idea fails gets quietly routed around it, and you will never learn where the idea's edge is — you will just have a system with an inexplicable pattern of exceptions in it.

That second habit reads as dogmatism and is the opposite. Exclusivity is an experimental protocol: it converts the question "is this concept sufficient?" from a matter of opinion into something the construction of a real system will answer. The corollary, which the same retrospective states plainly, is that you should not expect the concept to survive intact — the author's own verdict decades later was that the paradigm he had committed to lacked the elegance of true simplicity, and that judgment was available only because he had refused himself the alternatives.

**Source:** [Monitors and Concurrent Pascal: A Personal History](../works/monitors-and-concurrent-pascal-a-personal-history.md) — the sections tracing the idea from a shared verbal understanding through abandoned notations to a definition, together with the retrospective passage on complexity, which contrasts an idea held as a programming style with one embedded in a language and explains the decision to permit no other communication mechanism.
