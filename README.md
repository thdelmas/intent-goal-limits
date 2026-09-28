# intent-goal-limits


Intent, goal, limits. Is it worth it, and who says.
Specification-driven development for a human-agent pair. A spec has an intent (direction), a goal (success threshold) and limits (the balance between value and cost, with a named bearer for each cost). No single entity writes it: the pair authors it as a binome, two rounds then build, and the people who would pay are asked, each holding a seat that is filled or visibly empty. Every spec keeps an append-only ledger and climbs Written, Closed, Tested.

Read `SKILL.md`. Start a spec from `templates/SPEC.template.md`, keep its ledger per `templates/ledger.md`, and read its state with:

```
scripts/spec-state.py path/to/SPEC.md
```

`SPEC.md` in this repo is the skill's own spec, written with itself. `examples/office-noise/` shows conflicting seats and an empty irreversible seat that keeps a spec from closing.

MIT.
