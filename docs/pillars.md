# The map

What a platform must answer, and how well the suite answers it. Decision
0016 set this map on 2026-11-20, and decision 0030 added a sixth property
on 2026-11-23. It has three lists, and each list has its own test.

- **Six pillars.** A pillar is something a platform has. One app answers
  its whole question.
- **Six properties.** A property is something every pillar must be like.
  No app can own one. The suite's judge checks it.
- **Three outcomes.** An outcome is a number read off the whole. No app
  owns one. The catalog shows it.

Under all three sits the floor: what an estate brings. The suite offers
two members there, Rootstock and Toolshed, and requires neither
(decisions 0028 and 0042).

```text
Outcomes     Flow          Quality          Adoption
Pillars      Catalog   Change   Health   Cost   Rules   Record
Properties   Run as a product   Two doors   Self-service   One kit   Decided on purpose
The floor    forge, pipelines, deploy tool, sign-in, vault, telemetry, agent runtime, environments
```

The pillars say what a platform must answer. `garden.md` says what a
gardener must do, and rates the suite by tending job. The two pages are
read together: a pillar is a place in the garden, and a job is work done
there.

## Why the map changed

Until 2026-11-20 this page listed fourteen pillars. The platform guide tests
a pillar one way: one app answers its whole question (principle
`map-the-platform-as-pillars-each-one-a-question-it-must-answ`). Six of
the fourteen could never pass that test, because they were not things an
app can own. Decision 0016 holds the evidence. In short:

| What was checked | What was found |
| --- | --- |
| Which of the fourteen could never be covered | Six: platform as a product, agents, foundations, interfaces, growing conditions, quality. |
| What each member says about itself | No member names one pillar. They name two to five. |
| Whether the map and the members agree | Graft's own file says agents and actions. This page said golden paths. |
| How fast the list grew | Two pillars in six days. |
| What published frameworks do | Of fourteen read, none has more than seven items on top. Several keep capabilities, attributes, and measures in separate lists. |

The ratings below are a judgment, made on 2026-11-20. Each carries what
the old rows said was missing. No usage data went into them, and none was
raised by the change of map. Facts about a member were read from its
repository that day, at the version named.

- **Covered**: the owner answers the question for any estate.
- **Partial**: the owner answers part of it, or only for some estates.
- **Gap**: nothing answers it yet.

## The six pillars

| Pillar | The question | Owner | Rating | Parts in other members | What is missing |
| --- | --- | --- | --- | --- | --- |
| Catalog | What do we have, who owns it, and how does it connect? | Orrery | Covered | Vantage is its picture and holds its documents. My Apps is its front page. Muster feeds it the forges and each machine's work that never reached one. forgitten, which found that work, retired into Muster (decisions 0017 and 0025). | Pushers beyond Kubernetes and Entra live in each estate. The ground view is in preview. |
| Change | How does a change get asked for, shipped, and undone? | Graft | Partial | Orrery's actions engine runs every change that is not a change to a repository, and carries the ones that wait or run long as one job for each run (decision 0020, v1.157.0). | Graft changes a repository that exists, on two forges and one agent runtime, and only in the repositories its program file lists (v6.6.0). Starting a repository stays with the estate (decision 0008). One part of the answer lives in Orrery (decision 0016), and that line is fixed (decision 0020). |
| Health | Is it working, and does it come back when it breaks? | Dispatch | Partial | Trellis's telemetry pack judges whether a service emits telemetry. | Dispatch holds incidents, on-call, and postmortems, and sends notices (v0.0.40). The telemetry stack is the estate's. Nothing shows ahead of time that a thing comes back. |
| Cost | What does each thing cost, in money and in capacity? | Tally | Partial | None. | Cloud cost reads one cloud only. Model work is counted by conversation, not by its unit: nothing says what one document, request, or thread costs, or watches the five shapes that waste it (decision 0044). Rated Partial on 2026-11-25, a judgment, from Tally at v1.2.0. |
| Rules | Does everything stay inside what its owners said must hold? | Trellis | Partial | Graft's fences hold a change made through the desk. | Trellis reads one forge, its registry, and one cloud. It judges an estate's laws, its nine packs, and no repository's own laws (decision 0010). Its 99 rules still name the old pillars (v5.6.1). |
| Record | Who, or which agent, did what, and on whose say-so? | Annals | Partial | None. | Only Orrery, Dispatch, and Graft say they post to it. |

