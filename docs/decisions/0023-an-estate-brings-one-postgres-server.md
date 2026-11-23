# 0023. An estate brings one Postgres server, and each member takes a database on it

- Status: Accepted
- Date: 2026-11-22
- Standard: 2026.1120.2003
- Capture: e755e766-98f1-43f2-9078-f05a6c57d094

## Context

A member needs somewhere to keep its data. The suite has never said
whose job the database server is. `seam.md` lists what an estate brings:
a forge, sign-in, a vault, a telemetry stack. It does not list a
database.

Left unsaid, each member answers alone. A member that ships a database
cluster of its own makes the estate plan memory for that cluster on its
nodes, and pay for it, once per member.

These facts were read from each member's repository on 2026-11-22:

- **Orrery**, at v1.158.1, keeps its catalog in Postgres. It takes the
  server from one setting, and a second setting makes it sign in as the
  pod's workload identity, with no password. Its repository ships no
  chart and no database.
- **conform**, at v5.7.1, keeps a database only when an estate turns on
  its history. That database is Postgres. It takes the server by setting
  and signs in as the pod's workload identity.
- **Vantage**, at v3.1.0, keeps everything in Postgres, its only
  database. Its chart has two modes. The default runs a database cluster
  of its own in the estate's cluster, through an operator, and its deploy
  guide names two instances. The other mode takes an outside server.
  Since v2.29.0 (`46009f7`) it signs in as the pod's workload identity.
- **Dispatch** (v0.0.40), **Slipway** (v6.6.0), **redgreen** (v1.12.1),
  and **forgitten** (v0.1.9) each keep one SQLite file.
- **Tally**, at v0.0.45, keeps one SQLite file for what agents used, and
  only when an estate sets it.
- **My Apps**, at v0.0.47, has no database.
- **Ledger**, at v0.0.27, keeps its events in ClickHouse, which is
  neither.

A workload identity is the identity a cluster gives a pod, which a cloud
trusts in place of a password.

## Decision

1. **An estate brings one managed Postgres server.** Each member that
   needs Postgres takes its own database and its own role on that server.
2. **No member brings a database cluster of its own** into the estate's
   Kubernetes cluster as the way it is meant to run.
3. **A member needs Postgres only for a reason.** The reasons are two:
   more than one of its pods writes, or its design leans on what Postgres
   does. A member that fits one writer pod on one volume keeps SQLite,
   and that is not a lesser choice.
4. **A member takes the server by setting, and signs in as itself.** It
   signs in to the server as its pod's workload identity, with no
   password.
5. **The server runs as one instance, with backups.** An outage is
   accepted. A loss of data is not.
6. **High availability waits for a named trigger.** It is added when the
   application an estate builds on the suite becomes mission critical:
   when everyone spends half their working day or more inside it, or when
   commercial transactions run through it.
7. **A new feature takes a second database, never a new server.** A new
   feature inside a member that needs its own data takes a second
   database on the same server.
8. **The seam gains no crossing.** The server is one more foundation an
   estate brings. Its address reaches a member as configuration, and the
   pod's identity is the estate's to grant. This reading is a judgment.
9. **No member joins.** The suite still has ten members.

One thing was weighed and turned down: a database cluster per member.
Each member would then fail alone. But the estate would plan and pay for
the overhead once per member, and again for each new one.

The cost accepted: the members on the server go down together and
upgrade together.

Why an outage is accepted: these are internal tools. When they stop for
a few minutes, or even a day, work backs up and nobody is harmed. Lost
data cannot be worked around, so that is where the care goes.

## What members owe

Each is that member's own design, recorded in its own repository.

| Who | What it owes |
| --- | --- |
| Every member that uses Postgres | Take an outside server by setting, and sign in to it as the pod's workload identity, with no password. |
| Orrery | Nothing. It does both. |
| conform | Nothing. It does both. |
| Vantage | Sign in to its database as the pod's workload identity. Built, since v2.29.0. The proposal said it took only a password, which was true before that release. |
| Vantage | Make the estate's server the way its chart and its deploy guide say it is meant to run. This row comes from point 2 and the facts above, not from the proposal's own list. |
| Each estate | One managed Postgres server, with backups, and a database and a role on it for each member that needs one. |

## Left open

- **Whether Vantage's work tracking takes a second database.** The
  proposal asked for one, with its own role. Vantage's own record, read
  at v3.1.0, keeps an item's events in the hub's only database. And
  whether Vantage holds work at all is a proposal that waits for the
  owner's ruling. Point 7 stands either way.
- **What an estate brings for a store that is neither.** Ledger keeps its
  events in ClickHouse. This decision covers Postgres and SQLite only.
- **Which backup proves no data is lost.** The decision says a loss of
  data is not accepted. It does not say how old a backup may be, or how
  an estate proves a restore.

## Consequences

- `seam.md` lists the database server with what an estate holds, and
  with the foundations the suite does not build.
- `members.md` says where each member keeps its data.
- `strategy.md` says the suite is not a database server.
- `roadmap.md` gains rows 43 to 45, and three open questions.
- The diagram gains the estate's database server, and the three members
  that keep a database on it.
- The members on the server stop together and upgrade together.
- The suite's member count does not change. No rating changes.

## Rules

Builds to:

- `workload-identity-instead-of-cloud-keys`: a member signs in to the
  server as its pod's identity. No password or connection secret is
  added.
- `ask-for-a-paid-control-only-where-the-workload-s-criticality`: backups
  apply now. Redundancy is paid for only once the workload's class
  demands it.
- `set-rigor-by-what-a-failure-costs-in-a-few-named-classes`: the trigger
  for high availability is what a failure would cost.
- `production-availability-baseline`: the rule is aspirational, and its
  target is an availability target per class. Point 6 names the class
  that gets a second instance.
- `pick-the-backup-tier-in-the-same-change-as-new-data`: a member's new
  database is backed up from the day it is made, because the server is.
- `single-process-sqlite-with-streamed-backups-and-hourly-resto`: one
  writer on one volume keeps SQLite.
- `run-serving-and-background-work-as-two-roles-of-one-image-jo`: a
  member whose pods are joined only by the database is one that leans on
  what Postgres does.
- `keep-every-estate-on-its-own-side-of-a-seam-with-a-closed-li`: the
  list of crossings stays as it is.

Departs from:

- `production-availability-baseline`: the rule wants at least two
  instances of every backend in production. Here the server is one
  instance until the trigger in point 6. Why: an outage of an internal
  tool harms nobody, and a second instance is paid for every month.

New to the standard: the standard has no rule that an estate brings one
shared Postgres server for a suite's services, for a database and a role
per service on it, for a second database in place of a new server, for
when a service needs Postgres and when SQLite is enough, or for a named
trigger that turns high availability on.
