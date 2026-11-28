# `make check` is the gate before a commit. `make land` lands: release-damnit
# runs the config's check on the tree that lands and signs its proof. CI runs
# the document check too. From a worktree: make land BRANCH=<branch>.
SHELL := /bin/bash

.PHONY: check land

# hedge keeps every estate's names out of this repository; it runs where a
# register is installed, and its git hooks check each commit and push.
check:
	python3 scripts/check.py
	@if command -v hedge >/dev/null; then hedge audit; else echo "check: hedge is not installed here; its hooks did not run either" >&2; fi

land:
	release-damnit land $(BRANCH)
