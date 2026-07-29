---
type: lesson
title: "Learn only the part of the problem you cannot state yourself"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, cognitive-load, verifiability]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# Learn only the part of the problem you cannot state yourself

**Lesson:** Fitting a model from examples is not a universally superior alternative to writing down what you know; it is a specific trade you make when you cannot write down what you know. The honest test is whether a competent person could articulate the rule. Where the criterion is genuinely mysterious — why a particular viewer likes a particular film — inference from examples buys you something no author could have written. Where the criterion is common knowledge that merely happens to be tedious to encode, a directly specified rule tends to match or beat the learned one, and it costs less to build, run, and reason about. Reaching for the learned model in the second case is not sophistication, it is paying a premium for the illusion of one.

The premium is paid in two currencies. The first is loss of explanation: a fitted model that stacks many small decisions on top of one another may be accurate and still be unable to say why, and there is no way to recover the explanation after the fact. The second is loss of the ability to intervene — you cannot correct a specific misjudgement in a learned artefact the way you can edit a stated rule. Whether those losses matter is not a technical question but a question about who has to live with the output. A classifier that mislabels a message can shrug and say the message resembled others of its kind; a system that raises the price someone pays owes that person an account of the change. Explainability is therefore a property demanded by the deployment context, not a nice-to-have of the algorithm, and it should be settled before the model class is chosen rather than discovered afterwards.

The practical consequence is a habit of decomposition: try to state the rule first, in full, and let learning take only the residue that resists statement. This usually leaves a much smaller learned component than the reflexive approach produces, which is a double win — a smaller surface where behaviour is unexplained, and a smaller thing to train. It also reframes what a good result looks like. The interesting finding is not that the learner reached some accuracy, but that it beat the rule you could have written; if it did not, the rule was the better engineering all along.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the introductory survey of what "data mining" means across statistics, machine learning, and computer science, including the authors' account of a startup whose learned résumé-finder never outperformed hand-designed keyword rules, and their contrast between spam labelling and insurance pricing as settings where unexplainability is and is not tolerable.
