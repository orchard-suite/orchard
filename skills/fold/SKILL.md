---
name: fold
description: Fold open proposals into Orchard. Turns each proposal issue into a decision record, document changes, roadmap rows, and diagram changes, lands them, and closes the issue. Use on the machine that owns the Orchard repository, on a schedule or when the user asks to fold proposals, update the suite's roadmap, or bring Orchard up to date with what was decided.
---

# Fold proposals into the suite

Only the machine that owns `orchard-suite/orchard` folds. On any other
machine, say so and stop. Work in that repository's checkout and follow its
`AGENTS.md`. This usually runs with nobody watching: ask the person
nothing.

## Steps

1. List the open proposals, oldest first:
   `gh issue list -R orchard-suite/orchard --label proposal --state open --json number,title,labels,createdAt`.
   Leave out any that carry `needs-ruling`. With none, go to step 6.
2. Read each proposal and the records and documents it touches. Sort it:
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
3. Fold one proposal as one landing:
   - Look up the platform standard for the rules the decision builds to
     (its `consult` skill), and cite them by id with the standard's version.
   - Write the next decision record in `docs/decisions/`, in the shape of
     the records there: Status, Date, Standard, Context, Decision, what
     members owe, what is left open, Consequences, Rules. Its number is the
     highest number plus one.
   - Change every document the decision makes wrong, in the same pass.
   - Add a row to `docs/roadmap.md` for each thing a member now owes.
   - Change `docs/orchard.vantage.yaml` where the picture is now wrong,
     validate it, and render the pictures in `docs/diagrams/` again. The
     file names the documents beside it as its pages, so a changed
     document needs no second copy.
   - Run `python3 scripts/check.py`. Fix what it names.
   - Commit as `feat(orchard): decide <what>` and land.
   - Close the issue with a comment naming the record and the commit.
4. Keep the estate out. The proposal was written without names; the record
   must be too. A fact about an app is checked in that app's repository
   before it is written, with the date.
5. Check the roadmap, at most once a week. Skip this step when this pass
   folded nothing and any row's "Checked" day is inside the last seven
   days. Otherwise, for up to five rows still owed, oldest check first,
   read the member's repository and see whether the thing shipped. Mark a
   row done only with the version or commit that proves it, and set its
   "Checked" day. A row that moved is a `fix(orchard): ...` landing of its
   own.
6. Publish the pictures and the pages. When this pass changed the diagram
   file or a document it names as a page, save the file with every page
   to one hub: the diagram hub the owning machine's toolkit names for
   Orchard, the home hub. The suite's documents, decisions,
   roadmap, and diagrams are never copied to any other hub; a machine
   elsewhere reads them through the plugin.
7. Report in a few lines: what was folded into which record, what waits for
   a ruling and why, which roadmap rows moved, and anything skipped.
