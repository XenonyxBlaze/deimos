import asyncio
import os
import sys

sys.path.insert(0, r"c:\Users\ServeSmile IT\Projects\servenext\WEB\studio-engine\src\core")
from studio_runner import StudioEngine

EXHAUSTIVE_11_SCREEN_SCENARIO = {
    "id": "servesmile_merchant_complete_master_guide",
    "title": "ServeSmile Merchant OS — Interactive Platform Walkthrough",
    "scenes": [
        # Scene 1: Language Select
        {
            "id": "01_language_select",
            "step": 1,
            "title": "Multi-Language Accessibility",
            "subtitle": "Instant dialect switching for seamless cashier and manager workflows",
            "badge": "🌐 Regional Language Switcher",
            "benefit": "⚡ Zero Training Curve • Native Regional Dialects",
            "component": "merchant/VirtualAuth.html",
            "narration": "ServeSmile Merchant is built for frictionless staff adoption. Switch instantly between English, Hindi, Punjabi, and Gujarati so your store managers and cashiers can operate comfortably in their preferred language.",
            "actions": [
                { "type": "spotlight", "selector": "#lang-bar", "scale": 1.08, "wait_before": 0.8 },
                { "type": "tap", "x": 280, "y": 25, "selector": ".lang-btn:nth-child(2)", "wait_before": 0.8 },
                { "type": "tap", "x": 340, "y": 25, "selector": ".lang-btn:nth-child(3)", "wait_before": 0.8 },
                { "type": "tap", "x": 400, "y": 25, "selector": ".lang-btn:nth-child(4)", "wait_before": 0.8 },
                { "type": "tap", "x": 220, "y": 25, "selector": ".lang-btn:nth-child(1)", "wait_before": 0.8 },
                { "type": "clear_spotlight", "wait_before": 1.0 }
            ]
        },

        # Scene 2: Merchant Registration & Dual-Channel OTP (Registration Focus)
        {
            "id": "02_registration_form",
            "step": 2,
            "title": "60-Second Merchant Signup",
            "subtitle": "Fast partner registration with instant dual-channel mobile OTP",
            "badge": "🔒 Rapid Mobile Onboarding",
            "benefit": "⏱️ Under 60s Onboarding • Bank-Grade Data Security",
            "component": "merchant/VirtualAuth.html",
            "narration": "Signing up takes under sixty seconds. Enter your business details, create your password, and verify with an instant six-digit mobile OTP to immediately access your merchant portal.",
            "actions": [
                { "type": "spotlight", "selector": "#tab-register", "scale": 1.15, "wait_before": 0.6 },
                { "type": "tap", "x": 320, "y": 140, "selector": "#tab-register", "wait_before": 0.6 },
                { "type": "clear_spotlight", "wait_before": 0.4 },
                { "type": "spotlight", "selector": "#form-register", "scale": 1.04, "wait_before": 0.6 },
                { "type": "type", "selector": "#reg-name", "text": "Aarav Rajput", "wait_before": 0.4 },
                { "type": "type", "selector": "#reg-phone", "text": "9876543210", "wait_before": 0.4 },
                { "type": "type", "selector": "#reg-email", "text": "aarav@servesmile.com", "wait_before": 0.4 },
                { "type": "type", "selector": "#reg-pw", "text": "SecurePass2026!", "wait_before": 0.4 },
                { "type": "tap", "x": 215, "y": 530, "selector": "#form-register button[type='submit']", "wait_before": 0.8 },
                { "type": "clear_spotlight", "wait_before": 0.5 },
                { "type": "spotlight", "selector": "#view-otp", "scale": 1.1, "wait_before": 0.6 },
                { "type": "cursor_move", "x": 215, "y": 380, "wait_before": 1.5 },
                { "type": "clear_spotlight", "wait_before": 0.8 }
            ]
        },

        # Scene 3: Business Setup Wizard & 1-Tap GPS
        {
            "id": "03_business_onboarding_wizard",
            "step": 3,
            "title": "5-Step Storefront Setup & GPS",
            "subtitle": "Upload brand media & auto-detect coordinates in a single tap",
            "badge": "📍 1-Tap Geolocation & Setup",
            "benefit": "🎯 Accurate Store Listing • Automated Business Hours",
            "component": "merchant/VirtualStoreWizard.html",
            "narration": "Set up your retail outlet in five simple steps. Upload your brand logo and cover photos, lock in your exact store location with one-tap GPS geolocation, and configure your standard twenty percent member discount rate.",
            "actions": [
                { "type": "spotlight", "selector": "#sec-step-1", "scale": 1.05, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 215, "y": 240, "wait_before": 1.2 },
                { "type": "clear_spotlight", "wait_before": 0.5 },
                { "type": "scroll", "dy": 250, "wait_before": 0.6 },
                { "type": "spotlight", "selector": "#btn-gps", "scale": 1.12, "wait_before": 0.6 },
                { "type": "tap", "x": 215, "y": 360, "selector": "#btn-gps", "wait_before": 0.8 },
                { "type": "clear_spotlight", "wait_before": 1.2 },
                { "type": "scroll", "dy": 380, "wait_before": 0.6 },
                { "type": "spotlight", "selector": "#btn-launch", "scale": 1.12, "wait_before": 0.6 },
                { "type": "tap", "x": 215, "y": 520, "selector": "#btn-launch", "wait_before": 1.0 },
                { "type": "clear_spotlight", "wait_before": 0.8 }
            ]
        },

        # Scene 4: Public Store Discovery Showcase (High Visibility Consumer App)
        {
            "id": "04_public_discovery_showcase",
            "step": 4,
            "layout": "center",
            "title": "Live On ServeSmile Discovery",
            "subtitle": "High-visibility discovery driving local foot traffic to your counter",
            "badge": "🚀 Instant Customer Visibility",
            "benefit": "📈 Guaranteed Foot Traffic • 1.2k+ Active Cardholders",
            "component": "merchant/VirtualPublicShowcase.html",
            "narration": "Once published, your store is instantly featured on the ServeSmile Cardholder App. Nearby members discover your exclusive twenty percent offer, driving high-intent foot traffic directly to your business.",
            "actions": [
                { "type": "spotlight", "selector": "#showcase-cover", "scale": 1.05, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 215, "y": 180, "wait_before": 1.5 },
                { "type": "clear_spotlight", "wait_before": 0.6 },
                { "type": "spotlight", "selector": "#showcase-discount-banner", "scale": 1.1, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 215, "y": 320, "wait_before": 1.8 },
                { "type": "clear_spotlight", "wait_before": 0.6 },
                { "type": "spotlight", "selector": "#showcase-metrics", "scale": 1.1, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 215, "y": 420, "wait_before": 1.8 },
                { "type": "clear_spotlight", "wait_before": 1.0 }
            ]
        },

        # Scene 5: Managing Store Outlets
        {
            "id": "05_managing_store",
            "step": 5,
            "title": "Multi-Branch Store Management",
            "subtitle": "Monitor daily hours, online POS status & expand to new outlets",
            "badge": "🏪 Central Outlet Operations",
            "benefit": "📊 Centralized Control • Multi-Branch Ready",
            "component": "merchant/VirtualStoreManage.html",
            "narration": "Manage all your outlet locations and cashier terminals from a unified dashboard. Check live operating hours, monitor online terminal connectivity, and expand to multiple store branches with ease.",
            "actions": [
                { "type": "spotlight", "selector": "#active-store-card", "scale": 1.06, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 215, "y": 180, "wait_before": 1.2 },
                { "type": "clear_spotlight", "wait_before": 0.5 },
                { "type": "spotlight", "selector": "#store-metrics-grid", "scale": 1.12, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 215, "y": 310, "wait_before": 1.5 },
                { "type": "clear_spotlight", "wait_before": 0.5 },
                { "type": "spotlight", "selector": "#store-slots-banner", "scale": 1.1, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 215, "y": 440, "wait_before": 1.8 },
                { "type": "clear_spotlight", "wait_before": 1.0 }
            ]
        },

        # Scene 6: Updating KYC & Verified Partner Badge
        {
            "id": "06_updating_kyc",
            "step": 6,
            "title": "Verified Merchant Partner Badge",
            "subtitle": "Automated GSTIN and PAN audit unlocking official trust badge",
            "badge": "🛡️ Verified Compliance & Trust",
            "benefit": "⭐ Official Verified Badge • Next-Day Bank Settlement",
            "component": "merchant/VirtualKycHub.html",
            "narration": "Complete your KYC compliance in minutes. Submitting your GSTIN and business PAN unlocks the official green Verified Merchant Partner badge, establishing immediate trust with visiting cardholders.",
            "actions": [
                { "type": "spotlight", "selector": "#kyc-verified-card", "scale": 1.08, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 215, "y": 180, "wait_before": 1.5 },
                { "type": "clear_spotlight", "wait_before": 0.6 },
                { "type": "scroll", "dy": 200, "wait_before": 0.6 },
                { "type": "spotlight", "selector": "#kyc-audit-box", "scale": 1.06, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 215, "y": 320, "wait_before": 1.8 },
                { "type": "clear_spotlight", "wait_before": 1.0 }
            ]
        },

        # Scene 7: Catalog & Smart Inventory Management
        {
            "id": "07_catalog_inventory",
            "step": 7,
            "title": "Smart Catalog & Automated GST",
            "subtitle": "Track live stock & auto-calculate CGST and SGST with HSN codes",
            "badge": "📦 1-Click Inventory & Invoicing",
            "benefit": "💡 Automated 5% Tax Calculation • Barcode SKU Tracking",
            "component": "merchant/VirtualInventory.html",
            "narration": "Manage your product catalog with zero accounting headaches. Add dishes and items with official HSN codes to automatically calculate intra-state CGST and SGST tax splits on every bill.",
            "actions": [
                { "type": "spotlight", "selector": "#btn-add-product", "scale": 1.2, "wait_before": 0.8 },
                { "type": "tap", "x": 370, "y": 38, "selector": "#btn-add-product", "wait_before": 0.8 },
                { "type": "clear_spotlight", "wait_before": 0.5 },
                { "type": "spotlight", "selector": "#add-product-modal > div", "scale": 1.04, "wait_before": 0.8 },
                { "type": "tap", "x": 215, "y": 180, "selector": "#inp-new-name", "wait_before": 0.6 },
                { "type": "type", "selector": "#inp-new-name", "text": "Signature Handi Paneer", "wait_before": 0.5 },
                { "type": "tap", "x": 320, "y": 360, "selector": "#add-product-modal button:has-text('Browse Directory')", "wait_before": 0.8 },
                { "type": "clear_spotlight", "wait_before": 0.5 },
                { "type": "spotlight", "selector": "#hsn-directory-modal > div", "scale": 1.08, "wait_before": 0.8 },
                { "type": "tap", "x": 215, "y": 280, "selector": "#hsn-results-list > div:first-child", "wait_before": 1.2 },
                { "type": "clear_spotlight", "wait_before": 0.5 },
                { "type": "spotlight", "selector": "#add-product-modal button:has-text('Save to Catalog')", "scale": 1.12, "wait_before": 0.8 },
                { "type": "tap", "x": 215, "y": 510, "selector": "#add-product-modal button:has-text('Save to Catalog')", "wait_before": 0.8 },
                { "type": "clear_spotlight", "wait_before": 1.0 }
            ]
        },

        # Scene 8: 0ms Touch POS Billing, Member QR & Past Bills
        {
            "id": "08_pos_billing_card_past_bills",
            "step": 8,
            "title": "0ms Touch POS, Member QR & Past Bills",
            "subtitle": "Lightning-fast tap billing, 20% member QR scan & thermal receipts",
            "badge": "⚡ 0ms Offline POS & Thermal Bills",
            "benefit": "🚀 0ms Zero-Latency Billing • Direct Plain-Text QR Bills",
            "component": "merchant/VirtualPosRegister.html",
            "narration": "The touch POS register operates with zero latency, even completely offline. Tap dishes into the cart, adjust quantity steppers, and park rush-hour orders. When a member presents their pass, scan their QR code to instantly apply the twenty percent discount, generate paperless thermal QR receipts, and review past order invoices on demand.",
            "actions": [
                { "type": "spotlight", "selector": "#category-chips", "scale": 1.1, "wait_before": 0.8 },
                { "type": "tap", "x": 140, "y": 140, "selector": ".cat-chip:nth-child(2)", "wait_before": 0.8 },
                { "type": "clear_spotlight", "wait_before": 0.5 },
                { "type": "call_js", "code": "window.posTwin.addItem('dish-1');", "wait_before": 0.5 },
                { "type": "call_js", "code": "window.posTwin.stepQuantity('dish-1', 1);", "wait_before": 0.5 },
                { "type": "call_js", "code": "window.posTwin.addItem('dish-2');", "wait_before": 0.5 },
                { "type": "call_js", "code": "window.posTwin.addItem('dish-3');", "wait_before": 0.5 },
                { "type": "spotlight", "selector": "#btn-member-scan", "scale": 1.15, "wait_before": 0.8 },
                { "type": "call_js", "code": "window.posTwin.verifyMember('Aarav Rajput', '@aarav_alqasr');", "wait_before": 1.2 },
                { "type": "clear_spotlight", "wait_before": 0.6 },
                { "type": "spotlight", "selector": "#btn-checkout", "scale": 1.12, "wait_before": 0.8 },
                { "type": "call_js", "code": "window.posTwin.checkout();", "wait_before": 1.2 },
                { "type": "clear_spotlight", "wait_before": 0.6 },
                { "type": "spotlight", "selector": "#receipt-modal > div", "scale": 1.06, "wait_before": 0.8 },
                { "type": "call_js", "code": "window.posTwin.toggleThermalQr();", "wait_before": 1.2 },
                { "type": "clear_spotlight", "wait_before": 0.8 },
                { "type": "call_js", "code": "window.posTwin.closeReceipt();", "wait_before": 0.6 },
                { "type": "spotlight", "selector": "#btn-past-bills", "scale": 1.2, "wait_before": 0.8 },
                { "type": "call_js", "code": "window.posTwin.openPastBills();", "wait_before": 1.0 },
                { "type": "cursor_move", "x": 215, "y": 300, "wait_before": 2.0 },
                { "type": "clear_spotlight", "wait_before": 0.8 }
            ]
        },

        # Scene 9: Customer CRM, Verified Ratings & Retention
        {
            "id": "09_customer_crm_reviews_enquiries",
            "step": 9,
            "title": "Customer CRM & 5-Star Reviews",
            "subtitle": "Track member check-ins & reply directly to verified customer ratings",
            "badge": "⭐ Verified Reviews & Retention",
            "benefit": "🔁 3.4x Higher Repeat Visits • Direct Customer Messaging",
            "component": "merchant/VirtualCustomerCrm.html",
            "narration": "Turn first-time diners into loyal regular customers. Review verified cardholder ratings, track weekly member visit frequency, and reply directly to customer inquiries to maximize repeat visits.",
            "actions": [
                { "type": "spotlight", "selector": "#crm-rating-summary", "scale": 1.08, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 215, "y": 140, "wait_before": 1.5 },
                { "type": "clear_spotlight", "wait_before": 0.6 },
                { "type": "spotlight", "selector": "#review-card-1", "scale": 1.06, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 215, "y": 280, "wait_before": 2.0 },
                { "type": "clear_spotlight", "wait_before": 0.8 }
            ]
        },

        # Scene 10: Business Boost Growth & Promotional Video Reels
        {
            "id": "10_business_boost_subscriptions",
            "step": 10,
            "title": "Business Boost Growth Plans",
            "subtitle": "Unlock multi-branch expansion, promotional reels & top ranking",
            "badge": "💎 Business Boost Scaling Plans",
            "benefit": "🎥 Studio 4K Video Reels • Top Priority Search Placement",
            "component": "merchant/VirtualSubscriptions.html",
            "narration": "Accelerate your growth with Business Boost subscription tiers. Upgrade to unlock multi-branch management, professional 4K promotional video reels, managed social media advertising, and top priority search ranking across the network.",
            "actions": [
                { "type": "spotlight", "selector": "#active-tier-card", "scale": 1.06, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 215, "y": 180, "wait_before": 1.5 },
                { "type": "clear_spotlight", "wait_before": 0.6 },
                { "type": "scroll", "dy": 250, "wait_before": 0.6 },
                { "type": "spotlight", "selector": "#tier-pro-card", "scale": 1.08, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 215, "y": 360, "wait_before": 2.2 },
                { "type": "clear_spotlight", "wait_before": 1.0 }
            ]
        },

        # Scene 11: Merchant Help Desk & 24/7 Dedicated Hotline
        {
            "id": "11_help_center_support",
            "step": 11,
            "title": "24/7 Priority Merchant Support",
            "subtitle": "Direct WhatsApp merchant hotline, instant ticketing & printer setup",
            "badge": "🎧 24/7 Dedicated Merchant Support",
            "benefit": "💬 <2 Min WhatsApp Response • Dedicated Account Manager",
            "component": "merchant/VirtualHelpCenter.html",
            "narration": "Enjoy peace of mind with 24/7 merchant support. Connect directly with your dedicated account manager via our WhatsApp hotline, submit categorized technical tickets, or follow instant guides for thermal printer setup.",
            "actions": [
                { "type": "spotlight", "selector": "#help-hotline-card", "scale": 1.08, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 215, "y": 180, "wait_before": 1.8 },
                { "type": "clear_spotlight", "wait_before": 0.6 },
                { "type": "spotlight", "selector": "#help-ticket-card", "scale": 1.06, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 215, "y": 380, "wait_before": 2.0 },
                { "type": "clear_spotlight", "wait_before": 1.0 }
            ]
        }
    ]
}

async def main():
    engine = StudioEngine(EXHAUSTIVE_11_SCREEN_SCENARIO, voice="en-US-BrianMultilingualNeural")
    await engine.render_all()

if __name__ == "__main__":
    asyncio.run(main())
