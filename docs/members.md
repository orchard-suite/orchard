# The members

Nine apps, each in its own repository, each belonging to one pillar and
doing one tending job first (`pillars.md` holds the six pillars, and
`garden.md` defines the jobs). Six own a pillar. Three are parts of
Catalog: Vantage, My Apps, and Muster (decision 0016). redgreen took the
name Muster, and forgitten retired into it on 2026-11-23, once Muster
held each estate's machine reports through Tender (decisions 0017 and
0025). Its hub, store, page, and CLI are gone from each estate, and its
repository is archived. One more member,
Rootstock, belongs to no pillar and stands on the floor (decision 0028).
Its section follows the apps. Facts here were
read from each repository's `README.md`, `orrery.yaml`, and manifests on
2026-11-05, the table below again on 2026-11-07, and each tending job and
the shed on 2026-11-12. Orrery's ground was read on 2026-11-12, after it
was built. Graft was read on 2026-11-12, at v4.9.4, when it joined
(decision 0009), and again on 2026-11-18, at v6.2.0, with Trellis at
v5.5.0, for decision 0010. Vantage was read again on 2026-11-20, at
v2.27.2, for decision 0014, and Dispatch the same day, at v0.0.40, for
decision 0015. Graft was read again on 2026-11-20, at v6.6.0, and each
member's pillar the same day, for decision 0016. Orrery's reports were read on 2026-11-21, at v1.156.3, for
decision 0019, and its actions engine the same day, at v1.156.4 and
again at v1.157.0, for decision 0020. Vantage was read again on
2026-11-22, at v3.1.0, for decision 0022, and each member's store the
same day, for decision 0023. Muster, forgitten, Tender, and platformkit
were read on 2026-11-23, for decision 0025. "Reads" lists the APIs an app's `orrery.yaml` says it
consumes.

## How they fit together

Orrery is the spine and the one board. It is the estate's control plane
and the console for the people who run the platform, and every other
member is an engine behind it that keeps a panel of its own (decision
0029). Most members read it, and several
write back to it. Annals is the record: the members that act post to it.

Every member pushes an inventory of what it holds into the catalog
(decision 0022). The catalog lists those things, and the member stays
their home. Six members write to the catalog today. Vantage's inventory
is owed (the roadmap).

| App | Reads | Writes to |
| --- | --- | --- |
| Orrery | the forge's actions, Annals events, Graft's jobs, Alertmanager | Annals, Dispatch (every action run, as events) |
| Vantage | Orrery's catalog | none; an inventory of its workspaces is owed (decision 0022) |
| My Apps | Orrery's catalog and actions | Orrery (its list of applications) |
| Tally | Orrery's catalog and the bill in it, Prometheus | Orrery (cost on each namespace), metrics over OTLP |
| Annals | none | none; everyone posts to it |
| Trellis | Orrery, Prometheus, Loki, Tempo, policy reports, the forge, the registry, the vault, Azure Policy | Orrery (open findings, verdicts, packs, and, when named, every rule and every waiver it weighed) |
| Muster | the forges, the identity provider (to sign in to a forge), Orrery's Argo syncs and incidents, each machine's report through Tender | Orrery (repositories, pipelines, services, deployments, issues, and each machine's checkouts) |
| Dispatch | Orrery, Alertmanager, the events products send it | Annals, Orrery (every incident), an estate's chat, mail, and text services (each product's notices, to channels and to people) |
| Graft | Orrery's actions and catalog, Dispatch's incidents, the forge (GitHub and GitLab), the agent runtime | Annals (every step of a request), Orrery (a lane's action, each plan's run, and each request as a record), Dispatch (its notices, and each release as a change), the forge (a ticket, and the commits it lands) |
| Rootstock | each environment's apply record beside its state, each cluster's controller, the forge's release tags, the registry | Orrery (environments and landing zones as inventory, owed), Annals (every apply, rollback, and environment change, owed) |

## Where each keeps its data

