# 0016. Six pillars, five properties, three outcomes

- Status: Accepted, amended by 0017 (point 6: Muster is one part of Catalog)
- Date: 2026-11-20
- Standard: 2026.1120.2003
- Supersedes: point 4 of 0008, point 9 of 0010
- Amends: 0010 (point 8), 0011 (point 8)
- Capture: 2b86a196-4a6d-4d03-85ee-76e137896e58

## Context

The suite mapped fourteen pillars. The standard began with twelve.
Decision 0008 added growing conditions and decision 0010 added quality,
six days apart. The standard has since taken both and maps fourteen too
(read at version 2026.1120.2003).

The standard tests a pillar one way: one app answers its whole question.
Read against that test, the list of fourteen mixes three kinds of thing.

- **Something a platform has.** One app can own it. The catalog is one.
- **Something every part must be like.** No app can own it. "An agent can
  use every door a person can" is one.
- **Something read off the whole.** No app can own it. Quality is one.

Only the first kind can ever pass the test. So the list fails by its own
rule, and adding to it made that worse.

The evidence, each fact with the day it was read:

- Six of the fourteen can never pass: platform as a product, agents,
  platform software foundations, interfaces, growing conditions, and
  quality. None is a thing one app can own (`pillars.md`, 2026-11-18).
