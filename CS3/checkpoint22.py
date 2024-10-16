# คุณต้องรวบรวมหลายไอเทม
# แต่เบิร์ลต้องการอัญมณี!
# เลือกไอเทมที่ปรากฏทั้งหมดยกเว้นอัญมณี

while True:
    item = hero.findNearestItem()
    if item:
        if item.type != "gem":
            hero.moveXY(item.pos.x, item.pos.y)
        # หาก item.type ไม่เท่ากับ "gem":
        pass
            # ไปยังตำแหน่งของไอเทม