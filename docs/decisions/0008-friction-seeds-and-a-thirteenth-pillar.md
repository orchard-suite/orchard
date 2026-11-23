# 0008. Friction, seeds, and a thirteenth pillar

- Status: Accepted, amended by 0009 (Slipway joins, and plants no seed); point 4 superseded by 0016 (growing conditions is two outcomes, not a pillar)
- Date: 2026-11-12
- Standard: 2026.1107.1839

## Context

Decision 0007 made tending the suite's one job and left three questions
open: where friction sensing lives, whether a seed tool joins the suite,
and whether the pillars gain one for growing conditions. Each needed its
own record. This is that record for all three, because they were weighed
together and each answer leans on the others.

Friction is how often a grower gets stuck: retries, stops, redirects, and
failed tool calls per session. A seed is a template a new repository
starts from. Both words are defined in `garden.md`.

Since decision 0007, Orrery has built the ground view that decision asked
for. The facts about it below were read from Orrery's repository on
2026-11-12.

## Decision

1. **A new, small source counts friction.** It has no pages. It writes
   plain numbers onto each repository in the catalog, as a named source,
   the way redgreen writes pipelines. Orrery shows the numbers. The other
   two choices were a collector inside Tally and a full member with a
   board of its own. Tally answers what things cost, and friction is not a
   cost. A second board would break decision 0007, which keeps Orrery as
   the one board.
2. **The friction source is decided, not built, and not yet a member.** It
   joins the suite only by its own record, which applies the test in
   `seam.md`. Its pillar will be the new one in point 4.
3. **Seeds stay with each estate, and an Orrery action plants them.** The
   suite ships no seed and admits no seed tool. Decision 0003 stands. A
   seed carries an estate's own choices: its forge, its registry, its
   languages, its names. A seed that fits every estate would carry none of
   them. An estate keeps its templates in its own repositories and
   registers one action that starts a new repository from one.
4. **The suite maps thirteen pillars.** The new one is **Growing
   conditions**: is the place where software grows getting better or
   worse? It holds the three numbers of `garden.md` (loop, friction,
   weeds) and the work of tracing a weed to its stem. The standard maps
   twelve. The suite runs one ahead of it until the standard takes the
   pillar up or turns it down.
5. **The ground view is built, in preview.** Orrery shows the ground of
   any blueprint whose model says which of its fields mean what. The hub
   ships no such model. A number field may carry a budget, which is the
   stake. The view lists the templates entities were started from, which
   of them have fallen behind their template, and the action that starts a
   new one, which is how point 3 is met. An admin opens the view to nobody,
   to the people named, or to everyone. A new hub opens it to nobody.

## Left open

- **The friction source's name, and its reader.** It needs a reader on
  each machine where agents work. Tally's shipper already reads the same
  agent transcripts on each machine. Whether the two share code or run
  side by side is for the record that admits the source.
- **Which weeds get a source.** Orrery can show any count an estate
  writes. No member counts lint suppressions, skipped tests, or copied
  blocks yet.
- **When the ground view opens to everyone.** That is each estate's call,
  made on its own hub.

## Consequences

- `pillars.md` lists thirteen pillars and rates the new one.
- Golden paths moves from a gap to "bring your own". That is this
  decision's doing, not a new judgment of any app: point 3 puts the paved
  road with the estate on purpose.
- `garden.md` rates the stake and seed jobs again, and says the ground
  exists.
- `strategy.md` drops its list of open questions and points here.
- `members.md` says what Orrery's ground does and closes the question on
  Slipway.
- The suite still has nine members.

## Rules

Builds to:

- `admit-a-tool-to-the-platform-suite-only-by-a-written-members`: the
  friction source joins only by its own record.
- `the-hub-ships-no-catalog-the-model-belongs-to-the-user`: the ground is
  named in an estate's model, and the hub ships none.
- `new-capability-goes-to-a-standalone-product-not-the-house-vi`: friction
  counting is its own small product, not a part of Tally or Orrery.
- `count-course-corrections-from-stops-and-redirects-never-from`: what the
  friction source counts.
- `a-record-backend-writes-one-catalog-entity-as-a-named-source`: an
  action that plants a seed records the new repository this way.
- `decide-the-feature-flag-at-planning-operator-releases-after-`: the
  ground view shipped switched off, and whoever runs a hub opens it.

Departs from:

- `map-the-platform-as-pillars-each-one-a-question-it-must-answ`: the
  standard maps twelve pillars. This decision maps thirteen. The rule's
  test, one app that answers a pillar's whole question, still applies to
  the new pillar, and the pillar fails it today.

New to the standard: the standard has no rule for a pillar on growing
conditions, for where friction is counted, for templates that stay with an
estate and are planted by a catalog action, for a budget kept beside a
field that holds nothing back, or for opening a new view to named people
before everyone.
