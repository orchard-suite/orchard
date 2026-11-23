# 0017. redgreen and forgitten become one member, Muster

- Status: Accepted
- Date: 2026-11-20
- Standard: 2026.1120.2003
- Capture: 00b96b74-002b-4bdc-809a-e0b65138270d
- Amends: 0001 (ten members become nine once Muster ships), 0004 (redgreen takes a new name and a second reader), 0016 (point 6: Muster is one part of Catalog where two were)

## Context

Two members answer one question from two sides: where is the code, and
what state is it in? redgreen answers for work that reached a forge.
forgitten answers for work that never left the machine it was done on.

These facts were read from each repository on 2026-11-20:

- redgreen, at v1.12.0, is one Go program with no pages of its own. It
  reads the forges and writes repositories, pipelines, services,
  deployments, and issues into the catalog. Orrery is its board (decision
  0004).
- forgitten, at v0.1.9, is two programs: a CLI written in C# that scans a
  machine, and a hub written in TypeScript with its own store and its own
  page. A device signs in to the estate's identity provider with a code a
  person types, and keeps a refresh token. forgitten writes nothing to the
  catalog.

So forgitten today is what redgreen was before decision 0004: a second
inventory and a second board beside the catalog. Decision 0004 removed
that from redgreen. The standard says the same of any tool (rule
`read-the-catalog-first-and-keep-it-complete`). The suite's own diagram
says forgitten "stands alone".

The join also has a use neither has alone. A repository's record can show
its pipeline's health and, beside it, the machines that hold work it has
never seen.

Three things were weighed and turned down:

- **Keep both.** It keeps two inventories of the same repositories, and
  the only member with a board that is not Orrery.
- **Call the merged program "Forge".** The suite already uses that word
  for the thing it reads: a forge is GitHub, GitLab, or another like them.
  `strategy.md` says the suite is not a forge. A member with that name
  would read "Forge reads the forge" in every document.
- **Let each machine write to the catalog.** Every machine would then hold
  a catalog token. The owner ruled that out.

## Decision

1. **One member, Muster, answers where the code is and what state it is
   in.** It reads the forges, as redgreen does, and it takes what each
   machine reports about work that has not left it, as forgitten does.
2. **The catalog is its only board.** forgitten's hub, store, and page go
   away. What a machine reports lands on the repository's record in the
   catalog, beside what the forge says of it.
3. **It is one service, written in Go.** forgitten's CLI and hub are
   written again, not carried over.
4. **A machine never holds a catalog token.** Only Muster's service
   writes to the catalog. A machine's report reaches Muster through the
   suite's device agent (decision 0018).
5. **A report carries names and counts.** It never carries a file's
   contents, as forgitten's never did. What sits on a person's machine is
   more private than what sits on a forge, so an estate sets who may read
   it before it turns the reader on.
6. **The suite has ten members until Muster ships.** It has nine after
   that. redgreen and forgitten keep working, under their own names,
   until Muster holds what both hold.
7. **The name.** A muster is a roll call: everything is counted where it
   stands. To pass muster is to meet the bar. The first is forgitten's
   job, and the second is redgreen's.

Decision 0004 stands in everything else. Orrery is the board and the
math, and the health rules and delivery measures stay calculated fields
on the blueprints the member offers.

## What members owe

Each is that member's own design, recorded in its own repository.

| Who | What it owes |
| --- | --- |
| Muster (redgreen today) | Take what a machine reports and write it onto the repository's record in the catalog. Offer the fields for it, as redgreen offers its blueprints. |
| Muster | Say where work goes that has no forge record to sit on: a repository with no remote. |
| redgreen and forgitten | Retire forgitten's hub, store, page, and CLI once Muster holds what they hold, and take the new name. |

## Left open

- **Which repository holds Muster, and whether it is public.** redgreen's
  repository is public and forgitten's is private.
- **Whether Muster builds on the kit.** Decision 0004 keeps redgreen off
  it. A member that takes posts from machines needs a door, and the kit
  has one.
- **How much of a scan is kept.** Counts and branch names tell a gardener
  where to look. File names tell more, and say more about a person's
  work.

## Consequences

- `README.md`, `members.md`, and `pillars.md` say that the two will
  become Muster. Their own sections stay until it ships, because every
  fact about an app is read from what exists.
- `roadmap.md` gains rows 27 and 28.
- The diagram's view of what is owed draws forgitten folding into
  redgreen.
- No rating changes. Catalog stays Covered.

## Rules

Builds to:

- `read-the-catalog-first-and-keep-it-complete`: no second inventory and
  no second board beside the catalog.
- `map-the-platform-as-pillars-each-one-a-question-it-must-answ`: one app
  grows to cover a need, and a second app for the same need is not added.
- `delivery-outcomes-as-a-sibling-of-ci-health`: the forge reader stays
  the source for delivery measures.
- `devices-report-to-the-house-nothing-commands-them`: a device never
  writes to the catalog itself.
- `admit-a-tool-to-the-platform-suite-only-by-a-written-members`: two
  members become one by this record.
- `record-architecture-decisions-as-immutable-adrs`: decisions 0001 and
  0004 are amended here and not rewritten.

Departs from: none.

New to the standard: the standard has no rule for merging two members
that answer one question from two sides, or for showing work that never
reached a forge on the same record as the forge's own facts.
