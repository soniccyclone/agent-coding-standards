#!/usr/bin/env bash
# Run one benchmark arm through all rounds.
#
#   ./run.sh <arm>        arm in: control | incumbent | general | flavored
#
# Each arm builds the same job queue from the same round prompts, differing only
# in which CLAUDE.md is installed in the project directory. The global
# ~/.claude/CLAUDE.md is suppressed for every arm (including the incumbent, which
# gets it installed as a project file instead) so that all arms differ in exactly
# one variable.
#
# Requires --dangerously-skip-permissions to run unattended. Every arm writes
# only inside its own scratch workspace under BENCH_ROOT.

set -euo pipefail

ARM="${1:?usage: run.sh <control|incumbent|general|flavored>}"
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
ROUNDS="$REPO/tools/bench/rounds"

# Set by the Makefile to bench-runs/<timestamp>/. Deliberately not /tmp: the
# generated code is the artifact worth reading, and it has to still be there
# tomorrow.
BENCH_ROOT="${BENCH_ROOT:?set BENCH_ROOT, or run via 'make bench'}"
FLAVORED="${FLAVORED:-DISTILLED-FOUNDATIONS.md}"
MODEL="${MODEL:-claude-opus-5}"

WORK="$BENCH_ROOT/$ARM"
CFG="$BENCH_ROOT/.cfg-$ARM"     # isolated CLAUDE_CONFIG_DIR: no global CLAUDE.md
LOGS="$BENCH_ROOT/logs/$ARM"

rm -rf "$WORK" "$CFG"
mkdir -p "$WORK" "$CFG" "$LOGS"

# CLAUDE_CONFIG_DIR carries credentials as well as memory, so an empty one
# cannot authenticate. Seed it with the credential file and nothing else: that
# is what suppresses ~/.claude/CLAUDE.md while keeping the session logged in.
# Left to the operator deliberately, since it moves an auth token.
if [ ! -f "$HOME/.claude/.credentials.json" ]; then
  echo "no ~/.claude/.credentials.json; are you logged in?" >&2; exit 3
fi
cp "$HOME/.claude/.credentials.json" "$CFG/" && chmod 600 "$CFG/.credentials.json"

# Install the arm's CLAUDE.md. This is the only difference between arms.
case "$ARM" in
  control)   : ;;                                   # no CLAUDE.md at all
  incumbent) cp "$HOME/.claude/CLAUDE.md" "$HOME/.claude/RTK.md" \
                "$HOME/.claude/tropes.md" "$WORK/" ;;   # @-refs resolve locally
  general)   cp "$REPO/bundle/DISTILLED.md"  "$WORK/CLAUDE.md" ;;
  flavored)  cp "$REPO/bundle/$FLAVORED"     "$WORK/CLAUDE.md" ;;
  *) echo "unknown arm: $ARM" >&2; exit 2 ;;
esac

cd "$WORK"
git init -q
git config user.email bench@local
git config user.name bench
git add -A
git commit -q --allow-empty -m "round0: arm=$ARM claude.md installed"
git tag -f "round0" >/dev/null

for r in 1 2 3 4; do
  echo "[$ARM] round $r ..." >&2
  CLAUDE_CONFIG_DIR="$CFG" claude \
      -p "$(cat "$ROUNDS/r$r.md")" \
      --model "$MODEL" \
      --output-format json \
      --dangerously-skip-permissions \
      > "$LOGS/r$r.json" 2> "$LOGS/r$r.err" || {
        echo "[$ARM] round $r FAILED (see $LOGS/r$r.err)" >&2; exit 1; }

  git add -A
  git commit -q --allow-empty -m "round$r"
  git tag -f "round$r" >/dev/null
done

echo "[$ARM] done -> $WORK" >&2
