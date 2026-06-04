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

## Session 2026-05-31 — Batch F
- Bumped `--text-sm: 13px → 14px` per TODO + comment
- Updated typography demo: `.type-body` example now has `background: var(--bg-raised)` for containment
- Updated `.type-small` description text 12px → 14px
- Colors: swatch blocks taller `clamp(100px, 10vw, 160px)`, grid minmax `220px` for proportional large-screen layout
- Spacing: demo bars taller (28px), row gap increased (20px)
- Careful: Python string replace can break HTML tag boundaries when matching across lines; always verify tag closure after multi-line replacements

## Session 2026-05-31 — Sidebar Revert
- Reverted `.nav-heading` border-left and padding-left (was overdone)
- Removed `.nav-highlight` floating div + CSS block; `.active` class on links is sufficient
- Cleaned up unused `updateHighlightPosition` / `keepLinkInView` from nav_highlight.js
- Deduplicated `.kit-nav .nav-heading:first-child` rule in CSS

## Session 2026-05-31 — Batch G
- Ghost button: border-color now matches text-color (`var(--text-dim)`)
- Danger button: swapped default/hover — default is transparent, hover gains `var(--red-dim)` bg
- Fixed loading spinner animation: keyframes now include `translate(-50%,-50%)` alongside `rotate`, preventing diagonal drift
- Ghost loading spinner color updated to match new ghost text color

## Session 2026-05-31 — Batch H
- `.stepper-control` CSS: renamed selector from `.stepper` (was overriding phased stepper rule)
- Tabs: added multi-panel HTML for both Underline (4 panels) and Segmented (3 panels) demos
- Tabs: added JS click handler in interactions.js — cycles `.active` on tabs + panels, respects `disabled`
- Tab panels: added `display: none` default + `.tab-panel.active { display: block; }` in CSS
- Slider fill: added JS in interactions.js — sets `--slider-fill` custom property on each `input` event
- Review server: restarted with nohup after finding it down (curl returned 000)
- Headless Chrome screenshots confirmed non-functional on this Mac — rely on user verification in their Chrome

## Session 2026-05-31 — Batch I
- Cards: strengthened hover — `border-color: var(--accent)`, `translateY(-2px)`, added `box-shadow: 0 8px 24px rgba(0,0,0,0.4)`
- Bars: switched `.bar-wrap` from flex to `grid-template-columns: 72px 1fr` — ensures all bar tracks start at same X regardless of caption length
- Bars: updated `.bar-scale` margin-left `68px` → `84px` to align with new grid gutter
- Timeline: `.timeline-planned` stripes changed from `var(--text-dim) opacity:0.5` to `var(--text-bright) opacity:0.35` for higher contrast
- Timeline: legend color updated from `var(--text-dim)` to `var(--text-bright)` to match planned stripe color

## Session 2026-06-04 — Batch J
- Badges: 26px → 32px square across all variants (badge, badge-outline, badge-dim, badge-icon)
- Badge icon font-size: 14px → 16px
- Badge demos: reorganized to alert semantics — i (info), ✓ (success), ! (warning), ! (error) + numeric/outline/dim
- Default tag border: `var(--border-muted)` → `var(--border-dim)` for slightly more visibility
- Status offline: added `.status:has(.status-dot:not(.online):not(.away):not(.busy))` → `color: var(--text-muted)`
- Cleaned up duplicate `.badge-outline` / `.badge-dim` rules at end of CSS (leftover from earlier batch)
- Panel footers already had real metadata/actions — no changes needed
- Lists already had Bullets/Dashed/Triangle/Triple Dash variants — no changes needed
- RAG filled status tags already had black text on solid bg — no changes needed

## Session 2026-06-04 — Batch K
- CSS `.kv-grid` gap-trick (`gap: 1px` + `background: border-color`) breaks when increasing gaps; switched to explicit cell borders
- `.kv-cell:first-child { padding-left: 0 }` aligns first cell content with h1 text when grid container has no left padding/border
- Summary label strings in HTML must be updated alongside CSS font-size changes to stay accurate

## Session 2026-06-04 — Batch K Corrections
- KV grid: user prefers table-like (gap-trick + outer border) over separate tile cards; reverted tile approach
- Section `#steppers` had been missing `kit-section-title` for multiple batches — only caught now during numbering audit
- Renumbering sections: always count section titles against sidebar links to catch missing/extra titles

## Session 2026-06-04 — Sidebar Sync Principle
- **When adding/removing main content sections, ALWAYS sync the sidebar nav links** to match the actual section list. Sidebar is the source of truth for ordering, but it must also be the accurate reflection of what exists.
- Before committing any section add/remove, grep both the sidebar `<nav>` and the main `<section>` tags to verify 1:1 correspondence.

## Session 2026-06-04 — Batch M
- Dividers: accent divider now solid (no opacity), dashed divider uses brighter border color
- Tooltip: added arrow indicator via ::before; border brightened; demo text given dotted underline for affordance
- Header demo: 3-word title "Flight Control Dashboard" to test line-break behavior
- Skeleton section already had visuals — verified, no changes
- Footer demo already had timestamp + status — verified, no changes
- #vision section not present in HTML — no cleanup needed
