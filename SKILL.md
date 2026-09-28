---
name: intent-goal-limits
description: "Specification-driven development for a human-agent pair. A spec has three parts: intent (the direction), goal (the success threshold), limits (the balance between the value pursued and its cost, with a named bearer for every cost). No single entity can write one: the pair authors it as a binome (one proposes, the other challenges, switch, two rounds then build), and limits are set by asking the people who would pay, each of whom holds a seat that is either filled or visibly empty. Every spec carries an append-only ledger and climbs a ladder: Written, Closed, Tested. Specs change only from ledger rows, never from another draft. TRIGGERS: 'spec this', 'write the spec first', 'binome spec', 'who pays for this', 'is the spec closed', 'which seat is empty', 'spec or implementation', 'did the spec cause this bug', 'are we over-specifying', 'spec ladder'."
---

# intent-goal-limits: is it worth it, and who says

A spec is three parts: intent, goal, limits. Everything else in this skill exists to keep those three honest.

With agents doing the typing, the spec is where errors are cheap and where judgment lives. Reviewing forty lines of intent beats reviewing two thousand lines of output. This skill makes the spec the reviewed artifact, and it makes the spec honest about who pays for it.

Three claims underneath it:

1. **No single entity can define a spec.** The one who sets the goal is the wrong person to set its limits. The party who bears the cost of the goal is the one entitled to name where it stops, and that party sits outside the entity that wrote the goal. A second model debating the first shares its frame and is not a challenger.
2. **Limits are a balance, not a fence.** A limit is not a list of forbidden paths. It is the point where the value pursued no longer justifies its cost, judged by the person who carries that cost.
3. **Specs evolve, so they need a ledger.** A limit starts unasked, someone who pays is asked, the limit changes, the goal may die. Each event is a row. A spec that never changed was never tested.

## The three parts

| Part | What it is | Test |
| --- | --- | --- |
| **Intent** | The direction. The why being served. It has no end state. | Could a different goal serve it? If not, it is a goal, not an intent. |
| **Goal** | The success threshold. The point on the direction that counts as done. | Can it fail? A goal that cannot fail is a wish. |
| **Limits** | The balance between value and cost. Each cost has a named bearer. The goal or the intent becomes unworthy when the balance tips for that bearer. | Who pays, and were they asked? |

Worked example, not software: intent, people are happier. Goal, nobody is hungry. Limit, if others must suffer more so that nobody is hungry, the goal has become unworthy of the intent.

Intent, goal and limits are three levels. A missed goal leaves the intent standing and asks for a new threshold. A crossed limit can kill the goal, or the intent itself.

## Seats

Every cost in the limits names who bears it. Each bearer is a **seat**. A seat is either:

- **filled**: that person, or someone who bears that cost in their own life, was asked, and their answer is a row in the ledger;
- **empty**: nobody was asked. The spec says so, visibly. Filling a seat by imagination and tagging it filled is the one thing this skill forbids outright.

The seat's credential is bearing the cost, not holding a label or a diagnosis. When two seats disagree, both answers are rows and the limit they disagree on stays open. The spec does not average them.

Each seat computes its own value against cost balance. The skill makes that balance computable per seat. It never computes one number for everyone; a single ratio needs a single currency and a single payer, and erases the seat.

## Cost class

The spec declares whether a wrong build is **reversible** (a revert, a rollback, a deleted file) or **irreversible** (a person acted on it, money moved, a category was applied to someone). Cost class decides when building may start:

- reversible: build at Written, with empty seats visible;
- irreversible: no build before Closed.

## The ladder

A spec's state is read from its ledger, never from its prose.

| Rung | Condition |
| --- | --- |
| **Written** | Intent, goal and limits present. Every cost has a named bearer. Every seat tagged filled or empty. Cost class declared. An empty file fails. |
| **Closed** | Every seat bearing an irreversible cost has been asked. Disagreeing seats are both recorded and keep their limit open. Reversible seats may stay empty. |
| **Tested** | A row shows the spec stopped or changed a build: a limit fired, a goal was revised, an intent was dropped. |

The skill's own fitness signal is the share of specs that reach Tested, not the number of specs written.

## Binome authoring

Specs are written and corrected in plan mode, in conversation, never generated as a side effect of a build.

1. One of the pair proposes intent, goal and limits.
2. The other challenges, one point per part.
3. Switch: the challenger proposes the next version, the proposer challenges.
4. **Two rounds, then build.** More drafting is over-spec. After the second round, a spec changes only when a ledger row demands it.

The challenger must hold a frame the proposer does not. If the agent is only the human's second draft, say so and stop.

## Bugs go back to the spec

When a bug or blocker appears, before touching code, ask which level broke and say which:

1. the goal is off the direction (wrong goal for the intent);
2. a limit was crossed (the price tipped for some seat);
3. goal and limits hold and the implementation is off.

If the spec was wrong, fix the spec first, then the code. Never leave a spec stale behind a patched implementation. Each such finding is a row, and it is what moves a spec to Tested.

## Files

- `SPEC.md` next to the code it governs, from `templates/SPEC.template.md`.
- `SPEC.ledger.jsonl` beside it, append-only, one JSON object per line, from `templates/ledger.md`.
- `scripts/spec-state.py SPEC.md` reads both and prints the rung, the empty seats, and what is missing for the next rung. It refuses a spec that tags a seat filled without an asked row.

## Limits of this skill

By its own rule, this skill names where it stops being worth using:

- when specifying costs more than the build it guards;
- when it fills a seat by imagination and tags it filled;
- when it freezes a category the world still argues about;
- when it makes correction harder than the wrong build it was meant to prevent.

Its own `SPEC.md` and ledger are in this repo. It was written with itself, in four drafts, which was two too many; the two-round cap is the row that came out of that.
