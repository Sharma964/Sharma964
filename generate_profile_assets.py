"""
generate_profile_assets.py
==========================
Generates the exact viral Cyberpunk animated GitHub profile setup,
customized 100% comprehensively for Sonu Sharma (GitHub: Sharma964):
1. github-contribution-animation.svg (850x165): 53x7 calendar with diagonal wave sweep, specular glints, and neon glow.
2. terminal-card.svg (840x875): macOS terminal with circular ASCII portrait of Sonu from avatar.png, row-by-row reveal, sweeping cursor, and whoami footer.
3. info-card.svg (480x495): Neofetch-style terminal info card reflecting Sonu's Computer Engineering, AI/ML, Full-Stack, and project highlights.
4. README.md: Full comprehensive portfolio and GitHub profile integration.
"""

import os
import sys
import math
import random
import io
import requests

try:
    from PIL import Image, ImageEnhance  # type: ignore
except ImportError:
    Image = None
    ImageEnhance = None

GITHUB_USERNAME = "Sharma964"
FULL_NAME = "Sonu Sharma"
AVATAR_URL = f"https://github.com/{GITHUB_USERNAME}.png"
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))


# -------------------------------------------------------------------------
# 1. GENERATE github-contribution-animation.svg
# -------------------------------------------------------------------------
def generate_contribution_svg():
    width = 850
    height = 165
    cols = 53
    rows = 7

    colors = {
        0: "#161b22",
        1: "#0e4429",
        2: "#006d32",
        3: "#26a641",
        4: "#39d353"
    }
    flash_colors = {
        0: "#30363d",
        1: "#57ffb0",
        2: "#57ffb0",
        3: "#8dffcc",
        4: "#b5ffd9"
    }

    random.seed(1337)
    weights = [0.42, 0.22, 0.18, 0.12, 0.06]
    grid = []
    for c in range(cols):
        col_lvls = [random.choices([0, 1, 2, 3, 4], weights=weights)[0] for _ in range(rows)]
        grid.append(col_lvls)

    svg = []
    svg.append(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<defs>
<filter id="cellglow" x="-70%" y="-70%" width="240%" height="240%">
  <feGaussianBlur stdDeviation="2" result="blur"/>
  <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
</filter>
</defs>
<rect width="{width}" height="{height}" rx="16" fill="#0d1117" stroke="#30363d" stroke-width="1"/>
<text x="34" y="18" fill="#8b949e" font-size="10" font-family="system-ui,sans-serif">Jan</text>
<text x="90" y="18" fill="#8b949e" font-size="10" font-family="system-ui,sans-serif">Feb</text>
<text x="160" y="18" fill="#8b949e" font-size="10" font-family="system-ui,sans-serif">Mar</text>
<text x="216" y="18" fill="#8b949e" font-size="10" font-family="system-ui,sans-serif">Apr</text>
<text x="286" y="18" fill="#8b949e" font-size="10" font-family="system-ui,sans-serif">May</text>
<text x="342" y="18" fill="#8b949e" font-size="10" font-family="system-ui,sans-serif">Jun</text>
<text x="398" y="18" fill="#8b949e" font-size="10" font-family="system-ui,sans-serif">Jul</text>
<text x="468" y="18" fill="#8b949e" font-size="10" font-family="system-ui,sans-serif">Aug</text>
<text x="524" y="18" fill="#8b949e" font-size="10" font-family="system-ui,sans-serif">Sep</text>
<text x="594" y="18" fill="#8b949e" font-size="10" font-family="system-ui,sans-serif">Oct</text>
<text x="650" y="18" fill="#8b949e" font-size="10" font-family="system-ui,sans-serif">Nov</text>
<text x="720" y="18" fill="#8b949e" font-size="10" font-family="system-ui,sans-serif">Dec</text>
<text x="8" y="38" fill="#8b949e" font-size="9" font-family="system-ui,sans-serif">Mon</text>
<text x="8" y="66" fill="#8b949e" font-size="9" font-family="system-ui,sans-serif">Wed</text>
<text x="8" y="94" fill="#8b949e" font-size="9" font-family="system-ui,sans-serif">Fri</text>''')

    start_x = 34
    start_y = 28
    cell_pitch_x = 15
    cell_pitch_y = 14
    max_d = (cols - 1) + (rows - 1)

    for c in range(cols):
        for r in range(rows):
            lvl = grid[c][r]
            x = start_x + (c * cell_pitch_x)
            y = start_y + (r * cell_pitch_y)
            color = colors[lvl]
            flash = flash_colors[lvl]
            d = c + (6 - r)
            t1 = round((d / float(max_d)) * 0.40, 4)
            t2 = round(t1 + 0.0120, 4)
            t3 = round(t1 + 0.0500, 4)

            filter_attr = ' filter="url(#cellglow)"' if lvl >= 3 else ''

            if lvl == 0:
                svg.append(f'<rect id="s{c}_{r}" x="{x}" y="{y}" width="11" height="11" rx="2" fill="{color}" opacity="0">')
                svg.append(f'<animate attributeName="opacity" values="0;0;1;1" keyTimes="0;{t1:.4f};{t2:.4f};1" dur="7.0s" repeatCount="indefinite"/>')
                svg.append('</rect>')
            else:
                svg.append(f'<rect id="s{c}_{r}" x="{x}" y="{y}" width="11" height="11" rx="2" fill="{color}" opacity="0"{filter_attr}>')
                svg.append(f'<animate attributeName="opacity" values="0;0;1;1" keyTimes="0;{t1:.4f};{t2:.4f};1" dur="7.0s" repeatCount="indefinite"/>')
                svg.append(f'<animate attributeName="fill" values="{color};{color};{flash};{color}" keyTimes="0;{t1:.4f};{t2:.4f};{t3:.4f}" dur="7.0s" repeatCount="indefinite" calcMode="spline" keySplines="0 0 1 1;0.1 0 0.2 1;0.4 0 0.6 1"/>')
                svg.append('</rect>')
                svg.append(f'<rect x="{x+2}" y="{y+2}" width="4" height="2" rx="1" fill="white" opacity="0" pointer-events="none">')
                svg.append(f'<animate attributeName="opacity" values="0;0;0.55;0" keyTimes="0;{t1:.4f};{t2:.4f};{t3:.4f}" dur="7.0s" repeatCount="indefinite" calcMode="spline" keySplines="0 0 1 1;0 0 0.3 1;0.5 0 1 1"/>')
                svg.append('</rect>')

    svg.append('</svg>')
    output_path = os.path.join(OUTPUT_DIR, "github-contribution-animation.svg")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Generated: {output_path}")


# -------------------------------------------------------------------------
# 2. GENERATE terminal-card.svg
# -------------------------------------------------------------------------
def generate_terminal_card_svg():
    width = 840
    height = 875
    W = 100
    H = 53

    ascii_rows = []
    local_avatar = None
    force_download = os.environ.get("DOWNLOAD_AVATAR") == "1" or "--refresh-avatar" in sys.argv

    for cand in ["avatar.png", "avatar.jpg", "profile.jpg", "photo.jpg"]:
        cand_p = os.path.join(OUTPUT_DIR, cand)
        if os.path.exists(cand_p):
            local_avatar = cand_p
            break

    try:
        img = None
        if force_download or not local_avatar:
            if Image is not None:
                res = requests.get(AVATAR_URL, timeout=10)
                if res.status_code == 200:
                    img = Image.open(io.BytesIO(res.content)).convert("L")
                    # Save downloaded avatar locally
                    save_path = os.path.join(OUTPUT_DIR, "avatar.png")
                    with open(save_path, "wb") as f:
                        f.write(res.content)
                    print(f"Downloaded fresh avatar from {AVATAR_URL}")
        elif local_avatar and Image is not None:
            img = Image.open(local_avatar).convert("L")

        if img is not None:
            img = ImageEnhance.Contrast(img).enhance(1.8)
            img = img.resize((W, H), Image.Resampling.LANCZOS)
            chars = " .:-=+*sS%#@"

            for y in range(H):
                row = []
                ny = (y - (H / 2.0)) / (H / 2.0 * 0.94)
                for x in range(W):
                    nx = (x - (W / 2.0)) / (W / 2.0 * 0.94)
                    dist = math.sqrt(nx * nx + ny * ny)
                    if dist > 1.04:
                        row.append('#')
                    elif dist > 0.98:
                        row.append('@')
                    else:
                        val = img.getpixel((x, y))
                        char_idx = min(int(val / 256.0 * len(chars)), len(chars) - 1)
                        row.append(chars[char_idx])
                row_str = "".join(row).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                ascii_rows.append(row_str)
    except Exception as e:
        print(f"Notice during image conversion: {e}")

    if len(ascii_rows) < H:
        ascii_rows = []
        for y in range(H):
            row = []
            ny = (y - (H / 2.0)) / (H / 2.0 * 0.94)
            for x in range(W):
                nx = (x - (W / 2.0)) / (W / 2.0 * 0.94)
                dist = math.sqrt(nx * nx + ny * ny)
                if dist > 1.04:
                    row.append('#')
                elif dist > 0.98:
                    row.append('@')
                else:
                    row.append('.' if (x + y) % 2 == 0 else ' ')
            ascii_rows.append("".join(row))

    svg = []
    svg.append(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#111722"/>
    <stop offset="1" stop-color="#0d1117"/>
  </linearGradient>
</defs>
<!-- card background -->
<rect width="{width}" height="{height}" rx="12" fill="url(#bg)"/>
<rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="12" fill="none" stroke="#30363d" stroke-width="1"/>
<!-- title bar separator -->
<line x1="0" y1="30" x2="{width}" y2="30" stroke="#30363d"/>
<!-- macOS window buttons -->
<circle cx="20" cy="15.0" r="5" fill="#ff5f56"/>
<circle cx="36" cy="15.0" r="5" fill="#ffbd2e"/>
<circle cx="52" cy="15.0" r="5" fill="#27c93f"/>
<!-- window title -->
<text x="420.0" y="19.0" fill="#7d8590" font-size="12" text-anchor="middle">{GITHUB_USERNAME}@github: ~$ ./portrait.sh</text>
<!-- ASCII art rows -->''')

    row_dur = 0.11
    row_height = 15.0
    start_y = 37.0

    for i, row_text in enumerate(ascii_rows):
        start_time = round(i * row_dur, 3)
        end_time = round((i + 1) * row_dur, 3)
        row_y = start_y + (i * row_height)
        text_y = row_y + 11.1
        cursor_y = row_y + 1.0

        svg.append(f'<clipPath id="r{i}"><rect x="20" y="{row_y:.1f}" height="15" width="0"><animate attributeName="width" from="0" to="800" begin="{start_time:.3f}s" dur="{row_dur}s" fill="freeze"/></rect></clipPath>')
        svg.append(f'<g clip-path="url(#r{i})"><text xml:space="preserve" x="20" y="{text_y:.1f}" fill="#c9d1d9" font-size="12.9" textLength="800" lengthAdjust="spacing">{row_text}</text></g>')
        svg.append(f'<rect y="{cursor_y:.1f}" width="8" height="13" fill="#c9d1d9" opacity="0"><animate attributeName="x" from="20" to="820" begin="{start_time:.3f}s" dur="{row_dur}s" fill="freeze"/><set attributeName="opacity" to="0.85" begin="{start_time:.3f}s"/><set attributeName="opacity" to="0" begin="{end_time:.3f}s"/></rect>')

    svg.append(f'''<!-- footer separator -->
<line x1="0" y1="832.0" x2="{width}" y2="832.0" stroke="#30363d"/>
<!-- whoami line -->
<text x="20" y="851.0" fill="#7d8590" font-size="13">{GITHUB_USERNAME}@github:~$ whoami <tspan fill="#c9d1d9">{FULL_NAME}</tspan></text>
<!-- blinking cursor -->
<rect x="270" y="838.0" width="8" height="14" fill="#c9d1d9">
  <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.51;1" dur="1s" repeatCount="indefinite"/>
</rect>
</svg>''')

    output_path = os.path.join(OUTPUT_DIR, "terminal-card.svg")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Generated: {output_path}")


