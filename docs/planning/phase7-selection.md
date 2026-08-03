---
type: record
title: Phase 7 Selection Record
description: How the 80 candidate claims for DISTILLED.md were selected, and the 54 that were struck. The kill list is the more useful half. Run 2026-08-02.
tags: [phase7, distillation, okf]
---

# Phase 7 — Selection Record

DISTILLED.md holds 26 claims, chosen from 80 candidates by a process built to
keep my own reading bias out of it — the obvious failure mode being to write the
document from whatever I happened to have read most recently.

**Nomination.** Ten agents, one per subdomain plus one harvesting the 21 resolved
tensions, each capped at 8 candidates and told they were competing for ~20 slots.
Working per-subdomain rather than from recall means no region of the corpus goes
unread. The tension harvester was told to discard the tension framing and keep
only the switching conditions, since a rule with a stated condition changes
behaviour where a bare imperative gets skimmed past.

**Striking.** Three reviewers judged all 80 independently, with no stake in any of
them, against one primary test: *if this line were absent, would a good agent
behave differently?* Nominators' own arguments for why their claim was not a
default were passed along explicitly marked as advocacy rather than evidence.
Survival required 2 of 3 keep votes.

**Result: 54 struck or merged, 26 kept (67% killed).** 16 were unanimous. A pass
that killed little would have meant the reviewers were not working.

## Independent convergence, which is the strongest quality signal here

All three reviewers independently reported heavy duplication *across* slices.
Lampson's one-authoritative-representation rule was nominated three times, the
Torvalds stability boundary twice, buffer-absorbs-variance two to three times, and
timeout-is-not-evidence three times — each by agents working different subdomains
who could not see each other's nominations.

That convergence is worth more than any single nominator's argument. A claim that
surfaces independently from distributed systems, from operating systems, and from
databases is load-bearing rather than an artifact of one slice's reading. The
duplicates were merged, so the count understates how much of the corpus points at
those particular claims.

## What got struck, in the reviewers' own words

The recurring strike categories were consistent across all three: restatements of
"make illegal states unrepresentable", "parse don't validate", "validate at
boundaries", exhaustive matching, and avoiding reflection — all judged things a
competent agent already does. The second category was specialist material that
only bites in contexts most codebases never enter: query optimizer internals,
amortized-bound analysis, CAP-per-invariant reasoning. One reviewer noted that
several nominators "padded abstractions with vivid examples", which is worth
watching for on any re-run.

## A criterion that should never have existed

The strike prompt listed, among grounds for killing a claim:

> *It only bites in a specialist context most codebases never enter.*

That is self-defeating for this project. The corpus exists because most code is
bad; "most codebases never do this" is therefore evidence FOR a claim, not against
it. Worse, it compounds with the primary test into a pincer — strike what agents
already do (redundant) AND strike what codebases mostly don't do (specialist) —
which only admits claims in a narrow band around current median practice. That is
precisely the band the whole project was built to escape.

Measured damage: of 54 killed candidates, 17 carry at least one prevalence-based
strike and in 11 it was decisive. The figures it hit are the tell — Sussman three
times, Vardi twice, then Gödel, Rabin, Curry, Kleene, Scott, Church, Tarjan, Karp,
Edmonds, Ullman. A filter calibrated on median practice selectively eats the
foundational material, which is the opposite of what this corpus is for.

**The criterion is deleted. It must not appear in any future strike prompt.**

The distinction that survives, and the one to use instead, is TRANSFERABILITY
rather than PREVALENCE. A claim must be applicable outside its home domain — it
must survive translation into an ordinary service in a mainstream language. It does
not have to be something people currently do. Gödel on the limits of what can be
decided automatically transfers perfectly well despite almost nobody reasoning that
way; "amortized bounds matter for p99" transfers; "here is how a query planner
represents a join tree" does not, and that is a claim about applicability, not
popularity.

The primary test — would a competent agent already do this by default — survives,
because a document that tells an agent to do what it already does changes nothing.
It is a claim about the reader's behaviour rather than about what is fashionable.

Nathan caught this. It is the most consequential process error in Phase 7.

## Why the kill list is the useful half

Everything below was nominated by an agent that had read the source and believed
it was contributing something non-obvious. Most were struck as things a competent
coding agent already does. That makes this a record of what turns out to be
commonplace, which is exactly the material that would quietly bloat this document
on any future re-run.

## A correction worth recording

The first version of DISTILLED.md was built on a stale tally. I read the three
verdict files while the workflow was still running, treated them as final, and
published 23 survivors. Reviewer 3 subsequently rewrote its file, and the correct
tally is 26 survivors — six claims added, three removed. The standing rule on this
project is to diagnose from disk rather than from a workflow's return value, and
the corollary I missed is that disk is only authoritative once the writer has
finished. A completion signal was available and I did not wait for it.

---

## Struck or merged


**[1] sussman** (0/3 keep)

  A wrapper covers only the calls routed through it — Sussman: memoizing,
  retrying, tracing, or rate-limiting a function catches the outermost call
  while the function's internal self-calls go around it, so trace one call to
  the bottom and confirm the wrapper is on the recursive path, or route inner
  calls through the same indirection.

    - strike: Narrow decorator gotcha; agents already reason about where a
    - wrapper sits relative to the call it wraps.
    - merge: Merges into 42: both say an interposition point is worthless
    - while a path around it survives.
    - strike: Narrow language trivia; in the common case the decorated name
    - already captures recursive calls, and agents trace call paths anyway.

