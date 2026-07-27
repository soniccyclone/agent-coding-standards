---
type: lesson
title: "One name serving two concepts is a structural defect, not a style complaint"
figure: fagin
works: [degrees-of-acyclicity-for-hypergraphs-and-relational-database-schemes]
axes: [expressiveness, cognitive-load, verifiability]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# One name serving two concepts is a structural defect, not a style complaint

**Lesson:** Fagin's example is small enough to hold in your head and sharp enough to end an argument. A schema tracks where employees work and where they live, and both facts land in a column called city. Nothing is wrong with any single table. But now ask for the connection between an employee and a city, and there are two different answers depending on which route you take through the tables, both defensible, neither distinguished. The question is ambiguous, and the ambiguity is not a property of the question. It is a property of the schema. Rename the two columns to reflect what they actually mean, work-city and home-city, and the ambiguity vanishes.

The renaming does more than tidy up. Fagin shows that having a unique answer for every set of columns, for every consistent database, is exactly equivalent to the strongest useful degree of acyclicity in his hierarchy. So the schema before the rename fails a precise structural condition and the schema after it satisfies one, and every guarantee attached to that condition is unavailable in the first case and free in the second. He gives the same treatment to a scheme that fails a weaker condition and shows it too can be repaired by renaming. The lesson is not that naming matters for readability. It is that reusing one identifier for two distinct concepts creates real structure, the wrong structure, and removing the overload changes what the system can prove about itself.

The payoff is expressive rather than merely hygienic. When connections are unique, a user can state what they want without saying how to get it: name the columns of interest, and the system finds the route, because there is only one. Fagin points out that this is another rung up the same ladder that took queries from specifying index access paths to specifying tables, and that the freedom flows to the implementation, which now gets to choose the route based on what indexes happen to exist. He also notes a contemporary tool that maintained a side file recording which tables to combine for which requests, and observes that under the structural condition such a file is unnecessary. Ambiguity in the model gets paid for downstream, either in a configuration artifact somebody must maintain or in every caller having to spell out the path.

The transferable diagnostic is to treat every overloaded name as a hypothesis that two concepts have been conflated, and to check what that conflation makes ambiguous. A field reused across contexts, an identifier type shared by unrelated entities, a status enum whose meaning depends on which subsystem is reading it: each one silently creates multiple valid interpretations of the same query, and the cost shows up far from the name, as callers that must disambiguate, code paths that pick a default, and invariants nobody can state cleanly. Splitting the name is often the whole fix.

**Source:** [Degrees of Acyclicity for Hypergraphs and Relational Database Schemes](../works/degrees-of-acyclicity-for-hypergraphs-and-relational-database-schemes.md) — the section on properties of the strongest acyclicity degree, particularly the worked employee-and-city example whose two competing interpretations disappear under renaming, and the accompanying argument about queries that need not name the tables to combine.