# -------------------------------------------------------------------------
# 3. GENERATE info-card.svg (FOR SHARMA964)
# -------------------------------------------------------------------------
def generate_info_card_svg():
    width = 480
    height = 495

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
<defs>
  <linearGradient id="ibg" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#111722"/>
    <stop offset="1" stop-color="#0d1117"/>
  </linearGradient>
</defs>

<!-- card background -->
<rect width="{width}" height="{height}" rx="12" fill="url(#ibg)"/>
<rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="12" fill="none" stroke="#30363d"/>

<!-- title bar -->
<line x1="0" y1="30" x2="{width}" y2="30" stroke="#30363d"/>
<circle cx="20" cy="15.0" r="5" fill="#ff5f56"/>
<circle cx="36" cy="15.0" r="5" fill="#ffbd2e"/>
<circle cx="52" cy="15.0" r="5" fill="#27c93f"/>
<text x="240" y="19" fill="#7d8590" font-size="12" text-anchor="middle">{GITHUB_USERNAME}@github: ~$ neofetch</text>

<!-- ── ROW 0: identity header ── -->
<g opacity="0" transform="translate(0,5)">
  <text x="20" y="58" font-size="14" font-weight="700">
    <tspan fill="#3fb950">{GITHUB_USERNAME}</tspan>
    <tspan fill="#7d8590">@</tspan>
    <tspan fill="#22d3ee">github</tspan>
  </text>
  <line x1="160" y1="54" x2="460" y2="54" stroke="#30363d" stroke-opacity="0.8"/>
  <animate attributeName="opacity" from="0" to="1" begin="0.15s" dur="0.4s" fill="freeze"/>
  <animateTransform attributeName="transform" type="translate" from="0 5" to="0 0" begin="0.15s" dur="0.4s" fill="freeze" calcMode="spline" keySplines="0.2 0.8 0.2 1"/>
