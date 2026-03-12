# Project Research Summary

**Project:** Aerospace UI
**Domain:** Industrial/Aerospace UI Dashboards
**Researched:** 2025-05-23
**Confidence:** HIGH

## Executive Summary

The Aerospace UI project focuses on creating high-performance, high-density industrial dashboards using a "Vanilla-Plus" approach. Research indicates that for high-reliability environments like aerospace, the optimal path is a zero-dependency foundation using native web standards (HTML5, CSS Custom Properties, ES2024) to ensure maximum compatibility and stability. This approach avoids common pitfalls like "The Reactivity Tax" and "CSS Bloat" which can lead to input lag and layout thrashing in data-dense scenarios.

The recommended architecture balances a component-based design for maintainability with a single-page entry for real-time telemetry monitoring. Key differentiators include interactive SVG trends and adherence timelines, which provide critical context to real-time data. The main risks involve "Chromatic Overload" and "Information Density Collapse" on mobile devices, necessitating a strict visual language and a progressive disclosure strategy for small screens.

## Key Findings

### Recommended Stack

The stack prioritizes long-term stability and performance. Vanilla HTML/CSS/JS forms the core, supplemented by Lit for encapsulated UI primitives and D3.js for complex data visualizations.

**Core technologies:**
- Vanilla HTML5: Structural Foundation — Maximum compatibility, zero-dependency, and high-performance rendering.
- CSS Custom Properties: Dynamic Styling — Modern themeable UI architecture without pre-processor overhead.
- ES2024 (JavaScript): Logic & Interactivity — Native performance and modern API support (Web Workers, IntersectionObserver).
- Web Components (Lit): UI Primitives — Reusable, encapsulated components with a light footprint.

### Expected Features

Must-have features include real-time telemetry, status tags (RAG), and high-density grids. Differentiators like SVG trends and steppers for phased operations provide significant value.

**Must have (table stakes):**
- Real-time data — Critical for monitoring current states/telemetry.
- Status tags (RAG) — Immediate visual scanning of system-wide health.
- High-density grid — Standard for aerospace domain expectations.
- Scorecards — High-level KPI visibility at a glance.

**Should have (competitive):**
- SVG Trends — Interactive, precise historical trend lines.
- Steppers — Visualize complex multi-step processes (e.g., launch, landing).
- Adherence Timelines — Comparing scheduled vs. actual execution.

**Defer (v2+):**
- Predictive Alerts — ML-driven forecasting.
- Digital Twin Sync — 3D/2D visual mapping of sensors to assets.

### Architecture Approach

A hybrid "System" model using modular primitives (Component-based) composed into a "Cockpit" (Single-page) entry point. Assets are externalized (Linked Assets) to support a maintainable design system while ensuring high performance.

**Major components:**
1. Reference Cockpit (index.html) — Single-page entry point for high-density monitoring.
2. UI Kit Sections (.kit-section) — Modular primitives for building role-specific views.
3. Foundation Tuning (foundation_tune.js) — Core logic for state synchronization and performance.

### Critical Pitfalls

1. **The Reactivity Tax** — Avoid heavy frameworks for trivial states to prevent input lag.
2. **Information Density Collapse** — Use progressive disclosure and high-contrast targets (44x44px) for mobile.
3. **Chromatic Overload** — Reserve Amber/Red/Green strictly for state signaling, not branding.
4. **The "Jank" Threshold** — Avoid CSS bloat and layout thrashing by adhering to flat, monochromatic styling.
5. **Legibility Failure** — Use Geist Mono and adequate letter-spacing to prevent character blurring under stress.

## Implications for Roadmap

Based on research, suggested phase structure:

### Phase 1: Foundation & Core Telemetry
**Rationale:** Establishing the "Vanilla-Plus" architecture and core real-time capabilities is the highest priority for technical validation and performance baseline.
**Delivers:** Core design system, high-density grid, and real-time telemetry integration.
**Addresses:** Real-time data, Status tags, Scorecards.
**Avoids:** The Reactivity Tax (by keeping state close to the DOM).

### Phase 2: Advanced Visualization & Phased Ops
**Rationale:** Once the core telemetry is stable, adding analytical depth and process tracking provides the main competitive advantage.
**Delivers:** SVG Trend components and Stepper modules.
**Uses:** D3.js for data visualization and Lit for reusable primitives.
**Implements:** Interaction logic for historical data comparison.

### Phase 3: Mobile Optimization & Field Readiness
**Rationale:** Addressing the mobile pitfall ensures the dashboard is usable in field maintenance contexts where environmental factors impact legibility.
**Delivers:** Responsive views with "Ruthless KPI Prioritization" and touch-friendly targets.
**Addresses:** Information Density Collapse.

### Phase Ordering Rationale

- **Performance First:** Prioritizes core utility (telemetry) over secondary analysis (trends) to validate the "Vanilla" performance early.
- **Dependency Flow:** Trends and timelines require a working telemetry foundation and historical logging.
- **Risk Mitigation:** Separates desktop-density work from mobile optimization to address specific pitfalls like "Information Density Collapse" independently.

### Research Flags

Phases likely needing deeper research during planning:
- **Phase 1:** Real-time backend integration needs specific API research for low-latency WebSockets/SSE.
- **Phase 2:** D3.js performance profiling for 1000+ data points in high-frequency telemetry views.

Phases with standard patterns (skip research-phase):
- **Phase 1 (UI Foundation):** Well-documented "Amber-on-Black" and Tufte-style patterns are established.

## Confidence Assessment

| Area | Confidence | Notes |
|------|------------|-------|
| Stack | HIGH | Based on modern industrial standards and project analysis. |
| Features | HIGH | Aligned with NASA/SpaceX telemetry paradigms. |
| Architecture | HIGH | Hybrid model balances modularity and performance requirements. |
| Pitfalls | HIGH | Rooted in WCAG, Human Factors guidelines, and industrial HMI standards. |

**Overall confidence:** HIGH

### Gaps to Address

- **Telemetry Protocol:** Specific WebSocket/SSE backend implementation details are not yet defined.
- **HMI Hardware Targets:** Performance targets need validation on actual low-power target devices early in development.

## Sources

### Primary (HIGH confidence)
- Aerospace-UI Design Principles — Design system and performance guidelines.
- NASA/FAA Human Factors Guidelines — Typography and legibility standards.
- Industrial UI Standards 2025 — Tech stack recommendations and "Vanilla-Plus" shift.

### Secondary (MEDIUM confidence)
- Abnormal Situation Management (ASM) Consortium — Alarm and color signaling standards.
- Tufte Data-Ink Theory — Visual density and legibility principles.

---
*Research completed: 2025-05-23*
*Ready for roadmap: yes*
