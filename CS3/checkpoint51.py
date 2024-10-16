# แข่งมันชกินส์ลงไปในน้ำกลั่นโดยโอมาน บริวสโตน!
# ใช้คำสั่ง  `continue` หลบเลี่ยงพิษ
while True:
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    
    # หากไม่มีศัตรู ให้ออกจากลูปต่อไป
    if not enemy:
        continue
    
    # หากไม่มีไอเทม ให้ขอโพชั่นแล้วดำเนินการต่อ
    if not item:
        hero.say("ขอดื่มหน่อย!")
        continue
    
    # หากไอเทมประเภท "poison" ให้ดำเนินการต่อจากลูป
    if item.type == "poison":
        continue
    # ตอนนี้ โพชั่นต้องเป็นน้ำขวด
    # ดังนั้นให้ย้ายXY ไปที่โพชั่นแล้วกลับไปที่จุดเริ่มต้น!
    hero.moveXY(item.pos.x, item.pos.y)
    hero.moveXY(34, 47)
    
