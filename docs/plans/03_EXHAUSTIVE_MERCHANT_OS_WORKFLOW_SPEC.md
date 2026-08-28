# Plan 03: Exhaustive Merchant OS Workflow Specification

## 1. Scope & Core Objectives
To demonstrate the complete merchant lifecycle from onboarding to daily cashier billing with 100% merchant-centric focus (excluding extraneous customer app workflows).

## 2. Exhaustive 8-Stage Functional Flow

### Stage 1: Multi-Language Switcher & Secure Authentication
- **Interface**: `VirtualAuth.html`
- **Features**:
  - Dynamic locale toggle (`English`, `हिन्दी`, `ਪੰਜਾਬੀ`, `ગુજરાતી`).
  - Privacy-masked credential inputs (`••••••••••••`).
  - Dual-channel OTP verification.

### Stage 2: 5-Step Storefront Wizard & 1-Tap GPS Geolocation
- **Interface**: `VirtualStoreWizard.html`
- **Features**:
  - Store identity (*Al Qasr Fine Dining & Grill*), 1:1 logo, and showcase cover media.
  - 1-Tap instant GPS coordinate retrieval (`28.4950° N, 77.0890° E`).
  - 20% member savings rate preset, operating hours (11:00 AM - 11:00 PM), and official GSTIN / FSSAI license declarations.

### Stage 3: Bank-Grade KYC Compliance Hub
- **Interface**: `VirtualKycHub.html`
- **Features**:
  - 3-Stage regulatory verification (GSTIN, Business PAN, Aadhaar Biometrics).
  - Green *Official Verified Merchant Partner (KYC VERIFIED)* badge with AES-256 encrypted protection.

### Stage 4: Master Catalog & Government HSN/SAC Directory
- **Interface**: `VirtualInventory.html`
- **Features**:
  - Real-time stock tracking, custom SKUs, and barcodes.
  - Add Custom Product modal with built-in official HSN/SAC code directory search (`996331 - Restaurant and mobile food services`).
  - Auto-split intra-state GST tax configuration (2.5% CGST + 2.5% SGST).

### Stage 5: Zero-Latency Touch POS Register & Cart Queue Parking
- **Interface**: `VirtualPosRegister.html`
- **Features**:
  - 0ms offline-capable touch billing with category filter pills (`Main Course`, `Biryani & Rice`, `Tandoor Breads`).
  - In-card quantity steppers (`- 2 +`) and dynamic subtotal calculations.
  - Multi-cart queue parking: cashiers can hold an active order during peak rush (`Hold` $\rightarrow$ `Parked (1)`) and recall it instantly.

### Stage 6: Instant 20% Member Card QR Validation
- **Interface**: `VirtualPosRegister.html`
- **Features**:
  - Cashier scans customer's member card QR code (quick 5-second validation).
  - Floating verified celebration card (*Aarav Rajput • @aarav_alqasr*).
  - Green 20% member savings deduction applied automatically (`-₹330.00`).

### Stage 7: Digital Payments, Taxes & Paperless Thermal QR Receipts
- **Interface**: `VirtualPosRegister.html`
- **Features**:
  - Multi-mode checkout: Cash (with tendered amount & automatic change calculation) and Dynamic UPI QR code.
  - Itemized GST tax invoice with intra-state CGST & SGST breakdown.
  - Direct Plain-Text Thermal QR receipt: customers scan directly with their native camera/Google Lens without needing an app or internet connection.

### Stage 8: Business Boost Subscription Growth Tiers
- **Interface**: `VirtualSubscriptions.html`
- **Features**:
  - Tier comparison: Starter (Bronze, ₹2,599/yr), Pro (Silver, ₹4,999/yr - ACTIVE), Elite (Gold, ₹12,999/yr), and The Brand (Enterprise, ₹29,999/yr).
  - Multi-branch center expansion (up to 25 branches), monthly promotional video reel production, and priority neighborhood search ranking.
