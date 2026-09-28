# SPEC.ledger.jsonl

Append-only. One JSON object per line. Never edit a past row; a correction is a new row.

| Field | Meaning |
| --- | --- |
| `date` | YYYY-MM-DD |
| `kind` | one of `written`, `proposed`, `challenged`, `asked`, `answered`, `limit-changed`, `goal-revised`, `intent-dropped`, `build-stopped`, `build-changed`, `closed`, `note` |
| `seat` | the bearer this row concerns, or `_pair` for the authoring pair, or `_spec` for the spec as a whole |
| `by` | who wrote the row |
| `reason` | one line |

Rung derivation: `written` needs a `written` row and a valid SPEC.md; `closed` needs an `asked` row for every irreversible seat marked filled, and no filled seat without one; `tested` needs at least one `build-stopped`, `build-changed`, `limit-changed`, `goal-revised` or `intent-dropped` row dated after the `written` row.
