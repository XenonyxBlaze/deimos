import asyncio
import os
import sys
import json
import subprocess
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg
import edge_tts
from playwright.async_api import async_playwright

BASE_DIR = r"c:\Users\ServeSmile IT\Projects\servenext\WEB\studio-engine"
COMPONENTS_DIR = os.path.join(BASE_DIR, "src", "components")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
TEMP_DIR = os.path.join(BASE_DIR, "temp_render")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(ASSETS_DIR, exist_ok=True)

FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()

WIDTH = 1920
HEIGHT = 1080
FPS = 30

CURSOR_INJECTION_JS = """
(() => {
  if (document.getElementById('studio-cursor')) return;
  const cur = document.createElement('div');
  cur.id = 'studio-cursor';
  cur.style.position = 'fixed';
  cur.style.width = '24px';
  cur.style.height = '24px';
  cur.style.borderRadius = '50%';
  cur.style.backgroundColor = 'rgba(249, 115, 22, 0.75)';
  cur.style.border = '2px solid rgba(255, 255, 255, 0.95)';
  cur.style.boxShadow = '0 0 18px rgba(249, 115, 22, 0.9), 0 0 32px rgba(245, 158, 11, 0.6)';
  cur.style.pointerEvents = 'none';
  cur.style.zIndex = '9999999';
  cur.style.transition = 'transform 0.28s cubic-bezier(0.25, 1, 0.5, 1), background-color 0.15s ease';
  cur.style.transform = 'translate(-50px, -50px)';
  document.body.appendChild(cur);

  window.moveCursor = (x, y) => {
    cur.style.transform = `translate(${x}px, ${y}px)`;
  };

  window.clickCursor = (x, y) => {
    cur.style.transform = `translate(${x}px, ${y}px) scale(0.8)`;
    cur.style.backgroundColor = 'rgba(234, 88, 12, 0.95)';
    setTimeout(() => {
      cur.style.transform = `translate(${x}px, ${y}px) scale(1.0)`;
      cur.style.backgroundColor = 'rgba(249, 115, 22, 0.75)';
    }, 200);
  };

  let activeSpotlightEl = null;
  let backdropEl = null;

  window.spotlight = (selector, scale = 1.15) => {
    window.clearSpotlight();
    let el = null;
    try {
      el = document.querySelector(selector);
    } catch(e) {}
    
    if (!el && selector.includes(':has-text(')) {
      const match = selector.match(/:has-text\(['"](.+?)['"]\)/);
      if (match && match[1]) {
        const tag = selector.split(':')[0] || '*';
        el = Array.from(document.querySelectorAll(tag)).find(n => n.textContent.includes(match[1]));
      }
    }
    if (!el) return;

    backdropEl = document.createElement('div');
    backdropEl.id = 'studio-spotlight-backdrop';
    backdropEl.style.position = 'fixed';
    backdropEl.style.inset = '0';
    backdropEl.style.backgroundColor = 'rgba(0, 0, 0, 0.35)';
    backdropEl.style.backdropFilter = 'blur(2px)';
    backdropEl.style.zIndex = '999990';
    backdropEl.style.opacity = '0';
    backdropEl.style.transition = 'opacity 0.35s ease';
    backdropEl.style.pointerEvents = 'none';
    document.body.appendChild(backdropEl);

    setTimeout(() => { if (backdropEl) backdropEl.style.opacity = '1'; }, 10);

    activeSpotlightEl = el;
    el.setAttribute('data-orig-z', el.style.zIndex || '');
    el.setAttribute('data-orig-transform', el.style.transform || '');
    el.setAttribute('data-orig-shadow', el.style.boxShadow || '');
    el.setAttribute('data-orig-trans', el.style.transition || '');

    el.style.position = (getComputedStyle(el).position === 'static') ? 'relative' : el.style.position;
    el.style.zIndex = '999995';
    el.style.transition = 'transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s ease';
    el.style.transform = `scale(${scale})`;
    el.style.boxShadow = '0 0 35px rgba(249, 115, 22, 0.8), 0 0 0 2px rgba(249, 115, 22, 0.95)';
  };

  window.clearSpotlight = () => {
    if (backdropEl) {
      backdropEl.style.opacity = '0';
      const b = backdropEl;
      setTimeout(() => { if (b && b.parentNode) b.parentNode.removeChild(b); }, 350);
      backdropEl = null;
    }
    if (activeSpotlightEl) {
      activeSpotlightEl.style.transform = activeSpotlightEl.getAttribute('data-orig-transform') || '';
      activeSpotlightEl.style.boxShadow = activeSpotlightEl.getAttribute('data-orig-shadow') || '';
      activeSpotlightEl.style.zIndex = activeSpotlightEl.getAttribute('data-orig-z') || '';
      activeSpotlightEl.style.transition = activeSpotlightEl.getAttribute('data-orig-trans') || '';
      activeSpotlightEl = null;
    }
  };
})();
"""