**[2] tarjan** (0/3 keep)

  Tarjan: a component's guarantee class is part of its contract, not a
  footnote — an amortized part can only hold up an amortized whole, so a
  rehashing hash map, an amortized allocator, or a bursty rate limiter is an
  illegal substitution under a tail-latency or hard-deadline obligation even
  when the interface, the tests, and the big-O all match.

    - strike: Only bites under hard deadlines or strict p99 budgets, a context
    - most codebases never enter.
    - strike: Only bites under hard deadlines or strict tail-latency budgets;
    - most codebases never enter that context.
    - strike: Only bites under hard-deadline or p99 obligations most codebases
    - never state; specialist context.

**[3] tarjan** (0/3 keep)

  Tarjan: do not simplify a rule that was tuned against an accounting argument
  — eviction policy, backoff schedule, rebalancing trigger, preemption choice,
  retry heuristic — because two nearly identical rules can differ by an order
  of magnitude, and the sequences that separate a good rule from a fatal one
  are adversarial and will not be in your benchmark; redo the argument or
  leave the rule alone.

    - merge: Merges into 35: same rule, do not tidy code whose reason you
    - cannot re-derive.
    - merge: Merges into 35: same behaviour change, do not tidy code whose odd
    - shape encodes a reason you cannot see.
    - merge: Merges into 35: same instruction, leave oddly-shaped code with a
    - reason alone and record the reason.

**[4] denning/corbato** (0/3 keep)

  Denning: "more of the scarce resource can only help" is a structural
  property some designs have and others lack, not a law — before enlarging a
  cache, pool, batch, timeout, or replica set, name the containment or
  ordering property that makes the improvement monotone, because plausible
  policies fault more with more memory.

    - merge: Merges into 22: both refuse the reflexive knob-raise as the fix
    - for a capacity problem.
    - merge: Merges into 36: both stop the reflex of enlarging the knob
    - instead of fixing the mismatch.
    - merge: Merges into 22: raising the knob does not fix a structural rate
    - or policy mismatch.

**[5] sussman** (1/3 keep)

  Sussman: repetition buys confidence only against independent failures, so
  before choosing a retry count, resample, or redundant check, say what rules
  out the case where every attempt fails the same way — correlated failure is
  usually a property of the input, which makes it invisible in every trial you
  run.

    - keep: Retry-with-backoff is a top reflex; demanding an independence
    - argument before adding attempts changes real code.
    - merge: Merges into 39: both constrain reflexive retry by demanding a
    - bound and an argument before more attempts.
    - merge: Merges into 18: retry and timeout discipline belongs in one claim
    - about what repetition and expiry buy.

**[6] karp/edmonds** (0/3 keep)

  Karp and Edmonds: every place your design says "any" — which candidate the
  loop takes first, which of several valid plans the optimizer emits, what
  breaks a tie, what order a queue drains — is a family of algorithms whose
  worst member you will eventually get, so pin the rule and write down what it
  buys before someone reorders the loop for tidiness.

    - strike: Deterministic iteration order and explicit tie-breaks are
    - already default practice for competent agents.
    - strike: Agents already sort explicitly when order matters; pinning every
    - tie-break rarely changes a diff.
    - strike: Too abstract to act on; agents already pin sort keys and tie-
    - breaks when output determinism matters.

**[7] church/sussman** (0/3 keep)

  Church and Sussman: price the guard, not just the fast path — a special-case
  branch runs its test on every execution including the ones it does not help,
  so a fast path is real only if its entry test is strictly cheaper than what
  it skips, and when special cases start accumulating the classification wants
  to move earlier (decide once, reuse the decision) rather than becoming
  another runtime test.

    - strike: Covered by default perf discipline: measure the check's cost
    - before adding a fast path.
    - strike: Agents do not add speculative fast paths; avoiding premature
    - optimisation is already the default.
    - strike: Covered by the default measure-before-optimizing habit; agents
    - already benchmark a guard against the real workload.

**[12] ullman** (0/3 keep)

  Any state that cannot detect its own staleness needs a named periodic
  recomputation, not just invalidation: ask 'what would have to be true for me
  to notice this is wrong?' and if the answer is nothing, schedule the full
  rebuild and state its period (Ullman).

    - merge: Merges into 61: the rebuild path plus its schedule is one
    - derived-state obligation.
    - merge: Merges into 61: scheduled reconciliation is the rebuild path 61
    - already demands ship with derived state.
    - merge: Merges into 61: derived state ships with a rebuild path; the
    - scheduled sweep is that rule applied.

**[13] ullman** (0/3 keep)

  An optimizer can only exploit laws you gave it in advance, so treat every
  user-defined function, plugin point, and custom aggregate as an optimization
  barrier that will run exactly as written (Ullman).

    - strike: Database optimizer trivia, not transferable thinking for most
    - codebases.
    - strike: Query-optimizer trivia; only bites when writing UDFs against an
    - engine that could otherwise rewrite.
    - strike: Query-engine trivia; barely transfers outside planners and
    - rarely decides anything in ordinary application code.

**[14] vardi** (0/3 keep)

  Before anything resolves conflicts automatically, write down an explicit
  ranking of what may be sacrificed — integrity rules above stored facts above
  derived summaries — because minimality over a flat set will always drop
  whichever invariant is cheapest, not the most incidental (Vardi).

    - strike: Specialist to automatic conflict-repair systems; most code never
    - ranks invariants.
    - strike: Automatic conflict repair is a specialist context, and ranking
    - invariants is too abstract to apply unprompted.
    - strike: Abstract and rarely live; most merge and ON CONFLICT paths have
    - no ladder worth declaring.

