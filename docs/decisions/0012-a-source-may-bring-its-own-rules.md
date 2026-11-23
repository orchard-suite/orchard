# 0012. A source may bring its own rules

- Status: Accepted
- Date: 2026-11-18
- Standard: 2026.1107.1839

## Context

conform is the suite's one judge. Until now every rule it judged with was
written by hand: a pack file in git, holding rules as data. The standard
says so in `one-conformance-board-one-pack-per-standard-exceptions-as-da`:
"A standard is a pack: one YAML file of rules."

A cloud has its own policy engine. Azure Policy is one. It holds rules
(policy definitions), assigns them to a part of the estate (a management
group, a subscription, a resource group), judges every resource it covers,
and records exceptions (exemptions) with a reason and a category. A rule
written in conform about the same property judges it a second time, and
the two can disagree. An exception made in one engine does not reach the
other.

An estate's owner wants Azure's rules to live in Azure Policy, assigned at
management groups, with every exception made in Azure with its reason.
conform must not judge Azure again. It must read what Azure decided and
pass it through, so the catalog shows Azure's rules, verdicts, and
exceptions in one list beside conform's own.

These facts were read from a real tenant on 2026-11-18, shapes only:

- Resource Graph's `policyresources` table holds policy states,
  assignments, and exemptions. It holds no policy definitions and no
  initiatives (sets of definitions). Those are read through the
  management API, by id.
- Resource Graph returns assignments made at a management group only when
  the query is scoped to a management group. A query scoped to
  subscriptions returns the subscription assignments alone.
- A policy state says `Exempt` and the state under the exemption, but not
  which exemption. An exemption names its assignment, the initiative
  members it covers, and its scope in its own id.
- Many exemptions have no expiry and no owner.
- A mid-size estate holds about 20,000 policy states.

## Decision

1. **A source may bring its own rules.** A source that reads another
   engine may hand conform a pack each pass, generated from that engine's
   rules. conform judges with it beside the hand-written packs. The
   judge, the waiver rules, the deadlines, the rollup, the history, and
   the catalog sink are the same for both.
2. **conform passes the other engine's verdict through.** A generated
   rule's check reads the engine's verdict and nothing else. It never
   reads the resource's settings. The engine's "compliant" is a pass,
   "non-compliant" a fail, and "could not judge" is no data.
3. **The engine's exceptions are waivers.** Each exemption becomes a
   waiver with its reason, category, end, and owner. conform weighs it by
   the estate's waiver policy like any other. One with no end or no
   owner does not count: the finding stays open, and the board shows the
   waiver with why. The engine may accept what conform will not.
4. **A generated rule's id follows the rule, not where it is assigned.**
   The id is `azure.<definition name>`. Moving an assignment does not
   change it. An initiative is flattened into its member policies, and
   its compliance groups become the rule's controls.
5. **One engine per property.** Where a native policy engine judges a
   property, conform holds no hand-written rule for it. An estate deletes
   its hand-written rule once the engine's rule covers it. conform keeps
   hand-written rules only where no native engine exists. conform cannot
   tell that two rules mean the same thing, so this is the estate's duty,
   and it is written down here so it is kept.
6. **The catalog shows every rule and every waiver weighed.** The sink
   writes one entity per rule the board judged with, hand-written or
   brought, and one per waiver it weighed, with its status, reason,
   category, end, and source. A person reads every rule, verdict, and
   exception with its reason in one place.
7. **Severity and tier are the estate's.** The engine gives none conform
   can use. The source's settings give a default, and overrides by
   definition name or by policy category.

## Consequences

- conform's packs are no longer only files. A pack is still data, and it
  still enters through one door: the pack set the judge reads. The set is
  now made each pass, so a source's pack can change between passes.
- A source that fails keeps its last pack while its facts are carried,
  then drops it, so its findings do not vanish on one bad read.
- Generated rules have no fixtures of their own. The generator is tested
  with fixtures instead.
- Generated rules run on the board only. A pipeline's check does not read
  the cloud.
- Many exemptions that Azure accepts will not count in conform until they
  gain an end and an owner. That pressure is intended.
- The blueprint standard's waiver gains a category, so a waiver kept in
  the catalog says whether it is accepted risk or mitigated.
- The suite still has ten members and fourteen pillars.

## Rules

Builds to:

- `baseline-policies-bind-by-default-a-deviation-needs-a-writte`: every
  exemption is a written waiver with its reason.
- `cap-waiver-length-by-severity-and-categorize-every-waiver`: an
  exemption's category maps to accepted or mitigated, and the estate's
  limits still hold.
- `give-every-finding-an-owner-a-deadline-from-policy-and-an-ev`: a
  passed-through finding gets an owner, a deadline, and events like any
  other.
- `carry-a-source-s-last-facts-until-a-max-age-then-say-no-data`: a
  source's pack is carried with its facts.
- `a-policy-hierarchy-with-fixed-places-for-production-sandboxe`: rules
  are assigned where the hierarchy puts them, and read from there.
- `the-hub-ships-no-catalog-the-model-belongs-to-the-user`: the rule and
  waiver lists go only into blueprints the estate names.

Departs from:

- `one-conformance-board-one-pack-per-standard-exceptions-as-da`, which
  says a standard is a pack file and an exception is a waiver kept in git.
  Here a source generates a pack from another engine each pass, and the
  engine keeps the exceptions. Why: a cloud's policy engine already
  judges at the point of change, can deny a bad resource, and is where the
  cloud's owners make exceptions. Copying its rules into conform as files
  makes two engines that drift. The rest of that rule holds: one board,
  one verdict per rule and subject, and waivers that end and have an
  owner.

New to the standard: one engine per property; a source that brings its
own rules; an engine's verdict passed through and never judged again.
