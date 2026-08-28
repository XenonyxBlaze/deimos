import asyncio
import os
import sys

sys.path.insert(0, r"c:\Users\ServeSmile IT\Projects\servenext\WEB\studio-engine\src\core")
from studio_runner import StudioEngine

EXHAUSTIVE_MERCHANT_SCENARIO = {
    "id": "servesmile_merchant_exhaustive_guide",
    "title": "ServeSmile Merchant OS — Exhaustive Official Demonstration",
    "scenes": [
        # Scene 1: Multi-Language & Secure Access
        {
            "id": "01_auth_multilang",
            "step": 1,
            "title": "Multi-Language & Secure Access",
            "subtitle": "Language switcher, masked credentials & dual-channel OTP",
            "badge": "🌐 Multi-Language & Bank-Grade Security",
            "component": "merchant/VirtualAuth.html",
            "narration": "ServeSmile Merchant is built for multi-language flexibility, enabling business owners to seamlessly toggle between English, Hindi, and regional dialects. Access your account securely using your registered mobile number or email, protected by dual-channel OTP verification and privacy-masked passwords.",
            "actions": [
                { "type": "spotlight", "selector": ".lang-btn.active", "scale": 1.25, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 215, "y": 140, "wait_before": 0.6 },
                { "type": "clear_spotlight", "wait_before": 0.8 },
                { "type": "spotlight", "selector": "#form-login", "scale": 1.08, "wait_before": 0.8 },
                { "type": "tap", "x": 215, "y": 360, "selector": "#login-id", "wait_before": 0.6 },
                { "type": "type", "selector": "#login-id", "text": "aarav@servesmile.com", "wait_before": 0.4 },
                { "type": "tap", "x": 215, "y": 420, "selector": "#login-pw", "wait_before": 0.6 },
                { "type": "type", "selector": "#login-pw", "text": "SecurePass2026!", "wait_before": 0.4 },
                { "type": "tap", "x": 215, "y": 500, "wait_before": 1.0 },
                { "type": "clear_spotlight", "wait_before": 1.0 }
            ]
        },

        # Scene 2: Storefront Onboarding & 1-Tap GPS
        {
            "id": "02_store_onboarding_gps",
            "step": 2,
            "title": "5-Step Storefront Setup & GPS",
            "subtitle": "1-Tap GPS detection, 20% discount presets & declarations",
            "badge": "📍 1-Tap Geolocation & Branding",
            "component": "merchant/VirtualStoreWizard.html",
            "narration": "Setting up your business storefront takes just moments. Upload your brand logo and high-resolution cover media, auto-detect your exact physical coordinates using instant 1-tap GPS geolocation, configure your 20% member savings rate with daily operating hours, and declare your official GSTIN and FSSAI food safety licenses.",
            "actions": [
                { "type": "spotlight", "selector": "#sec-step-1", "scale": 1.06, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 215, "y": 260, "wait_before": 1.0 },
                { "type": "clear_spotlight", "wait_before": 0.6 },
                { "type": "scroll", "dy": 260, "wait_before": 0.8 },
                { "type": "spotlight", "selector": "#btn-gps", "scale": 1.15, "wait_before": 0.8 },
                { "type": "tap", "x": 215, "y": 370, "selector": "#btn-gps", "wait_before": 0.8 },
                { "type": "clear_spotlight", "wait_before": 1.2 },
                { "type": "scroll", "dy": 380, "wait_before": 0.8 },
                { "type": "spotlight", "selector": "#btn-launch", "scale": 1.12, "wait_before": 0.8 },
                { "type": "tap", "x": 215, "y": 520, "selector": "#btn-launch", "wait_before": 1.0 },
                { "type": "clear_spotlight", "wait_before": 1.0 }
            ]
        },

        # Scene 3: Bank-Grade KYC Compliance Hub
        {
            "id": "03_kyc_compliance_hub",
            "step": 3,
            "title": "Bank-Grade KYC & Verified Badges",
            "subtitle": "3-Stage regulatory audit with AES-256 data protection",
            "badge": "🛡️ Verified Merchant Compliance",
            "component": "merchant/VirtualKycHub.html",
            "narration": "Regulatory compliance is streamlined inside the KYC Hub. Verify your business identity using your GSTIN, company PAN card, or Aadhaar documentation. Once audited by the compliance board, your business center receives the official green Verified Merchant Partner badge across the network.",
            "actions": [
                { "type": "spotlight", "selector": "#kyc-verified-card", "scale": 1.08, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 215, "y": 180, "wait_before": 1.5 },
                { "type": "clear_spotlight", "wait_before": 0.8 },
                { "type": "scroll", "dy": 200, "wait_before": 0.8 },
                { "type": "spotlight", "selector": "#kyc-audit-box", "scale": 1.08, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 215, "y": 320, "wait_before": 1.8 },
                { "type": "clear_spotlight", "wait_before": 1.0 }
            ]
        },

        # Scene 4: Master Catalog & HSN/SAC Directory
        {
            "id": "04_catalog_hsn_inventory",
            "step": 4,
            "title": "Master Catalog & HSN/SAC Directory",
            "subtitle": "Import catalog items, assign official GST tax codes & track stock",
            "badge": "📦 Smart Catalog & HSN Taxes",
            "component": "merchant/VirtualInventory.html",
            "narration": "Manage your entire product catalog and inventory effortlessly. Track live stock quantities, custom SKUs, and barcodes. You can import pre-built industry templates or create custom products. With the built-in government HSN and SAC directory, simply search and assign official tax codes like 996331 to automatically configure intra-state CGST and SGST rates for GST-compliant invoicing.",
            "actions": [
                { "type": "spotlight", "selector": "#btn-add-product", "scale": 1.25, "wait_before": 0.8 },
                { "type": "tap", "x": 370, "y": 38, "selector": "#btn-add-product", "wait_before": 0.8 },
                { "type": "clear_spotlight", "wait_before": 0.6 },
                { "type": "spotlight", "selector": "#add-product-modal > div", "scale": 1.05, "wait_before": 0.8 },
                { "type": "tap", "x": 215, "y": 180, "selector": "#inp-new-name", "wait_before": 0.6 },
                { "type": "type", "selector": "#inp-new-name", "text": "Signature Handi Paneer", "wait_before": 0.5 },
                { "type": "tap", "x": 320, "y": 360, "selector": "#add-product-modal button:has-text('Browse Directory')", "wait_before": 0.8 },
                { "type": "clear_spotlight", "wait_before": 0.5 },
                { "type": "spotlight", "selector": "#hsn-directory-modal > div", "scale": 1.1, "wait_before": 0.8 },
                { "type": "tap", "x": 215, "y": 280, "selector": "#hsn-results-list > div:first-child", "wait_before": 1.2 },
                { "type": "clear_spotlight", "wait_before": 0.5 },
                { "type": "spotlight", "selector": "#add-product-modal button:has-text('Save to Catalog')", "scale": 1.15, "wait_before": 0.8 },
                { "type": "tap", "x": 215, "y": 510, "selector": "#add-product-modal button:has-text('Save to Catalog')", "wait_before": 0.8 },
                { "type": "clear_spotlight", "wait_before": 1.2 }
            ]
        },

        # Scene 5: Touch POS Register & Cart Queue Parking
        {
            "id": "05_touch_pos_parking",
            "step": 5,
            "title": "Zero-Latency Touch POS & Cart Parking",
            "subtitle": "Category chips, tap-to-bill items & multi-cart queueing",
            "badge": "⚡ 0ms Touch Billing & Cart Parking",
            "component": "merchant/VirtualPosRegister.html",
            "narration": "The touch POS register operates with zero latency, even offline. Cashiers can swiftly filter categories, tap items into the cart, and increment quantity steppers in real time. During peak rush hours, cashiers can park an active order with one tap to serve the next customer in line, and instantly recall the held cart when ready.",
            "actions": [
                { "type": "spotlight", "selector": "#category-chips", "scale": 1.12, "wait_before": 0.8 },
                { "type": "tap", "x": 140, "y": 140, "selector": ".cat-chip:nth-child(2)", "wait_before": 0.8 },
                { "type": "clear_spotlight", "wait_before": 0.6 },
                { "type": "call_js", "code": "window.posTwin.addItem('dish-1');", "wait_before": 0.6 },
                { "type": "call_js", "code": "window.posTwin.stepQuantity('dish-1', 1);", "wait_before": 0.6 },
                { "type": "call_js", "code": "window.posTwin.addItem('dish-2');", "wait_before": 0.6 },
                { "type": "call_js", "code": "window.posTwin.addItem('dish-3');", "wait_before": 0.6 },
                { "type": "spotlight", "selector": "#btn-hold", "scale": 1.3, "wait_before": 1.0 },
                { "type": "call_js", "code": "window.posTwin.parkCart();", "wait_before": 1.0 },
                { "type": "clear_spotlight", "wait_before": 0.8 },
                { "type": "spotlight", "selector": "#btn-held-carts", "scale": 1.25, "wait_before": 1.0 },
                { "type": "call_js", "code": "window.posTwin.recallCart();", "wait_before": 1.0 },
                { "type": "clear_spotlight", "wait_before": 1.0 }
            ]
        },

        # Scene 6: Instant 20% Member Card QR Verification
        {
            "id": "06_member_qr_verification",
            "step": 6,
            "title": "Instant 20% Member QR Verification",
            "subtitle": "1-Tap member scan with floating verified celebration card",
            "badge": "✨ 20% Member Discount Validation",
            "component": "merchant/VirtualPosRegister.html",
            "narration": "To provide member discounts, simply scan the customer's member QR code. The terminal validates their pass instantly, displays a verified celebration badge with their username, and automatically applies the 20% member savings to the active order.",
            "actions": [
                { "type": "call_js", "code": "window.posTwin.addItem('dish-1'); window.posTwin.addItem('dish-2');", "wait_before": 0.5 },
                { "type": "spotlight", "selector": "#btn-member-scan", "scale": 1.15, "wait_before": 0.8 },
                { "type": "call_js", "code": "window.posTwin.verifyMember('Aarav Rajput', '@aarav_alqasr');", "wait_before": 1.2 },
                { "type": "clear_spotlight", "wait_before": 0.6 },
                { "type": "spotlight", "selector": "#member-celebration > div", "scale": 1.12, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 215, "y": 120, "wait_before": 2.0 },
                { "type": "clear_spotlight", "wait_before": 0.8 },
                { "type": "spotlight", "selector": "#row-discount", "scale": 1.25, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 215, "y": 620, "wait_before": 1.8 },
                { "type": "clear_spotlight", "wait_before": 1.0 }
            ]
        },

        # Scene 7: Payments & Thermal QR Receipts
        {
            "id": "07_payments_thermal_receipt",
            "step": 7,
            "title": "Digital Payments & Thermal QR Receipts",
            "subtitle": "Cash change calculator, Dynamic UPI QR & paperless bill QR",
            "badge": "🧾 Paperless Direct-Scan Receipts",
            "component": "merchant/VirtualPosRegister.html",
            "narration": "Checkout is flexible and transparent. Accept cash with built-in change return calculations or generate dynamic amount-embedded UPI QR codes. Upon completing the bill, the terminal displays an itemized GST tax invoice and generates a direct plain-text thermal QR receipt that customers can scan directly with their phone camera.",
            "actions": [
                { "type": "call_js", "code": "window.posTwin.addItem('dish-1'); window.posTwin.addItem('dish-2'); window.posTwin.verifyMember('Aarav Rajput', '@aarav_alqasr');", "wait_before": 0.4 },
                { "type": "spotlight", "selector": "#cash-change-box", "scale": 1.15, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 215, "y": 550, "wait_before": 1.2 },
                { "type": "clear_spotlight", "wait_before": 0.6 },
                { "type": "spotlight", "selector": "#pay-upi", "scale": 1.25, "wait_before": 0.8 },
                { "type": "call_js", "code": "window.posTwin.setPaymentMode('UPI');", "wait_before": 0.8 },
                { "type": "clear_spotlight", "wait_before": 0.6 },
                { "type": "spotlight", "selector": "#btn-checkout", "scale": 1.15, "wait_before": 0.8 },
                { "type": "call_js", "code": "window.posTwin.checkout();", "wait_before": 1.2 },
                { "type": "clear_spotlight", "wait_before": 0.6 },
                { "type": "spotlight", "selector": "#receipt-modal > div", "scale": 1.08, "wait_before": 0.8 },
                { "type": "call_js", "code": "window.posTwin.toggleThermalQr();", "wait_before": 1.2 },
                { "type": "cursor_move", "x": 215, "y": 420, "wait_before": 2.5 },
                { "type": "clear_spotlight", "wait_before": 1.0 }
            ]
        },

        # Scene 8: Business Boost Plans & Expansion Upgrades
        {
            "id": "08_business_boost_tiers",
            "step": 8,
            "title": "Business Boost Plans & Upgrades",
            "subtitle": "Unlock multi-branch expansion, promotional reels & priority search",
            "badge": "💎 Business Boost Growth Tiers",
            "component": "merchant/VirtualSubscriptions.html",
            "narration": "Grow and scale your enterprise with Business Boost subscription tiers. Upgrade from the Starter plan to Pro, Elite, or The Brand to manage up to twenty-five store branches, unlock professional promotional video reel production, run managed social ad campaigns, and achieve top priority ranking across the customer network.",
            "actions": [
                { "type": "spotlight", "selector": "#active-tier-card", "scale": 1.08, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 215, "y": 180, "wait_before": 1.5 },
                { "type": "clear_spotlight", "wait_before": 0.6 },
                { "type": "scroll", "dy": 250, "wait_before": 0.8 },
                { "type": "spotlight", "selector": "#tier-pro-card", "scale": 1.12, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 215, "y": 360, "wait_before": 2.2 },
                { "type": "clear_spotlight", "wait_before": 1.0 }
            ]
        }
    ]
}

async def main():
    engine = StudioEngine(EXHAUSTIVE_MERCHANT_SCENARIO, voice="en-US-BrianMultilingualNeural")
    await engine.render_all()

if __name__ == "__main__":
    asyncio.run(main())
