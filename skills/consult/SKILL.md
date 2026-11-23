---
name: consult
description: Look up Orchard, the suite of core platform services, before work that touches it. Use when a task or a question is about what the suite is or is not, which apps are members and what each one answers, the pillars and what covers them, the line between the suite and an estate, how an estate keeps quality when agents write the changes, what a suite decision said, or what the suite still owes on its roadmap.
---

# Consult Orchard

This plugin is the Orchard repository itself. The documents sit two folders
above this file: `../../README.md` and `../../docs/`. Never edit them here;
a change goes in as a proposal (the `propose` skill).

| Question | Read |
| --- | --- |
| What is the suite, and who are its members | `README.md` |
| Why it exists, what it will and will not become | `docs/strategy.md` |
| The framework and its words (bed, grower, gardener, the five moves) | `docs/garden.md` |
| Each app: what it reads, writes, and tends | `docs/members.md` |
| The pillars, what covers each, what is missing | `docs/pillars.md` |
| How an estate keeps quality when agents write most changes | `docs/quality.md` |
| The line between the suite and an estate, and the test for joining | `docs/seam.md`, `docs/seam-audit.md` |
| What was decided, and why | `docs/decisions/`, one record each |
| What the suite still owes, and what is done | `docs/roadmap.md` |
| The suite as pictures | `docs/orchard.vantage.yaml` |

## Steps

1. Read `README.md` for the map. Then read the document the question
   belongs to, in full. Search `docs/` by keyword when the table does not
   make it plain.
2. The decision records are the authority. Where a document and a record
   disagree, the record wins. A later record amends or supersedes an
   earlier one, and the earlier one's status line says so. Read the status
   line before you rely on a record.
3. Cite what you use: the decision's number, and this plugin's version from
   `../../.claude-plugin/plugin.json`.
4. A fact about one app (a version, a command, a field) is checked in that
   app's own repository or through its own skill, not here. These documents
   say when each such fact was last read.
5. Say where the work departs. If the work does something a decision
   turned down, or something no decision covers, tell the person before you
   build. Once it is settled, send it back with the `propose` skill.

The suite names no estate. Nothing here says how one household or one
company runs it.
