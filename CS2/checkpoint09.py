# เดินตรวจตราที่ทางเข้าในหมู่บ้าน
# ถ้าพบศัตรู ให้โจมตีมัน
while True:
    hero.moveXY(35, 34)
    leftEnemy = hero.findNearestEnemy()
    if leftEnemy:
        hero.attack(leftEnemy)
        hero.attack(leftEnemy)
    # ตอนนี้ย้ายไปทางเข้าด้านขวา
    hero.moveXY(60, 31)
    # ใช้ findNearestEnemy อีกครั้งเพื่อค้นหาศัตรูที่เหมาะสม
    enemy = hero.findNearestEnemy()
    # ใช้ "if" เพื่อโจมตีสองครั้งหากมีศัตรูที่ถูกต้อง
    if enemy:
        hero.attack(enemy)
        hero.attack(enemy)
        
