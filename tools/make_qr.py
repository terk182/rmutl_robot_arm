"""Generate a QR code (SVG) for the GitHub Pages URL."""
import qrcode
import qrcode.image.svg

URL = "https://terk182.github.io/rmutl_robot_arm/"

factory = qrcode.image.svg.SvgPathImage
img = qrcode.make(URL, image_factory=factory, box_size=10, border=2)
img.save("qr.svg")
print("saved qr.svg", img.get_image().get("width"), "x", img.get_image().get("height"))
