# Pitfalls Research

**Domain:** Industrial/Aerospace UI Dashboards
**Researched:** 2024-05-22
**Confidence:** HIGH

## Critical Pitfalls

### Pitfall 1: The Reactivity Tax (Over-complex JS)

**What goes wrong:**
Using global state management (Redux, XState) or heavy reactivity frameworks for trivial UI states like dropdowns, tabs, or hover effects. In high-density dashboards (100+ telemetry points), every minor state change triggers a virtual DOM reconciliation cycle, leading to "input lag" where clicks or taps feel disconnected from the UI response.

**Why it happens:**
A "framework-first" mindset that ignores browser primitives. Developers often default to the patterns they use for standard CRUD apps without accounting for the extreme data density of industrial dashboards.

**How to avoid:**
Keep state as close to the DOM as possible. Use native CSS for disclosure patterns (`:hover`, `:focus-within`, `details/summary`). For real-time data, use direct DOM manipulation or localized component state rather than global stores.

**Warning signs:**
- Frame rates dropping below 60fps during simple UI interactions.
- Visible delay between clicking a button and seeing the "active" state.
- Profiler shows long "Recalculate Styles" or "Scripting" phases for minor events.

**Phase to address:**
Core Architecture / Interaction Logic

---

### Pitfall 2: Information Density Collapse (Poor Mobile Accessibility)

**What goes wrong:**
Attempting to mirror a desktop-density control room monitor onto a mobile screen without a progressive disclosure strategy. This results in touch target violations (targets smaller than 44x44px) and "Cognitive Overload," where the operator cannot quickly identify critical KPIs in the field.

**Why it happens:**
The "Data Dump" habit—believing that more data on screen equals more value. In mobile contexts, environmental factors like glare, gloves, or vibration make high-density layouts unreadable and untappable.