</g>

<!-- ── ROW 1: Role ── -->
<g opacity="0" transform="translate(0,5)">
  <text x="20" y="82" fill="#ffa657" font-size="12.5" font-weight="700">Role</text>
  <text x="100" y="82" fill="#c9d1d9" font-size="12.5">Computer Engineering Student</text>
  <animate attributeName="opacity" from="0" to="1" begin="0.22s" dur="0.4s" fill="freeze"/>
  <animateTransform attributeName="transform" type="translate" from="0 5" to="0 0" begin="0.22s" dur="0.4s" fill="freeze" calcMode="spline" keySplines="0.2 0.8 0.2 1"/>
</g>

<!-- ── ROW 2: Focus ── -->
<g opacity="0" transform="translate(0,5)">
  <text x="20" y="103" fill="#ffa657" font-size="12.5" font-weight="700">Focus</text>
  <text x="100" y="103" fill="#c9d1d9" font-size="12.5">AI/ML, Full-Stack Dev, Algorithms</text>
  <animate attributeName="opacity" from="0" to="1" begin="0.28s" dur="0.4s" fill="freeze"/>
  <animateTransform attributeName="transform" type="translate" from="0 5" to="0 0" begin="0.28s" dur="0.4s" fill="freeze" calcMode="spline" keySplines="0.2 0.8 0.2 1"/>