- No member names one pillar. conform names five in its own description
  file. Vantage, My Apps, Tally, and Ledger name three each. redgreen,
  Dispatch, and Slipway name two. Orrery and forgitten name none (each
  member's `orrery.yaml`, 2026-11-20).
- The map and the members disagree. Slipway's own file places it under
  agents and actions. `pillars.md` placed it under golden paths.
- conform's 99 rules each name a pillar. They use seven names: security
  48, observability 16, catalog 12, interfaces 8, golden paths 7, agents
  5, and control plane 3 (conform at v5.6.1, 2026-11-20). Every week adds
  rules and records written to names that do not fit.
- The list grows fast. It gained two pillars in six days.
- Fourteen published frameworks for platforms, clouds, and delivery were
  read at their publishers' pages on 2026-11-18. None has more than seven
  items at its top. The larger ones put few on top and more underneath.
- Several keep the kinds apart. The CNCF platforms white paper lists
  thirteen capabilities and, separately, seven attributes. "Platform as a
  product" and "self-service" are on its attributes list. Google's
  framework has six pillars and treats AI as a view across all of them.
  DORA keeps capabilities apart from metrics.
- No research-based framework was found for a platform whose users
  include agents. So that part of this decision is a judgment, not a
  measurement.

Three maps were weighed.

1. **Keep fourteen.** It costs nothing now. Six pillars stay that nothing
   can ever cover, and the cost of moving grows with every rule written.
2. **Twelve pillars and two outcomes.** It moves only the two newest
   pillars. Four older ones keep the same flaw, so the question returns.
3. **Six pillars, five properties, three outcomes.** It is the only one
   where every pillar can pass its own test. It costs the most to move to,
   and the cost is paid once.

One more fact bears on the numbers. DORA now counts five delivery
measures. The fifth is rework rate: the share of deployments that are
unplanned and happen because of an incident in production (read at
dora.dev on 2026-11-20). The suite counted four.

## Decision

1. **The map is three lists, and each list has its own test.** A pillar
   is something a platform has: one app answers its whole question. A
   property is something every pillar must be like: the suite's judge
   checks it. An outcome is a number read off the whole: no app owns it,
   and the catalog shows it.

2. **There are six pillars.** Each has one owner.

   | Pillar | The question | Owner |
   | --- | --- | --- |
   | Catalog | What do we have, who owns it, and how does it connect? | Orrery |
   | Change | How does a change get asked for, shipped, and undone? | Slipway |
   | Health | Is it working, and does it come back when it breaks? | Dispatch |
   | Cost | What does each thing cost, in money and in capacity? | Tally |
   | Rules | Does everything stay inside what its owners said must hold? | conform |
   | Record | Who, or which agent, did what, and on whose say-so? | Ledger |

   These are the six questions `strategy.md` opened with. The suite
   already has one app for each.

3. **There are five properties.** conform judges them.

   | Property | What it asks of every pillar |
   | --- | --- |
   | Run as a product | Its use is measured, and it improves from what people say. |
   | Two doors | An agent can use every door a person can, in one shape. |
   | Self-service | No ticket and no person stands in the way, unless the risk says so. |
   | One kit | The platform's own software is built from one shared kit. |
   | Decided on purpose | Each choice is written down, with why, and what would reopen it. |

4. **There are three outcomes.** Orrery shows them.

   | Outcome | The question | Its numbers |
   | --- | --- | --- |
   | Flow | How fast and how smoothly does work move? | Deploy frequency, lead time, the loop, friction. |
   | Quality | Is what ships good, and what does knowing that cost? | Change failure rate, rework rate, time to restore, laws that hold, weeds, cost of checking, catches. |
   | Adoption | Do people and agents choose it? | Who uses what, and what they ask for. |

5. **The floor is the estate's.** A forge, pipelines, a deploy tool,
   sign-in, a vault, a telemetry stack, an agent runtime, and environments
   sit under the pillars. An estate brings them. `seam.md` lists them.
   None is a pillar.

6. **A member belongs to one pillar.** An owner names its own. A member
   that is not an owner names the pillar it is part of. Vantage, My Apps,
   redgreen, and forgitten are parts of Catalog: its picture, its front
   page, and two of its feeds.

7. **Change has one owner and one engine.** Slipway owns Change. Orrery's
   actions engine runs every other kind of change, and it stays in Orrery,
   where the buttons are. So Change is rated Partial: one part of its
   answer lives in another app. This is a judgment. Both are kept.

8. **The guard is five delivery measures.** Rework rate joins deploy
   frequency, lead time, change failure rate, and time to restore. Point 8
   of decision 0010 said four.

9. **Each of the fourteen has one place to go.** `pillars.md` keeps the
   table. Nothing is dropped. Platform as a product becomes a property
   and an outcome. Agents becomes a property and the Record pillar.
   Measured outcomes, growing conditions, and quality become the three
   outcomes.

10. **A member keeps its old names until it moves.** These documents use
    the new map from today. conform's rules and each member's own file
    keep the fourteen's names until their roadmap rows are done. Until
    then a reader meets both, and `pillars.md` translates.

11. **The three lists are closed.** A new pillar, property, or outcome
    joins only by a decision that says which of the three tests it passes.
    A number that fits an outcome is added to that outcome. It does not
    become a pillar.

12. **No member joins.** The suite still has ten members.

Decision 0010 stands in every other point. conform is still the one judge
of quality, and quality is still bounded and not inspected. What changes
is where quality sits: it is what the whole map is for, not one column of
it. Point 8 of decision 0011 rated platform as a product Partial. That
rating now belongs to the property, and it is still Partial.

## What members owe

Each is that member's own design, recorded in its own repository.

| Who | What it owes |
| --- | --- |
| conform | Have each rule name one of the six pillars or one of the five properties, in place of the pillar it names today. |
| conform | Judge all five properties. Its rules reach two doors today, through its interfaces pack, and none of the other four. |
| Every member | Name one pillar in its own description file. |
| Orrery | Show the three outcomes for a whole estate, from the numbers each repository carries. |
| redgreen and Orrery | Count rework rate, beside the four delivery measures they count. |
| Each estate | Rename the pillar records in its own catalog. The hub ships no model, so these are the estate's. |

## Left open

- **Whether the standard takes the map.** It maps fourteen pillars and
  nine positions, and treats the kit, the engine, and interfaces as three
  pillars. This map folds all three ideas into one. That is turned up or
  down in the standard, not here.
- **How adoption is counted.** My Apps counts what people open. A request
  to Slipway is what they ask for. No member counts what an agent chooses,
  and nothing shows the three together.
- **Whether Health gets a proof of recovery.** Time to restore is counted
  after a failure. Nothing shows ahead of time that a thing comes back.
- **Whether Change keeps two apps.** Point 7 keeps Slipway and Orrery's
  engine apart. One app answering the whole question is the standard's
  aim.

## Consequences

- `pillars.md` is rewritten. It holds the three lists, a rating for each
  row, the table that places each of the fourteen, and the build order
  under the new names.
- `roadmap.md` gains a section for the map: rows 21 to 26. The question
  decision 0010 left open, whether the standard takes the pillar on
  quality, is closed: the standard took it.
- `README.md`, `strategy.md`, `members.md`, `garden.md`, and `quality.md`
  name the six pillars. `quality.md` and `garden.md` name five delivery
  measures.
- The diagram file gains a view of the map. Each member's box names one
  pillar.
- Point 4 of decision 0008 and point 9 of decision 0010 are superseded.
  Growing conditions and quality are outcomes, not pillars. Everything
  else those two records say stands.
- Ratings were not raised by this decision. Each new row carries what the
  old rows said was missing.
- The suite still has ten members.

## Rules

Builds to:

- `map-the-platform-as-pillars-each-one-a-question-it-must-answ`: its
  test, one app that answers a pillar's whole question, is kept and
  applied to every pillar.
- `build-the-platform-s-nine-positions-in-dependency-order-star`: the
  build order stands. Two of its positions, decided on purpose and run as
  a product, are properties here.
- `own-quality-with-the-one-conformance-judge-never-a-second-ju`: conform
  stays the one judge, and judges the properties too.
- `delivery-outcomes-as-a-sibling-of-ci-health` and
  `keep-loop-friction-and-weed-counts-on-every-repository-guard`: the
  numbers of flow and quality.
- `count-what-checking-costs-and-catches-and-prune-the-rest`: two of
  quality's numbers.
- `one-shape-for-every-product-s-interface`: the two doors property.
- `the-hub-ships-no-catalog-the-model-belongs-to-the-user`: an estate
  renames its own pillar records.
- `let-software-describe-itself-from-a-file-in-its-repository`: a member
  names its pillar in its own file.
- `record-architecture-decisions-as-immutable-adrs`: two points are
  superseded here, and no record is rewritten.
- `ship-a-suite-s-decisions-as-a-plugin-and-derive-its-roadmap-`: what
  this leaves owed becomes roadmap rows.
- `admit-a-tool-to-the-platform-suite-only-by-a-written-members`: weighed,
  and no member joins.

Departs from:

- `map-the-platform-as-pillars-each-one-a-question-it-must-answ`: the
  rule maps fourteen pillars. This decision maps six, and moves the other
  eight to two lists the rule does not have. Why: six of the fourteen can
  never pass the rule's own test.
- `the-platform-s-own-software-is-a-pillar-kit-engine-interface`: the
  rule treats the kit, the engine, and interfaces as three pillars. Here
  the kit and the interface shape are properties, and the engine is a
  part of Change. Why: a kit and a shape are things every pillar must
  have, not things one app answers.
- `own-quality-with-the-one-conformance-judge-never-a-second-ju`: the
  rule calls quality one more pillar. Here it is an outcome. Its judge
  does not change.
- `delivery-outcomes-as-a-sibling-of-ci-health`: the rule computes four
  delivery measures. The suite adds a fifth, rework rate. Why: DORA
  counts it, and it catches a defect that reached people without failing
  a deployment.

New to the standard: the standard has no rule that sorts what a platform
must answer into pillars, properties, and outcomes with a test for each,
for a member that names exactly one pillar, for a closed list that grows
only by a decision naming the test passed, for adoption as an outcome, or
for rework rate as a delivery measure.