An estate brings one managed Postgres server. A member that needs
Postgres takes its own database and its own role on it, and signs in as
its pod's workload identity, with no password. A member that fits one
writer pod on one volume keeps SQLite, and that is not a lesser choice
(decision 0023). Read from each repository on 2026-11-22.

| App | Store | Read at |
| --- | --- | --- |
| Orrery | Postgres, on a server it takes by setting. It signs in as the pod's workload identity. | v1.158.1 |
| Vantage | Postgres. It signs in as the pod's workload identity. Its chart's default is still a database cluster of its own, and taking the estate's server is the other mode (the roadmap). | v3.1.0 |
| Trellis | Postgres, only when an estate turns on its history. It signs in as the pod's workload identity. | v5.7.1 |
| Dispatch | One SQLite file. | v0.0.40 |
| Graft | One SQLite file. | v6.6.0 |
| Muster | One SQLite file. | v3.1.0 |
| Tally | One SQLite file for what agents used, only when an estate sets it. | v0.0.45 |
| My Apps | None. Its list lives in Orrery. | v0.0.47 |
| Annals | ClickHouse. Decision 0023 does not cover it. | v0.0.27 |

## Each app

### Orrery: Catalog, and the control plane

Orrery owns Catalog. It is also the estate's control plane and its
console, which is no pillar (decision 0029). The control plane is the one
service that holds the state of an estate's things and carries out
changes to them. The console is where the people who run the platform see
everything they own and act on it, as lists and actions. A member's
common lists and actions are reached here. A business app builds its own
portal and uses Orrery as an API, an inventory, an action runner, and an
approval system. No business logic lives in Orrery.

One graph of everything an estate owns and runs, with live status on top.
Blueprints (typed schemas for one kind of thing) define every list, page,
and form. The hub ships no model of its own; pushers run inside the estate
and only connect out. It also holds the self-service actions engine: a
button hands a payload to a backend the estate runs and records the
result. Pushers today: Kubernetes and Entra ID, plus a runner.

Tending job: the board, and the hands. It draws the estate as a sky: each
area of the catalog is a sector, and each kind of thing is a planet,
coloured by its worst status. It already holds calculated fields, trends,
and scorecards, so a repository's three numbers can live on its blueprint
with no new store. A gardener acts on many repositories through its
actions.

One layer down is the ground, in preview. A blueprint has a ground when an
estate's model says which of its fields mean loop, friction, and weeds.
Each entity is then drawn as a bed, worst first. A number field may carry
a budget, and its stake leans once the number is outside it. The ground
also says where to go first, lists the templates entities were started
from and which have fallen behind, forecasts which numbers are about to
leave their budgets, and runs one action on several beds at once. A
switch shows all of it as tables under plain names. The hub ships no
ground of its own. An admin opens the view to nobody, to the people named,
or to everyone, and a new hub opens it to nobody (decision 0008).

It also keeps reports. A team defines a report once and publishes it
again and again, and each published copy, an edition, is kept. Every data
set is read as the report's owner, so an edition is the owner's view of
the data, frozen on the day it was published. A publish tells the
report's recipients through Dispatch. At v1.156.3 whoever may see a
report's home sees the report. Decision 0019 says a report is private to
its owner and admins, and the owner shares it with people, a team, or an
audience, as a saved query is shared. Naming a recipient is a share. That
is owed (the roadmap).

Decision 0020 says work that waits for a person, or runs long, is never
held by the thing that asked. Since v1.157.0 the engine can start one job
for each run: a starter the estate runs starts one container the moment
the run is approved, and the job holds its own identity. A run is given
up only when the hub has not heard from it, never because a fixed time
ran out. Each estate still owes its own starter (the roadmap).

### Vantage: Catalog, its picture

Diagrams written in YAML, laid out and scored by the engine, rendered to
SVG, PNG, or interactive HTML. A hub keeps every version, merges edits, and
pulls live inventory from Orrery through connectors, so a diagram stays
true on its own.

A hub is also the home of a system's living documents (decision 0014). A
document holds its diagrams and its pages of prose together. A page is
Markdown that names the model's boxes by id, so a rename reaches every
page. Decision records live in a hub too, beside the diagrams of the
systems they decide about.

