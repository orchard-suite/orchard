# 0022. Every member pushes an inventory of what it holds into the catalog

- Status: Accepted
- Date: 2026-11-22
- Standard: 2026.1120.2003
- Capture: 8b964f1c-ca6e-4df2-9d55-a77f30c5d12d

## Context

The catalog is where an estate looks first. An admin goes there to see
everything the estate owns. A person goes there for their own things.

Some of what an estate owns lives inside the suite's own members: a
workspace of diagrams, a pack of rules, a lane of requests. Each member
keeps those records in its own store. Whether the catalog lists them
depends on the member.

`members.md` holds a table of what each member writes to the catalog. Six
members write there. conform is the plainest case: it writes its own
packs, so an estate sees the standards it holds beside the things they
judge. Three members write nothing: Vantage, Ledger, and forgitten.

These facts were read from Vantage's repository on 2026-11-22, at v3.1.0:

- A hub reads the catalog through a connector. It writes nothing to it.
- Its own spec says a hub pushes an inventory of its workspaces, members,
  documents, and items to the estate's catalog, and that the catalog
  lists them while the hub stays their home.
- The same spec says that pusher is the one part not built. It waits for
  kinds in the catalog for a workspace and an item.

So a person's workspaces and documents are the one part of their things
that the catalog cannot show them.

## Decision

1. **Every member pushes an inventory of what it holds into the catalog.**
   An estate's admin sees everything the suite holds in one place, beside
   everything else the estate owns.
2. **The catalog stays an inventory.** A member stays the source of truth
   for the records its own software creates. The catalog is never the
   store for them.
3. **Vantage pushes its workspaces.** For each workspace: its members,
   how many documents and diagrams it holds, and how much storage it
   uses. Each workspace links to the person records of its members.
4. **A person sees only their own.** In the catalog a person sees the
   workspaces they own or belong to, and what is in them. Admins see all
   of it. The member pushes the links that make this possible. The rule
   itself is kept in the catalog, where every access rule is kept, and it
   is set before the first push.
5. **If Vantage comes to hold work items, it pushes those too.** This
   decision does not say that it holds them.
6. **No member joins.** The suite still has ten members.

One thing was weighed and turned down: making the catalog the store for a
member's own records. A catalog takes snapshots from sources. It is not
built for records written one at a time.

The seam gains no crossing. A member already describes itself to the
estate's catalog, and already writes to it with a token the estate gives.

## What members owe

Each is that member's own design, recorded in its own repository.

| Member | It owes |
| --- | --- |
| Vantage | Push its workspaces, their members, document and diagram counts, and storage used into the catalog, linked to person records, readable by membership. |
| Vantage | Push its work items the same way, if a later decision gives it work items. |
| Every other member that holds records of its own and does not push them yet | Push an inventory of them. |

None is built.

## Left open

- **Which members still owe an inventory.** It was not checked member by
  member. `members.md` lists Ledger and forgitten as writing nothing to
  the catalog. What a machine reports already lands on the repository's
  record under decision 0017, so forgitten's part has a row.
- **Whether Vantage holds work items.** At v3.1.0 Vantage tracks items
  through a lifecycle. No suite decision says that is what Vantage is. A
  proposal that says so amends decision 0014, and it waits for the
  owner's ruling.

## Consequences

- `members.md` says every member pushes an inventory, and that Vantage's
  is owed.
- `strategy.md` says the members push what they hold to the catalog.
- `roadmap.md` gains rows 41 and 42, and one open question.
- The diagram gains one amber arrow, from Vantage to the catalog.
- An estate that runs Vantage and the catalog gains kinds for a
  workspace, and sets who may read them, before the first push.
- The suite's member count does not change. No rating changes.

## Rules

Builds to:

- `read-the-catalog-first-and-keep-it-complete`: one graph answers what
  exists, and nobody builds a second inventory beside it.
- `sort-every-catalog-blueprint-as-inventory-record-history-or-`: what a
  member pushes is inventory, overwritten by each push. The records stay
  with the member.
- `open-a-catalog-kind-s-entities-to-their-owners-with-a-curate`: a
  person outside a kind's audience sees only their own entities of it.
- `leave-out-what-a-reader-may-not-see-and-never-mark-it-restri`: a
  workspace a person is not in is left out, not marked.
- `pushers-and-imports-can-only-add-to-the-model`: a pusher's offer
  carries no access rule, so a kind that holds facts about people gets
  its rule before the first push.
- `the-hub-ships-no-catalog-the-model-belongs-to-the-user`: the member
  offers its kinds. The catalog ships none of them.

Departs from: none.

New to the standard: the standard has no rule that every service of a
platform suite pushes an inventory of what it holds into the catalog, or
that a diagram hub's workspaces and their members are catalog inventory.
