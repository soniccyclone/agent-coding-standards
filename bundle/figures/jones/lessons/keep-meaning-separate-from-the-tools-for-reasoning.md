---
type: lesson
title: "Keep the definition of meaning separate from the tools for reasoning, and then keep several tools"
figure: jones
works: [development-methods-for-computer-programs-including-a-notion-of-interference]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Keep the definition of meaning separate from the tools for reasoning, and then keep several tools

**Lesson:** There is an appealing shortcut in which the rules you use to reason about a construct are declared to be the definition of that construct. It saves building a separate model and it guarantees that the rules are sound by fiat. The cost only becomes visible later: with the rules serving as the definition, you get exactly one way to reason about each construct, and any second rule set looks like a competing definition rather than an additional instrument. If instead the meaning is fixed independently and each rule set is proved to respect it, rule sets become tools. You can have as many as you like, each shaped for a different situation, and adding one changes nothing about the language.

That freedom turns out to matter because reasoning tools of identical logical power are not remotely equal in usability. Argue about a loop by summarizing what the remaining iterations will do, or by what the completed iterations have accomplished so far, or by naming a quantity the body must leave alone: all three can prove the same things, and which one you pick determines whether the condition you must invent is a one-line expression or a tangled formula. Mismatch the tool to the loop and the difficulty shows up as an awkward invariant, which people then read as the problem being hard rather than as having reached for the wrong instrument. Recognizing the shape of the problem — are inputs consumed, or is a counter walked up toward an untouched bound, or is some combination held fixed — is the actual skill, and it is only available to someone holding more than one tool.

The same reasoning licenses tailored rules for common patterns instead of desugaring them. A bounded iteration can be rewritten as a general loop plus a counter and then handled by the general rule, but the rewrite manufactures obligations the original construct made unnecessary — termination, for one, which the bounded form guarantees by its shape. Where a construct carries structural information, a rule that exploits that information directly is smaller and truer to the design than a rule reached by translating the construct into something weaker. Prefer the tool that reasons about what you actually wrote.

**Source:** [Development Methods for Computer Programs including a Notion of Interference](../works/development-methods-for-computer-programs-including-a-notion-of-interference.md) — the proof-rules chapter's opening, which declines to treat the rules as a semantics and proves them against an independently given denotational definition, noting this permits alternative rules for the same construct; the presentation of several loop rules said to differ in convenience rather than power; the worked comparisons showing an inappropriate choice of loop rule yields a more cumbersome invariant; and the remark that tailoring a rule for bounded iteration is preferable to reducing it to the general form.