</g>

<!-- ── ROW 3: Portfolio ── -->
<g opacity="0" transform="translate(0,5)">
  <text x="20" y="124" fill="#ffa657" font-size="12.5" font-weight="700">Portfolio</text>
  <text x="100" y="124" fill="#58a6ff" font-size="12.5">sonusharma7.com.np</text>
  <animate attributeName="opacity" from="0" to="1" begin="0.34s" dur="0.4s" fill="freeze"/>
  <animateTransform attributeName="transform" type="translate" from="0 5" to="0 0" begin="0.34s" dur="0.4s" fill="freeze" calcMode="spline" keySplines="0.2 0.8 0.2 1"/>
</g>

<!-- ── ROW 4: Contact ── -->
<g opacity="0" transform="translate(0,5)">
  <text x="20" y="145" fill="#ffa657" font-size="12.5" font-weight="700">Email</text>
  <text x="100" y="145" fill="#c9d1d9" font-size="12.5">sonusharma.dev07@gmail.com</text>
  <animate attributeName="opacity" from="0" to="1" begin="0.40s" dur="0.4s" fill="freeze"/>
  <animateTransform attributeName="transform" type="translate" from="0 5" to="0 0" begin="0.40s" dur="0.4s" fill="freeze" calcMode="spline" keySplines="0.2 0.8 0.2 1"/>
</g>

<!-- ── SECTION: Stack ── -->
<g opacity="0" transform="translate(0,5)">
  <text x="20" y="174" fill="#58a6ff" font-size="12.5" font-weight="700">&#8212; Tech Stack</text>
  <line x1="110" y1="170" x2="460" y2="170" stroke="#30363d" stroke-opacity="0.8"/>
  <animate attributeName="opacity" from="0" to="1" begin="0.48s" dur="0.4s" fill="freeze"/>
  <animateTransform attributeName="transform" type="translate" from="0 5" to="0 0" begin="0.48s" dur="0.4s" fill="freeze" calcMode="spline" keySplines="0.2 0.8 0.2 1"/>
</g>

<!-- ── ROW: Languages ── -->
<g opacity="0" transform="translate(0,5)">
  <text x="20" y="196" fill="#ffa657" font-size="12.5" font-weight="700">Languages</text>
  <text x="100" y="196" fill="#c9d1d9" font-size="12.5">C, C++, Python, JavaScript, TypeScript</text>
  <animate attributeName="opacity" from="0" to="1" begin="0.54s" dur="0.4s" fill="freeze"/>
  <animateTransform attributeName="transform" type="translate" from="0 5" to="0 0" begin="0.54s" dur="0.4s" fill="freeze" calcMode="spline" keySplines="0.2 0.8 0.2 1"/>
</g>

<!-- ── ROW: Frontend ── -->
<g opacity="0" transform="translate(0,5)">
  <text x="20" y="217" fill="#ffa657" font-size="12.5" font-weight="700">Frontend</text>
  <text x="100" y="217" fill="#c9d1d9" font-size="12.5">React, Next.js, Tailwind CSS, HTML5/CSS3</text>
  <animate attributeName="opacity" from="0" to="1" begin="0.60s" dur="0.4s" fill="freeze"/>
  <animateTransform attributeName="transform" type="translate" from="0 5" to="0 0" begin="0.60s" dur="0.4s" fill="freeze" calcMode="spline" keySplines="0.2 0.8 0.2 1"/>
</g>

<!-- ── ROW: Backend ── -->
<g opacity="0" transform="translate(0,5)">
  <text x="20" y="238" fill="#ffa657" font-size="12.5" font-weight="700">Backend</text>
  <text x="100" y="238" fill="#c9d1d9" font-size="12.5">Node.js, Express.js, REST APIs</text>
  <animate attributeName="opacity" from="0" to="1" begin="0.66s" dur="0.4s" fill="freeze"/>
  <animateTransform attributeName="transform" type="translate" from="0 5" to="0 0" begin="0.66s" dur="0.4s" fill="freeze" calcMode="spline" keySplines="0.2 0.8 0.2 1"/>
