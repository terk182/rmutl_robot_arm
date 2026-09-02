"""Embed the generated QR code into the nav header of index.html."""
import re

with open("qr.svg", encoding="utf-8") as f:
    qr = f.read()

# extract the QR path element(s) from the generated SVG
paths = re.findall(r"<path[^>]*/>", qr)
assert paths, "no path found in qr.svg"
inner = "".join(paths)

url = "https://terk182.github.io/rmutl_robot_arm/"

qr_svg = (
    '<svg viewBox="0 0 33 33" role="img" aria-label="QR code ลิงก์เว็บสื่อการสอน" '
    'shape-rendering="crispEdges">' + inner + "</svg>"
)

badge = (
    '\n    <a class="qr-badge" href="' + url
    + '" target="_blank" rel="noopener" title="สแกน QR เพื่อเปิดเว็บสื่อการสอน">\n'
    + "      " + qr_svg + "\n"
    + '      <span>สแกน<br>เปิดเว็บ</span>\n'
    + "    </a>"
)

with open("index.html", encoding="utf-8") as f:
    html = f.read()

css = (
    "\n"
    "  .qr-badge{display:inline-flex;align-items:center;gap:8px;background:#fff;"
    "border-radius:10px;padding:5px 12px 5px 6px;color:#4338ca;text-decoration:none;"
    "box-shadow:0 2px 8px rgba(0,0,0,.18);flex-shrink:0;}\n"
    "  .qr-badge svg{width:34px;height:34px;display:block;}\n"
    "  .qr-badge span{font-size:.66rem;font-weight:800;line-height:1.3;text-align:left;}\n"
    "  .qr-badge:hover{transform:translateY(-1px);}\n"
    "  @media(max-width:640px){.qr-badge span{display:none;}}\n"
)
assert "</style>" in html
html = html.replace("</style>", css + "</style>", 1)

anchor = (
    '<div class="brand">🤖 แขนกลอัจฉริยะ 3DOF'
    "<small>Smart Robotic Arm : From CAD to AI</small></div>"
)
assert anchor in html, "nav brand anchor not found"
html = html.replace(anchor, anchor + badge, 1)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("QR badge inserted into index.html header")
