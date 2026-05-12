# Napkin

## Corrections

| Date | Source | What Went Wrong | What To Do Instead |
| ---- | ------ | --------------- | ------------------ |
| 2026-02-20 | self | CSS rules appeared correct but weren't applying in browser | Always hard-reload (ignoreCache: true) after CSS changes — python http.server caches aggressively |
| 2026-02-20 | self | Linter reformatted style.css and introduced a `calc()` change to `.summary` font-size | Check CSS syntax after linter runs — it may introduce unintended changes, not just formatting |

## User Preferences

- Aerospace UI Kit: dark industrial aesthetic, amber accent, data-first
- Use `aerospace-ui` styling by default for all HTML
- User expects comprehensive UX states: not just default, but disabled, loading, error, success, empty, hover, focus-visible
- "Intuitively familiar but futuristic" — standard interaction patterns, aerospace visual language

## Patterns That Work

- After every element group completion: visual-verify in browser, then commit — keeps git history useful and catches issues early
- Section-by-section visual verification via browser automation catches issues code review misses
- Committing along logical element groupings keeps git history useful

## Patterns That Don't Work

- Reading code alone to verify CSS — must render in browser to catch specificity/cascade issues
- Trusting cache after file edits — always force-reload
- Batching all CSS at end of file in one go — should add CSS after each element group, verify, then commit

## Domain Notes

- Project: aerospace-ui — industrial design system / component reference kit. LLM-friendly, human-first
- Color palette: #0a0a0a base, #f59e0b amber accent, alpha-channel borders
- Typography: Geist Mono, generous letter-spacing, all-caps labels
- Minimal border-radius (max 2px), 150ms transitions
- Review server: Python-based, Ctrl+I to toggle review mode
- 30 components total, numbered 01-30 sequentially
- Linter auto-formats on save — expect reformatted CSS/HTML between edits
