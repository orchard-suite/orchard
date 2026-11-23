---
name: fold
description: Fold open proposals into Orchard. Turns each proposal issue into a decision record and roadmap items in the hub, document changes in the repository, and diagram changes, lands them, and closes the issue. Use on the machine that owns the Orchard repository, on a schedule or when the user asks to fold proposals, update the suite's roadmap, or bring Orchard up to date with what was decided.
---

# Fold proposals into the suite

Only the machine that owns `orchard-suite/orchard` folds. On any other
machine, say so and stop. Work in that repository's checkout and follow its
`AGENTS.md`. This usually runs with nobody watching: ask the person
nothing.

The records, the roadmap, and the diagrams live in the hub that the
estate's Vantage settings map the repository to; `vantage.yaml` names the
registry (`ORC`), the roadmap kind (`ORCR`), and the document (`orchard`).
The documents live in `docs/` (decision `ORC-0027`). Print the hub and the
workspace with the Vantage plugin's `pointer.sh`. With no hub mapped, say
so and stop.

## Steps

1. List the open proposals, oldest first:
   `gh issue list -R orchard-suite/orchard --label proposal --state open --json number,title,labels,createdAt`.
   Leave out any that carry `needs-ruling`. With none, go to step 5.
2. Read each proposal and the records and documents it touches
   (`vantage_find` with `in: ORC`, then `vantage_read` the section). Sort
   it:
   - **Already decided.** An accepted record says the same thing. Close the
     issue with a comment naming the record. Nothing else changes.
   - **Adds.** It says `new ground` or `extends`, and contradicts no
     accepted record. Fold it (step 3).
   - **Changes a decision.** It amends or supersedes an accepted record, or
     reading it against the records shows a clash it did not name. Do not
     fold it. Add the label `needs-ruling` and a comment that quotes the
     record and the clash in a few lines. It waits for the owner.
   - **Not the suite's.** It is about one app, or a practice for any
     platform. Close it with a comment saying where it belongs.
3. Fold one proposal as one pass:
   - Look up the platform standard for the rules the decision builds to
     (its `consult` skill), and cite them by id with the standard's version.
   - Write the record with the `vantage:decide` skill: a `vantage_write`
     to `ORC`, category 0, the owner as its decision maker. It takes the
     next number. Give it the shape of the records there: Context opens
     with `- Standard:` and the lines that say what it amends or
     supersedes; Decision holds `What members owe`, `Left open`, and
     `Rules`; then Consequences and Alternatives considered. Set `related`
     and `governs` (the boxes and views of `orchard` it decides about).
   - A record it amends or supersedes in part keeps its body. Patch the
     status note at the top of that record's Context ("Accepted, amended
     by 0027 (...)"), and add the new record to its `related`.
   - Hand the record to `platform-standard:capture`, and add the
     `- Capture:` line it returns to the record's Context.
   - Change every document in `docs/` the decision makes wrong.
   - Add an `ORCR` item for each thing a member or an estate now owes: a
     `vantage_write` to `ORCR` with the labels `owes`, `from` (the
     records, as `ORC-0027`), `section`, and `checked` (today), and a body
     that says who owes it, the record it came from, and a `## State`
     section. Link each record with `vantage_item` (`link: { rel:
     decision, target: ORC-0027 }`). A new section is a new choice of the
     `section` label on `<workspace>/orchard-roadmap` and a new heading on
     the page `roadmap.md`, which names each item as `[[item:ORCR-58]]`.
     A new open question goes in that page's table.
   - Change the pictures: `vantage_checkout <workspace>/orchard`, edit the
     views the decision makes wrong and the page `roadmap.md`, copy each
     changed `docs/*.md` over its page of the same name, cite the record on
     the boxes it governs (`decisions:`), `vantage_validate`, and
     `vantage_sync`. Those pages are copies: never edit one in the hub.
   - Run `make check`. Fix what it names.
   - Commit the document changes as `feat(orchard): decide <what>` and land
     with `make land`. A decision that changes no document lands nothing.
   - Close the issue with a comment naming the record, and the commit when
     there is one.
4. Keep the estate out. The proposal was written without names; the record
   must be too. A fact about an app is checked in that app's repository
   before it is written, with the date.
5. Check the roadmap, at most once a week. Skip this step when this pass
   folded nothing and any item's `checked` day is inside the last seven
   days. Otherwise, for up to five items still planned, oldest `checked`
   first (`vantage_outline ORCR#planned`), read the member's repository and
   see whether the thing shipped. Move an item to `reported` only with a
   note naming the version or commit that proves it. An item partly built
   gets its `## State` section rewritten. Either way, set `checked`. These
   changes live in the hub alone and land nothing in the repository.
6. The suite's records, roadmap, and diagrams are never copied to any
   other hub. A machine elsewhere reads them in this hub, or reads only the
   documents through the plugin.
7. Report in a few lines: what was folded into which record, what waits for
   a ruling and why, which roadmap items moved, and anything skipped.
