# Plan 02: Studio Framework Breakthrough Architecture

## 1. Paradigm Shift: The Virtual Twin UI Automation Framework
Instead of driving live webapps connected to remote servers, the Studio framework introduces the **Virtual Twin Model**:
- Standalone, zero-dependency HTML5/Tailwind/Lucide templates that mirror production interfaces 1:1.
- In-memory state engines (`window.posTwin`, `window.invTwin`, `window.wizardTwin`) that react instantaneously to automated events.
- Zero network requests, zero backend timeouts, and zero authentication locks.

```
┌───────────────────────────────────────────────────────────────────────────┐
│                     SERVESMILE STUDIO ARCHITECTURE                        │
└───────────────────────────────────────────────────────────────────────────┘

   ┌─────────────────────────────────────────────────────────────────────┐
   │ 1. Scenario DSL / Command Script (JSON / Python / YAML)            │
   │    - Timeline Events (Tap, Drag, Type, Zoom, Spotlight, Steppers)  │
   │    - Dynamic Props (Store Profile, Member Tier, Catalog SKUs)       │
   │    - Neural Audio Synthesis (Edge-TTS Multilingual Voiceovers)      │
   └──────────────────────────────────┬──────────────────────────────────┘
                                      │
                                      ▼
   ┌─────────────────────────────────────────────────────────────────────┐
   │ 2. Studio State Machine & Micro-Interaction Fabric (Virtual Twin)   │
   │    - Pure Decoupled Component Mimicry (Merchant POS, KYC Hub)       │
   │    - Deterministic Clock (Discrete time-stepping @ 30/60fps)        │
   │    - Virtual Digitizer (Glowing Touch Cursor, Elastic Scroll)       │
   └──────────────────────────────────┬──────────────────────────────────┘
                                      │
                                      ▼
   ┌─────────────────────────────────────────────────────────────────────┐
   │ 3. Motion Graphics & Visual Compositing Canvas (OpenCV / Pillow)    │
   │    - Titanium 3D Device Frame (Dynamic Island, Bezel Glare, Shadows)│
   │    - Cinematic Spotlight Zoom & Background Vignette Blur            │
   │    - Kinetic Subtitles, Badges & Lower-Third Callouts               │
   └──────────────────────────────────┬──────────────────────────────────┘
                                      │
                                      ▼
   ┌─────────────────────────────────────────────────────────────────────┐
   │ 4. Deterministic Frame Renderer & Audio Muxer (FFmpeg)              │
   │    - 1080p Full HD Progressive Output                               │
   │    - Studio-Grade Narration Synchronization                         │
   └─────────────────────────────────────────────────────────────────────┘
```

## 2. Technical Stack
- **DOM Engine**: Playwright Headless Chromium (2x Retina device emulation).
- **Motion & Frame Compositor**: OpenCV + Pillow (Python-based procedural 3D bezel renderer).
- **Voiceover Engine**: Microsoft Edge-TTS (multilingual neural voice synthesis).
- **Muxer**: FFmpeg binary pipeline (`imageio-ffmpeg`).
