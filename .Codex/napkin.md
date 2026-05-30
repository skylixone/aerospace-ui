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

## Session 2026-05-29 — Review Comments Batches A-B
- Batch A: #39 overline tracking values, #46 step-label font-size → --text-lg
- Batch B: #38 typo code-block 2-col grid, #44 toggles restructured w/ kit-labels, #66/#69 div→pre code blocks, #70 stepper ghost btn styling
- #43 (btn active) already satisfied — pseudo-active states existed
-  CSS class added for code-block property highlighting
## Session 2026-05-30 — Review Comments Batch C
- #48 metric-label: removed flex+min-height, now hugs contents
- #49 panel td: added color: var(--text-bright) for high-contrast white
- #50/#51 bars: default track height 8px→16px (thick), thin 3px→4px
- #83 bar-val: text-align right→left
- #84 progress: added .thick (12px) and .thin (2px) variants + HTML demos
- #85 bars: added value scale with vertical guides (0–250) under first bar group
- #86 timeline: track height 12px→36px (3× fatter)
- #52 timeline: planned stripes brighter (var(--text-dim)), actual padding adjusted
- #52 timeline panel: max-width 60%, legend uses matching colors
## Session 2026-05-30 — Review Comments Batch D
- #97 cmd palette: added inline JS for arrow-key navigation (↑/↓ cycles .selected)
- #98 cmd shortcut: inverted on .selected (accent bg, dark text), 1.6× larger (10px→16px)
- #99 popover: pops right instead of below, single-line feel, bg→var(--bg), border→var(--border-bright)
- #100 popover inputs: added .input-handle slide indicators on bottom border
- #101 toast viewport: fixed bottom-center (left:50%, translateX(-50%), align-items:center)
- #102 mini-toast code block: already pre.code-block from Batch B
