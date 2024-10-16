# คุณสามารถใส่ if-statement หนึ่งในอีก if-statement หนึ่งได้
# ระวังว่าคำสั่ง if โต้ตอบกันอย่างไร
# ตรวจสอบให้แน่ใจว่าการอินเดนชั่นถูกต้อง!
# การเริ่มต้นด้วย if/else ภายนอกตัวหนึ่งจะช่วยได้มาก
# ใช้ความคิดเห็นเป็นตัวยึดสำหรับ if/else ภายใน:

while True:
    enemy = hero.findNearestEnemy()
    # ถ้ามีศัตรูแล้ว...
    if enemy:
        # สร้างตัวแปรระยะทางด้วย distanceTo
        distance = hero.distanceTo(enemy)
        # หากระยะทางน้อยกว่า 5 เมตรให้โจมตี
        if distance < 5:
            if hero.isReady("cleave"):
                hero.cleave(enemy)
            else:
                hero.attack(enemy)
        # Else (ศัตรูอยู่ไกล) แล้วป้องกัน
        else:
            hero.shield()
        pass
    # Else (ไม่มีศัตรู)...
    else:
        # ... แล้วเคลื่อนย้ายกลับไปที่ X
        hero.moveXY(40, 34)
