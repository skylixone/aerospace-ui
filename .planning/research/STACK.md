# Stack Research

**Domain:** Industrial/Aerospace UI Dashboards
**Researched:** 2025-05-23
**Confidence:** HIGH

## Recommended Stack

### Core Technologies

| Technology | Version | Purpose | Why Recommended |
|------------|---------|---------|-----------------|
| Vanilla HTML5 | Living Standard | Structural Foundation | Maximum compatibility, zero-dependency, and high-performance rendering. Critical for high-reliability industrial environments. |
| CSS Custom Properties | Standard | Dynamic Styling | Modern themeable UI architecture without the need for a pre-processor (SASS/LESS) or JS-in-CSS overhead. |
| ES2024 (JavaScript) | Latest | Logic & Interactivity | Native performance, `IntersectionObserver`, `Web Workers` for data processing, and `localStorage` for state persistence. |
| Web Components (Lit) | 3.2+ | UI Primitives | Reusable, encapsulated components that work across any environment (React, Vue, or Vanilla) while keeping a light footprint. |

### Supporting Libraries

| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| D3.js | 7.9+ | Data Visualization | When building complex, high-frequency telemetry displays or custom gauges. |
| marked.js | 12.0+ | Markdown Parsing | For rendering human-readable logs, checklists, or documentation within the UI. |
| Geist Mono | 1.3+ | Typography | High-legibility mono font, essential for the "Aerospace" aesthetic and data-dense readouts. |
| Lucide Icons | 0.400+ | Iconography | Lightweight, customizable SVG icons for industrial status and control interfaces. |

### Development Tools

| Tool | Purpose | Notes |
|------|---------|-------|
| Vite | Dev Server & Bundling | Provides HMR (Hot Module Replacement) and optimized production builds for the "Vanilla" stack. |
| PostCSS | CSS Modernization | Allows use of nesting and future CSS features while ensuring browser compatibility. |
| Prettier | Code Formatting | Ensures consistent code style across the "Industrial Design" codebases. |

## Installation

```bash
# Core (if using Vite)
npm init vite@latest aerospace-ui --template vanilla

# Supporting
npm install d3 marked lucide-static

# Dev dependencies
npm install -D vite postcss autoprefixer prettier
```

## Alternatives Considered

| Recommended | Alternative | When to Use Alternative |
|-------------|-------------|-------------------------|
| Vanilla + CSS Vars | Tailwind CSS v4 | Use when rapid prototyping is needed and utility-first styling is preferred over custom industrial tokens. |
| Web Components | React / Svelte | Use when the UI state becomes highly complex or when integrating with existing enterprise-wide frontend ecosystems. |
| Geist Mono | JetBrains Mono | Use if a slightly more "technical" and condensed aesthetic is required for narrow sidebar displays. |

## What NOT to Use

| Avoid | Why | Use Instead |
|-------|-----|-------------|
| Heavy Frameworks (Angular) | High overhead, slow initial load, and complex dependency management for simple dashboards. | Vanilla or Lit for lightweight, long-term stable components. |
| Bootstrap / jQuery | Outdated styling patterns and unnecessary DOM manipulation overhead. | Native CSS Flex/Grid and modern JS APIs. |
| CSS-in-JS (Styled-Components) | Performance hit for dynamic industrial telemetry; hard to theme outside of the framework. | CSS Custom Properties (Variables). |

## Stack Patterns by Variant

**If High-Frequency Telemetry:**
- Use **Canvas or WebGL** for real-time data streams.
- Because DOM-based SVG rendering can become a bottleneck at 60fps with 1000+ data points.

**If Air-Gapped / High-Reliability:**
- Use **Zero-Dependency Vanilla** (locally hosted fonts/assets).
- Because reliance on CDNs (Google Fonts, unpkg) can cause interface failure in restricted networks.

## Version Compatibility

| Package A | Compatible With | Notes |
|-----------|-----------------|-------|
| Lit@3.2.1 | ES2022+ | Requires modern browser features (Custom Elements V1). |
| D3.js@7.9 | Vite@5.2 | Fully compatible with ESM-based bundlers. |

## Sources

- `aerospace-ui/` — Analysis of current "Amber-on-Black" design system and Vanilla implementation.
- `the-Operation/dashboard.html` — Verified usage of `localStorage` for state and `marked.js` for dynamic content.
- Industrial UI Standards 2025 — Confidence: HIGH (reflecting shift back to "Vanilla-Plus" for reliability).

---
*Stack research for: Industrial/Aerospace UI Dashboards*
*Researched: 2025-05-23*
