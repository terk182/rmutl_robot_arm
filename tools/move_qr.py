"""Move the QR badge from the nav into the hero banner."""
import re

with open("index.html", encoding="utf-8") as f:
    html = f.read()

# 1) extract the full qr-badge block (anchor + svg + span)
m = re.search(r'<a class="qr-badge".*?</a>', html, re.S)
assert m, "qr-badge block not found"
badge = m.group(0)

# 2) remove it from the nav
assert badge in html
html = html.replace(badge, "", 1)

# 3) extract inner svg
svg_m = re.search(r"<svg.*?</svg>", badge, re.S)
svg = svg_m.group(0)

# 4) build the hero banner QR block
hero_qr = (
    '\n  <div class="hero-qr">\n'
    + "    " + svg + "\n"
    + '    <div class="hero-qr-text">\n'
    + '      <b>📱 สแกนเปิดเว็บสื่อการสอน</b>\n'
    + '      <span>https://terk182.github.io/rmutl_robot_arm/</span>\n'
    + "    </div>\n"
    + "  </div>\n"
    + "</header>"
)
assert "</header>" in html
html = html.replace("</header>", hero_qr, 1)

# 5) replace the old .qr-badge CSS with .hero-qr CSS
old_css = (
    "  .qr-badge{display:inline-flex;align-items:center;gap:8px;background:#fff;"
    "border-radius:10px;padding:5px 12px 5px 6px;color:#4338ca;text-decoration:none;"
    "box-shadow:0 2px 8px rgba(0,0,0,.18);flex-shrink:0;}\n"
    "  .qr-badge svg{width:34px;height:34px;display:block;}\n"
    "  .qr-badge span{font-size:.66rem;font-weight:800;line-height:1.3;text-align:left;}\n"
    "  .qr-badge:hover{transform:translateY(-1px);}\n"
    "  @media(max-width:640px){.qr-badge span{display:none;}}\n"
)
new_css = (
    "  .hero-qr{display:inline-flex;align-items:center;gap:14px;background:#fff;"
    "border-radius:16px;padding:12px 20px;margin:26px auto 0;box-shadow:0 8px 20px rgba(0,0,0,.2);}\n"
    "  .hero-qr svg{width:76px;height:76px;display:block;flex-shrink:0;}\n"
    "  .hero-qr-text{text-align:left;}\n"
    "  .hero-qr-text b{display:block;color:#4338ca;font-size:1rem;margin-bottom:2px;}\n"
    "  .hero-qr-text span{display:block;color:#6b7280;font-size:.74rem;word-break:break-all;}\n"
    "  @media(max-width:520px){.hero-qr-text span{font-size:.66rem;}}\n"
)
assert old_css in html, "old qr css not found"
html = html.replace(old_css, new_css, 1)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("QR moved from nav to hero banner")
