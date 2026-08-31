import asyncio
import os
import sys

sys.path.insert(0, r"c:\Users\ServeSmile IT\Projects\servenext\WEB\studio-engine\src\core")
from studio_runner import StudioEngine

EXHAUSTIVE_10_SCREEN_SCENARIO = {
    "id": "servesmile_merchant_complete_master_guide",
    "title": "ServeSmile Merchant OS — Complete 10-Step Interactive Demonstration",
    "scenes": [
        # Scene 1: Language Select
        {
            "id": "01_language_select",
            "step": 1,
            "title": "Multi-Language Regional Dialects",
            "subtitle": "Instant locale switcher for seamless merchant accessibility",
            "badge": "🌐 Regional Language Select",
            "component": "merchant/VirtualAuth.html",
            "narration": "ServeSmile Merchant is built for regional flexibility. Business owners can instantly switch between English, Hindi, Punjabi, and Gujarati, ensuring an intuitive, localized operating experience across diverse regional markets.",
            "actions": [
                { "type": "spotlight", "selector": ".lang-btn:nth-child(1)", "scale": 1.25, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 130, "y": 140, "wait_before": 0.8 },
                { "type": "clear_spotlight", "wait_before": 0.4 },
                { "type": "spotlight", "selector": ".lang-btn:nth-child(2)", "scale": 1.25, "wait_before": 0.6 },
                { "type": "cursor_move", "x": 190, "y": 140, "wait_before": 0.8 },
                { "type": "clear_spotlight", "wait_before": 0.4 },
                { "type": "spotlight", "selector": ".lang-btn:nth-child(3)", "scale": 1.25, "wait_before": 0.6 },
                { "type": "cursor_move", "x": 250, "y": 140, "wait_before": 0.8 },
                { "type": "clear_spotlight", "wait_before": 0.4 },
                { "type": "spotlight", "selector": ".lang-btn:nth-child(4)", "scale": 1.25, "wait_before": 0.6 },
                { "type": "cursor_move", "x": 310, "y": 140, "wait_before": 0.8 },
                { "type": "clear_spotlight", "wait_before": 1.0 }
            ]
        },

        # Scene 2: Registration & Dual-Channel Authentication
        {
            "id": "02_registration_form",
            "step": 2,
            "title": "Merchant Signup & Dual-Channel OTP",
            "subtitle": "Privacy-masked credentials & bank-grade dual-channel security",
            "badge": "🔒 Bank-Grade Authentication",
            "component": "merchant/VirtualAuth.html",
            "narration": "Creating an account and logging in is fast and secure. Authenticate with your mobile number or business email, protected by dual-channel OTP verification and privacy-masked passwords to safeguard sensitive business credentials.",
            "actions": [
                { "type": "spotlight", "selector": "#form-login", "scale": 1.08, "wait_before": 0.8 },
                { "type": "tap", "x": 215, "y": 360, "selector": "#login-id", "wait_before": 0.6 },
                { "type": "type", "selector": "#login-id", "text": "aarav@servesmile.com", "wait_before": 0.4 },
                { "type": "tap", "x": 215, "y": 420, "selector": "#login-pw", "wait_before": 0.6 },
                { "type": "type", "selector": "#login-pw", "text": "SecurePass2026!", "wait_before": 0.4 },
                { "type": "tap", "x": 215, "y": 500, "wait_before": 1.0 },
                { "type": "clear_spotlight", "wait_before": 1.0 }
            ]
        },

        # Scene 3: Business Onboarding Wizard
        {
            "id": "03_business_onboarding_wizard",
            "step": 3,
            "title": "5-Step Business Onboarding Wizard",
            "subtitle": "Brand showcase, 1-tap GPS geolocation & license declarations",
            "badge": "📍 1-Tap Geolocation & Branding",
            "component": "merchant/VirtualStoreWizard.html",
            "narration": "Onboard your business center in five simple steps. Upload your brand logo and high-resolution cover showcase, retrieve your exact physical coordinates using instant 1-tap GPS geolocation, configure your twenty percent member savings rate, and declare your official GSTIN and FSSAI licenses.",
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

        # Scene 4: Managing Store Outlets
        {
            "id": "04_managing_store",
            "step": 4,
            "title": "Managing Store Centers & Outlets",
            "subtitle": "Outlet profiles, live operating status & POS terminal launch",
            "badge": "🏪 Outlet Management & Multi-Branch",
            "component": "merchant/VirtualStoreManage.html",
            "narration": "Manage your retail outlets and storefront operations from one central dashboard. Monitor daily operating hours, toggle live open status, check online terminal connectivity, and expand to multiple store branches seamlessly.",
            "actions": [
                { "type": "spotlight", "selector": "#active-store-card", "scale": 1.08, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 215, "y": 180, "wait_before": 1.2 },
                { "type": "clear_spotlight", "wait_before": 0.6 },
                { "type": "spotlight", "selector": "#store-metrics-grid", "scale": 1.15, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 215, "y": 310, "wait_before": 1.5 },
                { "type": "clear_spotlight", "wait_before": 0.6 },
                { "type": "spotlight", "selector": "#store-slots-banner", "scale": 1.12, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 215, "y": 440, "wait_before": 1.8 },
                { "type": "clear_spotlight", "wait_before": 1.0 }
            ]
        },

        # Scene 5: Updating KYC Compliance Hub
        {
            "id": "05_updating_kyc",
            "step": 5,
            "title": "Bank-Grade KYC & Verified Partner Badge",
            "subtitle": "3-Stage regulatory audit with AES-256 encrypted verification",
            "badge": "🛡️ Verified Compliance Audit",
            "component": "merchant/VirtualKycHub.html",
            "narration": "Maintain full regulatory compliance inside the KYC Hub. Verify your business identity using GSTIN certificates, company PAN records, and biometric validation. Upon approval, your store displays the official green Verified Merchant Partner badge across the network.",
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

        # Scene 6: Catalog & HSN/SAC Inventory Management
        {
            "id": "06_catalog_inventory",
            "step": 6,
            "title": "Master Catalog & Government HSN/SAC Directory",
            "subtitle": "Track SKUs, search official tax codes & auto-split GST rates",
            "badge": "📦 Smart Inventory & HSN Taxes",
            "component": "merchant/VirtualInventory.html",
            "narration": "Manage your product catalog and inventory with precision. Track live stock counts, custom SKUs, and barcodes. Using the built-in government HSN and SAC directory, easily assign official tax codes like 996331 to automatically configure intra-state CGST and SGST rates for compliant invoicing.",
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

        # Scene 7: POS Functionality, Member QR & Past Bills
        {
            "id": "07_pos_billing_card_past_bills",
            "step": 7,
            "title": "0ms Touch POS Billing, Member QR & Past Bills",
            "subtitle": "Instant tap billing, in-card steppers, 20% member QR & thermal bills",
            "badge": "⚡ Offline POS & Plain-Text QR Bills",
            "component": "merchant/VirtualPosRegister.html",
            "narration": "The touch POS register operates with zero latency, even offline. Tap items into the cart, adjust quantity steppers, and park active orders during peak rush hours. Simply scan a customer's member QR code to instantly verify their pass and apply the twenty percent discount. Generate itemized tax invoices with direct plain-text thermal QR receipts, and review past order bills on demand.",
            "actions": [
                { "type": "spotlight", "selector": "#category-chips", "scale": 1.12, "wait_before": 0.8 },
                { "type": "tap", "x": 140, "y": 140, "selector": ".cat-chip:nth-child(2)", "wait_before": 0.8 },
                { "type": "clear_spotlight", "wait_before": 0.6 },
                { "type": "call_js", "code": "window.posTwin.addItem('dish-1');", "wait_before": 0.6 },
                { "type": "call_js", "code": "window.posTwin.stepQuantity('dish-1', 1);", "wait_before": 0.6 },
                { "type": "call_js", "code": "window.posTwin.addItem('dish-2');", "wait_before": 0.6 },
                { "type": "call_js", "code": "window.posTwin.addItem('dish-3');", "wait_before": 0.6 },
                { "type": "spotlight", "selector": "#btn-member-scan", "scale": 1.15, "wait_before": 0.8 },
                { "type": "call_js", "code": "window.posTwin.verifyMember('Aarav Rajput', '@aarav_alqasr');", "wait_before": 1.2 },
                { "type": "clear_spotlight", "wait_before": 0.6 },
                { "type": "spotlight", "selector": "#btn-checkout", "scale": 1.15, "wait_before": 0.8 },
                { "type": "call_js", "code": "window.posTwin.checkout();", "wait_before": 1.2 },
                { "type": "clear_spotlight", "wait_before": 0.6 },
                { "type": "spotlight", "selector": "#receipt-modal > div", "scale": 1.08, "wait_before": 0.8 },
                { "type": "call_js", "code": "window.posTwin.toggleThermalQr();", "wait_before": 1.2 },
                { "type": "clear_spotlight", "wait_before": 0.8 },
                { "type": "call_js", "code": "window.posTwin.closeReceipt();", "wait_before": 0.6 },
                { "type": "spotlight", "selector": "#btn-past-bills", "scale": 1.25, "wait_before": 0.8 },
                { "type": "call_js", "code": "window.posTwin.openPastBills();", "wait_before": 1.0 },
                { "type": "cursor_move", "x": 215, "y": 300, "wait_before": 2.0 },
                { "type": "clear_spotlight", "wait_before": 0.8 }
            ]
        },

        # Scene 8: Customer CRM, Reviews & Enquiries
        {
            "id": "08_customer_crm_reviews_enquiries",
            "step": 8,
            "title": "Customer CRM, Reviews & Member Enquiries",
            "subtitle": "Track verified cardholder ratings, visit frequency & queries",
            "badge": "⭐ Verified CRM & Member Retention",
            "component": "merchant/VirtualCustomerCrm.html",
            "narration": "Nurture customer loyalty with the built-in CRM. Track verified member check-in frequency, review 5-star customer ratings, and respond directly to customer inquiries to maximize repeat visits and long-term retention.",
            "actions": [
                { "type": "spotlight", "selector": "#crm-rating-summary", "scale": 1.1, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 215, "y": 140, "wait_before": 1.5 },
                { "type": "clear_spotlight", "wait_before": 0.6 },
                { "type": "spotlight", "selector": "#review-card-1", "scale": 1.08, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 215, "y": 280, "wait_before": 2.0 },
                { "type": "clear_spotlight", "wait_before": 0.8 }
            ]
        },

        # Scene 9: Business Boost Subscription Tiers & Upgrades
        {
            "id": "09_business_boost_subscriptions",
            "step": 9,
            "title": "Business Boost Growth Plans & Upgrades",
            "subtitle": "Unlock multi-branch expansion, promotional reels & priority search",
            "badge": "💎 Business Boost Scaling Tiers",
            "component": "merchant/VirtualSubscriptions.html",
            "narration": "Scale your enterprise with Business Boost subscription tiers. Upgrading from Starter to Pro, Elite, or The Brand unlocks up to twenty-five store branches, professional promotional video reel production, managed social media advertising campaigns, and top priority search ranking.",
            "actions": [
                { "type": "spotlight", "selector": "#active-tier-card", "scale": 1.08, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 215, "y": 180, "wait_before": 1.5 },
                { "type": "clear_spotlight", "wait_before": 0.6 },
                { "type": "scroll", "dy": 250, "wait_before": 0.8 },
                { "type": "spotlight", "selector": "#tier-pro-card", "scale": 1.12, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 215, "y": 360, "wait_before": 2.2 },
                { "type": "clear_spotlight", "wait_before": 1.0 }
            ]
        },

        # Scene 10: Help Center & Dedicated Support
        {
            "id": "10_help_center_support",
            "step": 10,
            "title": "Merchant Help Desk & Priority Support",
            "subtitle": "24/7 WhatsApp merchant hotline, ticketing & printer guides",
            "badge": "🎧 24/7 Dedicated Merchant Support",
            "component": "merchant/VirtualHelpCenter.html",
            "narration": "Get round-the-clock merchant support whenever you need it. Connect directly with your dedicated account manager via our 24/7 WhatsApp hotline, submit categorized technical tickets, or explore step-by-step guides for Bluetooth thermal printer setup.",
            "actions": [
                { "type": "spotlight", "selector": "#help-hotline-card", "scale": 1.12, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 215, "y": 180, "wait_before": 1.8 },
                { "type": "clear_spotlight", "wait_before": 0.6 },
                { "type": "spotlight", "selector": "#help-ticket-card", "scale": 1.08, "wait_before": 0.8 },
                { "type": "cursor_move", "x": 215, "y": 380, "wait_before": 2.0 },
                { "type": "clear_spotlight", "wait_before": 1.0 }
            ]
        }
    ]
}

async def main():
    engine = StudioEngine(EXHAUSTIVE_10_SCREEN_SCENARIO, voice="en-US-BrianMultilingualNeural")
    await engine.render_all()

if __name__ == "__main__":
    asyncio.run(main())