**[15] fagin** (0/3 keep)

  Ask whether misuse of your API, schema, or protocol is impossible or merely
  discouraged — 'a good way exists' obliges you to build and maintain the
  guide forever, while 'no legal use is wrong' deletes that machinery outright
  (Fagin).

    - merge: Merges into 70: tighten or delete the structure rather than
    - shipping guidance around a permissive one.
    - strike: Restates 'make illegal states unrepresentable', a maxim agents
    - already reach for by default.
    - strike: Design APIs that are hard to misuse is already a default agent
    - principle, phrasing aside.

**[16] wirth** (0/3 keep)

  Moving durable state into volatile store is a correctness change, not an
  optimization — score it by what the persistent structure looks like if power
  is lost at an arbitrary instant, and record declined optimizations with
  their reasons so the next person doesn't re-implement them (Wirth).

    - merge: Merges into 61: a write-back cache over durable state is the
    - derived-state-needs-a-rebuild-path case.
    - merge: Merges into 10: same rule that durability of state may not be
    - traded for speed silently.
    - merge: Merges into 10: both govern the gap between what is durable and
    - what the system exposes or trusts.

**[20] lampson** (1/3 keep)

  Give every cached or derived fact an expiry rather than an invalidation list
  (Lampson): tracking who holds a copy so you can notify them inverts the
  dependency and cannot be made to work under failure — make withdrawal a
  refusal to renew, and every copy becomes freely discardable.

    - keep: Invalidation fanout is what agents build; leases with renewal is a
    - different, more survivable design.
    - strike: TTL-plus-renewal is already the agent default for caches;
    - invalidation registries are the rarer choice.
    - merge: Merges into 61: leases are the disposable-derived-state rule
    - applied to cache coherence.

**[21] jones/sussman** (0/3 keep)

  Make shared state move in one direction and order stops mattering (Jones,
  Sussman): if updates only ever add information, stale reads are merely
  conservative, duplicate delivery is harmless, and no schedule is needed — so
  treat each operation that removes information as a global barrier and look
  first for a formulation that expresses it as an addition.

    - strike: Too abstract to apply, you must already know the monotone
    - reformulation for the advice to help.
    - strike: Too abstract to apply without already knowing the monotone
    - formulation; append-only is a common suggestion anyway.
    - merge: Merges into 23: answer contention by changing the data shape, not
    - by adding synchronization.

**[24] lamport** (1/3 keep)

  Reason about concurrent code with an invariant, never by tracing
  interleavings (Lamport): 'I walked through the orderings' is not evidence,
  because you sample the few a human imagines — state the predicate that must
  always hold and check that every atomic step of every participant preserves
  it, including steps taken by others.

    - merge: Merges into 80, which states the same invariant discipline as a
    - concrete rule about the observable window.
    - keep: Replaces the plausible three-case interleaving walkthrough agents
    - actually produce with a per-variable invariant check.
    - merge: Merges into 80, which states the same discipline as a concrete
    - rule about yield points inside the invariant window.

**[25] godel/rabin** (0/3 keep)

  Judge a new construct by what it can encode in combination with everything
  already present, not by its own power (Gödel): tractability is lost to
  feature interaction, never to one feature, so before adding interpolation to
  a config format, recursion to a query language, or a hook to a template
  engine, ask whether the combination can now simulate unbounded search.

    - strike: Abstract DSL-design concern; 'can it now simulate unbounded
    - search' is unanswerable in practice.
    - strike: Decidability-at-feature-interaction only bites in DSL and
    - config-language design; too abstract elsewhere.
    - strike: Specialist DSL and language-design concern; most codebases never
    - make the decision it governs.

**[26] turing/schonfinkel** (0/3 keep)

  Before accepting a design that is correct 'given X', price X as seriously as
  runtime cost (Turing): a guarantee whose precondition is as hard as the
  original problem has relocated the work, not removed it — prefer the weaker
  guarantee with the tractable obligation.

    - strike: Too abstract; offers no test for when a precondition is as hard
    - as the problem.
    - strike: Too abstract; no concrete decision flips that 61's rebuild-path
    - rule does not already cover.
    - strike: Too abstract to apply without already knowing whether the
    - precondition is hard; supplies no test.

**[27] curry/kleene/scott** (0/3 keep)

  Separate the layer that builds things from the layer that approves them
  (Curry): make representations total and validity a queryable predicate,
  because a constructor that throws destroys the evidence — anything you make
  unrepresentable you also make undiagnosable when it shows up in production
  anyway.

    - strike: Specialist parser architecture; agents already collect multiple
    - validation errors when it matters.
    - strike: Collecting all parse or validation errors rather than raising on
    - the first is already standard practice.
    - merge: Merges into 79: widen the result type and carry the defect
    - instead of throwing at the first bad element.

**[28] church** (0/3 keep)

  Price each newly supported configuration as a subtraction, not an addition
  (Church): what shared code may assume is the intersection over every
  platform, backend, version and tenant you claim to support, so name the
  assumption the core just lost — if you cannot name one, the configuration is
  redundant or you have not looked.

    - strike: Support-matrix accounting is a rare decision and the claim gives
    - no concrete test.
    - strike: Support-matrix accounting is unactionable in a coding session;
    - the cost never lands in any diff.
    - strike: Unfalsifiable in the moment; naming the lost assumption rarely
    - changes whether a supported backend is accepted.

