# The seam

Orchard sits between estates. Each estate plugs into it the same way, and
the suite knows nothing about any one of them.

```
  home estate  <--seam-->  Orchard  <--seam-->  a work estate
```

## What sits on each side

**Orchard** holds the products: their code, their container images, a
generic way to deploy them (a chart or a base set of manifests), their
docs, and fictional examples.

**An estate** holds everything that is true only of it: its hosts and
domains, its deploy overlays, its configuration and secrets, its database
server (decision 0023), its catalog model and pushers, its code analyzers (decision 0014), its chat bots
(decision 0015), its device certificates, from its device management or a
small certificate authority of its own, and the list of addresses its
device agent posts to (decisions 0018 and 0025), its Trellis packs and waivers, its classes, its lanes
and protected paths, each bed's own laws, its telemetry declarations, its
dashboards and alert rules, and its own apps.

## What crosses the seam

Only these. Each is a contract the product owns and documents.

| Crossing | Direction | Example |
| --- | --- | --- |
| Configuration | estate to product | environment variables and a config file, with no estate defaults baked in. The address of the estate's database server arrives this way (decision 0023) |
| Secrets | estate to product | read from the estate's vault by the estate's own secret operator |
| Sign-in | estate to product | the estate's front door says who the person is in `X-Forwarded-Email` and `X-Forwarded-Groups`; the product gives roles. A machine's agent is named by a certificate the estate issues (decision 0018) |
| Telemetry | product to estate | OTLP to the estate's collector, JSON logs to stdout |
| Self-description | product to estate | the product's `orrery.yaml`, read by the estate's Orrery |
| Audit | product to estate | events in Annals's shape, posted to the estate's Annals |
| Alerts | estate to product | Alertmanager's webhook, into Dispatch |
| The forge | product to estate | through an adapter per forge, never one forge's API in the core |
| The agent runtime | product to estate | through an adapter per runtime; the estate brings the runtime and the suite builds none (decision 0009) |

## Rules

1. **Product code names no estate.** No host, domain, person, household,
   company, or repository of an estate in code, defaults, schemas, tests,
   or examples. Examples use `example.com` and fictional names.
2. **An estate's deployment lives in the estate.** Overlays, values,
   dashboards, alert rules, and catalog entries for one estate live in
   that estate's repository, never in the product's.
3. **Bring your own foundations.** The suite builds no forge, build
   system, identity provider, secrets store, or observability stack. It
   reads them through adapters. It runs no database server either. An
   estate brings one managed Postgres server, and a member that needs
   Postgres takes its own database and role on it. No member brings a
   database cluster of its own as the way it is meant to run (decision
   0023).
4. **Every member runs in every estate.** A feature that only one estate
   can use is configuration that is off by default, or it belongs in that
   estate's own app.
5. **Work never appears in the suite.** A work estate uses Orchard the same
   way the home estate does. Nothing about it is written in any member's
   repository or in this one.

## How the seam is held

[hedge](https://github.com/orchard-suite/hedge) holds rules 1, 2, and 5 in
the path of work (decision 0024). An estate keeps a private register of its
own names, and says in its toolkit which repositories may name which
estate. hedge checks every write an agent makes, every commit, every push,
and every forge post against it, in the zone of the repository it goes to.
Every repository of the suite is estate-neutral: it may name no estate. A
repository goes public only through `hedge publish`, which checks its whole
history first. An estate's Trellis can judge hedge's findings in every
repository it reads.

## Who may join

A member passes all four:

1. **It serves tending.** It helps a gardener tend a platform: sense what
   grows there, trace a problem to what taught it, fix it at the source,
   stake it, fence it, or prune it (`garden.md`). Seeing what exists, what
   it costs, whether it is healthy, safe, and shipping, and who did what
   is the sensing part. A tool that serves one person's or one family's
   life is a private app. Decision 0007 widened this check from "it serves
   operations". The quick way to ask it: does the app help run the
   platform, or does it only run on the platform? A member helps run it
   (decision 0009).
2. **It fills a gap.** The market covers its pillar poorly, or not in a way
   that joins the rest of the suite. Where a good product exists, the
   estate brings it instead.
3. **It is estate-neutral.** It runs in any estate with configuration
   alone, by the rules above.
4. **It is built the suite's way.** It emits telemetry from its first
   release, describes itself to Orrery, posts what it does to Annals, and
   signs people in through the estate's front door.

A tool that passes the first two is a candidate. It joins by a decision
record, which lists what it must still change to pass the last two. Every
member joined this way in decision 0001, forgitten among them, and Graft
joined this way again in decision 0009; the open changes are in
`seam-audit.md`.

## The shed

The test above is for services an estate runs. A tending tool that is
installed on a machine (a CLI, a desktop app, a skill) does not take it
and is not a member. `members.md` lists these under "The shed". The five
rules above still bind a shed tool: it names no estate, and it works in
any estate.
