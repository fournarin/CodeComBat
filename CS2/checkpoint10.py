# เดินตรวจตราที่ทางเข้าในหมู่บ้าน
# สร้าง "กับดักไฟ" เมือคุณเห็นยักษ์
# อย่าระเบิดชาวบ้านนะ!

while True:
    hero.moveXY(43, 50)
    top = hero.findNearestEnemy()
    if top:
        hero.buildXY("fire-trap", 43, 50)

    hero.moveXY(25, 34)
    left = hero.findNearestEnemy()
    # ตรวจสอบว่า `left`' อยู่หรือไม่
    if left:
        hero.buildXY("fire-trap", 25, 34)
        
        # สร้างกับดักที่ 25, 34 ถ้ามีศัตรูอยู่
        
    hero.moveXY(43, 20)
    # ตั้งค่าตัวแปรสำหรับศัตรูตัวล่าง
    down = hero.findNearestEnemy()
    # ตรวจสอบว่าศัตรูด้านล่างมีอยู่หรือไม่
    if down:
        hero.buildXY("fire-trap", 43, 20)
        # สร้างกับดักที่ 43, 20 หากมีศัตรูอยู่
        