---
type: lesson
title: "An ambiguous outcome should widen what you record, not reject the request"
figure: vardi
works: [on-the-semantics-of-updates-in-databases]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [databases-and-data-management, foundations-of-computation]
tags: [lesson]
---
# An ambiguous outcome should widen what you record, not reject the request

**Lesson:** When a request admits several equally good ways of being satisfied, the reflex is to declare it ill-formed and refuse. Vardi's framework takes the opposite line, and the argument for it is sharp: a request is the most recent evidence you have about the world, so refusing it discards information in order to protect a representation that was merely too narrow to hold the result. What the ambiguity actually tells you is that your knowledge has become less specific than it was. The right response is to record that — the new state is the one asserting only what all the acceptable outcomes agree on, which is exactly the disjunction of them.

This turns an error case into an ordinary value, and it is the same move that makes null-and-unknown, sum types, confidence intervals, and multi-valued futures worth having. The precondition is that your representation can actually express partial knowledge. If the only states you can write down are fully determinate ones, ambiguity has nowhere to live and rejection is forced; the flaw is then in the state language, not in the request. Vardi is careful about the limit here too — sometimes the disjunction of the candidates is not expressible in the language at all, and it is worth knowing when your formalism runs out rather than pretending the case does not arise.

The design discipline that follows is to separate three questions that get conflated. Is the request meaningful? Is the outcome unique? Can the outcome be represented? Only the first is grounds for rejection. A non-unique outcome is a fact about the request's information content and should be preserved; an unrepresentable outcome is a deficiency in your state language and should be recorded as such rather than blamed on the caller. Systems that collapse all three into a single "invalid" response push the ambiguity out to callers, who then encode it in comments, retries, and conventions you cannot see.

**Source:** [On the Semantics of Updates in Databases](../works/on-the-semantics-of-updates-in-databases.md) — section two's discussion of what to do when several theories accomplish an update minimally: the explicit rejection of the earlier position treating such a case as an illegal update, the argument that an update conveys the user's latest knowledge so no update should be illegal, the construction of the new state as the class of models of the union of the candidates, and the caveat that this class is not always first-order axiomatizable.
