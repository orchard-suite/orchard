# Strategy

## The problem

A platform is the place where other people's software grows. Its
customers, people and agents, copy what they find there. What they make
becomes what the next one finds. So quality compounds, up or down, and
someone has to tend it.

Tending starts with seeing. A gardener asks the same questions every day.
What do we have? What does it cost? Is it healthy? Is it safe? Are we
shipping? Who, or which agent, changed what?

Then it asks the questions the old tools never did. Where do growers
struggle? What taught this mistake? Is the loop fast? What should be cut
back? A grower is whoever changes a repository: a person, or an agent
session. Agents make these questions urgent. An agent copies a bad example
faster than a person, pays a slow test loop on every change, and never
sends a support ticket to say it was stuck.

Agents also change what quality costs. Writing a change is now cheap.
Reading every change is not, and a second agent that reads the first one's
work is paid on every change and shares its blind spots. So a gardener asks
one more question: does each change stay inside what its owners said must
hold, and is each check worth what it costs?

The market answers each question with a separate product, priced for a
large company, and the products do not share a model of the estate. Some
questions it barely answers at all, such as what each agent conversation
cost, what every agent did across every tool, or where agents get stuck. A
small team, or one person, ends up spending its time on the platform
instead of on what it wanted to build.

## The bet

Build a small suite that does the tending job together, and nothing else.
Agents make a focused product cheap to build and cheap to keep correct.
One catalog under all of them makes them one system instead of ten
islands.

Orchard is that suite. With it, a person tends the platform in the time
left over, and spends the rest building their own applications, at home or
at work.

## What Orchard is

- **A gardener's tools, not a platform in a box.** Each member is its own
  repository, release, and service. An estate runs the ones it needs.
- **One job.** Every member helps sense, trace, fix, stake, fence, or
  prune. `garden.md` defines those words and rates what the suite covers.
- **One map.** Six pillars, each with one owner among the members. Six
  properties every pillar must have. Three outcomes the whole is for:
  flow, quality, and adoption. `pillars.md` rates each one (decisions
  0016 and 0030). The six pillars are the six questions this page opens with.
- **Joined by the catalog.** Orrery is the spine. The others read it,
  describe themselves to it, and write their findings back to it. Each
  pushes an inventory of what it holds, and stays the home of its own
  records (decision 0022).
- **One control plane, and one console.** Orrery is the estate's control
  plane: the one service that holds the state of an estate's things and
  carries out changes to them. It holds the model, the inventory, the
  actions, the approvals, the schedules, the reports, and the scores, in
  one product. It is also the console: the desk where the people who run
  the platform see everything they own and act on it. In the console
  everything is a list or an action (decision 0029).
- **Engines, each with a panel of its own.** A member feeds Orrery what
  it holds and offers what it can do as actions there. It also keeps its
  own pages, shaped for its purpose: its data, its settings, its
  analytics, its administration, and the views a list and an action
  cannot give. The console's action and the member's panel call the
  member's one API. A member whose whole job fits its API may have no
  panel. Where a member has pages, they are as good as Orrery's, and
  members are the same wherever they can be (decision 0029).
- **Built for the agent first.** An agent reaches a member through its
  agent tools and its API, and a person through its pages. So every
  member is held to the cost of a local disk: finding one fact, reading
  one part, or changing one sentence costs an agent no more than the same
  task on a file. A write sends what changed, a read answers what was
  asked, and a benchmark in each member's own check holds the bar. This
  is the map's sixth property (decision 0030).
- **One core.** Every member's server is Go. Orrery and Vantage are
  TypeScript today, and each is re-cored in Go in one release that
  changes no behavior, after a freeze. Their web apps stay TypeScript
  (decision 0035).
- **One gate.** Sign-in, sessions, tokens, and the agent door's sign-in
  server are written once, in Go, in the kit, and every member links
  them in (decisions 0033 and 0035).
- **Sized for a company, not a household.** Every member is designed and
  measured for one estate of 150 people after ten years: a million things
  in the catalog, a hundred changes a second, a hundred thousand diagrams.
  A small estate is where a change is tried, never proof that a member is
  fast enough. Every kind of record says whether it levels off or grows
  without end, and if it grows, how it ages out (decision 0034).
- **Actions, not a command line.** A command line that only calls a
  member's API is a tool for operations, and the console's actions take
  its place. A command line stays where it works on the files of the
  machine it runs on, or runs inside a container for a pipeline or a
  workflow (decision 0029).
