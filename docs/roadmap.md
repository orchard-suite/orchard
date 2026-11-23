# Roadmap

What the suite still owes, and what is done. This page is derived. A row
comes only from a decision record or from the build order in `pillars.md`.
Nobody adds a wish here: a new row needs a decision first (decision 0013).

Each row names who owes it. The work itself is that member's own design,
recorded in its own repository.

A row has one of three states:

- **Owed**: decided, and not built.
- **Partly**: some of it is built. The row says which part.
- **Done**: built. The row names the version or commit that proves it.

"Checked" is the day the state was last read from the member's repository,
or the day of the decision that recorded it. A state older than its check
is a guess.

## The order

The sections below are in the order the work should go.

1. **Sense.** The build order puts it first (decision 0007).
2. **The map.** It builds nothing. It renames, and renaming gets dearer
   with every rule written to the old names (decision 0016).
3. **Fence.** A bed's laws need the numbers that say what a check costs
   and catches.
4. **One shape.** The last four steps of the build order.

Documents, Notices, Reports, Jobs, Inventory, Data, and the section on
Muster and Tender come from decisions that stand alone. They wait on nothing
above, so their members build them when they choose.

## Sense

The numbers behind two outcomes, flow and quality (`pillars.md`). A
gardener cannot tend what it cannot see.

| # | What is owed | Who owes it | From | State | Checked |
| --- | --- | --- | --- | --- | --- |
| 1 | Count where growers get stuck: retries, stops, redirects, and failed tool calls per session, as plain numbers on each repository. | A new, small source. It is not admitted yet. | 0008 | Owed. No source has a repository yet. | 2026-11-21 |
| 2 | Loop, friction, and weeds as fields on each repository, beside the delivery measures. | Orrery and Muster | 0007, 0008 | Partly. Muster writes each pipeline's median duration, and Orrery keeps a budget beside a number. Friction and weeds have no source. | 2026-11-20 |
| 3 | Open the ground view to everyone. | Each estate, on its own hub | 0008 | Partly. Built, and still in preview at Orrery v1.156.3. | 2026-11-21 |
| 4 | Offer the cost of checking, catches, and the class as fields an estate's model may name. | Orrery | 0010 | Owed | 2026-11-20 |
| 5 | Write which check failed, per run, so catches can be counted. | Muster | 0010 | Owed | 2026-11-20 |
| 6 | Tell an agent session that checks from one that builds, for sessions outside the desk. | Tally | 0010, 0011 | Owed | 2026-11-20 |
| 25 | Count rework rate, the fifth delivery measure: the share of deployments that are unplanned and happen because of an incident in production. | Muster and Orrery | 0016 | Owed | 2026-11-20 |
| 26 | Show the three outcomes for a whole estate, from the numbers each repository carries. | Orrery | 0016 | Owed | 2026-11-20 |

## The map

Six pillars, five properties, and three outcomes replace fourteen pillars
(decision 0016). These documents use the new map already. The members do
not, and until they do a reader meets both sets of names.

| # | What is owed | Who owes it | From | State | Checked |
| --- | --- | --- | --- | --- | --- |
| 21 | Have each rule name one of the six pillars or one of the five properties, in place of the pillar it names today. | Trellis | 0016 | Owed. Its 99 rules name seven of the old pillars, at v5.7.1. | 2026-11-22 |
| 22 | Name one pillar in the member's own description file. | Every member | 0016 | Owed. Eight members name two to five of the old pillars. Orrery and forgitten name none. | 2026-11-22 |
| 23 | Rename the pillar records in the estate's own catalog, once Trellis writes the new names. | Each estate, on its own hub | 0016 | Owed | 2026-11-20 |
| 24 | Judge all five properties. | Trellis | 0016 | Partly. Its interfaces pack judges the shape of an HTTP API, which is part of two doors. No rule judges run as a product, self-service, one kit, or decided on purpose. | 2026-11-20 |

## Fence

