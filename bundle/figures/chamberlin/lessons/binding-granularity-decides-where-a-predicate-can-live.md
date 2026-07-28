---
type: lesson
title: "Distinguish binding forms by granularity and the clause zoo collapses"
figure: chamberlin
works: [quilt-an-xml-query-language]
axes: [primitive-count, cognitive-load, expressiveness]
subdomains: [databases-and-data-management, programming-languages-and-semantics]
tags: [lesson]
---
# Distinguish binding forms by granularity and the clause zoo collapses

Languages accumulate clauses because each new filtering stage seems to need its own keyword: filter the individual items here, group them, then filter the groups over there, then order the result. The alternative is to introduce exactly one distinction — whether a variable is bound to one item at a time, iterating, or to a whole collection at once — and let every stage distinction follow from it. A condition over individuals belongs wherever individual bindings are in scope; a condition over an aggregate belongs wherever the collection binding is in scope. Two binding forms and one filter clause then cover what elsewhere requires several dedicated clauses, because the position at which a predicate is legal is determined by the arity of what is in scope rather than by a keyword the programmer must remember to reach for.

Why it holds: aggregation is not a phase of query evaluation, it is a function on a collection. Once collections are first-class values a variable can name, "grouping" is just an iteration variable over the distinct keys plus a collection variable defined relative to it, and "filter the groups" is an ordinary predicate that happens to mention an aggregate. The phased vocabulary in older designs was an artifact of collections not being nameable, and it left a real cost behind: rules about which conditions may appear in which clause, learned by exception rather than derived.

The counterweight is that granularity becomes load-bearing and must be visible. If a variable's arity is ambiguous at a glance, programmers write predicates that are silently wrong — accepting or rejecting an entire collection when they meant to test its members. So the two binding forms need distinct syntax, and a condition that restricts the members of a collection has to be attached where the collection is defined rather than bolted on afterward. That is the honest trade: one fewer concept to memorize, in exchange for one concept you must always be conscious of.

**Source:** [Quilt: An XML Query Language for Heterogeneous Data Sources](../works/quilt-an-xml-query-language.md) — the sections defining the iterating and collection-binding clauses and the filter clause, plus the relational-query examples that reconstruct grouping, aggregate filtering, and outer joins without introducing counterparts to the corresponding SQL clauses.
