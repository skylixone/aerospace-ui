# Napkin

## Corrections
| Date | Source | What Went Wrong | What To Do Instead |
|------|--------|----------------|-------------------|
| 2026-05-29 | user | Killed review-server during verification — it was just slow, not hung | Never kill review-server unless explicitly told or verifiably hung (timeout >10s on restart)
| 2026-05-29 | user | Needed clarification on batch scope before execution | Ask for exact batch scope if not explicit |
| 2026-05-29 | user | Proceeded without executing tools after being told to execute | Always run tools immediately when instructed |

## User Preferences
- Execute tools immediately when the user instructs action; don't reply with status-only messages.
- Use semantic HTML (h1/h2) and style elements directly unless variant hooks are needed.
- For this repo: prefer small, verified batches with explicit approval gates.

## Patterns That Work
- Batch execution with verification stop is preferred for large TODOs.

## Patterns That Don't Work
- Adding extra visual affordances not requested (e.g., nav link bottom borders) leads to rework.

## Domain Notes
- UI kit lives at /Users/ikornii/Documents/aerospace-ui/components/index.html with shared styles in style.css.
## Session 2026-05-29 — Batch 6-9 Execution
- Executed TODO.md batches 6-9 autonomously per user instruction ("godspeed")
- Used Python for multi-line HTML/CSS replacements (sed chokes on newlines in substitute)
- Always verify HTML tag balance with `python3 -c` after edits
- CSS `:has()` works for status dot color matching (modern browsers)
- Badge-outline/badge-dim had duplicate definitions at end of CSS file — updated both
- When inserting into grid layouts, ensure new children are inside the grid container, not after its closing `</div>`