| # | What is owed | Who owes it | From | State | Checked |
| --- | --- | --- | --- | --- | --- |
| 7 | Read a repository's laws and their last results as facts, and judge them. Judge whether a change to a law path was an owner's. | Trellis | 0010 | Owed | 2026-11-20 |
| 8 | Read a bed's class. Hold decision records and law paths as protected in every program. | Graft | 0010 | Owed. At v6.6.0 a program protects the repository file and the paths its admin lists. | 2026-11-20 |
| 9 | Take a failed request's landed commits back out, or say on the request what it left on main. | Graft | 0011 | Done. v6.6.0. A build that fails its gate, or is not finished and proven, stalls and never reaches the forge. A landed change whose pipeline is not green stalls the request, and the ticket links the commit and each failed job. | 2026-11-20 |
| 10 | Say which checks the gate ran. | Graft | 0011 | Partly. At v6.6.0 a repository names its check in its own file, the builder is told the command, and a failed gate names it. A gate that passes does not say what ran. | 2026-11-20 |
| 11 | Let a postmortem name the law that would have caught the incident. | Dispatch | 0010 | Owed | 2026-11-20 |

## One shape

| # | What is owed | Who owes it | From | State | Checked |
| --- | --- | --- | --- | --- | --- |
| 12 | One CLI shape and one token story across the members. | Every member | Build order, step 5 | Owed. Orrery, Vantage, Tally, and Trellis each ship a CLI of their own. | 2026-11-21 |
| 13 | Move the members that are not on the shared kit onto it. | Those members | Build order, step 6 | Owed. Five of ten build on it. | 2026-11-20 |
| 14 | Put the forge behind an adapter, as Muster and Graft already do. | Trellis | Build order, step 7 | Owed. Its one forge source is GitHub, at v5.6.1. | 2026-11-21 |
| 15 | Post every act to Annals. | Every member that acts | Build order, step 8 | Owed | 2026-11-21 |

## Documents

A hub holds a system's living documents, and a code analyzer is an
estate's own runner (decision 0014).

| # | What is owed | Who owes it | From | State | Checked |
| --- | --- | --- | --- | --- | --- |
| 16 | Keep an attached file that is versioned and downloadable but never drawn, and let a tool read it back from the newest version. | Vantage | 0014 | Done. `702128e`, on its main branch after v3.1.0: a document lists files it keeps and versions and never draws, and a tool reads one back as text or as bytes. | 2026-11-22 |
| 17 | Read a pointer file a code repository carries (`vantage.yaml`: the hub, the workspace, the document), in the plugin. | Vantage | 0014 | Partly. At `397f5d7`, after v3.1.0, the onboarding skill writes the file and the plugin's session hook checks that it is there. No other skill reads the hub, the workspace, or the document out of it. | 2026-11-22 |
| 18 | Ship an onboarding skill that sees a project has no documents in the hub and offers to write the first set. | Vantage | 0014 | Done. `397f5d7`, on its main branch after v3.1.0: a session hook says when a repository has no pointer file, and the skill offers once and writes the first set. | 2026-11-22 |

## Notices

Dispatch is the one place a product's notices go out from (decision
0015).

| # | What is owed | Who owes it | From | State | Checked |
| --- | --- | --- | --- | --- | --- |
| 19 | Accept an event addressed to a person and deliver it to that person in Teams, one to one, with delivery status the sender can read. | Dispatch | 0015 | Partly. Dispatch takes an event addressed to a person and messages them in Teams as its bot, at v0.0.40. A sender cannot read how the delivery went. | 2026-11-20 |
| 20 | Serve more than one bot, each with its own identity and Teams app, and pick the bot by the product that sends. | Dispatch | 0015 | Owed | 2026-11-20 |

## Muster and Tender

redgreen and forgitten become one member, Muster (decision 0017). The
suite gets one device agent, Tender, in the shed (decision 0018). Both
are built together, and forgitten retires once Muster holds each
estate's machine reports (decision 0025).

