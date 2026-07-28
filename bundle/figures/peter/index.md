---
type: figure
title: Rózsa Péter
description: 1905-1977, Eötvös Loránd University, Budapest. Wrote the first systematic treatment of recursive function theory, clarifying primitive-recursion vs. general-recursion.
status: accepted
layer: design-thought
subdomains: [foundations-of-computation]
tags: [figure, accepted]
---

# Rózsa Péter

**Dates:** 1905-1977. Hungarian mathematician, Eötvös Loránd University, Budapest; barred from academic positions for years under Hungary's anti-Jewish laws.

## Why a candidate
Wrote the first systematic treatment of recursive function theory as a discipline in its own right, clarifying the primitive-recursion vs. general-recursion boundary that Gödel's and Kleene's definitions depend on — Kleene called her "the leading contributor to the special theory of recursive functions."

## Top 10 most influential works
1. *Rekursive Funktionen* (1951, first book-length treatment) — `paywalled`
2. *Recursive Functions* (1967, English translation) — `paywalled`
3. "Über den Zusammenhang der verschiedenen Begriffe der rekursiven Funktion" (1934) — `uncertain`
4. "Über die mehrfache Rekursion" (1950) — `uncertain`
5. *Playing with Infinity* (1943/1961, popular book, outside strict scope) — `paywalled`

## Phase 3 access flag
Items 1 and 2, *Rekursive Funktionen* (1951) and its 1967 English translation
*Recursive Functions* — the book-length treatment cited directly in this
figure's "why a candidate" case above ("wrote the first systematic treatment
of recursive function theory as a discipline in its own right") — have no
publicly accessible copy anywhere checked. Neither edition appears digitized
on the Internet Archive, HathiTrust, or the publisher (Akadémiai
Kiadó/Springer); both remain subscription/purchase-only. Item 5, *Playing
with Infinity*, is on the Internet Archive
(archive.org/details/playingwithinfin00pete) but only under Controlled
Digital Lending (time-limited borrow, access-restricted), which does not
meet this pass's public-access bar — left excluded as originally flagged.
By contrast, items 3 and 4 (the 1934 and 1936 Mathematische Annalen papers,
previously `uncertain`) are now confirmed public via the Göttinger
Digitalisierungszentrum's digitized run of the journal — see
`works/uber-den-zusammenhang-der-verschiedenen-begriffe-der-rekursiven-funktion.md`
and `works/uber-die-mehrfache-rekursion.md`. Note also that item 4's year is
corrected to 1936 in the work file; the 1950 date in this stub appears to
conflate it with a different, later JSL paper on the same theme.

## Lessons
Péter's two accessible Mathematische Annalen papers teach a single discipline:
treat expressive power as something you measure rather than something you read
off a definition's shape. A scheme that looks more general than primitive
recursion usually is not, and the way to find out is to compile it away, which
is why her method turns on encoding (packing a whole computation history into
one value so it fits through a single-value recursion slot, replacing nested
recursion depth with arithmetic on indices) and on staged reduction that keeps
peeling cases until the last one is trivial. Where a scheme genuinely is
stronger, the same measuring instinct demands a proof of strict separation, and
her tool there is to make the higher level enumerate the lower and then diagonalize
out of it, which reframes a hierarchy as a statement about what one level can
say about another rather than about syntax. Two further habits carry beyond
recursion theory: a recursion's real content is the well-ordering you impose on
its domain, so choosing that order is the actual design decision and everything
else is bookkeeping; and when a construction is hard to build directly, it is
often easier to specify a record that can be checked and then search for it
under a bound you can guarantee, trading constructive effort for verifiability.
Underneath all of it is her insistence on a deliberately narrow trusted base,
rebuilding borrowed machinery from a small set of primitives rather than
assuming it, which is what makes her classification claims mean anything at all.
