# Changelog

All notable changes to the Aerospace UI Kit.

## [Unreleased]

### Batch J — Badges / Status / Tags / Lists
- **Badges**: increased to 32×32px across all variants (was 26×26px); icon font-size 14px → 16px
- **Badge demos**: reorganized to alert semantics — `i` (info), `✓` (success), `!` (warning), `!` (error)
- **Tags**: default border color `var(--border-muted)` → `var(--border-dim)` for better visibility
- **Status**: offline state now uses `var(--text-muted)` text color to match dim dot
- **Cleanup**: removed duplicate `.badge-outline` / `.badge-dim` CSS block

### Batch I — Cards / Bars / Timeline
- **Cards**: hover affordance strengthened — border glows `var(--accent)`, lift `translateY(-2px)`, added `box-shadow`
- **Bars**: `.bar-wrap` switched from flex to `grid: 72px 1fr` — guarantees all bar tracks start at identical X regardless of caption length
- **Bars**: `.bar-scale` margin-left updated to `84px` to align with new grid gutter
- **Timeline**: planned stripes changed from `var(--text-dim) opacity:0.5` to `var(--text-bright) opacity:0.35` for higher contrast
- **Timeline**: legend color updated to match planned stripe color

### Batch H — Toggles / Tabs / Stepper / Slider
- **Toggles**: layout verified — full-width grid with `minmax(280px, 1fr)` and generous per-cell padding
- **Tabs**: added multi-panel HTML + JS interactivity for both Underline (4 tabs) and Segmented (3 tabs) variants
- **Tabs**: `.tab-panel` defaults to `display: none`; `.tab-panel.active` reveals with `display: block`
- **Stepper control**: fixed CSS selector — `.stepper` → `.stepper-control` (was being overridden by phased stepper rule)
- **Slider fill**: added JS logic to set `--slider-fill` CSS custom property on every `input` event
- **Stepper bars**: thickened indicator bars to 16px (same as Standard Bars) for both horizontal and vertical variants

### Batch G — Button Polish
- **Ghost button**: border-color now matches text color (`var(--text-dim)`)
- **Danger button**: swapped default/hover — default transparent, hover gains `var(--red-dim)` background
- **Loading spinner**: fixed keyframes to include `translate(-50%,-50%)` alongside `rotate`, preventing diagonal drift
- **Ghost loading spinner**: color synced to match new ghost text color

### Batch F — Typography + Colors + Spacing
- **`--text-sm`**: 13px → 14px
- **Typography demo**: `.type-body` example now has `background: var(--bg-raised)` for legibility
- **Color swatches**: blocks taller (`clamp(100px, 10vw, 160px)`), grid uses `minmax(220px, 1fr)`
- **Spacing demo**: bars taller (28px), row gaps increased

### Batch E — Sidebar Navigation
- **Sidebar width**: 240px → 260px
- **Nav links**: hover/active states use inset accent bar (`box-shadow: inset 2px 0 0 var(--accent)`) + `var(--bg-hover)` background
- **Nav headings**: spacing increased between groups
- **Cleanup**: removed `.nav-highlight` floating div; `.active` class on links is sufficient
- **Revert**: removed overdone `.nav-heading` border-left and padding-left

### Batch D — Overlays (Cmd / Popover / Toast)
- **Cmd palette**: uniform 36px item heights; persistent accent outline on focus
- **Cmd palette**: `Cmd+K` scrolls to section and focuses list for immediate arrow-key navigation
- **Cmd palette**: selected state matches sidebar hover style (`inset 2px` accent bar + `var(--bg-hover)`)
- **Popover**: toggle fixed; pops to the right with single-line feel; bg → `var(--bg)`, border → `var(--border-bright)`
- **Toasts**: viewport fixed to bottom-center (moves in from outside viewport bottom)
- **Mini-toast code block**: already uses `pre.code-block` format

### Batch C — Buttons / Metrics / Tables / Bars / Progress / Timeline
- **Buttons**: matrix table aligned by left side of cells; variation names changed to `.classes` in body text
- **Buttons**: default btn fill = accent color; text = darkest from palette; hover = shade lighter
- **Buttons**: ghost btn border matches value color; danger hover/default swapped; secondary caption matches border
- **Metrics**: `.metric-label` hugs contents (removed flex + min-height)
- **Tables**: high-contrast white cell text (`color: var(--text-bright)`)
- **Bars**: default track height 8px → 16px (thick), thin 3px → 4px
- **Bars**: value scale with vertical guides (0–250) under first bar group
- **Progress**: restored visuals with `.thick` (12px) and `.thin` (2px) variants + HTML demos
- **Timeline**: track height 12px → 36px; planned stripes brighter (`var(--text-dim)`)

### Batch B — Colors + Typography Alignment
- **Colors**: core palette + semantic swatches finalized
- **h2 / `.kit-section-title`**: top-aligned by cap line using `text-box-trim` where supported

### Batch A — Global Layout + Header
- **Sidebar**: link refinements — removed secondary border-bottom and redundant highlight
- **Header**: `.kv-grid` positioned below page title with 32px vertical distance
- **h1**: styled directly in CSS without `.title` class selector per W3C recommendation
- **`.kit-doc-link`**: commented out throughout
- **Typography section**: removed border and padding from body example

### Batch K — Code / Summary / KV / Empty State
- **Code block**: larger tabulated sample with section dividers and aligned columns
- **Summary sizes**: increased across all variants — lg `var(--text-2xl)`, md `var(--text-xl)`, sm `var(--text-lg)`
- **Summary text**: trimmed to ~80 chars per line
- **KV grid**: expanded to responsive multi-column (`auto-fill minmax(200px, 1fr)`); gap increased to `var(--space-md)`
- **KV cells**: explicit `border` per cell; first cell `padding-left: 0` + `border-left: none` to align with H1
- **KV labels**: contrast raised to `var(--text-bright)`
- **Empty state**: already "File Upload" with 3 states — no changes needed

### Batch K Fix — KV Grid + Section Numbering
- **KV grid**: restored table-like visual (reverted separate tiles; back to `gap: 1px` + `background: var(--border-dim)` + outer border)
- **Section numbering**: discovered `#steppers` was missing `kit-section-title`; added it; renumbered all 35 sections sequentially 01–35 to match sidebar order
- **Empty state**: verified present at `#empty` (renumbered to 23)

### Batch M — Dividers / Skeleton / Tooltip / Header / Footer
- **Dividers**: `.divider-accent` removed opacity (now solid `var(--accent)` at 2px); `.divider-dashed` border color upgraded to `var(--border-bright)`
- **Skeleton**: already populated with 3-card shimmer grid — no changes needed
- **Tooltip**: border upgraded to `var(--border-bright)`; added `::before` arrow indicator; demo text styled with dotted underline + bright color for affordance
- **Header demo**: changed to 3-word title "Flight Control Dashboard" (avoids forced line-break)
- **Footer**: already includes timestamp + status indicators — verified
- **Cleanup**: no `#vision` section present — nothing to remove