Vantage analyzes no source code. A code analyzer is an estate's own
runner, with its own access. It publishes a first set of pages and a
diagram into the hub. After that, people and coding agents keep them
fresh, and the analyzer only reports where they and the code disagree.
Read on 2026-11-22, on its main branch after v3.1.0: a document keeps
files it never draws, a repository points at its document with one small
file, and an onboarding skill offers to write a project's first set. No
other skill reads that pointer yet (the roadmap).

Decision 0022 says a hub pushes an inventory of its workspaces into the
catalog: the members of each, how many documents and diagrams it holds,
and the storage it uses. A person sees there only the workspaces they own
or belong to. At v3.1.0 a hub reads the catalog and writes nothing to it.
That is owed (the roadmap).

Tending job: sense. It shows the shape of the system, so a trace can
follow a problem across it.

### My Apps: Catalog, its front page

The front page. One tile per application a person may open, each with live
status, and a landscape of everything the estate offers. It has no
database: its list lives in Orrery.

Tending job: sense. It is where customers arrive. It gives them no way
yet to say what they need.

### Tally: Cost

What each workload, host, agent, and job costs, in money and in capacity,
with right-sizing advice. Every collector turns on from configuration:
Kubernetes, power, Azure cost and advice, machines, AI providers, agent
token use, the bill from Orrery, and AI subscription limits.

Tending job: sense cost, and prune. Its right-sizing says what to cut
back. A shipper on each machine already posts every agent conversation's
tokens and the work it belongs to.

### Annals: Record

One record of what every person and agent did, across every product. One
event shape, append-only, shapes and ids only and never a value or a
secret. Products post through an API; people read a board; agents ask
through MCP. It records its own actions too: token changes, who was shown
people, and what retention deleted.

Tending job: sense and trace. It answers who, or which agent, did what.
It does not count where an agent got stuck.

### Trellis: Rules

One judge over an estate's standards. A standard is a pack of rules kept
as data: security, telemetry, build, interfaces, catalog, access, alerts,
delivery, and one that judges a Graft program today.
The same packs run on the board, by hand, and in a repository's pipeline, so
they cannot disagree. Every rule ships a failing, a passing, and a no-data
fixture. Waivers carry a reason, an owner, and an end date. The
access pack judges access grants and how old each application's access
review is (decision 0005).

Tending job: stake and fence. A rule on the board shows; the same rule in
a pipeline stops. Its build pack checks that a repository has an
instruction file, which is the first check of its soil.

It reads Azure Policy as a source that brings its own rules: Azure's
definitions, verdicts, and exemptions pass through, and Trellis never
judges an Azure resource again (decision 0012). One engine per property.

It is the suite's one judge (decision 0010). Its packs are an estate's
laws. It does not yet read a repository's own laws. It also judges the
map's five properties, and its rules reach one of them today (decision
0016). Each of its 99 rules still names one of the old pillars.

### Muster: Catalog, where the code is

Muster answers where the code is and what state it is in, on a forge or
on a machine. It was redgreen, and took the name at v3.0.0 (decisions 0017
and 0025). Read on 2026-11-23, at v3.1.0, in `orchard-suite/muster`.

It reads every repository, pipeline, deployment, and
issue on GitHub, GitLab, and Azure DevOps into Orrery, and has no pages of
its own. The health rules (only a failing pipeline turns a repository red,
and a repository that runs nothing stays quiet) and the four DORA measures
(deploy frequency, lead time, change failure rate, time to restore) are
calculated fields on the blueprints it offers, so Orrery is the board.
Restores come from Dispatch's incidents in the catalog. Decision 0004.
A fifth measure, rework rate, is owed (decision 0016).

