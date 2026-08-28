# DemoMaker Studio 🎬✨

> **Autonomous, Deterministic UI Demonstration & Motion Graphics Video Generation Framework**

**DemoMaker Studio** is a modern motion graphics engine and video generation pipeline designed to create high-fidelity, 60/30fps marketing, onboarding, and developer walkthrough videos of web and mobile applications with **zero backend dependencies**, **zero authentication locks**, and **100% deterministic output**.

---

## 🌟 Key Highlights

- **🎭 Virtual Twin UI Architecture**: Uses decoupled, zero-dependency HTML5/Tailwind/Canvas component replicas matching production design 1:1.
- **🔍 Cinematic Spotlight Zoom**: Smoothly dims the background with a vignette blur and enlarges the active component with an illuminated glowing highlight ring.
- **📱 Procedural 3D Hardware Framing**: Renders realistic Titanium smartphone bezels, Dynamic Island pills, ambient drop shadows, and subtle harmonic float physics.
- **🎙️ Multilingual Neural Narration**: Synchronizes video pacing automatically with Microsoft Edge-TTS studio voices (`en-US-BrianMultilingualNeural`, `en-IN-PrabhatNeural`, etc.).
- **⚡ 0ms Offline Logic**: In-memory state engines for touch POS billing, cart queue parking, HSN tax lookups, and instant QR verification.

---

## 🏗️ Architecture Blueprint

```
┌───────────────────────────────────────────────────────────────────────────┐
│                     DEMOMAKER STUDIO ARCHITECTURE                         │
└───────────────────────────────────────────────────────────────────────────┘

   ┌─────────────────────────────────────────────────────────────────────┐
   │ 1. Scenario Timeline (JSON / Python / YAML)                         │
   │    - Tap, Type, Scroll, Spotlight, Hold Cart, Steppers              │
   │    - Audio Cues & Edge-TTS Multilingual Voiceovers                  │
   └──────────────────────────────────┬──────────────────────────────────┘
                                      │
                                      ▼
   ┌─────────────────────────────────────────────────────────────────────┐
   │ 2. Virtual Twin UI Fabric (HTML5 / Tailwind / Lucide)               │
   │    - Merchant POS, Inventory Catalog, Onboarding Wizard, KYC Hub    │
   │    - In-Memory Reactive State Machines                              │
   └──────────────────────────────────┬──────────────────────────────────┘
                                      │
                                      ▼
   ┌─────────────────────────────────────────────────────────────────────┐
   │ 3. Motion Graphics & Visual Compositor (OpenCV / Pillow)            │
   │    - Titanium 3D Smartphone Frame                                   │
   │    - Cinematic Spotlight Zoom & Background Vignette Blur            │
   │    - Lower-Thirds, Animated Progress Bars & Badges                  │
   └──────────────────────────────────┬──────────────────────────────────┘
                                      │
                                      ▼
   ┌─────────────────────────────────────────────────────────────────────┐
   │ 4. Deterministic Frame Muxer (FFmpeg)                               │
   │    - 1080p Full HD Progressive Video (30/60 FPS)                    │
   └─────────────────────────────────────────────────────────────────────┘
```

---

## 📂 Project Structure

```
demomaker-studio/
├── README.md                              # Main documentation
├── LICENSE                                # MIT License
├── requirements.txt                       # Python dependencies
├── src/
│   ├── core/
│   │   └── studio_runner.py               # Core Compositor & Playwright Engine
│   ├── components/                        # Virtual Twin UI Templates
│   │   ├── merchant/
│   │   │   ├── VirtualAuth.html           # Multi-language dual-channel login
│   │   │   ├── VirtualStoreWizard.html    # 5-step onboarding & 1-tap GPS
│   │   │   ├── VirtualKycHub.html         # Bank-grade KYC & verified badge
│   │   │   ├── VirtualInventory.html      # Catalog & official HSN directory
│   │   │   ├── VirtualPosRegister.html    # 0ms touch POS & cart parking
│   │   │   └── VirtualSubscriptions.html  # Business Boost growth tiers
│   │   └── customer/
│   │       └── VirtualCustomerWallet.html # Digital card wallet & dynamic QR
│   └── scenarios/
│       ├── exhaustive_merchant_master.py  # 8-scene official merchant demo
│       └── pos_master_showcase.py         # POS quick showcase demo
└── docs/
    └── plans/                             # Sorted Architectural Plans
        ├── 01_INITIAL_UI_WALKTHROUGH_IDEATION.md
        ├── 02_STUDIO_FRAMEWORK_BREAKTHROUGH_ARCHITECTURE.md
        ├── 03_EXHAUSTIVE_MERCHANT_OS_WORKFLOW_SPEC.md
        ├── 04_CINEMATIC_SPOTLIGHT_ZOOM_&_COMPOSITOR_ENGINE.md
        └── 05_DEMOMAKER_STUDIO_ROADMAP_&_DISTRIBUTION.md
```

---

## 🚀 Quick Start

### 1. Clone & Install Dependencies

```bash
git clone https://github.com/ServeSmileDev/demomaker-studio.git
cd demomaker-studio
pip install -r requirements.txt
playwright install chromium
```

### 2. Run Master Demonstration Render

```bash
python src/scenarios/exhaustive_merchant_master.py
```

The output video will be generated deterministically in `output/servesmile_merchant_exhaustive_guide.mp4`.

---

## 📜 Architectural Plans & Evolution

All design decisions and architectural blueprints are documented in the [docs/plans](docs/plans) directory:

1. [01. Initial UI Walkthrough & Video Automation Ideation](docs/plans/01_INITIAL_UI_WALKTHROUGH_IDEATION.md)
2. [02. Studio Framework Breakthrough Architecture](docs/plans/02_STUDIO_FRAMEWORK_BREAKTHROUGH_ARCHITECTURE.md)
3. [03. Exhaustive Merchant OS Workflow Specification](docs/plans/03_EXHAUSTIVE_MERCHANT_OS_WORKFLOW_SPEC.md)
4. [04. Cinematic Spotlight Zoom & Compositor Engine](docs/plans/04_CINEMATIC_SPOTLIGHT_ZOOM_&_COMPOSITOR_ENGINE.md)
5. [05. DemoMaker Studio Roadmap & Distribution](docs/plans/05_DEMOMAKER_STUDIO_ROADMAP_&_DISTRIBUTION.md)

---

## 📄 License

MIT License © 2026 ServeSmile IT / ServeSmileDev
