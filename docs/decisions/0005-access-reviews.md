# 0005. Access reviews

- Status: Accepted
- Date: 2026-11-07
- Standard: 2026.1106.144

## Context

An estate is often asked three things about a system: who has access, at
what level, and when the access was last reviewed. A work estate is asked
them by the people who audit it; the home estate asks them of itself. The
suite holds most of the parts already. Orrery keeps Entra users, groups,
and app assignments, and links each account to a person. conform judges any
catalog list through its mappings. Every Orrery action run lands in Ledger.
What is missing is one shape for an access grant, a review a person signs
off, and rules that judge both.

## Decision

Four layers, one job each.

| Layer | Member | Holds |
| --- | --- | --- |
| Inventory | Orrery | Who holds what access in which system, now. Pushed by each system, never typed. |
| Judgment | conform | Whether that access is in order: no stale accounts, admin roles through groups, reviews on time. |
| Review | Orrery's actions | A person checks the holders, keeps or removes each, and signs off. The sign-off is a record. |
| History | Ledger | Every grant, removal, and review over time, across systems. |

**Inventory.** Each system keeps its own lists, named after the system, as
the blueprint standard says: `entra_app_role_assignment` for Entra, and
whatever a system's own pusher brings. A grant reaches the application it
opens (`it_application`) through the shared relation name `application`,
directly or through the system's own app, as Entra's does through the
application's `sign_in`. Its account links to the core `person`. A system
with no pusher has no grants in the catalog, and its rules say no data.

**Judgment.** conform's `access` pack gains two tiers over grants and
applications:

- `hygiene`: no grant to an account that is gone or disabled; an admin
  role is held through a group, never by a person directly; a guest's
  grant is flagged.
- `reviewed`: an application that grants access has a review within
  `access_review_days`.

Which roles count as admin is the estate's own list, `admin_roles`, in its
conform tuning, because every system names its roles its own way.
`access_review_days` is tuning too. An estate turns on the tiers it wants.

**Review.** `it_access_review` is a record: one sign-off of one
application's access by one person, with what was kept and removed. An
Orrery action on the application writes it. For a system Orrery can change,
the review also removes what the reviewer took away, through the same
runner that grants. For one it cannot, the review records the decision, and
the removal happens in the system by hand.

**History.** Ledger's contract does not change. Orrery forwards every
action run, so each review and removal is already an event. A collector
that reads a system's own audit log posts `access.grant` and
`access.revoke` for changes made between reviews.

Orrery answers what is true now. Ledger answers what happened over time.

## Consequences

- The three questions are one application page each: its grants, its
  latest review, and conform's verdict, with the history in Ledger.
- The blueprint standard gains `it_access_review` and the shared name
  `application`. conform gains the two tiers. Orrery gains the review
  actions and a removal in its access runner. Ledger documents the access
  verbs.
- A system's pusher, its `admin_roles`, and its `access_review_days` live in the
  estate's own repository.
- Tamper evidence for Ledger (a hash chain anchored outside it) is left
  for later. Until it is on, an estate may move, migrate, or purge Ledger's
  store freely.

## Built to the standard

Standard 2026.1106.144:

- `sort-every-catalog-blueprint-as-inventory-record-history-or-`
- `the-system-of-record-pushes-a-person-types-only-short-slow-l`
- `human-access-only-through-project-role-groups-assigned-in-on`
- `one-ledger-of-what-every-agent-did-shape-defined-first`
- `extend-the-existing-actions-engine-every-run-goes-to-the-led`

New to the standard: no rule covers access reviews, who judges them, or
where the sign-off is kept. This decision sets it for the suite.
