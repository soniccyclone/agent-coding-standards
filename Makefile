# Distillation corpus + benchmark automation.
# Analysis dependencies live in a venv; this repo's own tooling is stdlib-only.

SHELL := /bin/bash
REPO  := $(shell pwd)
VENV  := $(REPO)/.venv
PY    := $(VENV)/bin/python
PIP   := $(VENV)/bin/pip

# Durable, reviewable, and out of /tmp. Each run is timestamped so runs never
# clobber each other and old runs stay around to compare against.
STAMP     ?= $(shell date +%Y%m%d-%H%M%S)
BENCH_ROOT?= $(REPO)/bench-runs/$(STAMP)
ARMS      ?= control incumbent general flavored
MODEL     ?= claude-opus-5
FLAVORED  ?= DISTILLED-FOUNDATIONS.md

export BENCH_ROOT MODEL FLAVORED

.PHONY: help setup lint bench bench-pilot analyze clean clean-runs

help:
	@echo "Corpus"
	@echo "  make lint          Check bundle consistency (stdlib, no setup needed)"
	@echo ""
	@echo "Benchmark"
	@echo "  make setup         Create .venv with the analysis tools"
	@echo "  make bench         Run all arms on $(MODEL), then score"
	@echo "  make bench-pilot   Same, on claude-sonnet-5, to shake out the harness"
	@echo "  make analyze       Re-score an existing run"
	@echo ""
	@echo "  Output lands in bench-runs/<timestamp>/ and is kept."
	@echo "  Each arm is a git repo with a tag per round:"
	@echo "    git -C bench-runs/<stamp>/general diff round1 round3"
	@echo ""
	@echo "  make analyze scores the newest run by default; RUN=<dir> picks one."
	@echo "  Override: ARMS='control general'  MODEL=...  FLAVORED=DISTILLED-LISP.md"
	@echo ""
	@echo "Housekeeping"
	@echo "  make clean         Remove the venv"
	@echo "  make clean-runs    Remove ALL benchmark runs (asks first)"

lint:
	@python3 tools/lint.py

setup: $(VENV)/.stamp
$(VENV)/.stamp:
	@python3 -m venv $(VENV)
	@$(PIP) -q install --upgrade pip
	@$(PIP) -q install radon coverage pytest
	@touch $@
	@echo "[setup] analysis tools installed in $(VENV)"

bench: setup
	@mkdir -p $(BENCH_ROOT)
	@echo "[bench] model=$(MODEL) arms='$(ARMS)'"
	@echo "[bench] output -> $(BENCH_ROOT)"
	@for arm in $(ARMS); do tools/bench/run.sh $$arm || exit 1; done
	@$(MAKE) --no-print-directory analyze RUN=$(BENCH_ROOT)

bench-pilot:
	@$(MAKE) --no-print-directory bench MODEL=claude-sonnet-5

# Defaults to the most recent run, so re-scoring never needs a timestamp typed
# out. RUN=<dir> to score a specific one.
analyze: setup
	@run="$(RUN)"; \
	 [ -n "$$run" ] || run=$$(ls -1d $(REPO)/bench-runs/*/ 2>/dev/null | sort | tail -1); \
	 [ -n "$$run" ] && [ -d "$$run" ] || { echo "no benchmark runs found; make bench"; exit 1; }; \
	 echo "[analyze] $$run"; \
	 $(PY) tools/bench/analyze.py "$$run" $(ARMS)

clean:
	@rm -rf $(VENV)
	@echo "[clean] venv removed; bench-runs/ left alone (use clean-runs)"

clean-runs:
	@echo "This deletes every benchmark run under $(REPO)/bench-runs/:"
	@ls -1 bench-runs 2>/dev/null || { echo "  (none)"; exit 0; }
	@read -p "Delete all of them? [y/N] " a; [[ $$a == y ]] && rm -rf bench-runs && echo "[clean-runs] removed" || echo "kept"