- **One board.** Orrery shows the whole estate as a sky, and each
  repository as a bed on the ground beneath it. The ground is in preview:
  an admin opens it to the people named. The suite builds no master app
  that replaces its members' own pages. A gardener acts on many beds
  through Orrery's actions, and opens a member for what only its panel
  shows (decision 0029).
- **One pair of hands.** Graft takes a request to change a repository
  that exists. An agent makes the change, and Graft lands it and watches
  it ship (decision 0009).
- **No seeds of its own.** A template a new repository starts from carries
  an estate's own choices. It stays with the estate, and an Orrery action
  plants it (decision 0008).
- **Recorded in one Annals.** What a person or an agent does through any
  member lands in Annals, in one shape.
- **One judge, and bounds before opinions.** Trellis judges an estate's
  laws and each bed's laws. A change is held by its size, the paths it may
  touch, the laws it must keep, and how it is undone. A request is
  evidence, not a specification, and an owner judges a plan, never the
  code. `quality.md` is the framework (decisions 0010 and 0011).
- **Estate-neutral.** The same build runs in any estate. The seam in
  `seam.md` keeps each estate's facts on its own side.

## What Orchard is not

- **Not a forge or a build system.** Bring GitHub, GitLab, Azure DevOps,
  or Bitbucket, and their pipelines.
- **Not an identity provider or a secrets store.** Bring your sign-in and
  your vault. The platform guide advises against building
  either (principle `new-capability-goes-to-a-standalone-product-not-the-house-vi`).
- **Not an observability stack.** Bring Prometheus, Loki, Tempo, Grafana,
  or their equal. Orchard sends to it and reads from it.
- **No deploy tool you must use.** The suite offers one, Rootstock, on
  the floor (decision 0028). Bring Argo CD, Flux, or your pipelines in its
  place, and Orrery's actions can ask them to act. No member requires
  Rootstock.
- **No tool installer you must use.** The suite offers one, Toolshed, on
  the floor (decision 0042). It says what may run on each kind of
  machine, and hands signed packs to the device management,
  configuration tool, and base images the estate already runs. It
  installs nothing itself, and no member requires it.
- **Not a database server.** Bring one managed Postgres server. Every
  member that holds data takes a database and a role on it, so any member
  can run two copies and roll with no downtime. No member supports two
  stores (decisions 0023 and 0036). The server is shared, and a member
  takes a managed server apart only for one of two reasons: it must stay
  up when the shared server is down or busy, or its load, measured at the
  scale target, starves the others (decision 0037). A server apart is a
  step on the scaling path: no estate brings one until the need is real
  or near, and Dispatch, the first expected to take it, stays on the
  shared server until then (decision 0038).
- **One name, and one staged move.** Everything an estate deploys for a
  member carries the member's name, and an older name is retired. An
  estate builds the new beside the old, moves data by a checked copy,
  and cuts over in one short planned window. The old stays untouched as
  the way back (decision 0039).
- **Not a message broker.** Bring one once two members are joined:
  Azure Service Bus, RabbitMQ, or their equal. Every event travels on
  it. A member saves each event with the change that made it, so none is
  lost, and a new reader subscribes with no change to a sender. Orrery
  holds what is, and the broker carries what happened (decision 0032).
- **Not a home for several organizations.** The estate is the tenant.
  One copy serves one organization. Inside it, a scope is the owner of a
  thing, the same in every member (decision 0031).
- **Not an agent runtime.** Bring the runtime. The suite senses what
  agents do and shapes the beds they work in. Graft starts agent
  sessions on the runtime an estate brings, and the suite builds none
  (decision 0009).
- **Not a test runner or a code reviewer.** Bring your test tools and
  your break-it engine. Bring the tool that stands up an environment, or
  take Rootstock's (decision 0028). The suite judges what they report. No member gates a change
  on a person's or a model's opinion of the code (decision 0010).
- **Not a controller.** Nothing in the suite changes a repository on its
  own. A person or an agent starts an action, and the action is recorded.
  Graft is held to this: it changes a repository only when asked.
- **Not a server on a person's machine.** What a member reads from a
  machine comes through one small device agent, Tender, which only
  reports (decisions 0018 and 0025).
- **Not a home for personal apps.** An app for one person or one family is
  a private app that may use the suite. It never joins it.
