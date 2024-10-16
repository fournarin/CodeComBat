# ยืนอยู่ระหว่างชาวบ้านกับหอคอย

while True:
    enemy = hero.findNearestEnemy()
    friend = hero.findNearestFriend()
    # คำนวณ x โดยเพิ่ม friend.pos.x ให้กับ enemy.pos.x
    # แล้วหารด้วย 2
    x = (friend.pos.x + enemy.pos.x) / 2
    # ตรวจสอบคำแนะนำหากคุณต้องการความช่วยเหลือเพิ่มเติม!
    
    # ทำกับ y แบบเดียวกัน
    y = (friend.pos.y + enemy.pos.y) / 2
    # ไปยังพิกัด x และ y ที่คุณคำนวณไว้
    hero.moveXY(x, y)