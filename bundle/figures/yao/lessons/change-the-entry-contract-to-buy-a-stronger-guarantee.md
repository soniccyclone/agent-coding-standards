---
type: lesson
title: "When the protocol cannot be strengthened, strengthen what participants must arrive holding — and pick the arrival format that lets stages chain"
figure: yao
works: [how-to-generate-and-exchange-secrets]
axes: [expressiveness, verifiability]
subdomains: [software-engineering-and-architecture, distributed-systems-and-concurrency]
tags: [lesson]
---
# When the protocol cannot be strengthened, strengthen what participants must arrive holding — and pick the arrival format that lets stages chain

**Lesson:** There is a ceiling on what any procedure can promise given what its participants are required to bring. If a party arrives holding nothing but a private value it alone can see, no arrangement of messages can bind it to that value; the strongest achievable guarantee stops short in a way no cleverness recovers. The productive response is to stop working on the procedure and work on its entry conditions: require each party to arrive already committed — carrying its input in a form the other side holds a sealed copy of, under a hardness assumption that makes the seal binding. The messages need not change much. What changed is that the interface now carries evidence, and every guarantee downstream of that evidence gets stronger for free.

The design lesson is where to look when a specification stalls. Two candidate designs can differ in nothing but their input and output shapes and still sit at different points on the strength curve, because the shapes decide what the parties can be held to. So treat the signature as a tunable part of the design rather than as given by the problem statement. Ask what the caller could be made to supply, or to prove it supplied, that would let the body promise more; the extra obligation on the caller is usually cheap when the caller already has the material, and it converts an unenforceable claim into an enforceable one. This is the same instinct as pushing a validity check into a type or a database constraint: not stronger logic, a stronger precondition.

The second half is why the format should be chosen for composition, not for the single stage in front of you. A stage whose outputs are shaped like the committed inputs of the next stage can be chained without a translation step and without re-establishing at every seam what the previous stage already established; a stage that emits bare values forces each successor to rebuild the evidence, and the guarantee degrades at every joint. So when you extend an interface to buy strength, make the enriched output the same species as the enriched input. The extra fields look like overhead in isolation and pay for themselves the first time two stages are put in series — which, in any system that grows, is immediately.

**Source:** [How to Generate and Exchange Secrets](../works/how-to-generate-and-exchange-secrets.md) — the general-computation section's two models: the first with plain private inputs, where a dishonest party can silently substitute a value and the guarantee is correspondingly capped, and the second where each party additionally arrives with a hard-to-factor modulus and a provably secure encryption of the other's parameter, yielding stronger privacy and fairness constraints; plus the remark that the second format is what arises naturally when protocols are concatenated.
