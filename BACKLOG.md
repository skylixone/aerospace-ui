# BACKLOG (Later / Ideas / Needs Decision)

Items that are not immediate fixes, need design direction, or require separate research.

## Visual / Design Explorations
- **Skeleton animation upgrade**: explore a more interesting loading animation than simple shimmer. Collect references + propose 2–3 options before implementing.
- **Link types**: define multiple link styles (e.g., inline, nav, quiet, destructive, external) with consistent states. Requires a mini design spec.
- **Empty state layout**: explore more aesthetic layout for file upload states (iconography, composition). Provide options.

## Interaction Research
- **Unicode spinner choice** for mini toast “updating” state: pick a readable mono-friendly glyph set; confirm with user before implementation.

## Systemic Refactors
- **Global link system**: if multiple link types are added, consider a small tokenized link system (colors, underline styles, focus ring), but only after samples are approved.

## Accessibility
- **Button disabled state WCAG failure**: `opacity: 0.35` on `.btn:disabled` fails WCAG AA contrast (4.5:1) on both filled and outline variants. Need to redesign disabled state with explicit muted colors instead of opacity reduction. Keep opacity for cursor/pointer-events but set explicit color values.

## Command Palette
- **State variants visualisation**: brainstorm and enrich in-depth state variants for the command palette — autocomplete dropdown, search result suggestions, loading/querying state, no-results empty state, highlighted match within results, group headers with collapse, recent/frequent items section, error state, and keyboard shortcut rebinding hints. Each variant needs distinct visual treatment while staying cohesive with the palette's dark, minimal aesthetic.