**[29] church** (0/3 keep)

  State a limitation in exactly one clause so that generalizing later is a
  deletion rather than a rewrite (Church): whether a restriction is cheap to
  revisit is decided when you impose it, and the same restriction inlined at
  forty sites is a permanent decision you did not notice making.

    - strike: 'Define the constant once and reference it' is ordinary DRY,
    - already default.
    - strike: Naming a shared assumption once instead of inlining it forty
    - times is default DRY behaviour.
    - strike: Extracting a named constant or single clause instead of inlining
    - an assumption is already default DRY practice.

**[30] sussman/turing** (0/3 keep)

  Treat any form-inspecting capability as a boundary that revokes substitution
  of equals (Sussman): reflection, macros, name-keyed registries, source-
  printing decorators and AST matchers make refactors that are unconditionally
  safe elsewhere — inline the constant, hoist the subexpression, rename — into
  claims requiring separate proof inside their reach.

    - strike: Narrow metaprogramming case; grep-for-string-references before
    - renaming is already default.
    - strike: Agents already prefer explicit registries and enums over getattr
    - or class-name string dispatch.
    - strike: Preferring explicit tokens over reflection and class-name
    - dispatch is already default agent advice.

**[32] vardi/fagin** (0/3 keep)

  Separate 'is this request meaningful' from 'is the outcome unique' and 'can
  my state language express it' (Vardi): several equally good answers is
  information about your knowledge, not a caller error, so record what all the
  acceptable outcomes agree on instead of rejecting.

    - strike: Narrow resolver-design case; most ambiguity really is a caller
    - error worth rejecting.
    - strike: Narrow to resolvers and matchers, and rejecting ambiguity is
    - frequently the right call anyway.
    - merge: Merges into 79: several acceptable answers is another case for a
    - wider return type rather than an exception.

**[33] lampson/torvalds/wirth** (0/3 keep)

  Designate exactly one representation as authoritative and optimize it for
  being checkable, not fast; every index, cache, or derived structure is a
  guess that must be verifiable before anything irreversible depends on it
  (Lampson).

    - merge: Merges into 61, which is the same Lampson claim stated with the
    - rebuild-function action.
    - merge: Merges into 61: same Lampson claim, and 61 states the concrete
    - rebuild-in-the-same-change action.
    - merge: Merges into 61, the same Lampson claim stated with the concrete
    - rebuild-function requirement.

**[34] torvalds/cutler** (0/3 keep)

  Spend all your stability at one boundary: freeze only what outsiders
  observe, reshape everything behind it freely, and make whoever changes an
  internal interface fix every caller in the same commit (Torvalds).

    - merge: Merges into 64, the same Torvalds one-boundary claim with the
    - same call-site action.
    - merge: Merges into 64: duplicate claim, and 64 names the concrete
    - commit-shape action.
    - merge: Merges into 64, the same Torvalds claim stated with the concrete
    - no-shim call-site rule.

**[36] hoare/wirth** (1/3 keep)

  A buffer or queue absorbs variance, never a rate deficit; one that keeps
  needing to be enlarged is a measurement telling you the two sides do not
  match, and the fix is on one of the sides (Hoare, Wirth).

    - merge: Merges into 22, which states the same buffer claim plus the per-
    - stream backpressure remedy.
    - keep: Blocks the universal reflex of raising queue depth or worker count
    - instead of matching rates or shedding load.
    - merge: Merges into 22, which carries the same buffer claim plus the per-
    - stream backpressure remedy.

**[37] torvalds** (0/3 keep)

  Move every check to where it costs nothing — types, compile time, startup —
  and become conservative as you move rightward: at run time prefer to report
  and limp, because aborting spends stakes you cannot see (Torvalds).

    - strike: Kernel-specific jurisdiction argument that contradicts fail-
    - fast, wrong general advice for application code.
    - strike: Context-dependent and contrarian; moving checks to compile time
    - is default, and limp-versus-abort is a product judgement.
    - strike: Half is the default move-checks-earlier habit; the limp-instead-
    - of-abort half is kernel-specific and contradicts fail-fast.

**[38] brooks/hoare** (1/3 keep)

  State what you do not guarantee as precisely as what you do, and make the
  code reject it, because a running system always answers and whatever it
  answers becomes the contract (Brooks, Hoare).

    - merge: Merges into 51: both stop accidental behaviour from becoming a
    - contract.
    - keep: Agents coerce and fall back by default; rejecting inputs the spec
    - is silent about is a real behaviour flip.
    - strike: Validate at boundaries and reject undefined input is a stated
    - default; agents already refuse malformed input.

**[39] hoare** (1/3 keep)

  Hidden work that can run unboundedly is indistinguishable from being hung,
  so hiding obliges you to bound it and to expose something that separates
  busy from stuck (Hoare).

    - strike: Bounded retries with a max attempt count are already default;
    - the progress signal is marginal.
    - keep: Forces a bound on hidden retry or background work plus a progress
    - signal, instead of opaque exponential backoff.
    - merge: Merges into 52: hidden retries and background work are cost and
    - failure the interface must not conceal.

**[40] liskov/dijkstra** (0/3 keep)

  Never let a timing guess be load-bearing for correctness — a timeout is a
  hint that something may be wrong, never evidence that it is, so any action
  taken on one must be survivable if taken wrongly (Liskov, Dijkstra).

    - merge: Merges into 18, the stronger statement of the same timeout-is-
    - not-evidence rule.
    - merge: Merges into 18: same timeout-is-not-evidence claim, stated less
    - concretely.
    - merge: Merges into 18, the same timing-versus-safety claim with the
    - stronger fencing and evidence requirement.

