# How to Think About Code

Claims that change decisions, drawn from the people who worked out why. Each is
attributed so you can reach for what you already know about that person's work.
Nothing here is a style preference; if a line does not change what you would
otherwise do, it does not belong.

## Before changing anything

Reconstruct the theory before you edit. Naur's claim is that the program text is a
by-product of an understanding nobody wrote down: which parts of the world the
structure corresponds to, and where that correspondence was never meant to reach.
A change can pass every test and still be wrong, because the tests encode the
behaviour, not the theory. Work out why the code is shaped the way it is before
reshaping it, and if you cannot, say so rather than patch around the gap.

When a change is fighting you, stop reading the control flow and change the data
representation. Brooks holds that logic is downstream of representation, so the
large wins are re-representations rather than cleverer procedures. Difficulty
threading a value through six functions is usually evidence the value is in the
wrong shape, not that you need a seventh.

## What an interface promises

Promise only what a caller actually needs. Iteration order, error message text,
timing, float formatting, and call counts are liabilities until you deliberately
guarantee them (Steele, Hoare). Refuse to assert them in tests — a test that pins
an incidental property converts it into a contract you never meant to sign.

Hide mechanism and location; never hide the possibility of failure or the cost.
An operation that can fail, or that crosses a network, must not read like a cheap
local one (Liskov, Dahl). The abstraction that makes a remote call look local is
not a convenience, it is a removed warning label.

Attack your own acceptance criteria with the laziest cheating implementation you
can write. Reynolds observes that "returns a sorted array" is satisfied by zeroing
every element. Write the cheat, then add the clause that stops it — including what
the operation promises *not* to touch, which is the clause people forget.

Put a check where the knowledge to finish it lives. Saltzer's point is that a
partial guarantee gets read as a total one, so a check placed below the layer that
knows what "correct" means may be sold as a performance improvement but never as a
guarantee.

Give any procedure that can stop on a resource limit a third answer, distinct from
pass and fail — Sifakis's "I ran out of budget". A truncated scan returned as a
clean result is a silent bug. Make every negative verdict hand back the witness
that produced it (Clarke, Emerson), because a failure you cannot reproduce is a
rumour.

Split expensive or heuristic work into an untrusted search and a small terminating
checker. Only the checker is trusted (Lampson); recognizing a good answer stays
decidable even where finding one is not (Church). Every failure of the untrusted
half should bias toward refusal.

## State

Designate exactly one representation as authoritative, and optimize it for being
checkable rather than fast (Lampson). Every index, cache, and denormalized field
is then a guess you are allowed to delete and rebuild at any moment. Two things
that both claim to be the truth is the bug you will spend a week on. Any derived
state that cannot detect its own staleness needs a named periodic recomputation
rather than invalidation alone (Ullman) — ask what would have to be true for you
to notice it had gone wrong, and if there is no answer, invalidation is a hope.

Moving durable state into volatile storage is a correctness change, not an
optimization (Wirth). Score it by what the persistent structure looks like if
power is lost at an arbitrary instant, not by the benchmark that motivated it.

Shape stored data from what determines what — the time-invariant dependencies of
the domain — rather than from today's access patterns, and split exactly where a
dependency forces it and no further (Codd, Fagin). Access patterns change on a
quarterly cycle; dependencies do not.

Ask of every field on a long-lived type what it holds when no operation is in
progress. A field with no honest answer is scratch space for one operation, and
belongs in something whose lifetime matches it (Reenskaug).

Treat an invariant as a promise at the entry and exit of an operation, not at
every instant. Jones's framing is that the right question is never "does this
hold" but "who can be looking, and when" — so strengthen an invariant by shrinking
the window or the audience, not by elaborating the predicate. The same question
governs refactoring: same-input-same-output justifies nothing if anything else can
write the same state, so read the fragment with an adversarial write spliced into
every gap, including before its first line (Jones, Hoare).

## Concurrency and failure

Your data representation sets the concurrency ceiling, not your concurrency
constructs (Liskov). If independent items share one container, every touch
contends for the whole thing, and no amount of finer-grained locking or extra
threads recovers what the type already gave away.

