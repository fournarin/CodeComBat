# ขั้นแรก กำจัดยักษ์ 6 ตัว
# แล้วเก็บเหรียญจนได้ 30 ทอง

# ตัวแปรนี้ใช้สำหรับการนับยักษ์
defeatedOgres = 0

# loop นี้ดำเนินการในขณะที่ defeatedOgres น้อยกว่า 6
while defeatedOgres < 6:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
        defeatedOgres += 1
    else:
        hero.say("Ogerษ์!")

# ย้ายไปทางด้านขวาของแผนที่
hero.moveXY(49, 36)

# loop นี้จะดำเนินการในขณะที่คุณมีน้อยกว่า 30 ทอง
while hero.gold < 30:
    # ค้นหาและรวบรวมเหรียญ
    item = hero.findNearestItem()
    if item:
        hero.moveXY(item.pos.x, item.pos.y)
    # ลบข้อความ say() นี้
    hero.say("ฉันควรรวบรวมเหรียญให้ได้ครบนะ!")

# ย้ายไปที่ทางออก
hero.moveXY(76, 32)