**[41] reenskaug** (0/3 keep)

  To understand unfamiliar code, reconstruct the runtime collaboration — who
  holds a reference to whom and what they send — before reading the type
  hierarchy, which records where implementation was shared and says nothing
  about how the thing works (Reenskaug).

    - strike: Agents already orient by tracing call paths from entry points
    - rather than summarizing class trees.
    - strike: Agents already orient by grepping call sites and tracing entry
    - points, not by reading class hierarchies.
    - strike: Agents already orient by grepping entry points and tracing call
    - paths, not by summarizing class hierarchies.

**[42] ungar** (1/3 keep)

  When you add an accessor, wrapper, cache layer, or handle, remove the direct
  path in the same change — an abstraction is worth exactly its weakest
  bypass, and any caller left on the old route is immune to every later
  refinement (Ungar).

    - merge: Merges into 64: delete the old path and fix every caller in the
    - same change.
    - keep: Converts additive non-breaking habit into migrate-or-do-not-
    - introduce; agents ship the accessor and leave direct access alive.
    - merge: Merges into 64: do not leave the old path alive when you
    - introduce the new one.

**[44] sussman** (0/3 keep)

  Before introducing a class, write down the state the feature actually needs
  and check whether it clusters — the object decomposition is earned only when
  state variables form groups that interact constantly inside and rarely
  across (Sussman, SICP).

    - merge: Merges into 31: both make the abstraction earn its existence
    - before it is introduced.
    - strike: The state-clustering test needs the answer before it can be
    - applied; preferring functions to stateful classes is already advised.
    - strike: Preferring functions over a stateful class for uncoupled state
    - is already a default agent inclination.

**[46] reenskaug** (0/3 keep)

  Where correctness needs a per-item judgement over an enumerable set — every
  field in a copy or serializer, every variant in a match — write the default
  case out explicitly and add a mechanical check that every item is mentioned,
  because silence makes an oversight indistinguishable from a decision
  (Reenskaug).

    - strike: Exhaustive matching and no-catch-all switches are already
    - default practice in typed code.
    - strike: Type checkers already enforce exhaustive matches, and agents
    - write per-field code rather than catch-alls.
    - strike: Exhaustive matches and lint-enforced case coverage are already
    - default; agents reach for them unprompted.

**[47] sutherland/ingalls** (0/3 keep)

  Build the slow method that handles every input before the fast one that
  handles the analyzable subset, and make 'the fast path did not apply' an
  ordinary measured outcome rather than an error (Sutherland; Ingalls: guard
  the frequent case and fall through).

    - strike: Prescribes building two implementations up front; speculative
    - work for a niche class of solvers.
    - strike: Agents already implement the general case first; analyzable-
    - subset-only solvers are rare in ordinary code.
    - strike: Build-order rule that bites mainly in solvers, planners and
    - optimizers, a context most codebases never enter.

**[48] chuck-moore/sutherland** (0/3 keep)

  Before writing code that recovers information a format threw away — parsers,
  normalizers, intent heuristics — check whether you control the format, and
  store the structure that produced an artifact rather than its flattened
  appearance (Chuck Moore, Sutherland).

    - merge: Merges into 57: fix the representation instead of writing the
    - procedure that copes with it.
    - merge: Merges into 57: both say fix the representation rather than build
    - machinery around it.
    - merge: Merges into 57: fix the representation rather than writing more
    - code to cope with it.

**[50] steele** (0/3 keep)

  Spend specification effort inversely to what the runtime checks: unchecked
  paths — raw casts, manual lifetimes, lock-free structures, anything marked
  unsafe — get a written-out contract and adversarial near-miss examples,
  while self-checking APIs get one line.

    - strike: Documentation-budget advice for unsafe blocks, a surface most
    - codebases barely have.
    - strike: Documentation-budget guidance; reallocating prose changes no
    - code and most codebases have few unchecked paths.
    - strike: Affects only documentation prose; document dangerous code
    - carefully is close enough to a default to change nothing.

**[53] hoare/liskov** (0/3 keep)

  Put an operation on a type only when implementing it efficiently requires
  the internal representation; anything a caller can compose from what exists
  at no penalty stays outside it.

    - strike: Interface-size taste; the cost criterion rarely flips a real
    - decision.
    - strike: Low-stakes placement question; keeping helpers out of classes
    - unless they need internals is close to default.
    - strike: Free function versus method is low-stakes style; agents already
    - resist bolting helpers onto unrelated classes.

**[54] sussman/landin** (0/3 keep)

  Before adding an accessor, equality, hash, or iterator to an existing type,
  enumerate which distinctions it newly makes observable — code written under
  the old equivalence is now wrong without anyone having edited it.

    - strike: Narrow; the observability-of-equality hazard almost never bites
    - practical code.
    - strike: Equivalence-widening from a new accessor or hash is a specialist
    - concern that rarely bites in practice.
    - strike: Subtle observability-of-equivalence concern that almost never
    - decides a real change; too specialist for twenty slots.

**[55] jones/hoare** (0/3 keep)

  A refactor justified by same-input-same-output is unsound anywhere else can
  write the same state — read the fragment with an adversarial write spliced
  into every gap, including before its first step and after its last, before
  hoisting or merging a read.

    - merge: Merges into 80: same window-of-observation analysis applied to
    - refactors.
    - merge: Merges into 80: both forbid moving reads or writes across a point
    - where another party can observe or interfere.
    - merge: Merges into 80: both forbid treating a window in shared-state
    - code as if nothing else can run.

