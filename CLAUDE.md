# Project Instructions for AI Agents

This file provides instructions and context for AI coding agents working on this project.

<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal (trimmed 2026-07-24, see note) -->
## Beads Issue Tracker

This project uses **bd (beads)** to track the OKF corpus build pipeline
(docs/planning/technical-plan.md phases). Run `bd prime` for full workflow
context and commands.

### Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work
bd close <id>         # Complete work
```

### Note on this project's actual conventions

bd's installer auto-generates a stronger version of this section — mandating
`bd` for all task tracking, `bd remember` instead of MEMORY.md, and a
mandatory `git push` at the end of every session. Trimmed deliberately: this
project uses TodoWrite for in-session tracking alongside bd, keeps the
existing MEMORY.md-based memory system, and **commits without pushing unless
explicitly asked** — bd's default template said the opposite of standing
instructions already given for this project. If bd gets reinstalled/updated,
re-trim rather than accepting the regenerated defaults.
<!-- END BEADS INTEGRATION -->


## Build & Test

_Add your build and test commands here_

```bash
# Example:
# npm install
# npm test
```

## Architecture Overview

_Add a brief overview of your project architecture_

## Conventions & Patterns

_Add your project-specific conventions here_