- **Not a portal for a business, and not an ERP.** An app an estate
  builds for its business has its own pages and its own rules. It uses
  Orrery as an API, an inventory, an action runner, and an approval
  system. No business logic lives in Orrery: it knows that a thing
  exists, who owns it, how it is doing, and what may be done to it
  (decision 0029).

## How it grows

1. **Sense friction first.** `garden.md` rates each tending job. Friction
   is the one number nothing measures: how often a grower gets stuck. A
   gardener cannot tend what it cannot see. A new, small source will count
   it and write it to the catalog, with no pages of its own (decision
   0008). It is not built.
2. **Give every bed its three numbers.** Loop, friction, and weeds, as
   plain fields on each repository in the catalog, with the five delivery
   measures as the guard.
3. **Show the ground.** Orrery has a ground view under its sky, in
   preview, so a gardener sees where to go first. Next it opens to
   everyone.
4. **Give every bed its laws.** Trellis reads which of a repository's
   checks are laws and judges them. Each bed carries what its checking
   costs and what each check caught, so a check that guards nothing is
   pruned (decision 0010). None of this is built.
5. **Close the gaps on the map.** `pillars.md` rates each pillar, each
   property, and each outcome. The weakest go next. The members move to
   the map's names first, because that is only renaming and it gets dearer
   the longer it waits (decision 0016).
6. **Close the seam.** `seam-audit.md` lists where members still name an
   estate or depend on one forge. Each row is fixed in the member's own
   repository.
7. **One shape.** Once the kit gives every member's API the same shape,
   build generated SDKs over all of them, and one docs site. No command
   line is built over them: the console's actions do that job (decision
   0029).
8. **Admit carefully.** A new member passes the test in `seam.md` and
   joins by a decision record. Most tools will not.

The roadmap lists each thing these steps and the decisions leave owed, who
owes it, and whether it is done. A decision made in any conversation
reaches this repository as a proposal and is folded into a record without
the owner carrying it (decision 0013). The records and the roadmap live in
a hub, and `vantage.yaml` names them (decision 0027).

## What is still open

Decision 0007 left three questions open. Decision 0008 settles them: a
new, small source counts friction, seeds stay with each estate, and the
suite maps a thirteenth pillar, growing conditions. Decision 0016 has
since made growing conditions part of two outcomes.

Decision 0008 leaves three smaller ones: the friction source's name and
whether its reader shares code with Tally's, which weeds get a source, and
when an estate opens the ground view to everyone.

Decision 0009 admitted Graft and left one: whether a request to Graft
changes the rating of platform as a product. Decision 0011 settles it. The
suite now listens, and the pillar stays Partial because two apps share its
question.

Decision 0010 sets how the suite answers for quality and leaves four:
where the one list of law paths lives, how a pipeline knows an owner
changed a law, whether break-it runs get a source, and whether the
guide takes the pillar.

Decision 0011 puts the start of quality at the request and leaves two: how
a request is weighed outside the desk, and which checks a desk's gate can
run.

Decision 0016 replaces the fourteen pillars with six pillars, five
properties, and three outcomes. It closes one question of decision 0010:
the guide took the pillar on quality, and the suite has since made
quality an outcome. It left four: whether the guide takes the new
map, how adoption is counted, whether Health gets a proof of recovery,
and whether Change keeps two apps. Decision 0020 has closed the last.

Decision 0017 merges redgreen and forgitten into one member, Muster. The
suite has ten members until forgitten retires, and nine after. It left
three questions: which repository holds Muster, whether it builds on the
kit, and how much of a machine's scan is kept.

Decision 0018 gives the suite one device agent, Tender, in the shed. No
member's server is installed on a person's machine. A machine proves
itself with a certificate its estate issues. It left five: whose
certificate that is, where the member's door lives, how Tender updates,
whether friction is one of its readers, and what an estate with no device
management does.

Decision 0025 settles all of these but friction. Muster is redgreen's
public repository, renamed. It takes only the kit's `device` door. A
report keeps counts and branch names, never file names. Tender runs as
the person, with a certificate that names the person and the device. It
never updates itself. An estate with no device management runs a small
certificate authority of its own, and each machine enrolls once by
sign-in. Where friction is sensed stays open (decision 0008).

