# ใช้ลูป while-true ทั้งเคลื่อนที่และโจมตี

while True:
    hero.moveRight()
    hero.moveUp()
    enemy = hero.findNearestEnemy()
    hero.attack(enemy)
    hero.attack(enemy)
    hero.moveRight()
    hero.moveDown(2)
    hero.moveUp()

    pass
