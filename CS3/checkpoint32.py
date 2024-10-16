# เอาชนะมันชกินส์ เก็บเหรียญ ตามปกติ
# ใช้ AND เพื่อตรวจสอบการมีอยู่และพิมพ์ในคำสั่งเดียว

while True:
    enemy = hero.findNearestEnemy()
    # ด้วย AND ตัว type (ประเภท) จะถูกตรวจสอบหากมีศัตรูอยู่เท่านั้น
    if enemy and enemy.type == "munchkin":
        hero.attack(enemy)
    # ค้นหาไอเท็มที่ใกล้ที่สุด
    item = hero.findNearestItem()
    # เก็บไอเทมหากมีอยู่และ type (ประเภท) ของมันคือ "coin"
    if item and item.type == "coin":
        hero.moveXY(item.pos.x, item.pos.y)