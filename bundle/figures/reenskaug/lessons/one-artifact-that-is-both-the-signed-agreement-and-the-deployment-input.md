---
type: lesson
title: "Make the signed agreement and the deployment input the same artifact"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Make the signed agreement and the deployment input the same artifact

**Lesson:** What a salesperson and a customer settle on is a contract: a document in the customer's terms, printed and signed. What the system needs is a configuration: which capabilities to switch on, for whom, with which values. These are normally two artifacts, produced by different people from the same conversation, and the gap between them is where a large class of real failures lives — the customer was sold something slightly different from what was deployed, and neither document is wrong on its own terms, so nothing detects it. The design here collapses them: the contract document *is* the input. It can be printed and signed, and it can be executed to install exactly what it describes.

The property this buys is not efficiency, though it saves a transcription step. It is that a specific disagreement becomes impossible to have. There is no longer any state in which what was agreed and what is running differ, because there is only one description and both readings — the human one and the machine one — are of the same bytes. Drift between two representations of one decision cannot be prevented by discipline or by review, since both documents can be individually correct while disagreeing; it can only be prevented by there being one document.

Two conditions make it feasible, and both are visible here. The artifact has to be readable by the party who signs it, which means it is written in the customer's vocabulary rather than the system's, with prose sections interleaved among the settled values — this is a document that happens to be executable, not a configuration file with a signature block. And it has to be authored through a tool that can only produce valid specifications, because an artifact that is simultaneously a legal commitment and a deployment instruction must not be capable of expressing an arrangement the system cannot honor. A signature on an unsatisfiable promise is worse than a rejected form.

The general reflex applies wherever a human agreement and a machine action are derived from one decision: order forms and provisioning, policies and enforcement configuration, architecture documents and infrastructure definitions. Ask whether the two representations could be one, and if they cannot, be clear that you have accepted a permanent reconciliation burden — one that no amount of care eliminates, because the failure is silent by construction.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 12 section 12.4, which proposes the Service Contract Document as the appropriate medium for defining Subscribers and their services, a document which may be printed and signed and which may be executed to cause the installation of the Subscribers and their services in the Service Domain; created in a syntax-directed editor controlled by an OOCS Schema that supports low-level concepts such as texts, graphics and tables alongside high-level ones such as services and selectors, with the sample contract in figure 12.6 mixing explanatory prose about individual users with the bound parameter values.
