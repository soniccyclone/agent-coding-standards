---
type: lesson
title: "Gate expressive power by the operator's competence, using the same machinery restricted differently"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [expressiveness, cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Gate expressive power by the operator's competence, using the same machinery restricted differently

**Lesson:** The same job title covers people with radically different training: a shop clerk who completed a short course, and a specialist consultant who tailors sophisticated arrangements for demanding customers. The usual responses are both bad. Build one interface for the median and the clerk is overwhelmed while the consultant is boxed in. Build two products and you maintain two systems that drift. The move here is a third: one underlying mechanism, and several restrictions over it — a small grammar issued to the clerk that admits only the arrangements they were trained on, and an elaborate one issued to the consultant.

The distinction from access control is worth being precise about, because they look similar and behave differently. Permissions answer *what may this person touch*, and are enforced by refusing operations, so an under-trained operator with broad permissions still faces the whole surface and is stopped only when they attempt something forbidden — having already had to consider it. A restricted grammar answers *what can this person express*, and is enforced by absence: constructions outside their scope are not offered, so complexity they were never trained for is not merely blocked, it is invisible. Their working surface is genuinely smaller, which is a cognitive result rather than a security one, and it is what allows the same machinery to be simple for one operator and powerful for another.

Two consequences make it worth the arrangement. Anything expressible in a restricted grammar is expressible in the wider one, so the operator's work stays valid as they are promoted, and promotion means being issued a larger vocabulary rather than migrating to a different tool. And the training and the tool become the same artifact: what the clerk learned and what the clerk can express are defined by the same document, so the gap between "what we taught them" and "what the system lets them do" — normally a permanent source of both accident and frustration — closes by construction.

The general reflex is to notice when a single role in your system is actually a spread of competences, and to reach for a restriction over shared machinery rather than either a lowest-common-denominator interface or a fork. The design question becomes which vocabulary each population should be handed, and that question has an evidence base: what they were trained on, and what they have demonstrated.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 12 section 12.5's note that several schemas can be defined: the Service Creator may define different OOCS Schemas for different categories of Service Provider, with one end of the spectrum being corner-shop clerks who get a small schema permitting only the simple services they learned in their training course, and the other a highly competent customer consultant given a very elaborate schema he knows how to exploit to tailor advanced services for sophisticated customers.
