# Research: Architecture — Industrial/Aerospace UI Dashboards

## Overview

In the context of **Industrial/Aerospace UI Dashboards**, architectural decisions are driven by the tension between **information density** and **operational reliability**. This research dimension explores how these systems are structured (Single-page vs. Component-based) and how assets are managed (Single-file vs. Linked Assets) to meet high-stakes performance requirements.

## Analysis: System Structure

### 1. Single-page (The "Cockpit" Model)
*   **Definition**: A monolithic, all-at-once view where all critical telemetry is visible simultaneously.
*   **Pros**: Zero-click access to data; consistent visual rhythm; simplified state synchronization.
*   **Cons**: High DOM weight; risk of "Information Saturation"; difficult to scale across different screen sizes.
*   **Industrial Context**: Ideal for **Performance Windows** and **Circadian Hero Metrics** where the user must see the "whole system" at once without navigation latency.

### 2. Component-based (The "System" Model)
*   **Definition**: Modular primitives (Atomic Design) composed into role-specific or drill-down views.
*   **Pros**: Isolation of failure (modular updates); reusable design system; easier testing and independent deployment.
*   **Cons**: Navigation overhead; potential for "Context Fragmentation" if the user loses the big picture.
*   **Industrial Context**: Mandatory for **Open Systems Architecture** where different vendors provide telemetry modules that must coexist within a unified interface.

## Analysis: Asset Strategy

### 1. Single-file (The "Black Box" Model)
*   **Definition**: All CSS, JS, and SVG assets are inlined into a single HTML file.
*   **Pros**: 100% portable; no "Broken Link" failures; versioning via simple file renaming; runs without a web server (local file system).
*   **Cons**: Massive file size; no browser caching for shared assets; maintenance complexity for large teams.
*   **Industrial Context**: Preferred for **Field Reports** and **Emergency Dashboards** that must run from a USB stick or a local cache in air-gapped environments.

### 2. Linked Assets (The "Fleet" Model)
*   **Definition**: Standard modern web structure with externalized CSS/JS and localized asset hosting.
*   **Pros**: Optimized loading via caching; smaller individual page sizes; centralized design system updates.
*   **Cons**: Requires a server/network context; dependency on file path integrity; risk of "Version Drift" between content and its styles.
*   **Industrial Context**: Best for **Fleet Management Dashboards** and **Ground Control Systems** where connectivity is guaranteed and multi-screen/multi-page setups are common.

## Contextual Application: Aerospace UI Kit

The current `aerospace-ui` implementation follows a hybrid path:

*   **Structure**: **Component-based Conceptually, Single-page Entry**. While the `index.html` functions as a "Reference Cockpit," the underlying design follows a component-based philosophy where each `.kit-section` is an independent primitive.
*   **Asset Strategy**: **Linked Assets**. The project utilizes separate files (`style.css`, `interactions.js`, `foundation_tune.js`) to maintain clean source code and allow shared styles across `index.html` and `landing.html`.

### Synthesis: The "Aerospace-UI" Recommendation

| Use Case | Page Strategy | Asset Strategy | Rationale |
| :--- | :--- | :--- | :--- |
| **Mission Control** | Single-page | Linked Assets | High density + High performance + Centralized infra. |
| **Field Maintenance** | Component-based | Single-file | Role-specific + Offline reliability + Zero-config. |
| **Executive Overview** | Single-page | Linked Assets | At-a-glance + Standard corporate deployment. |

**Founding Principle**: Prioritize the **Rhythm of Entry**. Whether single-page or component-based, the internal padding must equal the external gap to ensure the operator's eye can scan the high-density data without friction. The choice of **Linked Assets** in this project supports the goal of "Zero Build Steps" while keeping the source maintainable as the component library grows.
