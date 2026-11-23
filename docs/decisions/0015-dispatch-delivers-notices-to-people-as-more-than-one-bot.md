# 0015. Dispatch delivers notices to people, as more than one bot

- Status: Accepted
- Date: 2026-11-20
- Standard: 2026.1120.412
- Extends: 0001

## Context

Decision 0001 admitted Dispatch as the incident desk. The suite's
documents have described it that way since. Dispatch has grown a second
job in its own repository: it sends notices for other products.

An estate now has a product whose readers are business users, not the
platform team. Each person there picks, for each kind of notice, whether
it reaches them in the product, by email, in chat, or any mix. Email
already works. Chat needs a sender. If every product builds its own chat
bot and its own delivery code, an estate gets many small senders that
each retry, store secrets, and prove delivery in their own way. That is
the sprawl the suite exists to prevent.

A chat bot has a name, and people learn who is speaking by it. A notice
for business users should not arrive from a bot named for platform
engineering.

These facts were read from Dispatch's repository on 2026-11-20, at
v0.0.40:

- Its README says it is the one place every product's notices go out
  from. A product sends an event. Dispatch posts it to channels, and
  tells people through the apps they already have: Teams, Discord, text
  messages, and email.
- An event may name who it is for: a person, a group, or an on-call
  chain. In Teams, a person gets a chat from the bot, one to one.
- Every message is a stored row before it is sent, and it keeps the
  medium's answer. An admin reads these on a page of the desk. The API
  has no call a sender can use to read how its deliveries went.
- It runs one Teams bot. One setting names the bot's app, and one names
  the single product whose buttons the bot shows.
- It posts each routing decision to Ledger.

## Decision

1. **Dispatch is the one place a product's notices go out from.** A
   product sends Dispatch an event. It keeps no chat or mail code of its
   own. This is true of members and of an estate's own products alike.
2. **Dispatch delivers to people, one to one, not only to channels.** A
   product sends an event that names a person, and Dispatch messages
   that person directly in Teams.
3. **Dispatch can speak as more than one bot.** A product whose readers
   are a different audience from the platform team gets its own bot,
   named for the product. Dispatch sends that product's notices as that
   bot.
4. **The platform team's bot stays.** It is the voice for platform
   alerts, approvals, and deploys.
5. **A new bot still needs a reason.** The reasons are a new audience, a
   data boundary, or a different owner. Wanting another name is not one.
6. **A bot belongs to an estate.** Its identity and its chat app are the
   estate's. Dispatch takes them as configuration, and names none in its
   code.
7. **No member joins.** The suite still has ten members. Dispatch's
   pillar and its tending job do not change.

Two things were weighed and turned down:

- Sending every product's notices from the one platform bot. It is the
  wrong voice for an audience that is not the platform team.
- A separate bot service owned by the product. It would be a second
  delivery engine.

## What members owe

| Member | It owes |
| --- | --- |
| Dispatch | Accept an event addressed to a person and deliver it to that person in Teams, one to one, with delivery status the sender can read. |
| Dispatch | Serve more than one bot, each with its own identity and Teams app, and pick the bot by the product that sends. |

The first is partly built. Dispatch already takes an event addressed to a
person and messages them in Teams. The sender cannot yet read how the
delivery went.

## Left open

- **Whether a medium is a crossing.** Dispatch reaches a chat service, a
  mail service, and a text service that an estate brings. `seam.md` lists
  nine crossings, and none of them is a medium. Naming one would change
  the list decision 0002 closed, so it needs its own record.

## Consequences

- `members.md` says Dispatch sends notices, what it reads and writes for
  that, and what is owed.
- `seam.md` lists chat bots with what an estate holds.
- `README.md` names notices in Dispatch's row.
- `pillars.md` corrects two facts in the observability row. Dispatch no
  longer notifies through one webhook only, and it keeps on-call
  schedules. The rating is not judged again here.
- `roadmap.md` gains rows 19 and 20.
- The diagram file gains an estate's products sending notices, the chat
  service, and the two rows that are owed.

## Rules

Builds to:

- `send-every-product-s-notifications-through-one-delivery-serv`: one
  delivery service owns every medium, and products keep no mail or chat
  code.
- `one-platform-chat-bot-a-second-only-for-a-new-audience-data-`: a second
  bot only for a new audience, a data boundary, or a different owner.
- `post-every-routing-decision-a-notice-router-makes-to-the-led`: what
  Dispatch decides about a notice is in Ledger.
- `keep-every-estate-on-its-own-side-of-a-seam-with-a-closed-li`: a bot's
  identity is the estate's, and reaches Dispatch as configuration.
- `admit-a-tool-to-the-platform-suite-only-by-a-written-members`: weighed,
  and no member joins.

Departs from:

- `one-platform-chat-bot-a-second-only-for-a-new-audience-data-`: the rule
  says a bot for a different audience belongs to that product's team and
  lives in that product's own landing zone. Here the delivery service
  serves the second bot too. Why: a bot the product hosts needs its own
  delivery code, and that is a second delivery engine. The rule's three
  reasons for a second bot stay.

New to the standard: the standard has no rule for one delivery service
that speaks as several bots and picks the bot by the product that sends,
or for a sender reading back how its deliveries went.
