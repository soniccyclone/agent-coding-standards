---
type: lesson
title: "A tool that removes limits multiplies whoever holds it, downward as readily as upward"
figure: chuck-moore
works: [the-evolution-of-forth, forth-a-language-for-interactive-computing]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# A tool that removes limits multiplies whoever holds it, downward as readily as upward

**Lesson:** Some tools compress the range of outcomes their users can produce. Enough structure is imposed that a novice's result and an expert's result end up within shouting distance of each other, and the imposition is the point. Other tools do the opposite: with no type discipline, no fixed grammar, and the system's own internals open for redefinition, the difference between a skilled and an unskilled user is amplified rather than damped. Both are legitimate designs, but they are different products aimed at different situations, and the mistake is to evaluate one by the other's criteria. A permissive tool judged as a leveler looks reckless; a leveler judged as an amplifier looks like a straitjacket.

Choosing amplification has organizational consequences that follow directly from the mathematics and cannot be avoided by good intentions. It fits a small group of highly capable people and fits poorly a large group of mixed capability, because the variance the tool introduces has to be absorbed somewhere. Projects built this way have both spectacular successes and conspicuous failures on record. Examining the failures is instructive: they are attributable to the ordinary causes that sink projects regardless of tooling, which are unclear requirements, weak management, and expectations detached from reality. The amplification did not create those problems, it magnified them, and that is exactly what one should expect it to do.

The same trade shows up as a barrier to adoption, which is worth naming as a cost rather than dismissing as other people's confusion. A tool whose parts are not separable, which is at once a language, an environment, a storage scheme, and a means of interacting with a machine, resists being explained, because there is no familiar category to put it in. Practitioners regard exactly that integration as the source of their productivity, since a uniform way of doing anything at any level removes the friction of crossing between tools that do not know about one another. Both readings are correct simultaneously. A programmer who accepts this stops expecting a single design to be both the highest-ceiling tool and the most widely adoptable one, and chooses which of the two is actually wanted.

**Source:** [The Evolution of Forth](../works/the-evolution-of-forth.md) — the problems section, which contrasts leveling tools against amplifying ones, records the observation that a strong programmer can do extraordinary work with such a tool and a weak one disastrous work, traces documented failures to ordinary project-management causes, and draws the conclusion about small skilled teams; together with the discussion of unclear identity and the competing testimony on whether seamless integration is the chief asset or the chief obstacle. Also [FORTH — A Language for Interactive Computing](../works/forth-a-language-for-interactive-computing.md) — the closing statement of what the system does and does not undertake on the user's behalf, and the accompanying remark about who is and is not the intended audience.
