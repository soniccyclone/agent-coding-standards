---
type: lesson
title: "Rank by concentration, because neither frequency nor rarity identifies signal"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, cognitive-load]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# Rank by concentration, because neither frequency nor rarity identifies signal

**Lesson:** Asked which terms characterize a document's subject, the intuitive answer is the most frequent ones, and that answer is not merely imperfect but precisely inverted: the top of the frequency list is structural filler, words that carry grammar rather than content. Correcting to the opposite extreme fails too. Rare terms are not automatically informative — an unusual connective is as rare as a technical term from an obscure sport, and only one of them tells you what the document is about. Two natural orderings, both useless, which is what makes the third idea worth extracting.

The property that separates the informative rare term from the merely unusual one is how its occurrences are distributed across the corpus rather than how many there are. A specialist term is concentrated: it appears in few documents, and *within* those documents it recurs, because a text genuinely about that subject keeps needing the word. An unusual stylistic word is diffuse: it can appear anywhere, and appearing once gives no reason to expect a second occurrence. So the signal is burstiness — the interaction between a term's scarcity across the collection and its repetition inside a single member of it. Measuring one dimension alone cannot see this; the standard weighting exists precisely to combine corpus-level scarcity with document-level frequency into a single ordering.

The transferable move is to stop looking for the discriminating quantity among counts and start looking for it among *distributions of counts*. Whenever you need to find which items are diagnostic of a category, two cheap orderings will present themselves — most common and least common — and both will be wrong for the same underlying reason: neither uses information about how occurrences cluster. Log events, error codes, API calls, genetic markers, purchase items all have this shape. The frequent ones are ambient and describe nothing; the rare ones are a mix of the meaningful and the merely odd, and the way to tell those apart is whether an occurrence raises the probability of another occurrence nearby.

The corollary is a warning about normalization. Because the useful quantity is a ratio between two different scales of observation, it is easy to destroy by aggregating too early — collapse a corpus into one pooled bag of terms and the concentration information is gone, leaving only frequency, which is the ordering you already knew was inverted.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 1's treatment of word importance in documents, which observes that the intuition to use the most frequent words is exactly opposite of the truth since those are stop words, that not all rare words are useful indicators (contrasting "notwithstanding" or "albeit" with "chukker," which signals a document about polo), that the difference lies in the concentration of the useful words into few documents, that a topical term once present tends to be repeated while a stylistic rarity does not, and that TF.IDF formalizes this by multiplying a document-normalized term frequency by an inverse document frequency.
