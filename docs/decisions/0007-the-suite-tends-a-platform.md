# 0007. The suite tends a platform

- Status: Accepted
- Date: 2026-11-12
- Standard: 2026.1107.1839

## Context

The strategy said the suite answers six questions about running a
platform: what exists, what it costs, whether it is healthy, safe, and
shipping, and who changed what. Every one of them looks at the platform
from above. None asks how the software on it grows.

Two things made that too narrow.

First, most changes on a platform now come from agents. An agent copies
what it finds in a repository, faster and more exactly than a person. A
bad example spreads. A slow test loop is paid on every change. An
instruction file grows until nothing reads it all. The questions above
see none of this.

Second, the same holds for a platform with human customers, only slower.
Its customers copy what they find, and what they make becomes what the
next one finds. A platform is never built and handed over. It is tended.

The suite also had no name for tools that tend but are not services, and
its one board, Orrery, had no place to show the state of a repository as a
gardener needs it.

## Decision

1. **The suite has one job: tending a platform.** The six questions stay.
   They are the sensing part of that job, not the whole of it.
2. **`garden.md` is the suite's framework.** It defines a bed, a grower,
   and a gardener; the three materials (soil, stake, fence); the five
   moves (sense, trace, fix, stake, prune); the ladder of remedies; and
   the three numbers each bed carries (loop, friction, weeds). The four
   delivery measures stay as the guard.
3. **The first membership check widens.** It read "it serves operations".
   It now reads "it serves tending": a member helps a gardener sense,
   trace, fix, stake, fence, or prune. A tool that serves one person's or
   one family's life is still a private app. This supersedes check 1 in
   decision 0001. The other three checks, and every member admitted so
   far, stand.
4. **Orrery is the one board.** The suite builds no master app above its
   members. Orrery's sky stays the top view. The garden is a view inside
   Orrery, one layer down: the ground of a planet, where each repository
   is a bed. The view obeys three rules: every picture maps to one real
   number, the plain number is one click away, and tables and APIs use
   plain words. A reader can switch it off.
5. **Orchestration is Orrery's actions.** A gardener acts on many beds
   through an action and its backend. The suite builds no controller.
6. **The shed is a named class.** A tending tool that is installed on a
   machine, not run as a service, is listed in `members.md` under "The
   shed" with the job it does. It is not a member and does not take the
   membership test.
7. **The build order starts with sensing.** A gardener cannot tend what it
   cannot see. Friction, the one number nothing measures, goes first.

## Left open

This decision does not settle three things. Each needs its own record.

- **Where friction sensing lives.** A headless source that writes to the
  catalog, a collector inside Tally, or a new member.
- **Whether a seed tool joins.** Decision 0003 stands until a record says
  otherwise. Its reasons still hold today.
- **Whether the standard gains a pillar for growing conditions.**
  `pillars.md` keeps the standard's twelve until the standard changes.

## Consequences

- `strategy.md`, `seam.md`, `pillars.md`, `members.md`, and `README.md`
  are rewritten to this decision.
- `garden.md` rates each tending job. Friction and the seed are gaps.
- Each member gains a line saying which tending job it does.
- Orrery owes a ground view. Its design is Orrery's own, in its
  repository.
- Nothing is removed from the suite. No member changes its pillar.

## Rules

Builds to:

- `map-the-platform-as-pillars-each-one-a-question-it-must-answ`
- `turn-retrospective-findings-into-a-few-ranked-remedies-deter`
- `fix-what-s-broken-everywhere-at-the-source`
- `respond-to-an-escape-by-turning-it-off-then-closing-exactly-`
- `question-delete-simplify-speed-up-then-automate-in-that-orde`
  (Aspirational)
- `count-course-corrections-from-stops-and-redirects-never-from`
- `close-every-piece-of-agent-work-with-an-evidence-backed-retr`
- `new-capability-goes-to-a-standalone-product-not-the-house-vi`

Departs from:

- `admit-a-tool-to-the-platform-suite-only-by-a-written-members`: the
  rule's first check says "it serves operations". This decision widens it
  to tending. The written test and the decision record stay.
- `build-the-platform-s-nine-positions-in-dependency-order-star`: the rule
  starts with the three positions that produce the rest. This decision
  puts sensing friction first, because the suite already holds a catalog
  and has no way to see where growers struggle.

New to the standard: the standard has no rule for the three materials and
how hard each holds, for the ladder of remedies with an instruction as the
last rung, for a loop budget per repository, for counting friction or
weeds, or for a class of installed tending tools beside the suite.