Decision 0020 says work that waits for a person, or runs long, is never
held by the thing that asked. The actions engine starts one job for each
run, and a run lives by heartbeat. It closes the question on Change: two
apps, with a fixed line between them. It leaves two: how a run that ends
wakes the agent that asked, and where a conversation with an agent lives
when no machine is awake.

Decision 0022 says every member pushes an inventory of what it holds
into the catalog, and the catalog is never the store for a member's own
records. It leaves two: which members still owe an inventory, and whether
Vantage holds work items.

Decision 0023 says an estate brings one managed Postgres server, and
each member that needs Postgres takes a database on it. The server is one
instance with backups, until what an estate builds on the suite becomes
mission critical. It left three: whether Vantage's work tracking takes
a second database, what an estate brings for a store that is neither
Postgres nor SQLite, and which backup proves no data is lost. Decisions
0036 and 0040 have closed the second: no member keeps such a store.

Decision 0029 says what Orrery is: the estate's control plane, and the
console for the people who run the platform. A member is an engine behind
it and keeps a panel of its own. A business builds its own portal on top,
and no business logic lives in Orrery. The console takes the place of a
command line that only calls an API. It leaves five: what the bar for a
member's pages is and who judges it, whether Change stays Partial, which
members offer their lists and actions through Orrery today, which
members have no panel, and which commands of which members go.

Decision 0030 adds a sixth property, built for the agent first, and holds
every member to the cost of a local disk. It leaves three: where each
member stands against the bar, how a script signs in with no command
line, and what each member's tasks are.

Decision 0031 says the estate is the tenant, and that a scope inside it
is one shared owner. It leaves three: whether one view across estates is
ever wanted, how a member alone names an owner, and the claim's shape in
a token.

Decision 0032 has an estate bring a message broker once two members are
joined, and puts every event on it. The crossings of the seam become ten.
It leaves six: the wire, the envelope, the topics and who owns each,
order, an estate's own senders, and sign-in to a broker with no workload
identity.

Decision 0050 brings the estate's own change events onto that broker:
its cloud's event service, its forge's webhooks, and its cluster's watch.
Every event takes the CloudEvents 1.0 envelope, which settles two of
0032's six: the envelope and an estate's own senders. An event is a hint,
and a receiver reads the source again before it acts. Work starts from
events: Orrery's actions and sources, Rootstock's drift and applies, and
Trellis's judging. A clock is only the net, and a net that finds what no
event said is a finding. The crossings of the seam become eleven.

Decision 0033 writes the gate once, in Go. Decision 0035 has since made
it a library every member links, and closed its question on a Go core.
It leaves one: where the gate keeps tokens and sessions.

Decision 0034 sets the scale target: one estate of 150 people after ten
years. It leaves three: each member's speed limits at the target, how
often the benchmark runs, and the target for the record and for usage.

Decision 0035 re-cores Orrery and Vantage in Go, each in one release that
changes no behavior, after a freeze, with the store left as it is. It
leaves four: which hub goes first, how exact the same picture is for
Vantage, how long a freeze may last, and whether shared code could ship
to the browser as WebAssembly.

Decision 0036 puts every member's data in Postgres, and has each member
on SQLite move once. Decision 0040 has since settled Annals's store. It
leaves two: whether Trellis
holds data when its history is off, and a member run alone on a laptop.

Decision 0037 keeps one shared Postgres server for an estate, and lets a
member sit apart only for one of two named reasons. Decision 0038 has
since said no estate takes that step until the need is real or near, so
Dispatch stays on the shared server. Decision 0037 leaves four: whether Orrery or Annals sits apart, whether members connect
through a pooler, when the shared server gets a second instance, and what
apart means in an estate with one cluster and no cloud.

Decision 0038 leaves two: the numbers that mean near, and who watches.

Decision 0039 has an estate deploy every member under the member's name
and move in one staged cutover. It leaves two: how long the old stays
after a cutover, and whether a mover can run while the member still
writes.

Decision 0040 has Annals keep the record in Postgres, with the events
add-only and split by month behind a port of their own. A columnar store
is a later step, taken on a measurement at the scale target. It leaves
two: how many events the scale target really means, and how long an event
is kept whole.

Decision 0042 puts Toolshed on the floor. It leaves three: where the shed
file's format is published and whether an estate may keep more than one,
how Toolshed learns that a ring's machines are in the installer's group
when the installer cannot say, and whether a pack may name a tool that no
machine of its kind can run.

