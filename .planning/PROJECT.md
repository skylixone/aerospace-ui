# Aerospace UI Kit Update

## What This Is

An update to the Aerospace UI Kit (vanilla HTML/CSS/JS) to bring it in line with the design language established in `the-Operation/dashboard.html`. It focuses on refining the layout, typography, and component set while maintaining the core "amber-on-black" aesthetic.

## Core Value

Modernize the Aerospace UI Kit's layout and component set to match the latest operational requirements without introducing complex build dependencies.

## Requirements

### Validated

- ✓ Core Design Tokens (Amber, Black, Green, Red) — v1.0
- ✓ Typography System (Hero to Overline) — v1.0
- ✓ Basic Component Set (Buttons, Form Inputs, Toggles, Tabs, Tables, Bars, Progress, Panels, Alerts, Status Indicators, Lists, Code, Key-Value, Modal, Skeleton, Tooltip) — v1.0

### Active

- [ ] Implement Fixed Header Layout (56px)
- [ ] Implement Fixed Sidebar Layout (240px)
- [ ] Implement Status Tag variants (.stag with .sg, .sa, .sr, .sd)
- [ ] Implement Score Cards with Stepper/Slider controls
- [ ] Implement Compact Toast System (.toast-mini)
- [ ] Implement Adherence Timeline components
- [ ] Update Typography with standardized letter-spacing (0.12em for nav, 0.15em for overlines)
- [ ] Implement Expandable Sidebar sections (.nav-more)

### Out of Scope

- [Build Tools] — Sticks to Vanilla HTML/CSS/JS to avoid complexity and build steps.
- [Framework Migration] — The project remains framework-agnostic.

## Context

- The project is an evolution of an existing UI Kit.
- Current aesthetic: Amber-on-black, Geist Mono, 0px radius.
- Source of truth for updates: `the-Operation/dashboard.html`.

## Constraints

- **Tech Stack**: Vanilla HTML/CSS/JS — Requirement for simplicity and zero build step.
- **Aesthetic**: Amber-on-black, Geist Mono, 0px radius — Must maintain the "high-tech/aerospace" feel.
- **Compatibility**: Backward compatibility where possible — Avoid breaking existing implementations unless necessary for the new design.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Stick to Vanilla HTML/CSS/JS | Avoid build complexity and maintain portability. | — Pending |
| Prioritize `dashboard.html` design | Ensure the UI Kit reflects the latest and most refined operational interface. | — Pending |
| Standardize letter-spacing | Improve readability and aesthetic consistency across navigation and overlines. | — Pending |

---
*Last updated: 2024-05-23 after initial synthesis*
