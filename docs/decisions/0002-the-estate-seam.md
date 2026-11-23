# 0002. The estate seam

- Status: Accepted
- Date: 2026-11-05
- Standard: 2026.1103.322

## Context

The members were built for one estate first, and it shows: product code
names that estate's hosts and apps, and five members keep that estate's
deploy files in their own repositories (`seam-audit.md`). The suite has to
run in a work estate just as well, and nothing about a work estate may
appear in any member.

## Decision

Almanac is estate-neutral, by the five rules in `seam.md`:

1. Product code names no estate.
2. An estate's deployment lives in the estate's repository.
3. The suite builds no forge, build system, identity provider, secrets
   store, or observability stack, and reads each through an adapter.
4. Every member runs in every estate, by configuration alone.
5. A work estate never appears in the suite.

Only the crossings listed in `seam.md` pass between a member and an
estate: configuration, secrets, sign-in headers, telemetry,
self-description, audit events, alerts, and the forge through an adapter.

## Consequences

- Each member moves its estate folder out of its repository and into the
  estate's, and keeps a generic chart or base manifests in its place, as
  Vantage and forgitten already do.
- Defaults that name an estate become required settings or neutral
  values.
- Examples use fictional names.
- A member that reads one forge puts it behind an adapter, as redgreen
  does.

## Rules

Builds to `new-capability-goes-to-a-standalone-product-not-the-house-vi`
(products stay forge-agnostic and portable; build no forge, identity
provider, or secrets store), `the-hub-ships-no-catalog-the-model-belongs-to-the-user`,
`one-front-door-for-web-sign-in`, and
`let-software-describe-itself-from-a-file-in-its-repository`. New to the
standard: an estate's deploy files never live in the product's repository,
and a named, closed list of crossings between a suite and an estate.