</g>

<!-- ── ROW: AI / ML ── -->
<g opacity="0" transform="translate(0,5)">
  <text x="20" y="259" fill="#ffa657" font-size="12.5" font-weight="700">AI / ML</text>
  <text x="100" y="259" fill="#c9d1d9" font-size="12.5">Scikit-learn, Pandas, Data Science, GIS</text>
  <animate attributeName="opacity" from="0" to="1" begin="0.72s" dur="0.4s" fill="freeze"/>
  <animateTransform attributeName="transform" type="translate" from="0 5" to="0 0" begin="0.72s" dur="0.4s" fill="freeze" calcMode="spline" keySplines="0.2 0.8 0.2 1"/>
</g>

<!-- ── ROW: Database ── -->
<g opacity="0" transform="translate(0,5)">
  <text x="20" y="280" fill="#ffa657" font-size="12.5" font-weight="700">Database</text>
  <text x="100" y="280" fill="#c9d1d9" font-size="12.5">MySQL, SQLite</text>
  <animate attributeName="opacity" from="0" to="1" begin="0.78s" dur="0.4s" fill="freeze"/>
  <animateTransform attributeName="transform" type="translate" from="0 5" to="0 0" begin="0.78s" dur="0.4s" fill="freeze" calcMode="spline" keySplines="0.2 0.8 0.2 1"/>
</g>

<!-- ── ROW: Tools ── -->
<g opacity="0" transform="translate(0,5)">
  <text x="20" y="301" fill="#ffa657" font-size="12.5" font-weight="700">Tools</text>
  <text x="100" y="301" fill="#c9d1d9" font-size="12.5">Git, GitHub, Postman, VS Code, Linux</text>
  <animate attributeName="opacity" from="0" to="1" begin="0.84s" dur="0.4s" fill="freeze"/>
  <animateTransform attributeName="transform" type="translate" from="0 5" to="0 0" begin="0.84s" dur="0.4s" fill="freeze" calcMode="spline" keySplines="0.2 0.8 0.2 1"/>
</g>

<!-- ── SECTION: Highlights ── -->
<g opacity="0" transform="translate(0,5)">
  <text x="20" y="331" fill="#58a6ff" font-size="12.5" font-weight="700">&#8212; Key Highlights</text>
  <line x1="130" y1="327" x2="460" y2="327" stroke="#30363d" stroke-opacity="0.8"/>
  <animate attributeName="opacity" from="0" to="1" begin="0.90s" dur="0.4s" fill="freeze"/>
  <animateTransform attributeName="transform" type="translate" from="0 5" to="0 0" begin="0.90s" dur="0.4s" fill="freeze" calcMode="spline" keySplines="0.2 0.8 0.2 1"/>
</g>

<!-- ── BULLET 1 ── -->
<g opacity="0" transform="translate(0,5)">
  <circle cx="23" cy="351" r="2.5" fill="#3fb950"/>
  <text x="34" y="355" fill="#c9d1d9" font-size="12.5">AI Landslide Early Warning System for Nepal</text>
  <animate attributeName="opacity" from="0" to="1" begin="0.96s" dur="0.4s" fill="freeze"/>
  <animateTransform attributeName="transform" type="translate" from="0 5" to="0 0" begin="0.96s" dur="0.4s" fill="freeze" calcMode="spline" keySplines="0.2 0.8 0.2 1"/>
</g>

<!-- ── BULLET 2 ── -->
<g opacity="0" transform="translate(0,5)">
  <circle cx="23" cy="374" r="2.5" fill="#3fb950"/>
  <text x="34" y="378" fill="#c9d1d9" font-size="12.5">Smart Fire Emergency AI Response &amp; Rapid Alerts</text>
  <animate attributeName="opacity" from="0" to="1" begin="1.02s" dur="0.4s" fill="freeze"/>
  <animateTransform attributeName="transform" type="translate" from="0 5" to="0 0" begin="1.02s" dur="0.4s" fill="freeze" calcMode="spline" keySplines="0.2 0.8 0.2 1"/>
</g>

<!-- ── BULLET 3 ── -->
<g opacity="0" transform="translate(0,5)">
  <circle cx="23" cy="397" r="2.5" fill="#3fb950"/>
  <text x="34" y="401" fill="#c9d1d9" font-size="12.5">HerbTrace: Blockchain Ayurvedic Supply Provenance</text>
  <animate attributeName="opacity" from="0" to="1" begin="1.08s" dur="0.4s" fill="freeze"/>
  <animateTransform attributeName="transform" type="translate" from="0 5" to="0 0" begin="1.08s" dur="0.4s" fill="freeze" calcMode="spline" keySplines="0.2 0.8 0.2 1"/>
</g>

