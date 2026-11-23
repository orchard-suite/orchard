# 0003. Slipway leaves the suite

- Status: Superseded by 0009
- Date: 2026-11-05
- Standard: 2026.1103.322
- Amends: 0001

## Context

Decision 0001 made Slipway the member for golden paths. Slipway turns a
typed idea into a new repository with a released application, or lands a
named change. It is fun and useful, but it is not a paved road a team uses
to ship its own work. It creates repositories only on GitHub, publishes
only to the GitHub registry, and runs its agent on Ion, which is not a
member.

## Decision

Slipway is not a member of Almanac. It is a utility, like Ion and
SlopDrop, and may use the suite like any other tool. The suite has nine
members.

## Consequences

- The golden paths pillar has no member, and `pillars.md` rates it a gap,
  first in the build order with interfaces.
- Slipway's rows leave `seam-audit.md`; the seam rules no longer apply to
  it.
- Orrery still reads Slipway's jobs where an estate runs Slipway. That is
  an estate's choice, not a suite crossing.

## Rules

Builds to `map-the-platform-as-pillars-each-one-a-question-it-must-answ`:
a pillar with no honest answer is shown as a gap, not covered by a near
fit.
