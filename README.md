# AEROSPACE UI

[![Version](https://img.shields.io/badge/version-1.0-0a0a0a?style=flat-square&color=f59e0b)](https://github.com/skylixone/aerospace-ui)
[![License](https://img.shields.io/badge/license-Personal%20Use-0a0a0a?style=flat-square&color=666666)](LICENSE)
[![Components](https://img.shields.io/badge/components-29-0a0a0a?style=flat-square&color=22c55e)](https://skylixone.github.io/aerospace-ui)

> **A systematic interface design kit for data-dense applications.**  
> Amber on black. Geist Mono throughout. No rounded corners. Borders over shadows.

```
╔══════════════════════════════════════════════════════════════════╗
║  ▓▓▓  █████╗ ███████╗██████╗  ██████╗ ███████╗██████╗  █████╗   ║
║ ▓   ▓ ██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔════╝██╔══██╗██╔══██╗  ║
║ ▓   ▓ ███████║█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝███████║  ║
║ ▓   ▓ ██╔══██║██╔══╝  ██╔══██╗██║   ██║██╔══╝  ██╔══██╗██╔══██║  ║
║  ▓▓▓  ██║  ██║███████╗██║  ██║╚██████╔╝██║     ██║  ██║██║  ██║  ║
║       ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝  ║
╠══════════════════════════════════════════════════════════════════╣
║  SYSTEM STATUS: OPERATIONAL     │    THEME: DARK AEROSPACE       ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## PHILOSOPHY

**Data first. Decoration after.**

Aerospace UI is built on constraint-based design principles inspired by Karl Gerstner's *Designing Programmes* and Edward Tufte's data-ink theory. Every element serves a purpose. Every pixel carries information.

| PRINCIPLE | IMPLEMENTATION |
|-----------|----------------|
| **Monospace Grid** | Geist Mono at all weights. Tabular alignment for data. |
| **High Contrast** | Amber (#f59e0b) on pure black (#0a0a0a). No mid-tone ambiguity. |
| **Generous Whitespace** | 8px base grid. Breathing room is not wasted space. |
| **Zero Radius** | Sharp corners only. Industrial precision. |
| **Borders Over Shadows** | Depth via line weight, not blur. |

---

## COMPONENT MATRIX

### FOUNDATION
```
TYPOGRAPHY │ COLORS    │ SPACING
───────────┼───────────┼─────────
Hero 56px  │ bg        │ 4px  xs
Display 44 │ bg-raised │ 8px  sm
Heading 28 │ accent    │ 16px md
Subhead 20 │ text      │ 24px lg
Body 15px  │ dim       │ 32px xl
Small 12px │ muted     │ 48px 2xl
Overline 11│ green     │ 64px 3xl
           │ red       │
           │ blue      │
```

### CONTROLS
| Component | Purpose | Variants |
|-----------|---------|----------|
| **Button** | Primary actions | Primary, Secondary, Ghost, Danger |
| **Input** | Data entry | Text, Select, Textarea, Error states |
| **Toggle** | Binary states | Checked/Unchecked with animated track |
| **Checkbox/Radio** | Multi/single select | Native-styled, accessible |
| **Tabs** | View switching | Underline-active indicator |
| **Stepper** | Numeric adjustment | +/- with bounds, integrated validation |

### DATA DISPLAY
| Component | Purpose | Features |
|-----------|---------|----------|
| **Metric Card** | KPI display | Value + label + detail, semantic colors |
| **Table** | Structured data | Responsive wrapper, sortable headers |
| **Bar** | Value comparison | Horizontal with fill percentage |
| **Progress** | Completion status | Determinate, indeterminate, semantic |
| **Tag/Badge** | Categorization | Default, accent, semantic variants |

### OVERLAY
| Component | Purpose | Behavior |
|-----------|---------|----------|
| **Toast** | System feedback | Slide-in, actions, auto-dismiss |
| **Mini Toast** | Confirmation | Centered, inverted (green/dark), debounced |
| **Modal** | Critical decisions | Backdrop blur, focus trap |
| **Command Palette** | Quick actions | Keyboard-navigable, search-filtered |
| **Popover** | Contextual options | Anchor positioning, click-outside close |
| **Tooltip** | Supplementary info | Hover-triggered, arrow indicator |

### CONTENT
- **Panel** — Grouped data containers with header/body/footer
- **Card** — Elevated content blocks, hover lift effect
- **Alert** — System messages (info, success, warning, danger)
- **Status Indicator** — Online/away/busy/offline dots
- **List** — Bulleted or numbered with hexagon markers
- **Code Block** — Syntax-highlighted monospace blocks
- **Key-Value Grid** — Metadata display with label spacing
- **Empty State** — Zero-data placeholder with action

### LAYOUT
- **Page Header** — Title + overline + metadata grid
- **Page Footer** — System info + stats
- **Skeleton** — Loading placeholder with shimmer
- **Divider** — Solid, dashed, dotted separators

---

## USAGE

### Installation

```bash
# Clone the repository
git clone https://github.com/skylixone/aerospace-ui.git

# Or download the latest release
curl -L https://github.com/skylixone/aerospace-ui/archive/refs/heads/main.zip
```

### Basic Setup

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Your App</title>
  
  <!-- Geist Mono from Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Geist+Mono:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  
  <!-- Aerospace UI -->
  <link rel="stylesheet" href="aerospace-ui/style.css">
</head>
<body>
  <!-- Your application -->
</body>
</html>
```

### Component Examples

**Primary Button**
```html
<button class="btn btn-primary">Deploy System</button>
```

**Metric Card**
```html
<div class="metric">
  <div class="metric-label">SYSTEM LOAD</div>
  <div class="metric-value accent">42%</div>
  <div class="metric-detail">Within normal parameters</div>
</div>
```

**Stepper Control**
```html
<div class="stepper">
  <button class="stepper-btn" onclick="adjust(-1)">−</button>
  <span class="stepper-val" id="value">6.0</span>
  <button class="stepper-btn" onclick="adjust(1)">+</button>
</div>
```

**Mini Toast (JavaScript)**
```javascript
// Show success confirmation
Toast.show('Saved', 'success');

// Show updating state
Toast.show('Saving...', 'updating');
```

---

## DESIGN TOKENS

```css
:root {
  /* Background Layers */
  --bg: #0a0a0a;
  --bg-raised: #111111;
  --bg-surface: #0d0d0d;
  --bg-hover: #141414;
  
  /* Text Hierarchy */
  --text-bright: #ffffff;
  --text: #e8e8e8;
  --text-label: #888888;
  --text-dim: #666666;
  --text-muted: #444444;
  
  /* Accent & Semantic */
  --accent: #f59e0b;
  --accent-hover: #fbbf24;
  --green: #22c55e;
  --red: #ef4444;
  --blue: #3b82f6;
  
  /* Borders */
  --border: #333333;
  --border-dim: #222222;
  --border-input: #2a2a2a;
  
  /* Typography */
  --font-mono: 'Geist Mono', monospace;
  
  /* Spacing Scale */
  --space-xs: 4px;
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 24px;
  --space-xl: 32px;
  --space-2xl: 48px;
  --space-3xl: 64px;
}
```

---

## ARCHITECTURE

```
aerospace-ui/
├── index.html          # Live component reference
├── style.css           # Complete design system
├── foundation_tune.js  # Visual fine-tuning
└── nav_highlight.js    # Interactive navigation
```

The kit is designed as a **single-file system**. `style.css` contains all 29 components, hardened for production use. No build step. No dependencies (except Geist Mono).

---

## DEMONSTRATION

View the complete component reference at:  
**https://skylixone.github.io/aerospace-ui**

---

## LICENSE

Personal Use Only.  
For commercial licensing, contact: [your-email]

---

```
┌─────────────────────────────────────────────────────────────┐
│  BUILT FOR PRECISION. DESIGNED FOR DATA. OPERATIONAL STATUS:│
│                    [ ALL SYSTEMS NOMINAL ]                  │
└─────────────────────────────────────────────────────────────┘
```
