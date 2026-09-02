# 🤖 สื่อการสอนแขนกลอัจฉริยะ 3DOF (RMUTL)

เว็บสื่อการสอนแบบไฟล์เดียว (Single-file HTML) สำหรับค่าย **"นวัตกรรมแขนกลอัจฉริยะ (Smart 3DOF Robotic Arm: From CAD to AI)"** ระยะเวลา 3 วัน

## 🌐 เว็บไซต์ (GitHub Pages)

**https://terk182.github.io/rmutl_robot_arm/**

> สแกน QR code ที่มุมขวาบนของหน้าเว็บเพื่อเปิดเว็บไซต์จากมือถือ

## 📚 เนื้อหาในเว็บ

| หัวข้อ | รายละเอียด |
|---|---|
| ภาพรวมหลักสูตร | เป้าหมาย ระยะเวลา 3 วัน แผนการเรียน |
| วันที่ 1 | Onshape (ออกแบบ 3 มิติ), จัดซื้อ Shopee + BOM, พิมพ์ 3 มิติ |
| Onshape | การสมัคร/เริ่มใช้งาน, UI, คำสั่งพื้นฐาน, ทางลัด, AI ใน Onshape |
| วันที่ 2 | GitHub, ประกอบ, 3DOF Kinematics (FK/IK) + ตัวอย่างคำนวณ |
| วันที่ 3 | Local LLM (Ollama), Mini-Hackathon AI Pick & Place |
| Kinematics Simulator | Interactive 3DOF simulator (Canvas + FK/IK ตามโค้ดจริง) |
| ฮาร์ดแวร์ | แผนภาพเดินสายไฟ + ตาราง GPIO (จากโค้ดจริง) |
| โค้ด | โครงสร้างโปรเจกต์ terk_arm_esp32_v1, วิธีติดตั้ง Arduino IDE |
| API | API Reference ครบทุก endpoint + ตัวอย่าง Python |
| AI | Ollama → แขนกล, VLM/VLA ให้แขนกลมองเห็น |
| BOM | ตารางต้นทุนตัวอย่าง |

## 🧰 โครงสร้าง

```
├── index.html        # สื่อการสอน (ไฟล์เดียว, ใช้ได้แบบออฟไลน์)
├── .nojekyll         # บังคับ GitHub Pages ให้ serve แบบ static (ไม่ใช้ Jekyll)
├── README.md
└── tools/
    ├── make_qr.py    # สร้าง QR code (ต้องการไลบรารี qrcode)
    ├── add_qr.py     # ฝัง QR ลง header ของ index.html
    └── qr.svg        # ไฟล์ QR code ที่สร้างแล้ว
```

## 🔗 อ้างอิง

- โปรเจกต์เฟิร์มแวร์: [terk182/terk_arm_esp32_v1](https://github.com/terk182/terk_arm_esp32_v1)
- Onshape: https://www.onshape.com
- Ollama: https://ollama.com
