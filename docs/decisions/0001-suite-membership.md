# 0001. The suite's members

- Status: Accepted, amended by 0003 (Slipway leaves), 0007 (the first check widens), 0009 (Slipway joins again), and 0017 (redgreen and forgitten become one member)
- Date: 2026-11-05
- Standard: 2026.1103.322

## Context

The same hands built many tools: platform services, libraries, release
tools, an agent runtime, personal utilities, and an estate's own apps. They
were drawn together as one landscape. Some of them run a platform in any
estate. Others serve one person, one family, or one way of working. Mixing
them hides which ones an estate can adopt and which ones it should not.

## Decision

Almanac has ten members: Orrery, Vantage, My Apps, Tally, Ledger, conform,
redgreen, Dispatch, Slipway, and forgitten. Each passes the first two parts
of the test in `seam.md` (it serves operations, and it fills a gap), and
each joins with the changes it owes listed in `seam-audit.md`.

These stay out: platformkit (a library the members build on), release-damnit
(a release tool), Ion (an agent runtime Slipway uses), SlopDrop (a personal
hand-off box), cli-proxmox (a CLI for one hypervisor), and posture (retired
into conform). An estate's own apps consume the suite and never join it.

forgitten joins because it answers an operations question no member
answered: which work has not left the machine it was done on.

## Consequences

- The suite's pillar coverage is judged from these ten alone. The
  foundations pillar is covered by a library outside the suite, and
  `pillars.md` says so.
- A new member joins only by a new decision record.

## Rules

Builds to `map-the-platform-as-pillars-each-one-a-question-it-must-answ`
and `the-platform-s-own-software-is-a-pillar-kit-engine-interface`. New to
the standard: a written test for suite membership.