## The six properties

Trellis judges a property the way it judges any standard: by rule, with
findings and waivers. Today its rules reach one of the six.

| Property | What it asks of every pillar | Rating | What holds today | What is missing |
| --- | --- | --- | --- | --- |
| Run as a product | Its use is measured, and it improves from what people say. | Partial | My Apps counts what people open. A request to Graft is how a person says what they need, and each gets one answer (decision 0011). | No rule judges it. Use is not measured pillar by pillar. |
| Two doors | An agent can use every door a person can, in one shape. | Partial | Trellis's interfaces pack judges the shape of an HTTP API. Orrery, Vantage, Annals, and Dispatch each have a door for agents. | No one CLI shape, no generated SDKs, and no one docs site. No door for agents was found in the other five members. |
| Self-service | No ticket and no person stands in the way, unless the risk says so. | Partial | Orrery's actions engine runs, approves, and records. A lane in Graft sets how far a request goes with no person in the way. | No rule judges whether a capability still needs a ticket. |
| One kit | The platform's own software is built from one shared kit. | Partial | Five of eleven members build on the kit: My Apps, Tally, Annals, Dispatch, and Graft. | Orrery, Trellis, Vantage, and Rootstock do not, and Toolshed is not built yet. Muster takes only the kit's `device` door, and stays off the rest by decision 0004 (decision 0025). No rule judges it. |
| Decided on purpose | Each choice is written down, with why, and what would reopen it. | Partial | Orrery, Vantage, and Graft keep decision records in their repositories. The suite keeps its own here. | Seven members keep none in their repositories. No rule judges it. |
| Built for the agent first | An agent can afford every door: finding one fact, reading one part, or changing one sentence costs it no more than the same task on a local disk (decision 0030). | Partial | Vantage holds the bar by its own decision, with a benchmark in its check. Orrery bounds every answer an agent reads. | No other member was read against the bar. The kit has no wrapper that counts a tool call and no benchmark harness. No rule judges it. |

## The three outcomes

An outcome is read from the numbers each repository carries in the
catalog. `garden.md` defines the loop, friction, and weeds. `quality.md`
defines cost of checking and catches.

| Outcome | The question | Its numbers | What is counted today | What is not |
| --- | --- | --- | --- | --- |
| Flow | How fast and how smoothly does work move? | Deploy frequency, lead time, the loop, friction. | Deploy frequency and lead time are calculated in Orrery from what Muster writes. Muster writes each pipeline's median duration, which is most of the loop. | Nothing counts friction. Its source is decided and not built (decision 0008). |
| Quality | Is what ships good, and what does knowing that cost? | Change failure rate, rework rate, time to restore, laws that hold, weeds, cost of checking, catches. | Change failure rate and time to restore are calculated in Orrery. Graft keeps what each request's agents spent, by stage, on its catalog record (v6.5.0). | Rework rate, a repository's laws, weeds, and catches have no source. Cost of checking is not joined per change outside the desk. |
| Adoption | Do people and agents choose it? | Who uses what, and what they ask for. | My Apps counts what people open. Graft keeps each request. | No member counts what an agent chooses. Nothing shows these together. |

Orrery shows an outcome only where an estate's model names its numbers.
The hub ships no model. Showing the three for a whole estate is owed
(the roadmap).

## What the pillars are reached through

Orrery owns Catalog. It is also the estate's control plane and the
console for the people who run the platform (decision 0029). That work is
not a seventh pillar: it is what the other pillars are reached through.
Each member feeds Orrery what it holds and offers what it can do as
actions there, and keeps a panel of its own. The actions engine sits in
Orrery, where the buttons are, by design. Whether that still makes Change
Partial is open, and the rating above was not changed.

