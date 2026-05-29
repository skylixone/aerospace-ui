# TODO (Next Execution Pass)

Goal: convert comment feed into concrete, testable fixes. Keep changes small and verify in `http://localhost:8000/components/index.html`.

## Global / Layout
- **Contrast (nav links)**: raise sidebar link contrast to pass WCAG AA. Current `--text-label` on `--bg` is too dim. Increase link color + active/hover visibility. (selector: `nav.kit-nav`)
- **Link affordance system**: define consistent link styling (color, underline/border, hover, active) for body links and nav links. (selector: `a`)
- **Hero header**: restore consistent hero block layout/spacing; ensure title is not scrambled. (selector: `.page-header`, `.title`)
- **Section title hang**: ensure section numbers hang left of H2 consistently; verify position + spacing. (selector: `.kit-section-title`)
- **Section spacing**: increase vertical spacing between groups/rows where currently cramped. (general sections)
- **Remove unused “Usage” anchors**: remove `.kit-doc-link` throughout. (selector: `a.kit-doc-link`)

## Typography
- **Type body size**: enforce `16px` body size wherever `type-body` used. (selector: `.type-body`)
- **Type small**: bump `type-small` size by one step. (selector: `.type-small`)
- **Overline**: include letter-spacing explicitly in usage descriptions for any uppercase variants. (selector: `.type-overline`)
- **Background for body example**: add bg so `type-body` sample is legible/contained. (selector: `.type-body`)

## Colors
- **Color swatches**: make blocks + titles proportional on large screens; use `em` font sizing for labels and ensure WCAG-compliant sizes. (section: `#colors`)
- **Color variable labels**: use body text size for variable names (not tiny). (selector: `strong` inside swatch info)

## Spacing
- **Spacing demo**: enlarge; add a representative UI component to the right that visually encodes the spacing scale. (section: `#spacing`)

## Buttons
- **Layout matrix**: show every variant × size × state in a row/column grid. (section: `#buttons`)
- **Code block**: arrange in 2 columns of 4 items for button class list. (selector: `.code-block`)
- **Secondary caption**: increase caption contrast for `btn-secondary`. (selector: `.btn-secondary`)
- **Active state**: include active state demo in the matrix. (buttons section)

## Inputs / Toggles / Tabs / Slider / Stepper
- **Toggles layout**: move to full-width grid, each item in its own cell with generous padding. (section: `#toggles`)
- **Tabs**: redesign; current example is unclear/broken. (selector: `.tabs`)
- **Stepper labels**: step caption should be larger than body size. (selector: `.step-label`)
- **Stepper control**: make it horizontal like three ghost buttons: “- VALUE +”. (selector: `.stepper-control`)
- **Slider**: filled portion must be accent color. (slider fill element)

## Cards / Metrics / Tables / Bars / Progress
- **Cards**: increase hover affordance (currently barely noticeable). (selector: `.card`)
- **Metric labels**: make label container hug contents so large numbers align on baseline. (selector: `.metric-label`)
- **Tables**: add tab + filter examples. (section: `#tables`)
- **Table text**: ensure table cell text is high-contrast white. (selector: `td.text-bright`)
- **Bars**: 
  - Use thick bars by default.
  - Align left edge across stacked bars (caption width shouldn’t shift bar start).
  - Set table to ~60% width in bars panel.
  - Increase contrast for planned/actual + ensure legend colors match bars.
  (section: `#bars`)
- **Progress**: restore visuals (currently only titles). (section: `#progress`)

## Panels / Badges / Alerts / Status / Lists
- **Panel footer**: replace placeholder text with real metadata/actions. (selector: `.panel-footer`)
- **Tags**: increase contrast for default tags (white caption + muted border). (selector: `.tag`)
- **Badges**: increase size; update demos to match alert semantics. (section: badges/alerts)
- **Badge content**: use icon-only badges (i / ✓ / ! / ! filled for error). (badges section)
- **Status**: status text color must match dot color; fill status tags and make text black. (status section)
- **Lists**: rename default to “bullets”; add two variants: dashed + right-pointing outlined triangle (accent color). (section: `#lists`)

## Code / Summary / KV / Empty State
- **Code block**: add borders + padding; make 65% width; include larger tabulated code sample. (section: `#code`)
- **Summary**: increase size and reduce line length to ~80 chars. (section: `#summary`)
- **Key-Value**: expand to multi-column layout; increase vertical gaps; raise label contrast; align first cell with H1 (no left padding). (section: `#kv`)
- **Empty State**: rename to “File Upload” and include 3 states: empty / uploading / uploaded. (section: `#empty`)

## Overlays (Cmd, Toasts, Popover, Hovercard, Modal)
- **Cmd palette selection**: selected state must match sidebar hover style. (selector: `.cmd-item.selected`)
- **Popover/Hovercard**: prevent overlap into next section; reserve vertical space in parent (min-height or spacer). (sections: `#popover`, `#hovercard`)
- **Toasts**: 
  - Close “X” in upper-right baseline with title.
  - Add brief + in-depth variants (error code + details).
  (section: `#toast`)
- **Mini toasts**: fixed width (not 100%); increase checkmark size; remove filled circle below checkmark; use unicode spinner for “updating” later (see Backlog). (section: `#mini-toast`)
- **Modal**: render as actual window (not inline flat), fix broken close button + header alignment. (section: `#modal`)

## Dividers / Skeleton / Tooltip / Header / Footer
- **Dividers**: use accent + thicker stroke; show use examples (not 3 identical lines). (section: `#dividers`)
- **Skeleton**: add actual skeleton visuals (currently empty). (section: `#skeleton`)
- **Tooltip**: make tooltip render, not plain text. (selector: `.tooltip`)
- **Header**: try longer 3-word page title; avoid forced line-break. (section: `#header`)
- **Footer**: include timestamp + status indicators. (section: `#footer`)

## Cleanup
- **Remove #vision** section (not needed). (section: `#vision`)

