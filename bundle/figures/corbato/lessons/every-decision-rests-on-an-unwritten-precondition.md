---
type: lesson
title: "Every Decision Rests on an Unwritten Precondition"
figure: corbato
works: [on-building-systems-that-will-fail]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification, algorithms-and-complexity]
tags: [lesson]
---
# Every Decision Rests on an Unwritten Precondition

**Lesson:** The best-known story in Corbató's Turing lecture is a security failure with no villain in it. The CTSS text editor named its scratch file the same way every time, which was correct under a design where each directory had at most one active user. Later, with a dozen system programmers needing to maintain a live system, that one-user rule was relaxed for the system's own directory as an administrative convenience. Nobody connected the two facts. Two people edited at once, the temporary files collided, and the password file went out to every terminal in place of the message of the day. The editor's assumption had expired without expiring anything the compiler could notice.

He puts two other examples beside it, and the arrangement is deliberate. Floating-point underflow flattens a physically continuous curve because hardware treats a very small number as zero, which is locally reasonable and globally catastrophic, and invisible if the value is internal to a larger calculation. A graduate student's iterative root finder failed to converge on two of three roots, and his fix was to give up after a fixed number of tries — while the real situation was that his experimental coefficients were bad, two of the roots were complex and therefore unreachable by that method, the first root was garbage, and cubics have an exact closed form that made the iteration unnecessary to begin with. Three different mechanisms, one shape: the defect sits in the gap between the model in someone's head and what the machine is actually doing.

The practical consequence is a habit rather than a technique. Write down what a piece of code assumes about the world around it, because the assumptions that go unrecorded are exactly the ones that will be invalidated by a change somewhere that looks unrelated. Treat a relaxed constraint as a code change to everything that ever depended on it. And refuse to suppress a symptom you cannot explain: the student's patch made the program stop complaining, which is the worst possible outcome, because it converted a visible failure into a silent wrong answer.

**Source:** [On Building Systems That Will Fail](../works/on-building-systems-that-will-fail.md) — the mishap section recounting the CTSS password incident and the two lessons drawn from it, together with the underflow and Newton-Raphson examples presented earlier under the discussion of why testing and correctness proofs are not sufficient.
