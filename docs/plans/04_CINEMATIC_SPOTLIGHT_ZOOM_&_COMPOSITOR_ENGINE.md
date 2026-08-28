# Plan 04: Cinematic Spotlight Zoom & Compositor Engine

## 1. Visual Design Objectives
To transform dry screencasts into high-end product showcase videos using cinematic component highlighting and unhurried pacing.

## 2. Technical Architecture

### 2.1 Dynamic Spotlight & Vignette Dimming
```javascript
// Injected Spotlight Controller
window.spotlight = (selector, scale = 1.18) => {
  window.clearSpotlight();
  const el = document.querySelector(selector);
  if (!el) return;

  // 1. Create full-screen dark vignette backdrop
  const backdrop = document.createElement('div');
  backdrop.id = 'studio-spotlight-backdrop';
  backdrop.style.position = 'fixed';
  backdrop.style.inset = '0';
  backdrop.style.backgroundColor = 'rgba(0, 0, 0, 0.72)';
  backdrop.style.backdropFilter = 'blur(4px)';
  backdrop.style.zIndex = '999990';
  backdrop.style.opacity = '1';
  document.body.appendChild(backdrop);

  // 2. Elevate and scale target element
  el.style.zIndex = '999995';
  el.style.transition = 'transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s ease';
  el.style.transform = `scale(${scale})`;
  el.style.boxShadow = '0 0 45px rgba(249, 115, 22, 0.65), 0 0 0 2px rgba(249, 115, 22, 0.9)';
};
```

### 2.2 Procedural 3D Hardware Bezel
- **Resolution**: 430x932 mobile viewport inside a 466x968 titanium casing.
- **Ambient Lighting**: Multi-layered Gaussian drop shadows (12px, 16px blur) and 2px chamfered titanium rim.
- **Dynamic Island**: Dual-camera sensor pill with soft lens reflection.
- **Harmonic Float**: Smooth $\sin(t \cdot 2\pi)$ float dynamics.

### 2.3 Studio Neural Voice Pacing
- **Voice**: `en-US-BrianMultilingualNeural`
- **Dynamic Timing**: Each scene dynamically measures audio length ($t_{\text{audio}}$) and adds $+1.4\text{s}$ breathing room for smooth visual transitions.