Atomicity belongs to the transaction, not the object (Sussman, Herlihy). A class
that locks its own methods is correct only for operations touching it alone. Put
the lock at the caller's transaction boundary instead, and never do both, or the
composite ends up waiting on itself.

An effect must not become visible before it becomes durable (Liskov). Make the
readable point and the durable point the same point, and treat any window where a
reader can observe something a crash would erase as a defect, however narrow.

Let timing assumptions buy progress and never safety. A timeout cannot distinguish
a slow participant from a dead one (Fischer, Liskov, Lynch), so no irreversible
step — failover, takeover, deletion, marking-dead — may rest on an expiry alone.
It needs evidence actually received, or a lease the loser can be fenced by. A
timeout is a hint that something may be wrong, never evidence that it is, so any
action taken on one must be survivable if it turns out to have been taken wrongly
(Liskov, Dijkstra).

Repetition buys confidence only against independent failures (Sussman). Before
choosing a retry count, a resample, or a redundant check, say what rules out the
case where every attempt fails the same way — correlated failure is usually a
property of the input, which makes it invisible in every trial you run. Without
that argument, more attempts buy latency and nothing else.

Force determinism before you replicate, retry, or replay. A component whose
behaviour is not a function of its input history cannot be made redundant
(Lampson, Schneider), so hoist wall-clock reads, random draws, generated IDs, hash
iteration order, and ambient config out of the core and pass them in as inputs.

Size a transaction by what you can actually undo. Before setting the boundary,
list the irreversible acts inside it — external API calls, emails, payments, files
outside the store — and push them past the commit or shrink the unit
(Stonebraker).

## Adding and removing

Measure an abstraction against the enumeration it replaces. If the general
mechanism plus its call sites is no smaller than writing out the cases, the
generality is decorative and the honest move is to write out the cases (Chaitin).

When a rule blocks something you need, drop the rule or drop the need, but never
add the general bypass. An escape hatch added once becomes the path everything
takes. Correspondingly, when you want to stop a pattern, ship the construct that
does that job better rather than the prohibition (Church, Steele, Pike, Hoare).

Treat a request for hooks, plugins, config knobs, or a DSL as a measurement of
friction in the underlying primitives (Pike). Find the specific interaction
painful enough to prompt the request, fix that, and check whether the request
survives. Usually it does not.

An iteration that did not make the system smaller is one nobody has finished
thinking about (Wirth). Price every addition twice, once for building it and once
for its permanent presence, and prefer the change that retires a mechanism over
the one that adds a parallel path.

## Boundaries and cost

Spend all your stability at one boundary. Freeze what outsiders can observe,
rebuild freely behind it, and when you change an internal interface, fix every
caller in the same change instead of leaving a compatibility shim (Torvalds,
Wirth). Shims are how one boundary silently becomes five. The same rule applies
downward: when you add an accessor, wrapper, cache layer, or handle, remove the
direct path in the same change, because an abstraction is worth exactly its
weakest bypass (Ungar).

Code that compensates for a defect in a layer you do not control has no clean form
(Wirth). Confine it, label what is being worked around and what would let you
delete it, and do not refactor it into elegance — elegance hides that it is
temporary. Related, and easier to violate by accident: do not simplify a rule that
was tuned against an accounting argument (Tarjan). Eviction policies, backoff
schedules, rebalancing triggers and retry heuristics are places where two nearly
identical rules differ by an order of magnitude, and the sequences that separate a
good rule from a fatal one are adversarial and will not be in your benchmark.
Re-derive the bound or leave the rule alone.

Multiplexing independent work onto one queue couples it, and a bigger buffer only
delays the diagnosis (Hoare). Buffering absorbs variance, never a rate deficit, so
a queue that keeps needing to be enlarged is a measurement telling you the two
sides do not match. Give each stream its own backpressure path rather than more
capacity.

A pipeline costs what its worst moment costs, not what its output costs
(McMillan). Two implementations with byte-identical output can differ by orders of
magnitude in whether they run at all, so instrument peak intermediate size and
treat "materialize the combined thing, then query it" as a decision needing
justification.