<!-- ── BULLET 4 ── -->
<g opacity="0" transform="translate(0,5)">
  <circle cx="23" cy="420" r="2.5" fill="#3fb950"/>
  <text x="34" y="424" fill="#c9d1d9" font-size="12.5">Health AI Chatbot &amp; Interactive DSA Visualizer</text>
  <animate attributeName="opacity" from="0" to="1" begin="1.14s" dur="0.4s" fill="freeze"/>
  <animateTransform attributeName="transform" type="translate" from="0 5" to="0 0" begin="1.14s" dur="0.4s" fill="freeze" calcMode="spline" keySplines="0.2 0.8 0.2 1"/>
</g>

<!-- ── BULLET 5 ── -->
<g opacity="0" transform="translate(0,5)">
  <circle cx="23" cy="443" r="2.5" fill="#3fb950"/>
  <text x="34" y="447" fill="#c9d1d9" font-size="12.5">12+ Public Open-Source Repositories on GitHub</text>
  <animate attributeName="opacity" from="0" to="1" begin="1.20s" dur="0.4s" fill="freeze"/>
  <animateTransform attributeName="transform" type="translate" from="0 5" to="0 0" begin="1.20s" dur="0.4s" fill="freeze" calcMode="spline" keySplines="0.2 0.8 0.2 1"/>
</g>
</svg>'''

    output_path = os.path.join(OUTPUT_DIR, "info-card.svg")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated: {output_path}")


# -------------------------------------------------------------------------
# 4. INJECT INTO README.md (COMPREHENSIVE SHARMA964 PROFILE INTEGRATION)
# -------------------------------------------------------------------------
def inject_into_readme():
    readme_path = os.path.join(OUTPUT_DIR, "README.md")
    content = f'''<p align="center">
  <img src="github-contribution-animation.svg" alt="GitHub Contribution Graph" width="850"/>
</p>

<table>
  <tr>
    <td valign="centre"><img src="terminal-card.svg" alt="ASCII Portrait" width="400"/></td>
    <td valign="top"><img src="info-card.svg" alt="Info Card" width="500"/></td>
  </tr>
</table>

<!-- HERO SECTION -->
<div align="center">
  <h1>Hi 👋, I'm <a href="https://github.com/{GITHUB_USERNAME}">Sonu Sharma</a></h1>
  <h3><strong>Computer Engineering Student • AI/ML Enthusiast • Full-Stack Developer</strong></h3>
  <p><i>Building intelligent AI systems, robust full-stack web applications, and algorithmic solutions to solve real-world problems.</i></p>

  <p>
    <a href="https://github.com/{GITHUB_USERNAME}"><img src="https://komarev.com/ghpvc/?username={GITHUB_USERNAME}&label=Profile%20Views&color=0e75b6&style=for-the-badge" alt="Profile Views" /></a>
    <a href="https://github.com/{GITHUB_USERNAME}?tab=followers"><img src="https://img.shields.io/github/followers/{GITHUB_USERNAME}?label=Followers&style=for-the-badge&color=0e75b6" alt="GitHub Followers" /></a>
    <a href="https://github.com/{GITHUB_USERNAME}"><img src="https://img.shields.io/badge/GitHub-{GITHUB_USERNAME}-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" /></a>
    <a href="https://www.linkedin.com/in/sonu-sharma-2119ab328/"><img src="https://img.shields.io/badge/LinkedIn-Sonu%20Sharma-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
    <a href="https://sonusharma7.com.np"><img src="https://img.shields.io/badge/Portfolio-sonusharma7.com.np-38BDF8?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Portfolio" /></a>
    <a href="mailto:sonusharma.dev07@gmail.com"><img src="https://img.shields.io/badge/Email-sonusharma.dev07%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>
  </p>
</div>

<br/>

<!-- ================= ABOUT ME ================= -->
## 🚀 About Me

- 🎓 **Computer Engineering student** passionate about building practical, impact-driven technology solutions.
- 🤖 Deeply interested in **Artificial Intelligence, Machine Learning, and Data Science**.
- 💻 Building modern, responsive web applications with **React, Next.js, Node.js, and TypeScript**.
- 🧠 Continuously mastering **Data Structures &amp; Algorithms (DSA)** and competitive problem-solving.
- 🔬 Currently developing an **AI-Based Landslide Prediction &amp; Early Warning System** for disaster risk reduction in Nepal.
- 🌍 Exploring scalable backend systems, system design, cloud infrastructure, and Web3 / Blockchain.
- 🤝 Open to collaborating on innovative **AI/ML, Full-Stack Development, and Open Source projects**.

---

<!-- ================= FLAGSHIP PROJECT SPOTLIGHT ================= -->
## 🔭 Flagship Project Spotlight

### 🌋 [AI-Based Landslide Prediction &amp; Early Warning System](https://github.com/{GITHUB_USERNAME}/AI-LandSlide-Early-Predication)

An end-to-end AI-driven system engineered to evaluate landslide vulnerability and deliver real-time early warnings by integrating Machine Learning algorithms, environmental rainfall analytics, and GIS location datasets tailored for Nepal's terrain.