**How to avoid:**
Implement "Ruthless KPI Prioritization." Display only 3–5 "Hero Metrics" on the primary view. Ensure all interactive elements meet WCAG Success Criterion 2.5.8 (minimum 44x44px target). Use high-contrast ratios (4.5:1 minimum) and dark mode with high-intensity accents (Amber #f59e0b).

**Warning signs:**
- Users complaining they "missed a button" or "tapped the wrong thing."
- Horizontal scrolling on mobile devices.
- Critical alarms hidden behind multiple taps or tiny icons.

**Phase to address:**
Mobile Design / Responsive Implementation

---

### Pitfall 3: The "Jank" Threshold (CSS Bloat)

**What goes wrong:**
Using massive utility-first CSS frameworks or deeply nested selectors that increase the complexity of the CSSOM. In industrial dashboards updating hundreds of data points per second, this leads to "Layout Thrashing" and excessive memory consumption on low-power HMI (Human-Machine Interface) hardware.

**Why it happens:**
Relying on "modern" web styling defaults (shadows, rounded corners, gradients) that consume GPU memory and "data-ink" without adding information.

**How to avoid:**
Adhere to "Aerospace-UI" constraints: 0px border-radius, hard borders, and monochromatic scales (Zinc/Slate). Use Vanilla CSS or CSS Modules to keep the CSSOM lean. Use CSS Variables for theme consistency (Amber accents) without duplicating style blocks.

**Warning signs:**
- Browser crashes or slow performance on HMI panels compared to developer machines.
- Heavy "Style" phase in browser performance recordings during telemetry updates.
- Inconsistent alert colors due to "Specificity Wars" and `!important` overrides.

**Phase to address:**
Foundation / Styling System

---

### Pitfall 4: Chromatic Overload (Signal-to-Noise Collapse)

**What goes wrong:**
Using colors for branding, decorative flourishes, or "flavor" instead of strictly for state signaling. When Amber (#f59e0b) or Red are used for both branding and alarms, the operator's ability to instantly recognize a "Caution" or "Warning" state is compromised.

**Why it happens:**
Prioritizing "Aesthetics" over "Aeronautics." Marketing-driven design often conflicts with the functional requirement of color-as-information.

**How to avoid:**
Reserve high-intensity colors (Amber, Red, Green) exclusively for state signaling and interactive highlights. Use a monochromatic Zinc/Slate scale for 95% of the UI. Ensure color is never the *only* indicator of status (redundant encoding).

**Warning signs:**
- Operators reporting "Alert Blindness."
- Decorative elements using the same hex code as critical alarms.

**Phase to address:**
Design System / Visual Language

---

### Pitfall 5: The "Glass Cockpit" Legibility Failure

**What goes wrong:**
Using proportional fonts, poor tracking, or all-caps labels without adequate spacing. Under stress, vibration, or poor lighting, characters like 'I', '1', and 'L' blur together, leading to data misinterpretation.

**Why it happens:**
Defaulting to standard web typography designed for long-form reading rather than rapid scanning of tabular data.

**How to avoid:**
Use **Geist Mono** for all data points to ensure vertical character alignment. Apply **0.05em to 0.1em letter-spacing** to all-caps labels to maintain visual rhythm and prevent character crowding.

**Warning signs:**
- Misread metrics in user testing.
- Characters appearing as "blocks" rather than distinct letters in high-density grids.

**Phase to address:**
Typography / Data Visualization

## Technical Debt Patterns

| Shortcut | Immediate Benefit | Long-term Cost | When Acceptable |
|----------|-------------------|----------------|-----------------|
| Using Chart.js for sparklines | Fast initial implementation | Bundle bloat & initialization "Jank" | Only in low-density prototypes |
| Inline !important overrides | Fixes specificity issues quickly | UI becomes fragile and hard to theme | Never in production |
| Client-side data fetching only | Simpler backend logic | Cumulative Layout Shift (CLS) & "Flash of Empty State" | Only for non-critical telemetry |

## Integration Gotchas

| Integration | Common Mistake | Correct Approach |
|-------------|----------------|------------------|
| Telemetry Stream (WebSockets) | Updating the entire DOM on every message | Use localized updates or "throttled" rendering cycles |
| HMI Hardware | Assuming high-power GPU/RAM | Test on low-power target devices early in development |
| Authentication | Session timeouts during critical monitoring | Use "Heartbeat" mechanisms or persistent monitoring tokens |

## Performance Traps

| Trap | Symptoms | Prevention | When It Breaks |
|------|----------|------------|----------------|
| Event Listener Saturation | Memory leaks & slow teardowns | Use **Event Delegation** on tables | > 500 interactive cells |
| Deep DOM Nesting | Recalculate Styles > 16ms | Flatten component hierarchy | > 10 levels of nesting |
| Large SVG polyfills | High CPU usage | Use inline `<polyline>` or `<path>` | > 100 simultaneous charts |

## Security Mistakes

| Mistake | Risk | Prevention |
|---------|------|------------|
| Log-Leaked Telemetry | Exposure of industrial secrets/processes | Scrub sensitive metadata before logging |
| Command Injection via UI | Unauthorized machine control | Strict input validation on all control widgets |
| Lack of Audit Trail | Hard to trace operator error vs system failure | Log all UI interactions with precise timestamps |

## UX Pitfalls

| Pitfall | User Impact | Better Approach |
|---------|-------------|-----------------|
| Hover-Dependency | Mobile users can't access info | Visible labels or tap-to-expand |
| Abbreviation Ambiguity | Mental exhaustion in crises | Descriptive labels + standard units in () |
| Hidden Navigation | Users "lost" in deep hierarchies | Flat structure with breadcrumbs |

## "Looks Done But Isn't" Checklist

- [ ] **Data Tables:** Often missing empty states or loading skeletons — verify behavior on slow connections.
- [ ] **Alarms:** Often missing redundant encoding (text + color) — verify accessibility for colorblind users.
- [ ] **Control Widgets:** Often missing "Optimistic UI" feedback — verify visual confirmation of command receipt.
- [ ] **Responsive View:** Often missing "Thumb-Friendly" zones — verify one-handed use on mobile.

## Recovery Strategies

| Pitfall | Recovery Cost | Recovery Steps |
|---------|---------------|----------------|
| CSS Bloat | MEDIUM | Refactor to CSS Variables and flat utility structure |
| JS input lag | HIGH | Identify state bottlenecks; migrate to local state or native primitives |
| Poor Legibility | LOW | Switch to Geist Mono; adjust tracking and contrast |

## Pitfall-to-Phase Mapping

| Pitfall | Prevention Phase | Verification |
|---------|------------------|--------------|
| Reactivity Tax | Architecture | Frame-rate profiling during telemetry stress test |
| Density Collapse | Mobile UI | User testing on 6-inch devices with gloves |
| CSS Bloat | Styling | Bundle size analysis and CSSOM complexity check |

## Sources

- [NASA/FAA Human Factors Guidelines]
- [Abnormal Situation Management (ASM) Consortium]
- [WCAG 2.2 Accessibility Guidelines]
- [Aerospace-UI Design Principles]

---
*Pitfalls research for: Industrial/Aerospace UI Dashboards*
*Researched: 2024-05-22*
