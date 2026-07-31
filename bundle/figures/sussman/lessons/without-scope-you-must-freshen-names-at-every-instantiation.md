---
type: lesson
title: "Where there is no scope there must be freshening, because a template used twice will otherwise constrain itself"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Where there is no scope there must be freshening, because a template used twice will otherwise constrain itself

**Lesson:** A reusable description contains placeholders, and the placeholders have names. As long as the description is used once, the names are private by accident and nothing goes wrong. Use it twice — two different templates that happen to share a placeholder name, or, far more insidiously, one template invoked at two levels of its own recursion — and if the bindings all accumulate in one shared space, the two uses will be forced to agree on something they have no relationship to. The failure is not a crash. It is a silent narrowing: solutions that exist are not found, because an unrelated coincidence of naming was interpreted as a genuine constraint.

The two available remedies are worth seeing as the same requirement met by different means. One is scope: give each instantiation its own space, resolve names within it, and let identical names in different spaces denote different things. The other is renaming: before instantiating, walk the description and replace every placeholder with a name manufactured to be unique to this use, typically by combining the original name with a per-use counter. Where a structured environment is available the first is cleaner and cheaper. Where bindings live in a single flat space — as they do in any system that must let partial information from different parts of a computation constrain each other — the first is not available and the second is the straightforward answer, at the price of copying the description and generating names on every use.

The important recognition is that this is a requirement rather than a technique, and that it applies to anything instantiated repeatedly against a shared store of bindings: rules, macros, type schemes, generic signatures, query fragments, parameterized templates of any kind. The question to ask of such a system is where the freshening happens, and if the answer is nowhere, the system has a latent capture bug whose symptom is missing results rather than wrong ones — which is exactly the symptom nobody investigates, since a query returning fewer answers looks like a query about which there was less to say.

There is a corollary about recursion specifically. Self-application is the case where the collision is guaranteed rather than accidental, because the two uses are textually identical and therefore share every name. Any mechanism that supports recursive instantiation must freshen, and a mechanism that appears to work on non-recursive cases is not evidence, because non-recursive cases only collide when two authors happen to have chosen the same letter.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) — chapter 4 section 4.4.4.4, the rule-application procedure, which renames all the variables in a rule with unique new names before unifying its conclusion with the query pattern, with the stated reason that variables from different rule applications must not become confused: two rules using the same variable name may each add a binding for it, those bindings have nothing to do with each other, and the system should not be fooled into thinking they must be consistent; the accompanying remark that a cleverer environment structure could be devised instead of renaming, with renaming chosen as the most straightforward if not the most efficient approach; and the implementation, which obtains a fresh application identifier per use and tree-walks the rule combining that identifier with each original variable name.