| # | What is owed | Who owes it | From | State | Checked |
| --- | --- | --- | --- | --- | --- |
| 27 | Take what a machine reports and write unpushed work onto each repository's record in the catalog. | Muster | 0017, 0025 | Done. Muster 3.1.0 writes each report as `sw_checkout` records and counts `machines_with_unseen_work` on each repository. | 2026-11-23 |
| 28 | Retire forgitten's hub, store, page, and CLI once Muster holds what they hold, and take the new name. | Muster and forgitten | 0017, 0025 | Partly. Muster took the name at 3.0.0; forgitten's hub, store, page, and CLI retire once each estate's machines report. | 2026-11-23 |
| 29 | Build Tender: readers that stay off until given an address, a question before it sends, a certificate as its identity, a saved place, and sending again. | Tender, a new tool in the shed | 0018, 0025 | Done. Tender 0.0.2, in `orchard-suite/tender`. | 2026-11-23 |
| 30 | Offer its reader as a small module, take a reader's posts at a door that checks a device certificate, and stop installing its server on machines. | Tally | 0018 | Owed. `tally ship` is the server program in another mode, at v0.0.45. | 2026-11-20 |
| 31 | Offer its reader as a small module, and the same door. | Muster | 0017, 0018, 0025 | Done. The reader module at `reader/v1.0.0`, and the `device` door from platformkit 3.1.0, at Muster 3.1.0. | 2026-11-23 |
| 32 | Issue device certificates from its own device management, and push the list of addresses for the members it runs. | Each estate | 0018 | Owed | 2026-11-20 |

## Reports

A report in the catalog is private to its owner, and shared by the
owner's act (decision 0019).

| # | What is owed | Who owes it | From | State | Checked |
| --- | --- | --- | --- | --- | --- |
| 33 | Keep a report, and every edition of it, to its owner and admins by default, and make the owner a link the access rules walk. | Orrery | 0019 | Owed. At v1.156.3 whoever may see a report's home sees it, and the owner is a field. | 2026-11-21 |
| 34 | Let an owner share a report with people, a team, or an audience, as a saved query is shared. A recipient is a share. | Orrery | 0019 | Owed | 2026-11-21 |
| 35 | On upgrade, make each existing report private and shared with its current recipients, so nobody who gets the mail loses the page. | Orrery | 0019 | Owed | 2026-11-21 |
| 36 | Check the reader's access on the route that serves an edition's drawn page. | Orrery | 0019 | Owed. At v1.156.3 the route judges the caller by the rule as it stands, which is the home's. | 2026-11-21 |
| 37 | Say, when the owner shares, that the reader will see data drawn with the owner's access. | Orrery | 0019 | Owed | 2026-11-21 |
| 38 | Have the Report kind's own description say who reads it, and be true. | Orrery | 0019 | Owed. At v1.156.3 it says anyone who may see the home reads it. | 2026-11-21 |

## Jobs

Work that waits for a person, or runs long, is never held by the thing
that asked for it. The actions engine starts one job for each run
(decision 0020).

| # | What is owed | Who owes it | From | State | Checked |
| --- | --- | --- | --- | --- | --- |
| 39 | Start one job for each run from the actions engine: a backend, a starter for a cluster and one for a cloud's job service, runs that live by heartbeat, and a credential good for one run. | Orrery | 0020 | Done. v1.157.0 (`306f872`): a `job` backend, a starter for a Kubernetes cluster and for one cloud's job service, runs given up only when the hub has not heard from them, and a credential good for one run. | 2026-11-21 |
| 40 | Run a starter, give jobs a place to run, and give each family of job its own identity. | Each estate | 0020 | Owed | 2026-11-21 |

## Inventory

Every member pushes an inventory of what it holds into the catalog. The
catalog lists it, and the member stays its home (decision 0022).

| # | What is owed | Who owes it | From | State | Checked |
| --- | --- | --- | --- | --- | --- |
| 41 | Push its workspaces, their members, document and diagram counts, and storage used into the catalog, linked to person records, readable by membership. | Vantage | 0022 | Owed. At v3.1.0 a hub reads the catalog and writes nothing to it. Its spec says the pusher waits for kinds in the catalog for a workspace and an item. | 2026-11-22 |
| 42 | Push an inventory of the records it holds. | Every other member that holds records of its own and does not push them yet | 0022 | Owed. Not checked member by member. `members.md` lists Annals and forgitten as writing nothing to the catalog, and row 27 covers what a machine reports. | 2026-11-22 |

