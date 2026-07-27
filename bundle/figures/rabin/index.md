---
type: figure
title: Michael O. Rabin
description: 1931-2026, Hebrew University/Harvard. Co-founded nondeterminism theory; pioneered randomized algorithms with provable probabilistic bounds.
status: accepted
layer: implementation-mapping
subdomains: [algorithms-and-complexity]
tags: [figure, accepted]
---

# Michael O. Rabin

**Dates:** 1931-2026 (died April 2026). Israeli-American computer scientist; Hebrew University of Jerusalem and Harvard.

## Why a candidate
Co-founded (with Dana Scott) the formal theory of nondeterminism in computing, and separately pioneered randomized algorithms with provable probabilistic bounds (Miller-Rabin primality, Rabin-Karp string search) — a direct extension of cost analysis into probabilistic/expected-time territory.

## Top 10 most influential works
1. "Finite Automata and Their Decision Problems" (1959, with Scott, IBM J. Res. Dev.) — `public` (IBM-hosted PDF)
2. "Efficient Randomized Pattern-Matching Algorithms" (1987, with Karp, Rabin-Karp) — `public` (IBM journal)
3. "Digitalized Signatures and Public-Key Functions as Intractable as Factorization" (1979, MIT/LCS tech report) — `public` (MIT LCS self-archived)
4. "Probabilistic Algorithm for Testing Primality" (1980, J. Number Theory) — `paywalled` (widely taught/mirrored)
5. "Probabilistic Automata" (1963, Information and Control) — `paywalled`
6. "Randomized Byzantine Generals" (1983, FOCS) — `uncertain`

Fewer than 10 works clearly central to this subdomain specifically (several are automata theory or cryptography adjacent).

## Phase 3 access flag
Verified 2026-07-24. Two works resolved public after re-fetching: #1 ("Finite
Automata and Their Decision Problems," 1959) is not actually available from
IBM or from Internet Archive's scan of IBM J. Res. Dev. 3(2) — that scan is
`access-restricted-item: true` (controlled digital lending, not free) — but a
third-party academic mirror (Chalmers University, cse.chalmers.se) hosts a
directly downloadable copy. #3 ("Digitalized Signatures...," MIT/LCS/TR-212,
1979) is public via bitsavers.org (MIT's own DSpace listing exists but its
bitstream endpoint only serves a JS interstitial, not a fetchable file).

The two works most central to the "why a candidate" case — Miller-Rabin
primality and Rabin-Karp string search, the two examples named directly in
that section above — are genuinely unavailable from any public source
checked: #2 "Efficient Randomized Pattern-Matching Algorithms" (Karp & Rabin,
1987, IBM J. Res. Dev.) and #4 "Probabilistic Algorithm for Testing
Primality" (1980, J. Number Theory). Checked: publisher pages (both return
403/require subscription), Unpaywall (both `oa_status: closed`, no repository
copy), Semantic Scholar (`openAccessPdf` closed/empty), Google Scholar's
Rabin profile (no PDF links attached to either entry), and Rabin's own
Harvard homepage (people.seas.harvard.edu/~rabin/, live and via Wayback —
directory has no index/publications listing, only a CV PDF). No self-archived,
institutional, or legitimate third-party-rehost copy of either paper turned
up anywhere. Both are excluded from `works/`.

Also excluded, checked with the same rigor but not central to the
why-candidate case specifically: #5 "Probabilistic Automata" (1963,
Information and Control) — Unpaywall `closed`, no OA copy found anywhere —
and #6 "Randomized Byzantine Generals" (1983, FOCS) — Semantic Scholar
`openAccessPdf.status: CLOSED`, Unpaywall `closed`, no self-archived or
rehosted copy found. Both were `paywalled`/`uncertain` in the Phase 1 pass;
that resolves to genuinely unavailable, not just unchecked.

## Lessons

Rabin's two available works teach one continuous habit of mind: decide in
advance which claims you intend to be able to establish, then choose the
weakest, smallest construct that lets you establish them, even when that
construct is less general or less tidy than the obvious alternative. In the
automata work this shows up as deliberate self-limitation — bound the state
space and infinite verification obligations collapse into finite searches;
characterize a task by the distinctions its own inputs force rather than by
any machine that handles it, and impossibility proofs plus the minimal
implementation fall out together; add a capability and audit what you just
lost, since composability of specifications breaks before decidability does.
It also supplies the separation between a convenient branching description
and the single-path device a mechanical translation derives from it, which is
the general licence to write in the form that reasons well and generate the
form that runs well. In the cryptography work the same reflex points at
guarantees: build on the operation whose inversion is already interchangeable
with a known-hard problem so that "secure" becomes derivable rather than
merely unrefuted; state the guarantee with a quantifier that survives an
opponent choosing inputs, since a small easy minority is all anyone needs;
and use randomness twice over, once to replace intricate construction with a
cheap guess-and-check loop carrying a proven per-attempt probability, and
once to strip an adversary of the ability to aim a privileged operation. The
through-line is that analyzability is a design input, not a property
discovered afterward — and that paying for it in generality, elegance, or
interface neatness is usually the cheapest currency available.
