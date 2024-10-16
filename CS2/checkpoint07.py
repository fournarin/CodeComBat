# จำไว้ว่าศัตรูอาจจะยังไม่เกิดขึ้น
while True:
    enemy = hero.findNearestEnemy()
    # ถ้ามีศัตรู จงโจมตีมัน!
    if enemy:
     hero.attack(enemy)
     hero.attack(enemy)