## Data

An estate brings one managed Postgres server, and each member that needs
Postgres takes its own database and role on it (decision 0023).

| # | What is owed | Who owes it | From | State | Checked |
| --- | --- | --- | --- | --- | --- |
| 43 | Take the estate's Postgres server by setting, and sign in to it as the pod's workload identity, with no password. | Every member that uses Postgres | 0023 | Done. Orrery v1.158.1 and Trellis v5.7.1 do both. Vantage has since v2.29.0 (`46009f7`). | 2026-11-22 |
| 44 | Make the estate's server the way its chart and its deploy guide say it is meant to run, in place of a database cluster of its own. | Vantage | 0023 | Owed. At v3.1.0 the chart's default is a cluster of its own, run by an operator, and the deploy guide names two instances. | 2026-11-22 |
| 45 | Bring one managed Postgres server, with backups, and give each member that needs one a database and a role on it. | Each estate | 0023 | Owed | 2026-11-22 |

## Open source

Every member and the suite's own shed tools are public in
`orchard-suite`, and hedge holds the seam (decision 0024).

| # | What is owed | Who owes it | From | State | Checked |
| --- | --- | --- | --- | --- | --- |
| 46 | Move to a public repository in `orchard-suite`, from today's files with a fresh history, with its full CI on hosted runners. | Every member | 0024 | Done. Orrery 2.0.0, Vantage 4.0.0, My Apps 1.0.0, Tally 1.0.0, Annals 1.0.0, Trellis 6.0.0, Dispatch 1.0.0, Graft 7.0.0, forgitten 1.0.0, Muster 2.0.1, as redgreen. | 2026-11-23 |
| 47 | Keep a private register of its names and its zones, and run hedge on every machine its people and agents work on. | Each estate | 0024 | Owed | 2026-11-23 |
| 48 | Judge hedge's findings in every repository it reads: `hedge audit --facts` through Trellis's command source, and a rule in its own pack. | Each estate | 0024 | Owed | 2026-11-23 |

## Open questions

These are not owed work. Each needs a decision before it can become a row.
They are listed where they were left open.

| Question | Left open by |
| --- | --- |
| Where friction sensing lives, and whether its reader shares code with Tally's | 0007, 0008 |
| Which weeds get a source | 0008 |
| Where the list of law paths lives, so Graft and Trellis read one list | 0010 |
| How a pipeline knows an owner changed a law, outside the desk | 0010 |
| Whether break-it runs get a source | 0010 |
| Whether a request weighed outside the desk gets an investigator, a brief, and rounds | 0011 |
| How a desk asks for an environment its gate can run a check in | 0011 |
| Where a person reads what a code analyzer found | 0014 |
| Whether a medium Dispatch sends through is a crossing of the seam | 0015 |
| Whether the standard takes the map of six pillars, five properties, and three outcomes | 0016 |
| How adoption is counted, and who counts what an agent chooses | 0016 |
| Whether Health gets a proof that a thing comes back, ahead of a failure | 0016 |
| Whether friction is counted by a reader in Tender | 0008, 0018 |
| Whether a person who subscribes to a report on Dispatch is a reader of it | 0019 |
| Whether the standard keeps a report to its home team or to its owner | 0019 |
| How a run that ends wakes the agent that asked for it | 0020 |
| Where a conversation with an agent lives when no machine is awake | 0020 |
| Whether Vantage holds work items, and so pushes them with its inventory | 0022 |
| Whether Vantage's work tracking takes a second database on the estate's server | 0023 |
| What an estate brings for a member whose store is neither Postgres nor SQLite | 0023 |
| Which backup proves that no data is lost, and how old it may be | 0023 |

One question is closed. Decision 0010 asked whether the standard takes the
pillar on quality. It did, at version 2026.1120.2003. Decision 0016 has
since made quality an outcome, and asks the standard a larger question.