## The floor

A forge, pipelines, a deploy tool, sign-in, a vault, a telemetry stack, a
message broker (decision 0032), an agent runtime, and environments. An estate brings each one, and the suite
reads it through an adapter. `seam.md` holds the full list and the line.
None is a pillar, and none is rated here.

The floor holds two members. Rootstock is the deploy tool and
environment tool the suite offers, and delivers software to environments
(decision 0028). Toolshed delivers tools to machines: it says what may
run on an estate's machines, where it came from, and whether it is on
every machine that should have it (decision 0042). Neither answers a
pillar's question, so neither is rated. An estate may take each or bring
its own, and no member requires either.

A member stands on the floor only when all three hold (decision 0043):

1. **It puts the platform in place.** It delivers software,
   infrastructure, or tools into environments or onto machines. It does
   not answer a question about what is there; that is a pillar's job.
2. **It works first.** It runs in a new estate before any other member
   exists, so the estate can be built with it alone. It needs no member
   to do its work.
3. **Nothing needs it.** No member needs it to run or to be deployed,
   and an estate may bring its own instead.

The test leaves importance out. A tool that answers a pillar's question
goes to that pillar, however important it is. A tool that fails the
second or third point is a feature of a member, or a shed tool.

## Where the fourteen went

Nothing was dropped. Each old pillar has one place, or two where it mixed
two kinds.

| Until 2026-11-20 | Now |
| --- | --- |
| 1 Platform as a product | Property: run as a product. Outcome: adoption. |
| 2 Golden paths | Pillar: Change. |
| 3 One control plane | Pillar: Change, as a part of the floor an estate brings. |
| 4 Security and compliance | Pillar: Rules. |
| 5 Observability | Pillar: Health. |
| 6 Catalog and ownership | Pillar: Catalog. |
| 7 Cost | Pillar: Cost. |
| 8 Agents | Property: two doors. Pillar: Record. |
| 9 Measured outcomes | Outcomes: flow and quality. |
| 10 Platform software foundations | Property: one kit. |
| 11 Self-service actions | Pillar: Change, for the engine. Property: self-service. |
| 12 Interfaces | Property: two doors. |
| 13 Growing conditions | Outcomes: flow, for the loop and friction. Quality, for weeds. |
| 14 Quality | Outcome: quality. |

A member's own files and Trellis's rules still use the old names until
their roadmap rows are done. This table translates until then.

## Build order

Decision 0007 puts sensing first. A gardener cannot tend what it cannot
see, and the suite already holds the catalog the other steps need. The
steps keep their numbers. Their names follow the new map.

1. **Friction (Flow).** Count where growers get stuck: retries, stops,
   redirects, and failed tool calls per session, as plain numbers on each
   repository. Nothing measures this today. A new, small source will, with
   no pages of its own (decision 0008). It is not built.
2. **The numbers on every bed (Flow and Quality).** The loop, friction,
   and weeds as fields on each repository in the catalog, beside the five
   delivery measures. Muster already writes each pipeline's median
   duration. Orrery keeps a budget beside a number, so each can be a
   stake. Cost of checking and catches ride with them.
3. **The ground view (Catalog).** Built, in preview. Orrery shows each
   repository as a bed, under its sky, to the people an admin names. What
   is left is to open it to everyone.
4. **A bed's laws (Rules).** Trellis reads which of a repository's checks
   are laws, and judges them and who changed them. The class goes on each
   bed's catalog entry (decision 0010).
5. **Two doors.** One CLI shape and one token story across the members.
6. **One kit.** Move the other five members onto the kit, which also
   gives them one door, one telemetry setup, and one Annals client.
7. **Forge reach (Rules).** Trellis reaches one forge. Put the forge
   behind an adapter, as Muster and Graft already do.
8. **Record.** Every member that acts posts to Annals.

Moving the members to the new map is not a step in this order. It builds
nothing new. It is renaming, and it gets dearer with every rule written to
the old names, so it goes first among the work that is only renaming
(the roadmap, ORCR-21 to ORCR-23).