**[56] sussman** (1/3 keep)

  If a conditional's arms grow with the number of call sites rather than with
  the problem, the caller should be handing over the behavior itself instead
  of a token to be interpreted.

    - strike: 'Replace a growing switch with polymorphism or a callback' is
    - textbook default advice.
    - strike: Replace-conditional-with-strategy is a textbook refactoring
    - agents already know and apply.
    - keep: Growth-rate diagnostic is concrete and non-default; agents append
    - another enum arm without noticing the inverted dependency.

**[59] parnas/liskov** (0/3 keep)

  Parnas: a guarantee that is true but unnecessary is a design error — publish
  only the properties clients actually need, because every incidental fact you
  state (ordering, error text, that the result is sorted) becomes a promise
  you can never revise.

    - merge: Merges into 51, the more concrete statement including the test-
    - assertion consequence.
    - merge: Merges into 51: same do-not-promise-incidental-facts claim, and
    - 51 also covers the test suite.
    - merge: Merges into 51, the same do-not-promise-incidentals rule with a
    - concrete test-suite consequence.

**[60] torvalds** (1/3 keep)

  Torvalds: an abstraction may hide data, never control flow — anything that
  looks like a call must return to the next statement, so no macro, decorator,
  or wrapper that swallows exceptions, jumps out, or silently retries.

    - strike: 'Do not swallow exceptions in a wrapper' is already default; the
    - rest is style.
    - keep: Blocks the exception-swallowing decorator or context manager
    - agents produce when asked to DRY error handling.
    - merge: Merges into 52: a decorator that swallows an exception is hiding
    - failure, which 52 already forbids.

**[65] brooks/kay** (0/3 keep)

  Before proposing to shrink or rewrite a large subsystem, estimate what
  fraction of it exists only to satisfy formats, protocols, or APIs fixed by
  people outside the project: where that fraction is low the size is an open
  question and a smaller formulation is worth funding, where it is high the
  bulk is other people's decisions on other people's revision schedule and the
  correct response is to layer and confine rather than to compress
  (Brooks/Kay).

    - strike: Rare rewrite-scale decision requiring judgement the reader would
    - already need to have.
    - strike: Rewrite-scope estimation is a rare decision and the conformity
    - fraction is unmeasurable in practice.
    - strike: Estimating a conformity fraction is unfalsifiable in practice
    - and rarely the decision actually in front of the agent.

**[66] codd/bachman/ullman** (0/3 keep)

  Treat an index, cache, denormalized read model, or projection as legitimate
  exactly when it is recomputable from the authoritative data, discardable
  without loss, and maintained by the engine rather than by application code;
  when the application maintains it, its derivation rule and staleness bound
  belong in the schema as first-class, and where the structure you are
  choosing is itself the bottom (wire format, shard key, on-disk record,
  directory layout) there is no level below to re-derive from and expected
  access rightly governs the design (Codd/Bachman/Ullman).

    - merge: Merges into 61: recomputable, discardable derived state with a
    - stated rebuild path.
    - merge: Merges into 61: same recomputable-derived-data rule with extra
    - database-specific detail.
    - merge: Merges into 61, which carries the same recomputable-and-
    - discardable rule for derived state.

**[67] wirth/kay** (0/3 keep)

  Decide static enforcement per boundary, not per codebase: where every
  participant is compiled in one build, enforce declarations and collect the
  payoff, which is the exhaustive list of affected call sites when you change
  something; at plugin boundaries, peers running an older version, and
  anywhere you read data somebody else wrote, the participant set is open,
  exhaustive checking has no moment at which it could run, and that boundary
  must validate and negotiate at runtime no matter what the type signature
  claims (Wirth/Kay).

    - strike: Validating parses at deserialization boundaries instead of
    - trusting casts is already default.
    - strike: Validating parse at deserialization boundaries is already
    - default; agents reach for schema validators unprompted.
    - strike: Validating parse at deserialization boundaries is the stated
    - default; agents already distrust external data.

**[68] jones** (0/3 keep)

  Before deleting state that no current operation can observe, ask whether any
  operation the subject matter admits could observe it, not whether any
  operation on today's interface does: ordering in a set modelled as a list is
  notation residue and goes unconditionally, but a queue's removed elements
  are a fact about queues that a peek, audit, replay, or undo would expose,
  and collapsing that queue to a counter is not removing residue, it is
  deciding queues are counters (Jones).

    - strike: Needs domain judgement the rule cannot supply; too abstract to
    - change a deletion decision.
    - strike: Requires already knowing the domain answer to apply, and mostly
    - licenses keeping unused state.
    - strike: Too abstract to apply without already knowing the domain model;
    - rarely the live decision in a simplification pass.

**[69] hoare/wirth** (0/3 keep)

  One name may cover two realizations only when exactly one of them is live in
  any given running program and it was chosen once, at deployment; when both
  are live and selected per call site — local versus remote, cached versus
  fetched, in-process versus queued — the merged interface deletes exactly the
  information each caller needs to be written correctly, so give them separate
  names and move anything the caller must actually handle into the shared
  description (Hoare/Wirth).

    - merge: Merges into 52: do not put local and remote behind one name that
    - hides the cost.
    - merge: Merges into 52: same rule that a call hiding a network or cost
    - difference needs its own name.
    - merge: Merges into 52: a name that hides whether the call crosses the
    - network is hiding cost.