It takes each machine's report through Tender, the suite's device agent,
at `/tender/v1/readers/muster`, behind the `device` door from platformkit.
A report holds names and counts, never a file's name or contents. Muster
writes it as `sw_checkout` records, one for each repository on each
machine, linked to the repository's record and to the machine's.
A checkout is private to the machine's person and the estate's admins.
Muster writes none until the estate sets that access rule. Each
repository's record carries `machines_with_unseen_work`: the machines
that hold work its forge has not seen. Muster's reader is the module
`github.com/orchard-suite/muster/reader`, at `reader/v1.0.0`, and Tender
carries it.

It takes only the `device` package from platformkit (decision 0025).
Otherwise it stays off the kit (decision 0004).

Tending job: sense, and prune. It writes each pipeline's median duration, 30-day
success rate, and a flaky flag, which is most of a repository's loop
number. The delivery measures are the guard on the other three. Its
checkouts show the stranded work a gardener lands or clears away.

### Dispatch: Health

The incident desk. Alertmanager's webhook, or anything that posts JSON,
opens incidents. Each has an owner, a state, and a timeline, and the desk
exports time to acknowledge and time to restore. After an incident is
resolved it holds a postmortem and its action items.

It is also the one place a product's notices go out from (decision 0015).
A product sends an event. Dispatch posts it to the channels that
subscribe to it, and tells the people, groups, and on-call chains it
names, through the apps they already have: chat, email, and text
messages. A person named in an event gets a chat from Dispatch's bot, one
to one. Every message is stored before it is sent, and keeps the answer
it got. A product keeps no chat or mail code of its own.

It speaks as one bot today. Decision 0015 says it will speak as more than
one: a product whose readers are not the platform team gets a bot named
for the product. A sender cannot yet read how each of its deliveries
went. Both are owed (the roadmap).

Tending job: trace. An incident is a weed, and its postmortem is the
trace back to what caused it.

### Graft: Change

A request desk for software that already exists. A person reports a
problem or asks for a change, from Graft's page or from inside an
application. Graft answers with an explanation, a ticket, or a tested
change that is released.

A request enters a lane: who is asking. A lane sets how much a request may
do with no person in the way. An admin names each lane's members in a
program file, with the repositories, their protected paths, and who
approves a plan. One agent investigates in a clone and holds no
credential. It takes the request as evidence, and checks each claim in it
against the code and its history. It writes a verdict and a plan in two
documents: a brief its approvers read in two minutes, and a build plan its
builder follows. In a lane whose plans wait, a
feature, or any change in behaviour, waits for the program's approvers,
and each answer they give is the plan's next round. The person who asked never decides it. A second
agent builds the approved plan.

A machine judges the diff, not what the agent says about it. A clear
defect lands unasked only in a lane an admin marks, and only when a new
test fails without the fix, no test that was there is edited or deleted,
no protected path is touched, no dependency or data shape changes, and the
change is under a size limit. Graft lands the commits from its own
clone, watches the pipeline, and takes its commits back out past its last
round. A new feature ships switched off. It has no review gate of its own.

Since v6.6.0 a build lands only when its builder says it is finished and
each criterion of its plan is proven, by a test, a screenshot, or an
approver's waiver. A stage that fails stalls and keeps its work, and an
approver retries it on the same request. Only a green pipeline counts as
released. Graft keeps what each agent run spent, and writes each
request's spend to its catalog record by stage.

It reaches the forge and the agent runtime through adapters: GitHub and
GitLab, and one runtime. The template and the build-from-an-idea job that
decision 0009 removed are gone.

Tending job: fix. It is the hands that change a bed. It changes one
repository per request. It is also where the suite already bounds a
change: by size, by path, by plan, and by an undo (decision 0010), and
where a request is weighed before anything is built (decision 0011).

## Rootstock: the floor

Rootstock is the deploy tool and the environment tool the suite offers
(decision 0028). It answers no pillar, and nothing requires it: no member
needs it to run or to be deployed, and it needs no member to deploy
anything. That is what lets it deploy the suite itself. It works on the
forge, pipelines, builders, registries, and cloud an estate brings, and
hosts none of them.

It has three parts:

- `infra` plans and applies Terraform from an image of the project's
  commit, keeps an apply record beside each environment's state, and runs
  a drift job that puts back what the last apply set. It asks Orrery for
  approval when the estate runs it. Read on 2026-11-23, at v2.15.2, in its
  own repository.
- `dev` stands up an environment from one file, on a person's machine or
  in a cluster, through a controller in the cluster that keeps the
  cluster's record of environments. Read on 2026-11-23, at v4.12.0, in its
  own repository.
- The hub, one per estate, owed. It shows the whole fleet: every landing
  zone, infrastructure environment, cluster, and application environment,
  the version each runs, the version ready, its runs, its drift, and the
  version of each shared module it runs. It reads the apply records and
  the controllers, and replaces neither. It serves one `/v1` API and the
  one web panel.

The two programs move into one repository, `orchard-suite/rootstock`,
each keeping its own version (the roadmap).

Tending job: sense, for the fleet. It also plants: it is the hands that
deploy the platform.

## The shed

Tending tools that are installed on a machine, not run as a service. They
are not members and do not take the membership test (decision 0007,
`seam.md`). Each is listed with the tending job it does.

| Tool | What it is | Tending job |
| --- | --- | --- |
| climb | A CLI that improves one measured number in a repository, and keeps only real gains. | Stake and prune: it works against a fixed measurement. |
| Rudder | A desktop app that maps, scores, and tunes a repository's agent instruction files. | Soil: it ranks what to delete as well as what to add. |
| release-damnit | A release tool and a landing command with a commit check. | Fence and loop: every change lands the same way. |
| Observatory | A local dashboard of events from agents as they work. | Sense: one machine's agents, live. |
| platformkit | A library the members build on. Since v3.1.0 it holds the `device` package, the door a member puts in front of a device's posts (decision 0025). Every member, shed tool, and estate app takes it as a public module by version, and nothing vendors it ([[decision:ORC-5001]]). | Seed stock: the door, telemetry, and Annals client a new service starts with. |
| hedge | A CLI and an agent hook that keep an estate's names out of every repository that may not hold them, on every write, commit, push, and post, against a register the estate keeps private (decision 0024). | Fence: the seam itself, in the path of work. |
| pipelines | The pipeline kit, in `orchard-suite/pipelines`, owed. Reusable workflows per kind of bed, and one action that signs, attests, verifies, and tags an image. Every member calls it at a major version, and an estate may (decision 0026). | Fence and loop: every pipeline has one shape, and a release waits only for what its class needs. |
| Tender | The suite's one device agent, in `orchard-suite/tender`, built, at v0.0.2. It runs as the person and carries Muster's reader. Each reader stays off until the estate gives it an address. It asks a member before it posts, signs each post with the device certificate's key from the operating system's store, saves its place, and sends again after a failure. An estate with no device management enrolls a machine by sign-in with a step-ca authority, and Tender renews only a certificate it enrolled. It never updates itself (decisions 0018 and 0025). | Sense: what exists only on a machine. |

## What is not a member

These are built by the same hands but are not suite apps. They are tools,
side projects, or apps that use the suite. Some of them are in the shed
above; the shed is a list of tending tools, not a kind of membership.

| Tool | Why it stays out |
| --- | --- |
| platformkit | A library, not a service. Five members build on it (My Apps and Tally on v1.3.2; Annals, Dispatch, and Graft on v3.0.0, read on 2026-11-23). Muster takes only its `device` package, at v3.1.0. In the shed. |
| hedge | A guard installed on a machine, not a service. In the shed. |
| release-damnit | A release tool for one way of working, not a platform service. In the shed. |
| climb, Rudder, Observatory | Installed tools, not services. In the shed. |
| Tender | An agent installed on a machine, not a service. In the shed (decisions 0018 and 0025). |
| Ion | An agent runtime. Graft drives it today. An estate brings its own runtime (decision 0009). |
| SlopDrop | A personal hand-off box. |
| cli-proxmox | A CLI for one hypervisor. |
| posture | Retired. Its rules are Trellis's security pack. |

An estate's own apps, such as a household assistant or a household portal,
consume the suite. They are never members.
