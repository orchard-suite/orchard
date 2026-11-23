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
- **One map.** Six pillars, each with one owner among the members. Five
  properties every pillar must have. Three outcomes the whole is for:
  flow, quality, and adoption. `pillars.md` rates each one (decision
  0016). The six pillars are the six questions this page opens with.
- **Joined by the catalog.** Orrery is the spine. The others read it,
  describe themselves to it, and write their findings back to it. Each
  pushes an inventory of what it holds, and stays the home of its own
  records (decision 0022).
- **One board.** Orrery shows the whole estate as a sky, and each
  repository as a bed on the ground beneath it. The ground is in preview:
  an admin opens it to the people named. The suite builds no master app
  above its members. A gardener acts on many beds through Orrery's
  actions.
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
  your vault. The standard forbids building either (rule
  `new-capability-goes-to-a-standalone-product-not-the-house-vi`).
- **Not an observability stack.** Bring Prometheus, Loki, Tempo, Grafana,
  or their equal. Orchard sends to it and reads from it.
- **Not a deploy tool.** Bring Argo CD, Flux, or your pipelines. Orrery's
  actions can ask them to act.
- **Not a database server.** Bring one managed Postgres server. A member
  that needs Postgres takes a database and a role on it. A member that
  fits one writer keeps SQLite (decision 0023).
- **Not an agent runtime.** Bring the runtime. The suite senses what
  agents do and shapes the beds they work in. Graft starts agent
  sessions on the runtime an estate brings, and the suite builds none
  (decision 0009).
- **Not a test runner, an environment tool, or a code reviewer.** Bring
  your test tools, your break-it engine, and the tool that stands up an
  environment. The suite judges what they report. No member gates a change
  on a person's or a model's opinion of the code (decision 0010).
- **Not a controller.** Nothing in the suite changes a repository on its
  own. A person or an agent starts an action, and the action is recorded.
  Graft is held to this: it changes a repository only when asked.
- **Not a server on a person's machine.** What a member reads from a
  machine comes through one small device agent, Tender, which only
  reports (decisions 0018 and 0025).
- **Not a home for personal apps.** An app for one person or one family is
  a private app that may use the suite. It never joins it.

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
   build one CLI and generated SDKs over all of them, and one docs site.
8. **Admit carefully.** A new member passes the test in `seam.md` and
   joins by a decision record. Most tools will not.

`roadmap.md` lists each thing these steps and the decisions leave owed, who
owes it, and whether it is done. A decision made in any conversation
reaches this repository as a proposal and is folded into a record without
the owner carrying it (decision 0013).

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
standard takes the pillar.

Decision 0011 puts the start of quality at the request and leaves two: how
a request is weighed outside the desk, and which checks a desk's gate can
run.

Decision 0016 replaces the fourteen pillars with six pillars, five
properties, and three outcomes. It closes one question of decision 0010:
the standard took the pillar on quality, and the suite has since made
quality an outcome. It left four: whether the standard takes the new
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
mission critical. It leaves three: whether Vantage's work tracking takes
a second database, what an estate brings for a store that is neither
Postgres nor SQLite, and which backup proves no data is lost.

## Built to the standard

This strategy builds to these rules of the platform standard. The list
was read at version 2026.1107.1839, and the three rules decision 0016
departs from were read again at version 2026.1120.2003:

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

It departs from seven rules. Decision 0007 says why for the first two,
decision 0016 for the third, fifth, and sixth, decision 0009 for the
fourth, and decision 0018 for the seventh:

- `admit-a-tool-to-the-platform-suite-only-by-a-written-members`: the
  first check widens from "serves operations" to "serves tending".
- `build-the-platform-s-nine-positions-in-dependency-order-star`: sensing
  friction goes first.
- `map-the-platform-as-pillars-each-one-a-question-it-must-answ`: the
  rule maps fourteen pillars. The suite maps six, and keeps the rule's
  test of one app per pillar. The other eight are properties and outcomes.
- `keep-every-estate-on-its-own-side-of-a-seam-with-a-closed-li`: the
  rule closes the list of crossings at eight. The suite adds a ninth, the
  agent runtime.
- `the-platform-s-own-software-is-a-pillar-kit-engine-interface`: the
  rule treats the kit, the engine, and interfaces as three pillars. Here
  the kit and the interface shape are properties, and the engine is a
  part of Change.
- `delivery-outcomes-as-a-sibling-of-ci-health`: the rule computes four
  delivery measures. The suite adds rework rate.
- `enroll-an-installed-agent-through-device-management-s-own-sc`: the
  rule enrolls an agent with a token made on the machine. The suite's
  device agent holds a certificate the estate issues, and no token.

New to the standard: the standard has no rule for the three materials, the
ladder of remedies, a loop budget per repository, counting friction or
weeds, or a class of installed tending tools. Decision 0007 sets those
here. Nor has it a rule for a pillar on growing conditions, for templates
that stay with an estate, or for opening a new view to named people first.
Decision 0008 sets those. Nor has it a rule for the one question that
tells a member from an estate's own app, for a member that changes
repositories, or for an agent runtime reached through an adapter.
Decision 0009 sets those. Nor has it a rule that defines quality, for
bounding a change in place of inspecting it, for a law as a check its
grower cannot change, for a ladder of proof, for counting what checking
costs and catches, or for a pillar on quality. Decision 0010 sets those.
Nor has it a rule that a request is evidence and not a specification, that
an owner judges a brief of the plan and never the code, or for the kind of
a change as a dial beside its class. Decision 0011 sets those. Nor has it
a rule that sorts what a platform must answer into pillars, properties,
and outcomes, for a member that names one pillar, or for adoption as an
outcome. Decision 0016 sets those. The standard has since taken the
pillars on growing conditions and quality, and several rules on quality.
The membership test of decision 0001 and the
seam of decision 0002 were new to the standard when they were written.
Both are rules of it now.
