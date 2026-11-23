# 0019. A report is private to its owner, and shared by the owner's act

- Status: Accepted
- Date: 2026-11-21
- Standard: 2026.1120.2003
- Capture: b59f0258-a0c7-47a6-a499-8a0b323ef5bd

## Context

Orrery keeps reports. A team defines a report once and publishes it again
and again. Each published copy is an edition, and it is kept to read and
compare later.

These facts were read from Orrery's repository on 2026-11-21, at v1.156.3:

- Every data set of a report is read as the report's owner. So an edition
  is the owner's view of the data, frozen on the day it was published.
- A report belongs to one home, usually a team. Whoever may see the home
  sees the report, and whoever sees the report sees its editions.
- The owner is a field on the report. The hub's ownership paths follow
  relations, so they do not reach it.
- A saved query is shared by its owner: with nobody, with the people who
  own its home, with an audience, or with everyone. Whoever opens it reads
  it with their own access.
- A publish tells the report's recipients through Dispatch, each only
  while they may see the report. The hub keeps no mail code (decision
  0015).
- The Report kind is the hub's own. Its description says anyone who may
  see the home reads the report.

Together these open a way around the access rules. A reader who sees a
report's home reads the owner's view of data that the reader could not
query. In an estate where every signed-in person can see every team, a
team's report was open to all of them.

A work estate closed this the same day with the hub's own access
settings: a report is read by its home team's members, that team's lead,
and admins. The platform standard holds that as its rule today. It leaves
two gaps. A report cannot be shared beyond its home team. An owner who is
not on the home team would not see their own report.

The Report kind belongs to the hub, so its default is the product's to
get right. An estate should not have to close it. This reading is a
judgment.

## Decision

1. **A report is private by default.** A report, and every edition of it,
   is seen by its owner and by admins only. Seeing the report's home no
   longer grants it.
2. **Sharing is the owner's act.** The owner, or an admin, shares a report
   with named people, a team, or an audience, the same way a saved query
   is shared. Unsharing takes it away, editions included.
3. **A recipient is a share.** Naming someone a recipient shares the
   report with them, so the mail and its link to the edition keep working.
   Removing them ends it.
4. **Every place that shows a report asks the same question.** Lists,
   search, a home's own page, the catalog's agent tools, and an edition's
   data and drawn page show a report only to those who may read it.
5. **No member joins.** The suite still has ten members.

Two things were weighed and turned down:

- Going back to the mailer the report replaced.
- A reporting system that anyone can browse.

The seam gains no crossing. Who is in a team or an audience stays the
estate's. What a hub-owned kind opens by default is the product's.

## What members owe

Each is that member's own design, recorded in its own repository.

| Member | It owes |
| --- | --- |
| Orrery | A report is private to its owner and admins by default, and the owner is a link the access rules walk. |
| Orrery | An owner shares a report with people, a team, or an audience, as a saved query is shared. A recipient is a share. |
| Orrery | On upgrade, each existing report becomes private and shared with its current recipients, so nobody who gets the mail loses the page. |
| Orrery | The route that serves an edition's drawn page checks the reader's access. |
| Orrery | When the owner shares, the hub says the reader will see data drawn with the owner's access. |
| Orrery | The Report kind's own description says who reads it, and it is true. |

None is built. At v1.156.3 the route that serves an edition's drawn page
judges the caller by the rule as it stands, which is the home's.

## Left open

- **Whether a subscriber is a reader.** Orrery sends a report to at most
  twenty recipients. A wider audience subscribes to the report on
  Dispatch. A subscription is the reader's act, not the owner's, so it is
  not a share. What a subscriber who may not read the report is sent is
  not settled.
- **Whether the standard's rule changes.** The standard keeps a report to
  its home team by default. This decision keeps it to its owner. The
  standard's owner rules on that.

## Consequences

- `members.md` says Orrery keeps reports, who reads one today, and what
  is owed.
- `roadmap.md` gains rows 33 to 38.
- The diagram's view of what is owed next says rows 33 to 38 change no
  flow.
- On upgrade, a person who read a report only because they saw its home,
  and who is not a recipient, stops seeing it until its owner shares it.
- An estate that closed reports with its own access settings may take
  that setting out once Orrery ships the default.
- The suite's member count does not change. No rating changes.

## Rules

Builds to:

- `keep-a-recurring-report-as-a-definition-plus-its-kept-editio`: every
  data set is read as the report's owner, so an edition is safe only
  while its readers are no wider than the owner chose.
- `leave-out-what-a-reader-may-not-see-and-never-mark-it-restri`: a
  report a reader may not read is left out of lists, search, a home's
  page, and the agent tools.
- `open-a-catalog-kind-s-entities-to-their-owners-with-a-curate`: an
  owner sees their own report through an ownership path, on a kind they
  are otherwise kept out of.
- `build-catalog-access-from-named-audiences-and-field-classes-`: a share
  names an audience the estate already keeps.
- `keep-reports-to-frozen-catalog-snapshots-and-live-series-in-` and
  `send-every-product-s-notifications-through-one-delivery-serv`: an
  edition still reaches its recipients through the one delivery service,
  and the event names only those who may see it.

Departs from:

- `keep-a-report-to-its-home-team-by-default-and-widen-it-only-`: the
  rule lets a report's home team, that team's lead, and admins read it
  by default. Here only the owner and admins do. Why: an edition is the
  owner's view, not the team's, and the rule names its own two gaps: a
  report cannot reach anyone outside its home team, and an owner outside
  the home team would not see their own report. The rest of the rule is
  kept: seeing a team never opens its reports, and widening is the
  owner's deliberate act.

New to the standard: the standard has no rule for sharing a report the
way a saved query is shared, for a recipient counting as a share, for an
upgrade that turns each report's recipients into its shares, or for
telling an owner, at the moment they share, that the reader will see data
drawn with the owner's access.
