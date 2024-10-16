# เก็บเห็ด 9 ดอก

# ฟังก์ชั่นนี้ทำให้สัตว์เลี้ยงไปเอายามาให้คุณ
def onSpawn(event):
    while True:
        # สัตว์เลี้ยงสามารถค้นหาไอเท็มที่ใกล้ที่สุดตามประเภทของมัน
        potion = pet.findNearestByType("potion")
        # ให้สัตว์เลี้ยงไปเอายาหากมีอยู่:
        pet.fetch(potion)

pet.on("spawn", onSpawn)

# เห็ดมีพิษ อย่าเก็บเร็วเกินไป
while True:
    someItem = hero.findNearestItem()
    if someItem and hero.health > hero.maxHealth / 3:
        # รวบรวม someItem:
        hero.moveXY(someItem.pos.x, someItem.pos.y)
        pass
