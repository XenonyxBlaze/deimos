import asyncio
import os
import sys

sys.path.insert(0, r"c:\Users\ServeSmile IT\Projects\servenext\WEB\studio-engine\src\core")
from studio_runner import StudioEngine

MASTER_SHOWCASE_SCENARIO = {
    "id": "servesmile_studio_master_showcase",
    "title": "ServeSmile Platform Master Showcase (Virtual Twin Framework)",
    "scenes": [
        {
            "id": "01_virtual_auth",
            "step": 1,
            "title": "Multi-Language & Secure Access",
            "subtitle": "Language switcher, masked credentials & partner referrals",
            "badge": "🌐 Multi-Language & Bank-Grade Security",
            "component": "merchant/VirtualAuth.html",
            "narration": "ServeSmile Merchant provides full multi-language flexibility, allowing store owners to switch instantly between English, Hindi, and regional dialects. Access your terminal with dual-channel verification and privacy-masked passwords.",
            "actions": [
                { "type": "cursor_move", "x": 215, "y": 140, "wait_before": 0.5 },
                { "type": "tap", "x": 215, "y": 360, "selector": "#login-id", "wait_before": 0.8 },
                { "type": "type", "selector": "#login-id", "text": "aarav@servesmile.com", "wait_before": 0.3 },
                { "type": "tap", "x": 215, "y": 420, "selector": "#login-pw", "wait_before": 0.6 },
                { "type": "type", "selector": "#login-pw", "text": "SecurePass2026!", "wait_before": 0.3 },
                { "type": "tap", "x": 215, "y": 500, "wait_before": 1.0 }
            ]
        },
        {
            "id": "02_virtual_store_wizard",
            "step": 2,
            "title": "5-Step Storefront Setup & GPS",
            "subtitle": "1-Tap GPS detection, 20% discount presets & declarations",
            "badge": "📍 1-Tap Geolocation & Branding",
            "component": "merchant/VirtualStoreWizard.html",
            "narration": "Launch your business in minutes with the 5-step onboarding wizard. Pinpoint your storefront using instant 1-tap GPS auto-fill, set your 20% member savings offer, configure daily operating hours, and declare your official GSTIN and FSSAI licenses.",
            "actions": [
                { "type": "cursor_move", "x": 215, "y": 280, "wait_before": 0.5 },
                { "type": "scroll", "dy": 250, "wait_before": 0.8 },
                { "type": "tap", "x": 215, "y": 370, "selector": "#btn-gps", "wait_before": 1.0 },
                { "type": "scroll", "dy": 350, "wait_before": 1.2 },
                { "type": "tap", "x": 215, "y": 520, "selector": "#btn-launch", "wait_before": 1.5 }
            ]
        },
        {
            "id": "03_virtual_kyc_hub",
            "step": 3,
            "title": "Bank-Grade KYC & Verified Badges",
            "subtitle": "3-Stage regulatory audit with AES-256 data protection",
            "badge": "🛡️ Verified Merchant Compliance",
            "component": "merchant/VirtualKycHub.html",
            "narration": "Establish trust with bank-grade KYC compliance. Complete 3-stage validation for GSTIN certificates, business PAN, and biometric Aadhaar. Once approved, your store earns the official Verified Partner badge across the network.",
            "actions": [
                { "type": "cursor_move", "x": 215, "y": 220, "wait_before": 0.6 },
                { "type": "scroll", "dy": 200, "wait_before": 1.2 }
            ]
        },
        {
            "id": "04_virtual_pos_terminal",
            "step": 4,
            "title": "0ms Touch POS, 20% Member Validation & Thermal QR",
            "subtitle": "Instant category filtering, cart steppers & paperless receipts",
            "badge": "⚡ 0ms Touch Billing & Member Validation",
            "component": "merchant/VirtualPosRegister.html",
            "narration": "Experience lightning-fast point of sale billing. Cashiers can filter catalog categories, tap dishes into the cart, adjust quantity steppers, and scan member passes to apply 20% savings with celebratory banners before generating paperless thermal QR receipts.",
            "actions": [
                { "type": "tap", "x": 120, "y": 140, "selector": ".cat-chip:nth-child(2)", "wait_before": 0.5 },
                { "type": "call_js", "code": "window.posTwin.addItem('dish-1');", "wait_before": 0.8 },
                { "type": "call_js", "code": "window.posTwin.stepQuantity('dish-1', 1);", "wait_before": 0.6 },
                { "type": "call_js", "code": "window.posTwin.addItem('dish-2');", "wait_before": 0.7 },
                { "type": "call_js", "code": "window.posTwin.addItem('dish-3');", "wait_before": 0.6 },
                { "type": "call_js", "code": "window.posTwin.verifyMember('Aarav Rajput', '@aarav_alqasr');", "wait_before": 1.2 },
                { "type": "scroll", "dy": 250, "wait_before": 1.0 },
                { "type": "call_js", "code": "window.posTwin.checkout();", "wait_before": 1.2 },
                { "type": "call_js", "code": "window.posTwin.toggleThermalQr();", "wait_before": 1.5 }
            ]
        },
        {
            "id": "05_virtual_subscriptions",
            "step": 5,
            "title": "Business Boost Growth Plans",
            "subtitle": "Multi-branch slots, promotional reels & priority ranking",
            "badge": "💎 Multi-Branch & Promo Growth Tiers",
            "component": "merchant/VirtualSubscriptions.html",
            "narration": "Accelerate your revenue with Business Boost plans. Unlock up to twenty-five store branches, receive monthly promotional video reels, run managed ad campaigns, and command top search rankings across the customer network.",
            "actions": [
                { "type": "cursor_move", "x": 215, "y": 240, "wait_before": 0.6 },
                { "type": "scroll", "dy": 300, "wait_before": 1.5 }
            ]
        },
        {
            "id": "06_virtual_customer_wallet",
            "step": 6,
            "title": "Customer 3D Holographic Pass & QR Magazine",
            "subtitle": "Instant 20% discount card & rolling token magazine",
            "badge": "✨ Customer Pass & Dynamic QR",
            "component": "customer/VirtualCustomerWallet.html",
            "narration": "ServeSmile customers enjoy a unified holographic membership pass. Dynamic QR tokens rotate automatically for zero-trust offline verification, unlocking instant 20% savings across nearby partner restaurants and retailers.",
            "actions": [
                { "type": "cursor_move", "x": 215, "y": 220, "wait_before": 0.6 },
                { "type": "scroll", "dy": 200, "wait_before": 1.5 }
            ]
        }
    ]
}

async def main():
    engine = StudioEngine(MASTER_SHOWCASE_SCENARIO)
    await engine.render_all()

if __name__ == "__main__":
    asyncio.run(main())
