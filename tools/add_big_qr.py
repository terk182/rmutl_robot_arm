"""Enlarge the hero QR and add a large printable/share QR card."""
import re

with open("tools/qr.svg", encoding="utf-8") as f:
    qr = f.read()
paths = re.findall(r"<path[^>]*/>", qr)
assert paths, "no path in qr.svg"
inner = "".join(paths)

with open("index.html", encoding="utf-8") as f:
    html = f.read()

# --- 1) enlarge hero QR via CSS ---
old_css = (
    "  .hero-qr{display:inline-flex;align-items:center;gap:14px;background:#fff;"
    "border-radius:16px;padding:12px 20px;margin:26px auto 0;box-shadow:0 8px 20px rgba(0,0,0,.2);}\n"
    "  .hero-qr svg{width:76px;height:76px;display:block;flex-shrink:0;}\n"
    "  .hero-qr-text{text-align:left;}\n"
    "  .hero-qr-text b{display:block;color:#4338ca;font-size:1rem;margin-bottom:2px;}\n"
    "  .hero-qr-text span{display:block;color:#6b7280;font-size:.74rem;word-break:break-all;}\n"
    "  @media(max-width:520px){.hero-qr-text span{font-size:.66rem;}}\n"
)
new_css = (
    "  .hero-qr{display:inline-flex;align-items:center;gap:18px;background:#fff;"
    "border-radius:18px;padding:16px 26px;margin:30px auto 0;box-shadow:0 10px 24px rgba(0,0,0,.22);}\n"
    "  .hero-qr svg{width:132px;height:132px;display:block;flex-shrink:0;}\n"
    "  .hero-qr-text{text-align:left;}\n"
    "  .hero-qr-text b{display:block;color:#4338ca;font-size:1.25rem;margin-bottom:4px;}\n"
    "  .hero-qr-text span{display:block;color:#6b7280;font-size:.82rem;word-break:break-all;}\n"
    "  @media(max-width:520px){.hero-qr svg{width:96px;height:96px;}.hero-qr{flex-direction:column;text-align:center;}.hero-qr-text{text-align:center;}.hero-qr-text span{font-size:.7rem;}}\n"
    "  .big-qr{display:flex;flex-direction:column;align-items:center;gap:6px;padding:10px;}\n"
    "  .big-qr svg{width:240px;height:240px;display:block;background:#fff;border-radius:14px;box-shadow:0 4px 18px rgba(0,0,0,.14);}\n"
    "  .big-qr .url{font-weight:800;color:var(--primary-dark);word-break:break-all;text-align:center;font-size:1rem;}\n"
)
assert old_css in html, "hero-qr css not found"
html = html.replace(old_css, new_css, 1)

# --- 2) add big share QR card at end of resources section ---
qr_svg = (
    '<svg viewBox="0 0 33 33" role="img" aria-label="QR code ลิงก์เว็บสื่อการสอน" '
    'shape-rendering="crispEdges">' + inner + "</svg>"
)
card = (
    '\n    <div class="card" id="share-qr">\n'
    '      <h4>📱 แชร์เว็บสื่อการสอนนี้</h4>\n'
    '      <p style="text-align:center;">สแกน QR ด้านล่างเพื่อเปิดเว็บไซต์บนมือถือ — '
    'แชร์ให้เพื่อน หรือพิมพ์ติดห้องเรียนได้เลย</p>\n'
    '      <div class="big-qr">\n'
    '        ' + qr_svg + '\n'
    '        <span class="url">https://terk182.github.io/rmutl_robot_arm/</span>\n'
    '      </div>\n'
    '    </div>\n'
    "  </section>"
)
anchor = (
    '        <div class="note warn"><span class="label">💡 วันที่ 3:</span> '
    "Local LLM กับ Cloud AI ต่างกันอย่างไร? ปลอดภัยกว่าตรงไหน? จะทำให้ AI ตีความผิดพลาดน้อยลงได้ยังไง?</div>\n"
    "      </div>\n"
    "    </div>\n"
    "  </section>"
)
assert anchor in html, "resources section anchor not found"
html = html.replace(anchor, anchor.replace("  </section>", "") + card, 1)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("hero QR enlarged + big share QR card added")
