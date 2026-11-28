---
name: consult
description: Look up Orchard, the suite of core platform services, before work that touches it. Use when a task or a question is about what the suite is or is not, which apps are members and what each one answers, the pillars and what covers them, the line between the suite and an estate, how an estate keeps quality when agents write the changes, what a suite decision said, or what the suite still owes on its roadmap.
---

# Consult Orchard

This plugin is the Orchard repository itself. Its documents sit two
folders above this file: `../../README.md` and `../../docs/`. Its decision
records, its roadmap, and its diagrams live in a Vantage hub, and
`../../vantage.yaml` names them (decision `ORC-0027`). Never edit any of
them from here; a suite decision is written as an `ORC` record with the
`vantage:decide` skill, with its `ORCR` items and the document changes in
the same pass (decision `ORC-0048`).

| Question | Read |
| --- | --- |
| What is the suite, and who are its members | `README.md` |
| Why it exists, what it will and will not become | `docs/strategy.md` |
| The framework and its words (bed, grower, gardener, the five moves) | `docs/garden.md` |
| Each app: what it reads, writes, and tends | `docs/members.md` |
| The pillars, what covers each, what is missing | `docs/pillars.md` |
| How an estate keeps quality when agents write most changes | `docs/quality.md` |
| The line between the suite and an estate, and the test for joining | `docs/seam.md`, `docs/seam-audit.md` |
| What was decided, and why | the registry `vantage.yaml` names (`decisions`), in the hub |
| What the suite still owes, and what is done | the roadmap kind `vantage.yaml` names (`roadmap`), in the hub, and the document's page `roadmap.md` |
| The suite as pictures | the document `vantage.yaml` names (`document`), in the hub |

## Reading the hub

Use the Vantage plugin's tools. The estate's own Vantage settings map this
repository to the hub and the workspace; the plugin's `pointer.sh` prints
them. With `ORC` and `ORCR` as the names in `vantage.yaml`:

- **Records**: `vantage_outline ORC` lists them, one line each.
  `vantage_find` with `in: ORC` searches them. `vantage_read
  ORC-0013#decision` reads one section. A document that says "decision
  4005" means `ORC-4005`.
- **Roadmap**: `vantage_outline ORCR` lists the items and their states
  (`ORCR#planned` for one state). `vantage_read ORCR-9` reads one: who owes
  it (`owes`), the records it comes from (`from`), its section, its state,
  and the day it was checked. The page `<workspace>/orchard/roadmap.md`
  gives the order of the work and the open questions.
- **Pictures**: `vantage_outline <workspace>/orchard` lists the views, and
  `vantage_render` draws one.

When no hub on this machine holds the registry, say so: the documents in
`docs/` still answer what the suite is, and the records and the roadmap
cannot be read here.

## Steps

1. Read `README.md` for the map. Then read the part the question belongs
   to: search `docs/` for its heading, or `vantage_find` the registry, and
   read that section, not the whole document or record. Read a whole one
   only when the question is about all of it.
2. The decision records are the authority. Where a document and a record
   disagree, the record wins. A later record amends or supersedes an
   earlier one, and the earlier one's status note, at the top of its
   Context, says so. Read it before you rely on a record.
3. Cite what you use: the record's citation (`ORC-4005`), and this
   plugin's version from `../../.claude-plugin/plugin.json` for a
   document.
4. A fact about one app (a version, a command, a field) is checked in that
   app's own repository or through its own skill, not here. The documents
   and the roadmap items say when each such fact was last read.
5. Say where the work departs. If the work does something a decision
   turned down, or something no decision covers, tell the person before you
   build. Once it is settled, write it as a record in the registry, as
   above.

The suite names no estate. Nothing here says how one household or one
company runs it.
