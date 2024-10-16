# จำไว้ว่าศัตรูอาจจะยังไม่เกิดขึ้น
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # ถ้ามีศัตรู จงโจมตีมัน!
        hero.attack(enemy)
        hero.attack(enemy)
        pass
