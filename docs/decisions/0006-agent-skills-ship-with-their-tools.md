# 0006. Agent skills ship with their tools

- Status: Accepted
- Date: 2026-11-08
- Standard: 2026.1107.1839

## Context

A person's agent needs to know how to work with a member: when to read
the catalog, how to write a diagram, how to describe an app. That
knowledge is a skill, a folder of instructions a harness loads, carried
in a plugin with the MCP wiring that reaches the member. A person uses
the same members in more than one estate, and the estates have different
rules: one must never install anything from a repository it does not
run, and must never show a personal repository in its catalog.

Two things were going wrong. A skill lived in a toolkit beside the rules
of the estate, so each estate carried its own copy of it and the copies
drifted. And an estate that could not point its harness at the member's
repository had no way to install the plugin at all, so its people typed
the member's rules into their own skills by hand.

A second question rode along: the market is adding "AI hubs", pages that
list an organization's skills, plugins, MCP servers, and agents. Should
Almanac gain a member for that?

## Decision

**A member's skill ships inside the member.** The repository that builds
the member also holds its plugin: the manifest, the skills, and the MCP
wiring. The plugin's version is the member's version. A skill never
carries a copy of what the member can say for itself; it reads the
member's own guide tools at run time. No toolkit carries a copy of a
member's skill.

**Three layers, merged when the skill runs, each with one owner.**

| Layer | Owner | Holds |
| --- | --- | --- |
| The member's repository | the suite | the tool, its skill, its MCP wiring |
| An estate's toolkit | the estate | the estate's rules for the tool, in a config file the tool or skill reads; where the estate has a rule, it wins |
| A project's repository | the project | the project's own settings |

**How an estate takes a member depends on how it is used, not who wrote
it.**

- A *hosted service*, an app the estate's cluster runs, is consumed as a
  URL. The platform pulls its image from wherever it is published.
- A *distributed artifact*, anything people install on their machines (a
  CLI, a skill, a plugin, an MCP server), comes from the estate's own
  forge. The estate's catalog and marketplaces point only there.

**Every release publishes the plugin on its own.** Beside its image, a
member's release pushes the plugin as a zip to a public package in the
same registry namespace, as an OCI artifact, signed keyless by the
release workflow like the image. The zip holds the plugin alone. Its
sha256 is the artifact's single layer digest, so a harness that pins an
archive by digest and a registry that stores the artifact by digest agree
without a second file.

**One marketplace per estate.** An estate's harness installs plugins from
one marketplace file the estate owns, which pins every member's plugin to
a release. An estate that may install straight from the member's
repository pins a release tag there. An estate that may not runs a
recipes pipeline in its own forge: for each plugin on its list, resolve
the release, verify the signature against the member's release identity,
pull the zip, check the digest, upload the zip to the forge's own package
registry, and write the marketplace file with archive sources pinned by
sha256. A bump in either estate is one version change. The forge
publishes nothing that was not released, signed, and verified first.

**A member an estate must build itself** (one with no hosted service and
no release the estate may consume) is mirrored as source into a
read-only project in the estate's forge, with no commits of its own,
refreshed on a schedule, built by a tag pipeline, and published under the
upstream's version.

**Remote wiring is the plugin's default.** A plugin's MCP wiring connects
to the member's hosted hub over HTTP with a personal key, found per hub by
a command or a file the estate's toolkit sets. A plugin that needs a
checkout of the member to work is a plugin an estate cannot distribute.

**The AI hub is an Orrery pack, not a member.** The things a hub lists
are inventory and records like any other: `ai_skill`, `ai_plugin`,
`ai_marketplace`, `ai_mcp_server`, `ai_agent`, and `ai_install` (which
machine has which plugin at which version, pushed by the workstation
agent). They link to `person`, `team`, and the `sw_` blueprints they
serve. Scorecards judge them: signed, pinned, current, installed from the
estate's marketplace. Which skills are used, and how often, is telemetry
the harnesses already emit, read from the estate's observability stack,
not entities. The one product change is generic: a catalog page composed
of several blueprints' views, declared in the catalog file, so an estate
can give its hub a front page without Orrery knowing what a skill is.

## Consequences

- Orrery and Vantage publish their plugin zips from their release
  workflows today. Vantage's released plugin carries remote wiring to a
  hub; the checkout-based wiring stays for developers.
- A new member is not released until its plugin publishes with it.
- An estate's toolkit loses every copy of a member's skill, and gains a
  marketplace file (or a recipes list) and the config files its rules
  live in.
- The blueprint standard gains the `ai_` pack. Orrery gains composed
  pages. forgitten, as the workstation agent, learns to push
  `ai_install`. None of these have shipped; each lands in its own
  repository.
- The toolkit rule in the standard says a fix to a skill both toolkits
  carry reaches the other only by copying. For a member's skill that is
  no longer true: there is one copy, in the member, and both estates
  take it by version. The rule should narrow to skills that belong to a
  context.

## Built to the standard

Standard 2026.1107.1839:

- `skills-in-the-agent-plugin-read-the-rules-from-the-hub-and-n`
- `keep-one-copy-of-a-standard-and-withdraw-rules-out-loud`
- `build-and-sign-every-house-image-in-its-own-repository-s-wor`
- `keep-agent-keys-personal-and-fetched-from-the-vault`
- `name-blueprints-by-pack-on-one-standard`
- `sort-every-catalog-blueprint-as-inventory-record-history-or-`
- `keep-one-agent-toolkit-per-context-with-one-layout-and-a-che`,
  narrowed as the last consequence says.

New to the standard: no rule covers where a tool's skill lives, how a
plugin is signed and carried into an estate that cannot read its source,
or that the AI hub is a pack rather than a product. This decision sets
them for the suite.