- 🤖 **Machine Learning Predictive Modeling**: High-precision risk classification based on geological &amp; meteorological data.
- 🌧️ **Environmental Factors**: Live precipitation thresholds, soil saturation, and slope gradient parameters.
- 🗺️ **GIS Risk Mapping**: Interactive geospatial visualization and danger zone mapping.
- 🚨 **Automated Alerts**: Rapid early warning triggers for communities and disaster response teams.
- 📊 **Tech Stack**: `Python` • `TypeScript` • `Machine Learning` • `GIS` • `Data Analytics`

<p>
  <a href="https://github.com/{GITHUB_USERNAME}/AI-LandSlide-Early-Predication">
    <img src="https://img.shields.io/badge/View%20Repository-AI--LandSlide--Early--Predication-black?style=for-the-badge&logo=github" alt="View Repository" />
  </a>
</p>

---

<!-- ================= FEATURED PROJECTS ================= -->
## 🚀 Featured Projects

<table>
  <tr>
    <td width="50%" valign="top">
      <h3 align="center">🌋 <a href="https://github.com/{GITHUB_USERNAME}/AI-LandSlide-Early-Predication">AI Landslide Early Prediction</a></h3>
      <p>AI-powered landslide prediction and early warning platform combining ML, environmental indicators, and GIS mapping for disaster risk reduction in Nepal.</p>
      <p align="center"><code>Python</code> • <code>TypeScript</code> • <code>ML</code> • <code>GIS</code></p>
    </td>
    <td width="50%" valign="top">
      <h3 align="center">🔥 <a href="https://github.com/{GITHUB_USERNAME}/Smart-Fire-Emergency-Response">Smart Fire Emergency Response</a></h3>
      <p>AI-driven smart fire emergency response system designed for rapid hazard detection, instant alert dissemination, and emergency logistics coordination.</p>
      <p align="center"><code>JavaScript</code> • <code>AI / ML</code> • <code>IoT</code> • <code>APIs</code></p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3 align="center">🌿 <a href="https://github.com/{GITHUB_USERNAME}/HerbTrace-ayur-block-chain">HerbTrace Blockchain</a></h3>
      <p>Decentralized provenance and verification platform utilizing blockchain to authenticate and track Ayurvedic herb supply chains from origin to consumer.</p>
      <p align="center"><code>TypeScript</code> • <code>Blockchain</code> • <code>Smart Contracts</code> • <code>Web3</code></p>
    </td>
    <td width="50%" valign="top">
      <h3 align="center">🩺 <a href="https://github.com/{GITHUB_USERNAME}/Health-AI-Chatbot">Health AI Conversational Assistant</a></h3>
      <p>Intelligent healthcare conversational assistant providing symptom guidance, medical information triage, and intuitive health insights.</p>
      <p align="center"><code>JavaScript</code> • <code>AI / NLP</code> • <code>Node.js</code> • <code>APIs</code></p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3 align="center">📊 <a href="https://github.com/{GITHUB_USERNAME}/DSA-Visualizer">Interactive DSA Visualizer</a></h3>
      <p>Dynamic web-based algorithm visualizer bringing sorting, graph traversals, trees, and core data structures to life with step-by-step animations.</p>
      <p align="center"><code>TypeScript</code> • <code>Algorithms</code> • <code>Data Structures</code> • <code>Canvas</code></p>
    </td>
    <td width="50%" valign="top">
      <h3 align="center">🌐 <a href="https://github.com/{GITHUB_USERNAME}/Personal-Portfolio">Personal Portfolio Website</a></h3>
      <p>Modern personal portfolio showcasing projects, technical competencies, and developer journey with responsive layouts and interactive UI.</p>
      <p align="center"><code>TypeScript</code> • <code>React</code> • <code>Tailwind CSS</code> • <code>Vite</code></p>
    </td>
  </tr>
</table>

<p align="center">
  <a href="https://github.com/{GITHUB_USERNAME}?tab=repositories">
    <img src="https://img.shields.io/badge/Explore%20All%2012+%20Repositories-181717?style=for-the-badge&logo=github" alt="Explore All Repositories" />
  </a>
</p>

---

<!-- ================= TECHNICAL SKILLS ================= -->
## 🛠️ Technical Competencies

### 💻 Programming Languages
<p align="left">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/c/c-original.svg" width="40" height="40" alt="C"/>&nbsp;&nbsp;
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/cplusplus/cplusplus-original.svg" width="40" height="40" alt="C++"/>&nbsp;&nbsp;
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="40" height="40" alt="Python"/>&nbsp;&nbsp;
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" width="40" height="40" alt="JavaScript"/>&nbsp;&nbsp;
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/typescript/typescript-original.svg" width="40" height="40" alt="TypeScript"/>
</p>

