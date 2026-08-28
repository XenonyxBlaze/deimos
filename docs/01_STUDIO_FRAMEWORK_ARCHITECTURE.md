# 01. DemoMaker Studio — Framework Architecture & Blueprint

## Overview

**DemoMaker Studio** (`studio-engine`) is an autonomous, high-fidelity UI demonstration, motion graphics, and video automation framework. It allows developers and product teams to generate pixel-perfect, 60/30fps marketing, onboarding, and developer walkthrough videos of complex web and mobile applications with zero dependencies on live production databases, backend APIs, or network state.

```
+-------------------------------------------------------------------------------+
|                             DEMOMAKER STUDIO                                 |
+-------------------------------------------------------------------------------+
|                                                                               |
|  +------------------------+      +-------------------+     +---------------+  |
|  | Virtual Twin UI Models | ---> | Scenario Timeline | --> | Playwright    |  |
|  | (1:1 Decoupled DOM)    |      | (Actions & Cues)  |     | 2x Retina Rec |  |
|  +------------------------+      +-------------------+     +---------------+  |
|                                                                    |          |
|  +------------------------+                                        v          |
|  | Edge-TTS Neural Voice  | --------------------------------> +---------------+
|  | (Multilingual Audio)   |                                   | Motion Engine |
|  +------------------------+                                   | (3D Titanium) |
|                                                               +---------------+
|                                                                    |          |
|                                                                    v          |
|                                                              +---------------+
|                                                              | FFmpeg Master |
|                                                              | 1080p Video   |
|                                                              +---------------+
+-------------------------------------------------------------------------------+
```

---

## Key Pillars of the Architecture

### 1. The Virtual Twin UI Paradigm
Traditional E2E recording tools (e.g. Cypress, Playwright on live apps) suffer from non-deterministic failures:
- Flaky network requests and backend timeouts.
- OTP SMS / Email verification barriers.
- Database state drift (already-registered users, deleted stores).
- Sensitive credentials leakage (API keys, test tokens).

**DemoMaker Studio** solves this by decoupling the presentation layer into **Virtual Twins**:
- Standalone HTML5/Tailwind/Lucide templates matching the production codebase 1:1.
- In-memory reactive state machines (`window.posTwin`, `window.invTwin`, `window.wizardTwin`).
- Zero external CDN dependencies; pure vector graphics and offline Canvas algorithms (e.g. `drawRealisticQR`).

### 2. Cinematic Spotlight & Vignette Engine
To draw viewer attention without jarring cuts:
- Active components are highlighted with `window.spotlight(selector, scale)`.
- The background DOM is darkened with a 72% opacity vignette with 4px backdrop blur.
- The active element scales smoothly ($1.15\times - 1.35\times$) with an illuminated glowing border (`box-shadow: 0 0 45px rgba(249, 115, 22, 0.65)`).
- After performing the action, `window.clearSpotlight()` smoothly eases the viewport back to normal.

### 3. Procedural 3D Hardware Framing
- Renders a photorealistic Titanium smartphone bezel around the 430x932 mobile viewport.
- Adds dynamic ambient drop shadows, anti-aliased corner radiuses, camera pill (Dynamic Island), and speaker rungs.
- Sub-pixel floating physics (`sin(t * 2π) * 4px`) giving the device natural life.

### 4. Deterministic Multilingual Narration
- Generates studio-grade neural voiceovers using Microsoft Edge-TTS (`en-US-BrianMultilingualNeural`, `en-IN-PrabhatNeural`, etc.).
- Measures precise audio durations in milliseconds and dynamically paces the UI timeline so animations and voiceover cues synchronize perfectly.
