# ใช้ทักษะ "ฟันหมุน" ที่คุณมีบ่อยที่สุดเท่าที่ทำได้

hero.moveXY(23, 23)
while True:
    enemy = hero.findNearestEnemy()
    if hero.isReady("cleave"):
        # ฟันศัตรูให้ขาด!
        hero.cleave(enemy)
        pass
    else:
        # ถ้า cleave ไม่พร้อมใช้งาน ให้โจมตีตามปกติ
        hero.attack(enemy)
        hero.attack(enemy)
        pass
