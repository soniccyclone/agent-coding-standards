---
type: lesson
title: "When a rival definition of the same property appears, satisfy it rather than defend yours"
figure: yao
works: [how-to-generate-and-exchange-secrets]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, algorithms-and-complexity]
tags: [lesson]
---
# When a rival definition of the same property appears, satisfy it rather than defend yours

**Lesson:** Whenever a property is important enough to formalize, several inequivalent formalizations of it will exist, each defensible and each shaped by the concerns of whoever wrote it. One may be behavioral — nothing an observer can compute afterward improves — and another structural, describing what a participant is permitted to learn in terms of what could have been produced without the interaction at all. The reflex when a competing definition appears is to argue that yours captures the intent better. That argument is unwinnable and, worse, uninformative: definitions are not true or false, and the field cannot use the outcome even if you win.

The move that produces knowledge instead is to take the rival definition as a second obligation and discharge it against the construction you already have. Doing so yields three things the argument would not have. Your result becomes usable by everyone working in either vocabulary, without translation and without them having to trust your reading of their definition. You learn something factual about the relationship between the two notions, because your construction is now a witness that the definitions are at least compatible on this class of problems — and if the discharge fails, you have located a real separation, which is more valuable still. And your own definition survives on merit rather than on advocacy: if it demanded something the other did not, the demonstration shows what that something bought.

Read this as the general policy for definitional disagreement in design work — competing formulations of what "consistent," "available," "isolated," or "correct" is supposed to mean. Prefer building the artifact that satisfies both formulations over the memo arguing that one is right. The artifact settles what the memo can only assert, and the effort of satisfying both is usually less than the effort of the debate. Where both cannot be satisfied, that impossibility is the finding, and it is a far sharper contribution than a preference.

**Source:** [How to Generate and Exchange Secrets](../works/how-to-generate-and-exchange-secrets.md) — the closing connections section, which acknowledges that the paper adopted a semantic definition of privacy stated in terms of what predicates remain uncomputable, notes the separately introduced minimum-knowledge-transfer notion as an alternative capturing the same intent, and then states a further theorem showing the paper's own protocols meet that alternative too.