## What it leans on in the guide

The book behind the suite now publishes a guide: it teaches how to decide
and prescribes nothing, so the suite builds to no standard of the book's.
The suite names no estate, so it cites neither estate's own platform
standard. It leans on these principles of the guide. The list was read at
version 2026.1107.1839, when the guide was still called the standard, and
the three principles decision 0016 chooses against were read again at
version 2026.1120.2003:

- `map-the-platform-as-pillars-each-one-a-question-it-must-answ`
- `the-platform-s-own-software-is-a-pillar-kit-engine-interface`
- `new-capability-goes-to-a-standalone-product-not-the-house-vi`
- `the-hub-ships-no-catalog-the-model-belongs-to-the-user`
- `one-shape-for-every-product-s-interface` (Aspirational)
- `judge-a-dependency-by-license-maintenance-and-governance-and`
- `fix-what-s-broken-everywhere-at-the-source`
- `turn-retrospective-findings-into-a-few-ranked-remedies-deter`
- `question-delete-simplify-speed-up-then-automate-in-that-orde`
  (Aspirational)
- `count-course-corrections-from-stops-and-redirects-never-from`
- `keep-every-estate-on-its-own-side-of-a-seam-with-a-closed-li`
- `judge-results-with-a-cross-provider-council-never-gate-worki`
- `set-rigor-by-what-a-failure-costs-in-a-few-named-classes`
- `respond-to-an-escape-by-turning-it-off-then-closing-exactly-`

It chooses against seven principles. Decision 0007 says why for the first two,
decision 0016 for the third, fifth, and sixth, decision 0009 for the
fourth, and decision 0018 for the seventh:

- `admit-a-tool-to-the-platform-suite-only-by-a-written-members`: the
  first check widens from "serves operations" to "serves tending".
- `build-the-platform-s-nine-positions-in-dependency-order-star`: sensing
  friction goes first.
- `map-the-platform-as-pillars-each-one-a-question-it-must-answ`: the
  principle maps fourteen pillars. The suite maps six, and keeps the principle's
  test of one app per pillar. The other eight are properties and outcomes.
- `keep-every-estate-on-its-own-side-of-a-seam-with-a-closed-li`: the
  principle closes the list of crossings at eight. The suite adds a ninth, the
  agent runtime, a tenth, events on a message broker (decision 0032), and an
  eleventh, the estate's own events on that broker (decision 0050).
- `the-platform-s-own-software-is-a-pillar-kit-engine-interface`: the
  principle treats the kit, the engine, and interfaces as three pillars. Here
  the kit and the interface shape are properties, and the engine is a
  part of Change.
- `delivery-outcomes-as-a-sibling-of-ci-health`: the principle computes four
  delivery measures. The suite adds rework rate.
- `enroll-an-installed-agent-through-device-management-s-own-sc`: the
  principle enrolls an agent with a token made on the machine. The suite's
  device agent holds a certificate the estate issues, and no token.

New to the guide: the guide has no principle for the three materials, the
ladder of remedies, a loop budget per repository, counting friction or
weeds, or a class of installed tending tools. Decision 0007 sets those
here. Nor has it a principle for a pillar on growing conditions, for templates
that stay with an estate, or for opening a new view to named people first.
Decision 0008 sets those. Nor has it a principle for the one question that
tells a member from an estate's own app, for a member that changes
repositories, or for an agent runtime reached through an adapter.
Decision 0009 sets those. Nor has it a principle that defines quality, for
bounding a change in place of inspecting it, for a law as a check its
grower cannot change, for a ladder of proof, for counting what checking
costs and catches, or for a pillar on quality. Decision 0010 sets those.
Nor has it a principle that a request is evidence and not a specification, that
an owner judges a brief of the plan and never the code, or for the kind of
a change as a dial beside its class. Decision 0011 sets those. Nor has it
a principle that sorts what a platform must answer into pillars, properties,
and outcomes, for a member that names one pillar, or for adoption as an
outcome. Decision 0016 sets those. Nor has it a principle for a signed pack
of tools per kind of machine, rolled out in rings through the estate's
own installers, or for a test that tells which of the platform's own
software stands under the pillars. Decisions 0042 and 0043 set those. The guide has since taken the
pillars on growing conditions and quality, and several principles on quality.
The membership test of decision 0001 and the
seam of decision 0002 were new to the guide when they were written.
Both are principles of it now.