### 🌐 Frontend Development
<p align="left">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original.svg" width="40" height="40" alt="React"/>&nbsp;&nbsp;
  <img src="https://cdn.worldvectorlogo.com/logos/nextjs-2.svg" width="40" height="40" alt="Next.js"/>&nbsp;&nbsp;
  <img src="https://www.vectorlogo.zone/logos/tailwindcss/tailwindcss-icon.svg" width="40" height="40" alt="Tailwind CSS"/>&nbsp;&nbsp;
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original.svg" width="40" height="40" alt="HTML5"/>&nbsp;&nbsp;
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original.svg" width="40" height="40" alt="CSS3"/>
</p>

### ⚙️ Backend, APIs &amp; Databases
<p align="left">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nodejs/nodejs-original.svg" width="40" height="40" alt="Node.js"/>&nbsp;&nbsp;
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/express/express-original.svg" width="40" height="40" alt="Express.js"/>&nbsp;&nbsp;
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original.svg" width="40" height="40" alt="MySQL"/>&nbsp;&nbsp;
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/sqlite/sqlite-original.svg" width="40" height="40" alt="SQLite"/>&nbsp;&nbsp;
  <img src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" width="40" height="40" alt="Postman"/>
</p>

### 🤖 AI, Machine Learning &amp; Data Science
<p align="left">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="40" height="40" alt="Python"/>&nbsp;&nbsp;
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original.svg" width="40" height="40" alt="Pandas"/>&nbsp;&nbsp;
  <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" width="40" height="40" alt="Scikit-learn"/>&nbsp;&nbsp;
  <img src="https://seaborn.pydata.org/_images/logo-mark-lightbg.svg" width="40" height="40" alt="Seaborn"/>
</p>

### 🛠️ Developer Tools &amp; Environments
<p align="left">
  <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" width="40" height="40" alt="Git"/>&nbsp;&nbsp;
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/github/github-original.svg" width="40" height="40" alt="GitHub"/>&nbsp;&nbsp;
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/vscode/vscode-original.svg" width="40" height="40" alt="VS Code"/>&nbsp;&nbsp;
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" width="40" height="40" alt="Linux"/>
</p>

---

<!-- ================= GITHUB STATS & STREAK ================= -->
## 📈 GitHub Streak &amp; Activity

<p align="center">
  <img src="https://streak-stats.demolab.com/?user={GITHUB_USERNAME}&theme=tokyonight&hide_border=true" alt="GitHub Contribution Streak"/>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_USERNAME}/output/github-contribution-grid-snake-dark.svg" alt="GitHub Contribution Snake" />
</p>

---

<!-- ================= CURRENT FOCUS & 2026 GOALS ================= -->
## 🎯 Current Focus &amp; 2026 Goals

- 🚀 **Deploy Real-World AI Systems**: Expand AI Landslide Prediction and Smart Fire Response into field-tested solutions.
- 🧠 **Master Advanced DSA**: Deepen algorithmic intuition, graph theory, dynamic programming, and complexity optimization.
- 🌐 **Scalable Architecture**: Engineer scalable full-stack applications with microservices and caching.
- 🤝 **Open-Source Contributions**: Contribute meaningfully to major developer tooling and AI/ML ecosystems.
- 📚 **System Design &amp; Cloud**: Gain practical mastery of distributed systems, cloud computing, and CI/CD pipelines.

---

<!-- ================= CONNECT WITH ME ================= -->
## 🤝 Connect With Me

<div align="center">
  <p>
    <a href="https://github.com/{GITHUB_USERNAME}"><img src="https://img.shields.io/badge/GitHub-{GITHUB_USERNAME}-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" /></a>
    <a href="https://www.linkedin.com/in/sonu-sharma-2119ab328/"><img src="https://img.shields.io/badge/LinkedIn-Sonu%20Sharma-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
    <a href="https://sonusharma7.com.np"><img src="https://img.shields.io/badge/Website-sonusharma7.com.np-38BDF8?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Website" /></a>
    <a href="mailto:sonusharma.dev07@gmail.com"><img src="https://img.shields.io/badge/Email-sonusharma.dev07%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>
  </p>

  <p>
    <i>📍 Nepal &nbsp;•&nbsp; ✉️ <a href="mailto:sonusharma.dev07@gmail.com">sonusharma.dev07@gmail.com</a> &nbsp;•&nbsp; 🌐 <a href="https://sonusharma7.com.np">sonusharma7.com.np</a></i>
  </p>
  
  <p>
    <i>✨ Building • Learning • Experimenting • Growing 🚀</i>
  </p>
</div>
'''
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated README.md with 100% comprehensive Sharma964 profile integration!")


# -------------------------------------------------------------------------
# MAIN
# -------------------------------------------------------------------------
if __name__ == "__main__":
    generate_contribution_svg()
    generate_terminal_card_svg()
    generate_info_card_svg()
    inject_into_readme()
    print("All tasks completed successfully for Sharma964!")
