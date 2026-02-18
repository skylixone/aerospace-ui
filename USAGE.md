# Aerospace UI Kit - Usage Guide

## Overview
A heavy-duty, data-first industrial design system for web applications. Built on Geis Mono, it prioritizes information density, high contrast (Amber on Black), and strict left alignment.

## Quick Start
1.  **Serve Locally**:
    ```bash
    python3 -m http.server 8000
    # OR if you want the review capabilities:
    ./review-server.py
    ```
2.  **Open Browser**:
    Navigate to `http://localhost:8000`.

## Key Files
*   `index.html`: The living documentation and component reference. Contains all HTML structures.
*   `style.css`: The complete CSS system. No external dependencies (other than fonts).
*   `nav_highlight.js`: Smart sidebar navigation interaction logic.
*   `foundation_tune.js`: Utility for real-time CSS variable tuning (console-based).
*   `review-server.py`: Custom Python server enabling the "Review Mode" overlay (Ctrl+I).

## Review Workflow
1.  Run `./review-server.py`.
2.  Open the page in your browser.
3.  Press `Ctrl+I` to activate the Review Overlay.
4.  Click any element to attach a comment.
5.  Comments are saved to `comments.json` for later processing.

## Customization
Modify `style.css` variables at the top of the file to adjust the global theme:
*   `--accent`: Main brand color (default: Amber).
*   `--bg`: Background color (default: `#09090b`).
*   `--font-mono`: Typeface stack.

## Principles
*   **Data First**: Content precedes chrome.
*   **One Direction**: Left-align everything.
*   **Maximize Space**: Use the full width where possible; don't constrain data unnecessarily.
*   **Raw aesthetic**: Borders over shadows. No rounded corners (mostly).
