---
type: lesson
title: "Nobody asks for what they believe is impossible, so absence of a request is not absence of a need"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Nobody asks for what they believe is impossible, so absence of a request is not absence of a need

**Lesson:** The rule offered for abandoning an established technology is strict: the only acceptable reason is a pressing requirement the current technology cannot satisfy. Fashion does not qualify, and neither does the expectation that the new thing will eventually be better. What makes this more than conservatism is the qualifier attached — the requirements must be *real* rather than *perceived* — and the reason given for the distinction, borrowed from psychology: people only ask for things they believe to be feasible.

That single observation undermines requirements gathering as normally practiced. The set of requests you collect has already been filtered through what your users think is possible, and their model of what is possible was formed by the tools they currently have. So the requirements you receive are systematically biased toward what the incumbent technology can already do, and the needs that would actually justify a change are exactly the ones least likely to be voiced. "Nobody has asked for it" therefore carries almost no information about demand. It is at least as likely to mean the capability is unimaginable from where your users stand.

The trap has two jaws and the discipline has to address both. Read requests literally and you will never find a reason to change anything, because the genuinely new need never surfaces as a request. Read them liberally and you will manufacture justifications for whatever you already wanted to build, since any technology change can be motivated by a hypothetical requirement nobody stated. The way through is to distinguish what people cannot do from what people have not asked to do, and to seek evidence of the former in behavior rather than in interviews: the workarounds they maintain, the tasks they abandon partway, the things they do by hand alongside the system, the questions they answer outside it. Those are visible without anyone having to conceive of the solution.

The same asymmetry runs the other direction and is the reason the rule is stated so strictly. Replacing something mature is not a like-for-like exchange — the incumbent's accumulated tooling, reliability and institutional knowledge all go at once, while the replacement's advantages are mostly prospective. Given that the ledger is already tilted, a motivation drawn from a request nobody made is not enough weight to move it.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 11 section 11.3's boxed account of the author's wife, an experienced database manager, reacting with frustration to object orientation as a return to coding and debugging; the first lesson drawn is that nobody should replace a mature technology without good reason, with pressing requirements unsatisfiable by the current technology the only acceptable one, followed by the citation that psychologists claim we only ask for things we believe to be feasible and the warning to read pressing requirements as real rather than perceived requirements.
