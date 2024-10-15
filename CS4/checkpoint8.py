# รวบรวม 7 โพชั่นผักโขม
# แล้วคุณจะแข็งแกร่งพอที่จะเอาชนะพวกยักษ์โอเกอร์ได้

potionCount = 0

# ห่อรหัสคอลเลกชัน potion ไว้ข้างใน while loop
# ใช้เงื่อนไขเพื่อตรวจสอบ potionCount
while potionCount < 7:
    item = hero.findNearestItem()
    if item:
        hero.moveXY(item.pos.x, item.pos.y)
        potionCount += 1

# เมื่อ while looop เสร็จสิ้น
# ไปเลย! ต่อสู้!
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)