**[70] hoare** (1/3 keep)

  When a design question has no principled answer, attempt deletion before
  adding a configuration option: restate every legitimate need in the
  vocabulary that remains after the concept is removed, and only if one
  refuses to translate does somebody own the distinction and earn a small,
  enumerable menu — deletion is the cheap move whose failure is loud and
  immediate, while every declared option is a permanent obligation on
  everything that reasons about the interface thereafter (Hoare).

    - keep: Reverses the ordering agents use, treating deletion of the
    - distinction as the first move rather than a new flag.
    - merge: Merges into 45: both refuse the new config knob and attack the
    - underlying need first.
    - merge: Merges into 45: try deleting the distinction before adding a
    - knob, hook or option.

**[71] ritchie/lampson** (0/3 keep)

  The evidence that a codebase is missing a primitive is the shape of what
  people built instead — file-based locks, hand-rolled retry loops, the same
  encoding open-coded at forty call sites — not a filed complaint or a feature
  request, because an expensive composition silently produces coarse-grained
  programs and generates no bug report; publish the price of the workaround
  you are asking callers to accept, then read the resulting program shapes as
  the measurement (Ritchie/Lampson).

    - strike: Abstract; 'extract a helper' vs 'reprice the substrate' is not
    - adjudicable from the rule as stated.
    - strike: Applies only to platform or library work, and it pushes an agent
    - toward adding foundation primitives.
    - merge: Merges into 45: repeated workarounds and extension requests are
    - the same evidence that a primitive is priced wrong.

**[72] brewer/lamport/lynch** (0/3 keep)

  Under partition, decide by whether the system can restore the violated
  invariant later using only state it owns: unilaterally repairable invariants
  stall or reconcile and no replica may commit a value the reconciliation
  cannot undo, while an invariant whose repair needs an outside party's
  consent cannot be preserved by local restraint at all, so spend the design
  there on logging each risked operation with the invariant it risked,
  bounding the exposure window, and stating a reconciliation deadline
  (Brewer/Lamport/Lynch).

    - strike: Specialist partition-design content most codebases never touch.
    - strike: Per-invariant partition analysis is specialist distributed-
    - systems work; the safety core is already in 18.
    - strike: Per-invariant partition analysis only bites for teams writing
    - replication; most codebases never enter that context.

**[73] dijkstra/lamport/jones** (0/3 keep)

  Write the postcondition and the loop invariant before the loop body, then
  let each statement's required starting condition become its guard —
  Dijkstra's derivation and Lamport's rule that the proof precedes the code.

    - merge: Merges into 80: invariant-first reasoning, stated there with a
    - concrete window rule.
    - strike: Formal loop-invariant derivation is ritual for ordinary code;
    - agents already state intent and tests before writing.
    - strike: Rigor exhortation about construction order, hard to verify it
    - happened, and largely subsumed by 74 and 80.

**[75] lamport/lynch/liskov/hoare** (0/3 keep)

  Sort every requirement into safety (nothing bad happens) and liveness
  (something good eventually happens) as Lamport insists, let timing
  assumptions buy progress and never correctness (Lynch, Liskov), and replace
  every 'eventually' with a numeric bound something actually keeps score of
  (Hoare).

    - merge: Merges into 18, which states the safety-versus-liveness split
    - with the fencing mechanism.
    - merge: Merges into 18: the timing-buys-progress-not-safety asymmetry is
    - 18's core, stated there more concretely.
    - merge: Merges into 18, the same safety-versus-liveness asymmetry with
    - concrete fencing and evidence requirements.

**[77] hoare/sifakis/church/corbato** (1/3 keep)

  When a question keeps producing arbitrary answers, remove the ability to ask
  it rather than answering it carefully — Hoare drops wall-clock time and
  keeps only event order — and turn any property you keep re-checking into a
  rule about how parts may be combined (Sifakis).

    - keep: Truncated scans returned as clean results is a real silent bug; a
    - third outcome plus witness is a type-level fix.
    - strike: Restates 'make illegal states unrepresentable', which agents
    - already invoke by default.
    - strike: Make illegal states unrepresentable is already a default agent
    - move; the deletion half lives in 45 and 70.

**[78] church/steele/mcmillan** (0/3 keep)

  A discipline plus an escape hatch used wherever the discipline bites is
  strictly worse than either extreme, Church's verdict on the axiom of
  reducibility: you pay the full cost of the ceremony and hold none of the
  guarantee, so pick an end or narrow the exemption in advance and argue the
  property survives inside it.

    - merge: Merges into 49, the same Church escape-hatch argument with the
    - replacement-construct action.
    - merge: Merges into 49: identical Church claim, and 49 adds the ship-the-
    - better-construct half.
    - merge: Merges into 49, which states the same dominated-middle claim plus
    - the replacement-construct half.


---

## Kept

**[9] stonebraker** (3/3)

  Size a transaction by what you can actually undo: before setting the
  boundary, list the irreversible acts inside it — external API calls, emails,
  payments, files outside the store — and push them past the commit or shrink
  the unit (Stonebraker).

**[17] sussman/herlihy** (3/3)

  Atomicity belongs to the transaction, not the object (Sussman, Herlihy): a
  class that locks its own methods is correct only for operations that touch
  it alone, so put the lock at the caller's transaction boundary instead of
  inside the type — and never do both, because the composite then waits on
  itself.

**[18] fischer/liskov/lynch** (3/3)

  Let timing assumptions buy progress and never safety (Fischer, Liskov,
  Lynch): a timeout cannot distinguish a slow participant from a dead one, so
  no irreversible step — failover, takeover, deletion, marking-dead — may rest
  on an expiry alone; it needs evidence actually received, or a lease/epoch
  the loser can be fenced by.

