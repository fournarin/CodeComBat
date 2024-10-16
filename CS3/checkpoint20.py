# อย่าดูหมิ่นเผ่าอสูรที่สงบสุขเผ่านี้

while True:
    item = hero.findNearestItem()
    if item:
        # หาก item.type ไม่เท่ากับ "gem"
        if item.type != "gem":
            # จากนั้นตามหมาป่าสัตว์เลี้ยงของคุณ
            hero.moveXY(pet.pos.x, pet.pos.y)
        # Else
        else:
            # ย้ายไปยังตำแหน่งของอัญมณี
            hero.moveXY(item.pos.x, item.pos.y)