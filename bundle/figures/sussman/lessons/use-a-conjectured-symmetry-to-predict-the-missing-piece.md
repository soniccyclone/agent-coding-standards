---
type: lesson
title: "Push a conjectured symmetry until it predicts something you have not noticed, then go looking for it"
figure: sussman
works: [lambda-the-ultimate-declarative]
axes: [cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Push a conjectured symmetry until it predicts something you have not noticed, then go looking for it

**Lesson:** Symmetry in a design is usually treated as decoration, a sign that the pieces were arranged tastefully. It is worth much more than that when it is used as an instrument. Suppose you have noticed a correspondence between two halves of a system — the machinery that governs when things happen and the machinery that governs what names mean — and you have a list of facts about each half that pair up. The productive move is to take the correspondence as a hypothesis with predictive obligations rather than an observation to admire: find an entry that exists on one side and has no partner on the other, and go look for the partner. Either it is there and you have learned something you did not know, or it is not and the symmetry is superficial, which is also worth learning. Both outcomes beat cataloguing the pairs you had already seen.

The instructive case is a prediction made and then confirmed in the same document. Given that invoking something implicitly creates a hidden object encoding what to do with the result, symmetry demands a hidden object created on the other side, at the moment of returning — and there is one: an unnamed place holding a partial result while the rest of the surrounding expression is worked out. Those hidden intermediate values had been sitting in plain sight for decades, discussed only as an allocation nuisance, without anyone recognizing them as the exact counterpart of the hidden return destination. The prediction came first and the recognition second, which is the whole point. Had the author only looked for symmetries among the things he already had names for, this one would have stayed invisible, because the notation of the language actively suppresses both of the objects involved.

There is a discipline attached, or the method degrades into pattern-matching on anything. The correspondence has to be stated as a table of specific pairs rather than a vague sense that two things resemble each other, because only a specific table has holes in it, and only a hole can be a prediction. And when the predicted object turns up, its existence is evidence that the symmetry is structural rather than accidental, which licenses using it again. Any language, system, or protocol with two apparently independent halves is worth this treatment: write the pairs in two columns, find the row with one entry, and go see what belongs in the empty cell.

**Source:** [Lambda: The Ultimate Declarative](../works/lambda-the-ultimate-declarative.md) — the conclusions section, where the author sets out a table of correspondences between forms and functions, evaluation and application, control and environment, and states explicitly that the last symmetry was not known to him beforehand: assuming control and environment structures are symmetric, and knowing that implicit continuations are created before invoking a function, he predicted that implicit temporaries must be created on return and only then noticed that they do occur. The relevant machinery is developed earlier, in the discussion of hidden environment operations accompanying returns.