**[19] lampson/schneider** (3/3)

  Force determinism before you replicate, retry, or replay (Lampson,
  Schneider): a component whose behaviour is not a function of its input
  history cannot be made redundant, so hoist wall-clock reads, random draws,
  generated IDs, hash-iteration order, and ambient config out of the core and
  pass them in as ordinary inputs.

**[31] chaitin/kolmogorov** (3/3)

  Measure an abstraction against the enumeration it replaces (Chaitin): if the
  general mechanism plus its call sites is no smaller than writing out the
  cases, the generality is decorative and the honest move is to write out the
  cases.

**[35] wirth** (3/3)

  Code that compensates for a defect in a layer you do not control has no
  clean form — confine it, label what is being worked around and what would
  let you delete it, and do not refactor it into elegance (Wirth).

**[49] church/steele/pike/hoare** (3/3)

  When a rule blocks something you need, drop the rule or drop the need —
  never add the general bypass; and when you want to stop a pattern, ship the
  construct that does that job better instead of the prohibition.

**[51] steele/hoare** (3/3)

  Promise only what a caller actually needs — treat iteration order, error
  text, timing, float formatting, and call counts as liabilities until
  deliberately guaranteed, and refuse to assert them in tests.

**[52] liskov/dahl** (3/3)

  Hide mechanism and location; never hide the possibility of failure or the
  cost — an operation that can fail or that crosses a network must not read
  like a cheap local one.

**[57] brooks** (3/3)

  When a change is fighting you, stop reading the control flow and go change
  the data representation — Brooks holds that logic is downstream of
  representation, so the large wins are re-representations, not cleverer
  procedures.

**[58] naur** (3/3)

  Naur: the program text is a by-product of a theory nobody wrote down, so a
  change that passes every test can still be wrong — reconstruct why the code
  is shaped this way before editing, and if you cannot, say so rather than
  patch.

**[61] lampson/torvalds/saltzer** (3/3)

  Lampson: designate exactly one representation as authoritative and optimize
  it for being checkable, not fast; every index, cache, or denormalized field
  must be a guess you are allowed to delete and rebuild at any moment.

**[62] saltzer** (3/3)

  Saltzer: a partial guarantee gets read as a total one, so a check placed
  below the layer that knows what 'correct' means may be sold as a performance
  improvement but never as a guarantee — put the real check where the
  knowledge to finish it lives.

**[64] torvalds/wirth** (3/3)

  Torvalds: spend all your stability at one boundary — freeze what outsiders
  can observe, rebuild freely behind it, and when you change an internal
  interface, fix every caller in the same change instead of leaving a
  compatibility shim.

**[74] reynolds/hoare** (3/3)

  Attack your own acceptance criteria with the laziest cheating implementation
  you can write — Reynolds notes that 'returns a sorted array' is satisfied by
  zeroing every element — and add the clause that stops it, including what the
  operation promises not to touch.

**[80] jones/hoare** (3/3)

  Treat an invariant as a promise at the entry and exit of an operation, not
  at every instant — Jones's point that the right question is never 'does this
  hold' but 'who can be looking, and when' — and strengthen it by shrinking
  the window or the audience rather than by elaborating the predicate.

**[8] mcmillan** (2/3)

  McMillan: a pipeline costs what its worst moment costs, not what its output
  costs, so instrument peak intermediate size and treat "materialize the
  combined thing, then query it" as a decision that needs justifying — two
  implementations with byte-identical output can differ by orders of magnitude
  in whether they run at all.

**[10] liskov** (2/3)

  An effect must not become visible before it becomes durable: make the
  readable point and the durable point the same point, and treat any window
  where a reader can observe something a crash would erase as a defect no
  matter how narrow (Liskov).

**[11] codd/fagin** (2/3)

  Shape stored data from what determines what — the time-invariant
  dependencies of the domain — not from today's access patterns, and split
  exactly where a dependency forces it and no further (Codd, Fagin).

**[22] hoare** (2/3)

  Multiplexing independent work onto one queue couples it, and a bigger buffer
  only delays the diagnosis (Hoare): buffering absorbs variance, never a rate
  deficit, so when a shared pipeline stalls give each stream its own
  backpressure path rather than more capacity.

**[23] liskov** (2/3)

  Your data representation sets the concurrency ceiling, not your concurrency
  constructs (Liskov): if independent items share one container, every touch
  contends for the whole thing, and no amount of finer locking or extra
  threads recovers what the type gave away.

**[43] reenskaug** (2/3)

  Ask of every field on a long-lived type what it holds when no operation is
  in progress; a field with no honest answer is scratch space for one
  operation and belongs in something whose lifetime matches it (Reenskaug).

**[45] pike** (2/3)

  Treat a request for hooks, plugins, config knobs, or a DSL as a measurement
  of friction in the underlying primitives: find the specific interaction
  painful enough to prompt it, fix that, and check whether the request
  survives (Pike).

**[63] wirth** (2/3)

  Wirth: an iteration that did not make the system smaller is one nobody has
  finished thinking about — price every addition twice, for building it and
  for its permanent presence, and prefer the change that retires a mechanism
  over the one that adds a parallel path.

**[76] lampson/church/post** (2/3)

  Split any expensive or heuristic step into an untrusted search and a small
  terminating checker — Lampson's rule that only the checker is trusted and
  Church's that recognizing an answer must be decidable even when finding one
  is not — and make every failure of the untrusted half bias toward refusal.

**[79] sifakis/clarke/emerson** (2/3)

  Give any procedure that can stop on a resource limit a third answer distinct
  from pass and fail — Sifakis's 'I ran out of budget' — and make every
  negative verdict hand back the witness that produced it (Clarke, Emerson).