def create_gradient_background(w, h):
    bg = np.zeros((h, w, 3), dtype=np.uint8)
    bg[:, :] = (12, 10, 10)
    cv2.circle(bg, (260, 240), 500, (18, 42, 90), -1)
    cv2.circle(bg, (1620, 820), 580, (15, 68, 155), -1)
    cv2.circle(bg, (960, 540), 320, (12, 28, 55), -1)
    return cv2.GaussianBlur(bg, (201, 201), 0)

def draw_phone_frame(screen_img):
    sw, sh = 430, 932
    if screen_img.shape[1] != sw or screen_img.shape[0] != sh:
        screen_img = cv2.resize(screen_img, (sw, sh), interpolation=cv2.INTER_LANCZOS4)
        
    bezel_w = 466
    bezel_h = 968
    
    frame = Image.new("RGBA", (bezel_w + 40, bezel_h + 40), (0, 0, 0, 0))
    draw = ImageDraw.Draw(frame)
    
    # Ambient Drop Shadows
    draw.rounded_rectangle([12, 12, bezel_w + 28, bezel_h + 28], radius=52, fill=(0, 0, 0, 160))
    draw.rounded_rectangle([16, 16, bezel_w + 24, bezel_h + 24], radius=50, fill=(0, 0, 0, 200))
    
    # Titanium Bezel Rim
    draw.rounded_rectangle([20, 20, bezel_w + 20, bezel_h + 20], radius=48, fill=(32, 32, 36, 255), outline=(75, 75, 82, 255), width=2)
    draw.rounded_rectangle([26, 26, bezel_w + 14, bezel_h + 14], radius=42, fill=(10, 10, 12, 255))
    
    # Mask and paste screen
    screen_rgb = cv2.cvtColor(screen_img, cv2.COLOR_BGR2RGB)
    screen_pil = Image.fromarray(screen_rgb).convert("RGBA")
    mask = Image.new("L", (sw, sh), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle([0, 0, sw, sh], radius=32, fill=255)
    frame.paste(screen_pil, (38, 38), mask)
    
    # Sleek Micro Dynamic Island (higher up in bezel so it NEVER overlaps screen headers!)
    draw.rounded_rectangle([bezel_w//2 - 30 + 20, 24, bezel_w//2 + 30 + 20, 36], radius=6, fill=(0, 0, 0, 255))
    draw.ellipse([bezel_w//2 + 15 + 20, 27, bezel_w//2 + 23 + 20, 34], fill=(18, 24, 42, 255))
    
    # Home Indicator Bar
    draw.rounded_rectangle([bezel_w//2 - 50 + 20, bezel_h - 2 + 20, bezel_w//2 + 50 + 20, bezel_h + 2 + 20], radius=2, fill=(210, 210, 215, 140))
    
    return cv2.cvtColor(np.array(frame), cv2.COLOR_RGBA2BGRA)

class StudioEngine:
    def __init__(self, scenario_config, voice="en-US-BrianMultilingualNeural"):
        self.scenario = scenario_config
        self.voice = voice
        self.output_file = os.path.join(OUTPUT_DIR, f"{self.scenario['id']}.mp4")

    async def synthesize_voiceover(self, scene_id, text):
        wav_path = os.path.join(ASSETS_DIR, f"{scene_id}.wav")
        mp3_path = os.path.join(ASSETS_DIR, f"{scene_id}.mp3")
        
        communicate = edge_tts.Communicate(text, self.voice, rate="+1%", pitch="+0Hz")
        await communicate.save(mp3_path)
        
        subprocess.run([
            FFMPEG_EXE, "-y", "-i", mp3_path,
            "-ac", "2", "-ar", "44100", wav_path
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        
        res = subprocess.run([FFMPEG_EXE, "-i", wav_path], stderr=subprocess.PIPE, text=True)
        dur = 8.0
        for line in res.stderr.splitlines():
            if "Duration:" in line:
                dur_str = line.split("Duration:")[1].split(",")[0].strip()
                h, m, s = dur_str.split(":")
                dur = float(h)*3600 + float(m)*60 + float(s)
                break
        return wav_path, round(dur, 2)

    async def record_virtual_scene(self, scene, target_duration):
        scene_id = scene["id"]
        component_file = os.path.join(COMPONENTS_DIR, scene["component"])
        file_url = f"file:///{component_file.replace(chr(92), '/')}"
        
        scene_dir = os.path.join(TEMP_DIR, scene_id)
        os.makedirs(scene_dir, exist_ok=True)
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                viewport={"width": 430, "height": 932},
                device_scale_factor=2,
                record_video_dir=scene_dir,
                record_video_size={"width": 430, "height": 932},
                is_mobile=True,
                has_touch=True
            )
            page = await context.new_page()
            await page.goto(file_url, wait_until="networkidle")
            await page.evaluate(CURSOR_INJECTION_JS)
            await page.wait_for_timeout(600)
            
            # Execute scripted actions
            actions = scene.get("actions", [])
            for act in actions:
                act_type = act.get("type")
                await page.wait_for_timeout(int(act.get("wait_before", 0.6) * 1000))
                
                if act_type == "spotlight":
                    sel = act.get("selector")
                    scale = act.get("scale", 1.18)
                    await page.evaluate("(args) => window.spotlight(args.sel, args.scale)", {"sel": sel, "scale": scale})
                elif act_type == "clear_spotlight":
                    await page.evaluate("() => window.clearSpotlight()")
                elif act_type == "cursor_move":
                    x, y = act.get("x", 215), act.get("y", 400)
                    await page.evaluate("(args) => window.moveCursor(args.x, args.y)", {"x": x, "y": y})
                elif act_type == "tap":
                    x, y = act.get("x", 215), act.get("y", 400)
                    await page.evaluate("(args) => { window.moveCursor(args.x, args.y); window.clickCursor(args.x, args.y); }", {"x": x, "y": y})
                    selector = act.get("selector")
                    if selector:
                        el = await page.query_selector(selector)
                        if el: await el.click()
                elif act_type == "type":
                    selector = act.get("selector")
                    text = act.get("text", "")
                    if selector:
                        el = await page.query_selector(selector)
                        if el: await el.type(text, delay=80)
                elif act_type == "call_js":
                    js_code = act.get("code", "")
                    if js_code:
                        await page.evaluate(js_code)
                elif act_type == "scroll":
                    dy = act.get("dy", 200)
                    await page.evaluate(f"window.scrollBy({{ top: {dy}, behavior: 'smooth' }});")

            await page.wait_for_timeout(1500)
            await page.close()
            await context.close()
            await browser.close()
            
        vid_files = [f for f in os.listdir(scene_dir) if f.endswith(".webm")]
        if vid_files:
            raw_vid_path = os.path.join(scene_dir, vid_files[0])
            mp4_vid_path = os.path.join(TEMP_DIR, f"{scene_id}_raw.mp4")
            subprocess.run([
                FFMPEG_EXE, "-y", "-i", raw_vid_path,
                "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
                "-r", str(FPS),
                mp4_vid_path
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            return mp4_vid_path
        return None

    def render_composited_clip(self, scene, raw_vid_path, audio_file, target_duration, out_clip_path):
        scene_id = scene["id"]
        step_num = scene.get("step", 1)
        total_steps = len(self.scenario["scenes"])
        title = scene["title"]
        subtitle = scene["subtitle"]
        badge = scene["badge"]
        narration = scene["narration"]
        
        cap = cv2.VideoCapture(raw_vid_path)
        raw_frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        if raw_frame_count == 0: raw_frame_count = 1
        
        total_frames = int(target_duration * FPS)
        bg_template = create_gradient_background(WIDTH, HEIGHT)
        temp_avi = os.path.join(TEMP_DIR, f"{scene_id}_comp.avi")
        fourcc = cv2.VideoWriter_fourcc(*"MJPG")
        out_writer = cv2.VideoWriter(temp_avi, fourcc, FPS, (WIDTH, HEIGHT))
        
        try:
            font_title = ImageFont.truetype("arialbd.ttf", 40)
            font_sub = ImageFont.truetype("arial.ttf", 22)
            font_badge = ImageFont.truetype("arialbd.ttf", 21)
            font_narr = ImageFont.truetype("arial.ttf", 21)
            font_step = ImageFont.truetype("arialbd.ttf", 16)
        except:
            font_title = ImageFont.load_default()
            font_sub = font_title
            font_badge = font_title
            font_narr = font_title
            font_step = font_title
            
        layout_mode = scene.get("layout", "split")
        benefit = scene.get("benefit", "⚡ Instant 0ms Checkout • Guaranteed Revenue Growth")
        
        for frame_idx in range(total_frames):
            t = frame_idx / float(total_frames)
            target_raw_idx = int(t * raw_frame_count)
            cap.set(cv2.CAP_PROP_POS_FRAMES, min(target_raw_idx, raw_frame_count - 1))
            ret, frame = cap.read()
            if ret: last_frame = frame
            else: frame = last_frame
            
            framed_phone = draw_phone_frame(frame)
            float_offset_y = int(np.sin(t * np.pi * 2) * 5)
            
            canvas = bg_template.copy()
            ph_h, ph_w = framed_phone.shape[:2]
            
            if layout_mode == "center":
                phone_x = int((WIDTH - ph_w) / 2)
                cur_y = 56 + float_offset_y
            else:
                # Dynamic smooth camera motion (gliding gently during demonstration)
                phone_x = int(1170 - 25 * np.sin(t * np.pi))
                cur_y = 56 + float_offset_y
            
            roi = canvas[cur_y:cur_y+ph_h, phone_x:phone_x+ph_w]
            alpha = framed_phone[:, :, 3] / 255.0
            for c in range(3):
                roi[:, :, c] = (alpha * framed_phone[:, :, c] + (1.0 - alpha) * roi[:, :, c]).astype(np.uint8)
            canvas[cur_y:cur_y+ph_h, phone_x:phone_x+ph_w] = roi
            
            pil_img = Image.fromarray(cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB))
            draw = ImageDraw.Draw(pil_img)
            
            if layout_mode == "center":
                # Centered Public Showcase Overlay
                draw.rounded_rectangle([140, 120, 580, 240], radius=24, fill=(20, 20, 24, 230), outline=(249, 115, 22, 180), width=2)
                draw.text((165, 145), "PUBLIC DISCOVERY PLATFORM", font=font_step, fill=(249, 115, 22))
                draw.text((165, 175), "Live On ServeSmile App", font=font_title, fill=(255, 255, 255))
                
                draw.rounded_rectangle([1340, 120, 1780, 240], radius=24, fill=(20, 20, 24, 230), outline=(16, 185, 129, 180), width=2)
                draw.text((1365, 145), "FOOT TRAFFIC & CUSTOMERS", font=font_step, fill=(52, 211, 153))
                draw.text((1365, 175), "1.2k+ Active Members", font=font_title, fill=(255, 255, 255))
                
                # Bottom Voiceover Card
                draw.rounded_rectangle([320, 840, 1600, 960], radius=24, fill=(18, 18, 22, 240), outline=(55, 55, 65, 220), width=1)
                draw.text((360, 860), "MERCHANT ADVANTAGE", font=font_step, fill=(249, 115, 22))
                draw.text((360, 895), narration, font=font_narr, fill=(245, 245, 250))
            else:
                # Standard Split Layout with Left Motion Graphic Storyboard
                # Step & Badge
                draw.rounded_rectangle([120, 110, 260, 144], radius=16, fill=(249, 115, 22, 45), outline=(249, 115, 22, 190), width=1)
                draw.text((138, 118), f"STEP {step_num:02d} / {total_steps:02d}", font=font_step, fill=(255, 180, 90))
                
                draw.rounded_rectangle([120, 160, 780, 208], radius=20, fill=(30, 30, 36, 230), outline=(245, 158, 11, 150), width=1)
                draw.text((140, 172), badge, font=font_badge, fill=(255, 205, 110))
                
                # Title & Subtitle
                title_words = title.split(" ")
                if len(title) > 28:
                    t_line1 = " ".join(title_words[:4])
                    t_line2 = " ".join(title_words[4:])
                    draw.text((120, 230), t_line1, font=font_title, fill=(255, 255, 255))
                    draw.text((120, 280), t_line2, font=font_title, fill=(255, 255, 255))
                    sub_y = 340
                else:
                    draw.text((120, 230), title, font=font_title, fill=(255, 255, 255))
                    sub_y = 290
                    
                draw.text((120, sub_y), subtitle, font=font_sub, fill=(200, 200, 210))
                
                # Key Performance Benefit Pill
                draw.rounded_rectangle([120, sub_y + 40, 780, sub_y + 90], radius=18, fill=(16, 185, 129, 25), outline=(16, 185, 129, 160), width=1)
                draw.text((140, sub_y + 54), benefit, font=font_step, fill=(52, 211, 153))
                
                # Progress Bar
                bar_w = 720
                draw.rounded_rectangle([120, 520, 120 + bar_w, 528], radius=4, fill=(45, 45, 52))
                fill_w = int(bar_w * t)
                if fill_w > 4:
                    draw.rounded_rectangle([120, 520, 120 + fill_w, 528], radius=4, fill=(249, 115, 22))
                    
                # Voiceover Card
                draw.rounded_rectangle([120, 720, 960, 910], radius=24, fill=(20, 20, 24, 230), outline=(55, 55, 65, 220), width=1)
                draw.text((150, 745), "MERCHANT DEMONSTRATION GUIDE", font=font_step, fill=(249, 115, 22))
                
                words = narration.split(" ")
                lines = []
                cur = []
                for w in words:
                    cur.append(w)
                    if len(" ".join(cur)) > 55:
                        lines.append(" ".join(cur))
                        cur = []
                if cur: lines.append(" ".join(cur))
                
                ny = 778
                for l in lines[:4]:
                    draw.text((150, ny), l, font=font_narr, fill=(240, 240, 245))
                    ny += 28
                    
                draw.text((120, 970), "ServeSmile Merchant OS  •  Empowering Retail & Dining Partners", font=font_sub, fill=(125, 125, 135))
                
            frame_bgr = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
            out_writer.write(frame_bgr)
            
        cap.release()
        out_writer.release()
        
        subprocess.run([
            FFMPEG_EXE, "-y",
            "-i", temp_avi,
            "-i", audio_file,
            "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k",
            "-shortest",
            out_clip_path
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        
        if os.path.exists(temp_avi): os.remove(temp_avi)

    async def render_all(self):
        scenes = self.scenario["scenes"]
        print("\n=======================================================")
        print(f"[Studio] Starting Exhaustive Master Render: {self.scenario['title']}")
        print(f"Total Scenes: {len(scenes)} | Voice: {self.voice}")
        print("=======================================================\n")
        
        rendered_clips = []
        for idx, sc in enumerate(scenes):
            sc_id = sc["id"]
            print(f"[{idx+1}/{len(scenes)}] Synthesizing audio: {sc_id}...")
            wav_path, audio_dur = await self.synthesize_voiceover(sc_id, sc["narration"])
            target_dur = round(audio_dur + 1.4, 2)
            
            print(f"[{idx+1}/{len(scenes)}] Executing spotlight UI actions: {sc_id} ({target_dur}s)...")
            raw_vid = await self.record_virtual_scene(sc, target_dur)
            
            out_clip = os.path.join(TEMP_DIR, f"{sc_id}_final_clip.mp4")
            print(f"[{idx+1}/{len(scenes)}] Compositing 3D Titanium Phone Frame -> {out_clip}...")
            self.render_composited_clip(sc, raw_vid, wav_path, target_dur, out_clip)
            rendered_clips.append(out_clip)
            
        concat_list = os.path.join(TEMP_DIR, "master_concat.txt")
        with open(concat_list, "w", encoding="utf-8") as f:
            for c in rendered_clips:
                f.write(f"file '{c.replace(chr(92), '/')}'\n")
                
        print(f"\nMerging all scenes into Master Video: {self.output_file}...")
        subprocess.run([
            FFMPEG_EXE, "-y",
            "-f", "concat", "-safe", "0",
            "-i", concat_list,
            "-c", "copy",
            self.output_file
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        
        print("\n=======================================================")
        print(f"[Studio] EXHAUSTIVE DEMO RENDER COMPLETE: {self.output_file}")
        print("=======================================================\n")
        return self.output_file
