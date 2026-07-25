---
type: lesson
title: "Your validity rules are control flow whether you intended them to be or not"
figure: abiteboul
works: [comparing-workflow-specification-languages]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, databases-and-data-management, formal-methods-and-verification]
tags: [lesson]
---
# Your validity rules are control flow whether you intended them to be or not

**Lesson:** Constraints on what a state may look like are normally filed under data quality, a separate concern from the logic that decides what the system does next. This work shows the separation is fictional. If an action is permitted only when the resulting state remains valid, then the set of valid states determines which actions can happen, and a rule intended purely to describe well-formed data has become a condition on the transition. The paper pushes this to its limit and finds that state-validity rules alone, with no explicit sequencing mechanism of any kind, can reproduce guarded actions, finite-state control, and constraints written over the history of the run. Structural rules over the shape of the data are a complete process control mechanism hiding in plain sight.

The reason is worth internalizing because it generalizes past the specific formalism. Any step that must leave the world in a permitted state is implicitly conditioned on the whole of the permission criterion, and the permission criterion can talk about anything present in the state, including whatever record of past activity happens to be lying around. Extra structure kept in the state, even structure introduced for unrelated reasons, becomes available as a variable that the constraints can consult, and consulting it is what turns a static rule into a phase gate. This is why systems accumulate behavior nobody designed: a uniqueness rule, a required field, a foreign key added for hygiene, each of these silently removes possible sequences of operations, and the removed sequences are usually discovered by a user hitting one.

Two habits follow. When debugging why a system will not advance, read the validity rules as part of the state machine rather than treating them as a separate layer to be checked afterward, because they are the reason a transition is unavailable at least as often as the explicit logic is. When designing, decide deliberately which of your behavioral requirements you want stated as invariants over state and which you want stated as explicit sequencing, since invariants give you an argument that holds no matter how the system got there while explicit sequencing gives you a reader who can see the intended order. The trap is doing both accidentally, so that the real behavior is the intersection of an explicit process definition and a set of constraints written by someone who thought they were only describing data.

**Source:** [Comparing Workflow Specification Languages](../works/comparing-workflow-specification-languages.md) — the description of the core model in the introduction, which notes that requiring an action to preserve the static constraints already supplies control over execution, and the main results establishing that those constraints suffice to simulate the guard-based, automaton-based, and history-based specification mechanisms.
