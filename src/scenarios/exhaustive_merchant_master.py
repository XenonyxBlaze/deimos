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
            "narration": "Welcome to ServeSmile Merchant. On your first launch, you can personalize your operating language right from the top navigation bar. Tap between English, Hindi, Punjabi, or Gujarati. The entire interface adapts in real time, making it effortless for your counter staff and store managers to operate comfortably in their native language.",
            "actions": [
                { "type": "spotlight", "selector": "#lang-bar", "scale": 1.08, "wait_before": 1.0 },
                { "type": "tap", "x": 280, "y": 25, "selector": ".lang-btn:nth-child(2)", "wait_before": 1.2 },
                { "type": "tap", "x": 340, "y": 25, "selector": ".lang-btn:nth-child(3)", "wait_before": 1.2 },
                { "type": "tap", "x": 400, "y": 25, "selector": ".lang-btn:nth-child(4)", "wait_before": 1.2 },
                { "type": "tap", "x": 220, "y": 25, "selector": ".lang-btn:nth-child(1)", "wait_before": 1.2 },
                { "type": "clear_spotlight", "wait_before": 1.5 }
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
            "narration": "To create your merchant account, tap on the 'Create Account' tab. Enter your full name, primary mobile number, business email, and set a secure password. You can also enter an optional referral code. Tap 'Register & Get OTP' to receive an instant six-digit verification code on your mobile. Once submitted, your business account is verified and ready to configure in under sixty seconds.",
            "actions": [
                { "type": "spotlight", "selector": "#tab-register", "scale": 1.15, "wait_before": 0.8 },
                { "type": "tap", "x": 320, "y": 140, "selector": "#tab-register", "wait_before": 0.8 },
                { "type": "clear_spotlight", "wait_before": 0.5 },
                { "type": "spotlight", "selector": "#form-register", "scale": 1.04, "wait_before": 0.8 },
                { "type": "type", "selector": "#reg-name", "text": "Aarav Rajput", "wait_before": 0.6 },
                { "type": "type", "selector": "#reg-phone", "text": "9876543210", "wait_before": 0.6 },
                { "type": "type", "selector": "#reg-email", "text": "aarav@servesmile.com", "wait_before": 0.6 },
                { "type": "type", "selector": "#reg-pw", "text": "SecurePass2026!", "wait_before": 0.6 },
                { "type": "tap", "x": 215, "y": 530, "selector": "#form-register button[type='submit']", "wait_before": 1.0 },
                { "type": "clear_spotlight", "wait_before": 0.6 },
                { "type": "spotlight", "selector": "#view-otp", "scale": 1.08, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 215, "y": 380, "wait_before": 2.0 },
                { "type": "clear_spotlight", "wait_before": 1.0 }
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
            "narration": "Next, our five-step onboarding wizard guides you through launching your digital storefront. Upload your brand logo and high-resolution cover photo. With a single tap on 'Detect GPS Location', the system automatically pins your exact shop coordinates. Set your opening hours, confirm your standard twenty percent member discount rate, and agree to the partner terms to publish your store.",
            "actions": [
                { "type": "spotlight", "selector": "#sec-step-1", "scale": 1.05, "wait_before": 1.0 },
                { "type": "cursor_move", "x": 215, "y": 240, "wait_before": 1.5 },
                { "type": "clear_spotlight", "wait_before": 0.6 },
                { "type": "scroll", "dy": 250, "wait_before": 0.8 },
                { "type": "spotlight", "selector": "#btn-gps", "scale": 1.12, "wait_before": 0.8 },
                { "type": "tap", "x": 215, "y": 360, "selector": "#btn-gps", "wait_before": 1.0 },
                { "type": "clear_spotlight", "wait_before": 1.5 },
                { "type": "scroll", "dy": 380, "wait_before": 0.8 },
                { "type": "spotlight", "selector": "#btn-launch", "scale": 1.12, "wait_before": 0.8 },
                { "type": "tap", "x": 215, "y": 520, "selector": "#btn-launch", "wait_before": 1.2 },
                { "type": "clear_spotlight", "wait_before": 1.0 }
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
            "narration": "Once published, your storefront is instantly showcased across the ServeSmile Cardholder Network. Over one thousand nearby members can discover your restaurant, view your live open status, check your menu, and see your exclusive twenty percent discount offer—driving high-intent foot traffic straight to your counter.",
            "actions": [
                { "type": "spotlight", "selector": "#showcase-cover", "scale": 1.05, "wait_before": 1.0 },
                { "type": "cursor_move", "x": 215, "y": 180, "wait_before": 2.0 },
                { "type": "clear_spotlight", "wait_before": 0.8 },
                { "type": "spotlight", "selector": "#showcase-discount-banner", "scale": 1.1, "wait_before": 1.0 },
                { "type": "cursor_move", "x": 215, "y": 320, "wait_before": 2.2 },
                { "type": "clear_spotlight", "wait_before": 0.8 },
                { "type": "spotlight", "selector": "#showcase-metrics", "scale": 1.1, "wait_before": 1.0 },
                { "type": "cursor_move", "x": 215, "y": 420, "wait_before": 2.2 },
                { "type": "clear_spotlight", "wait_before": 1.2 }
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
            "narration": "From the Stores tab, you have full multi-branch management. Check your live open or closed status, review daily operating hours, and verify connected POS cashier terminals. As your business grows, you can expand to multiple store centers and add new retail branch slots in just a single tap.",
            "actions": [
                { "type": "spotlight", "selector": "#active-store-card", "scale": 1.06, "wait_before": 1.0 },
                { "type": "cursor_move", "x": 215, "y": 180, "wait_before": 1.8 },
                { "type": "clear_spotlight", "wait_before": 0.6 },
                { "type": "spotlight", "selector": "#store-metrics-grid", "scale": 1.12, "wait_before": 1.0 },
                { "type": "cursor_move", "x": 215, "y": 310, "wait_before": 2.0 },
                { "type": "clear_spotlight", "wait_before": 0.6 },
                { "type": "spotlight", "selector": "#store-slots-banner", "scale": 1.1, "wait_before": 1.0 },
                { "type": "cursor_move", "x": 215, "y": 440, "wait_before": 2.2 },
                { "type": "clear_spotlight", "wait_before": 1.2 }
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
            "narration": "To unlock automated next-day bank settlements and establish instant customer trust, navigate to the KYC Hub. Submitting your business GSTIN certificate and PAN card triggers our rapid compliance audit, awarding your store the official green Verified Merchant Partner badge.",
            "actions": [
                { "type": "spotlight", "selector": "#kyc-verified-card", "scale": 1.08, "wait_before": 1.0 },
                { "type": "cursor_move", "x": 215, "y": 180, "wait_before": 2.0 },
                { "type": "clear_spotlight", "wait_before": 0.8 },
                { "type": "scroll", "dy": 200, "wait_before": 0.8 },
                { "type": "spotlight", "selector": "#kyc-audit-box", "scale": 1.06, "wait_before": 1.0 },
                { "type": "cursor_move", "x": 215, "y": 320, "wait_before": 2.2 },
                { "type": "clear_spotlight", "wait_before": 1.2 }
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
            "narration": "Setting up your digital catalog is completely seamless. Tap 'Add Product' to enter your dish name, selling price, and available inventory count. Open the built-in government HSN tax directory to select SAC code 996331 for restaurant food services, which automatically computes your standard five percent GST tax split between CGST and SGST on every invoice.",
            "actions": [
                { "type": "spotlight", "selector": "#btn-add-product", "scale": 1.2, "wait_before": 1.0 },
                { "type": "tap", "x": 370, "y": 38, "selector": "#btn-add-product", "wait_before": 1.0 },
                { "type": "clear_spotlight", "wait_before": 0.6 },
                { "type": "spotlight", "selector": "#add-product-modal > div", "scale": 1.04, "wait_before": 1.0 },
                { "type": "tap", "x": 215, "y": 180, "selector": "#inp-new-name", "wait_before": 0.8 },
                { "type": "type", "selector": "#inp-new-name", "text": "Signature Handi Paneer", "wait_before": 0.6 },
                { "type": "tap", "x": 320, "y": 360, "selector": "#add-product-modal button:has-text('Browse Directory')", "wait_before": 1.0 },
                { "type": "clear_spotlight", "wait_before": 0.6 },
                { "type": "spotlight", "selector": "#hsn-directory-modal > div", "scale": 1.08, "wait_before": 1.0 },
                { "type": "tap", "x": 215, "y": 280, "selector": "#hsn-results-list > div:first-child", "wait_before": 1.5 },
                { "type": "clear_spotlight", "wait_before": 0.6 },
                { "type": "spotlight", "selector": "#add-product-modal button:has-text('Save to Catalog')", "scale": 1.12, "wait_before": 1.0 },
                { "type": "tap", "x": 215, "y": 510, "selector": "#add-product-modal button:has-text('Save to Catalog')", "wait_before": 1.0 },
                { "type": "clear_spotlight", "wait_before": 1.2 }
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
            "narration": "The touch POS terminal operates with zero latency, even completely offline. Browse menu categories and tap dishes into the active cart, or adjust quantities using the in-card steppers. If a line forms, tap 'Hold' to park the order. When a ServeSmile cardholder presents their pass, tap 'Scan Pass' to instantly verify their identity and apply their twenty percent savings. Choose between Cash, Dynamic UPI QR, or Card, and tap 'Complete & Bill' to generate an itemized thermal receipt with a direct plain-text QR bill. You can also open 'Past Bills' at any time to review your complete transaction history.",
            "actions": [
                { "type": "spotlight", "selector": "#category-chips", "scale": 1.1, "wait_before": 1.0 },
                { "type": "tap", "x": 140, "y": 140, "selector": ".cat-chip:nth-child(2)", "wait_before": 1.0 },
                { "type": "clear_spotlight", "wait_before": 0.6 },
                { "type": "call_js", "code": "window.posTwin.addItem('dish-1');", "wait_before": 0.6 },
                { "type": "call_js", "code": "window.posTwin.stepQuantity('dish-1', 1);", "wait_before": 0.6 },
                { "type": "call_js", "code": "window.posTwin.addItem('dish-2');", "wait_before": 0.6 },
                { "type": "call_js", "code": "window.posTwin.addItem('dish-3');", "wait_before": 0.6 },
                { "type": "spotlight", "selector": "#btn-member-scan", "scale": 1.15, "wait_before": 1.0 },
                { "type": "call_js", "code": "window.posTwin.verifyMember('Aarav Rajput', '@aarav_alqasr');", "wait_before": 1.5 },
                { "type": "clear_spotlight", "wait_before": 0.8 },
                { "type": "spotlight", "selector": "#btn-checkout", "scale": 1.12, "wait_before": 1.0 },
                { "type": "call_js", "code": "window.posTwin.checkout();", "wait_before": 1.5 },
                { "type": "clear_spotlight", "wait_before": 0.8 },
                { "type": "spotlight", "selector": "#receipt-modal > div", "scale": 1.06, "wait_before": 1.0 },
                { "type": "call_js", "code": "window.posTwin.toggleThermalQr();", "wait_before": 1.5 },
                { "type": "clear_spotlight", "wait_before": 1.0 },
                { "type": "call_js", "code": "window.posTwin.closeReceipt();", "wait_before": 0.8 },
                { "type": "spotlight", "selector": "#btn-past-bills", "scale": 1.2, "wait_before": 1.0 },
                { "type": "call_js", "code": "window.posTwin.openPastBills();", "wait_before": 1.2 },
                { "type": "cursor_move", "x": 215, "y": 300, "wait_before": 2.5 },
                { "type": "clear_spotlight", "wait_before": 1.2 }
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
            "narration": "Retain more diners with our built-in Customer CRM. Track your overall customer satisfaction rating and read verified feedback from actual cardholders. Monitor weekly member check-in frequency and reply directly to customer reviews and inquiries to turn first-time guests into lifelong regulars.",
            "actions": [
                { "type": "spotlight", "selector": "#crm-rating-summary", "scale": 1.08, "wait_before": 1.0 },
                { "type": "cursor_move", "x": 215, "y": 140, "wait_before": 2.0 },
                { "type": "clear_spotlight", "wait_before": 0.8 },
                { "type": "spotlight", "selector": "#review-card-1", "scale": 1.06, "wait_before": 1.0 },
                { "type": "cursor_move", "x": 215, "y": 280, "wait_before": 2.5 },
                { "type": "clear_spotlight", "wait_before": 1.2 }
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
            "narration": "Ready to scale your foot traffic even further? Explore our Business Boost subscription plans. Upgrading to Pro Silver or Elite Gold unlocks multi-branch management, professional 4K promotional video reels produced for your brand, managed social media advertising, and top priority search ranking across the customer app.",
            "actions": [
                { "type": "spotlight", "selector": "#active-tier-card", "scale": 1.06, "wait_before": 1.0 },
                { "type": "cursor_move", "x": 215, "y": 180, "wait_before": 2.0 },
                { "type": "clear_spotlight", "wait_before": 0.8 },
                { "type": "scroll", "dy": 250, "wait_before": 0.8 },
                { "type": "spotlight", "selector": "#tier-pro-card", "scale": 1.08, "wait_before": 1.0 },
                { "type": "cursor_move", "x": 215, "y": 360, "wait_before": 2.5 },
                { "type": "clear_spotlight", "wait_before": 1.2 }
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
            "narration": "Whenever you need assistance, priority merchant support is always available. Connect directly with your dedicated account manager via our priority WhatsApp hotline with response times under two minutes, submit categorized technical tickets, or follow instant troubleshooting guides for Bluetooth thermal receipt printers.",
            "actions": [
                { "type": "spotlight", "selector": "#help-hotline-card", "scale": 1.08, "wait_before": 1.0 },
                { "type": "cursor_move", "x": 215, "y": 180, "wait_before": 2.2 },
                { "type": "clear_spotlight", "wait_before": 0.8 },
                { "type": "spotlight", "selector": "#help-ticket-card", "scale": 1.06, "wait_before": 1.0 },
                { "type": "cursor_move", "x": 215, "y": 380, "wait_before": 2.5 },
                { "type": "clear_spotlight", "wait_before": 1.2 }
            ]
        }
    ]
}

async def main():
    engine = StudioEngine(EXHAUSTIVE_11_SCREEN_SCENARIO, voice="en-US-BrianMultilingualNeural")
    await engine.render_all()

if __name__ == "__main__":
    asyncio.run(main())
