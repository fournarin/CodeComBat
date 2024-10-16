# อยู่ตรงกลางและป้องกัน!

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # ไม่ว่าจะโจมตีศัตรู...
        hero.attack(enemy)
        hero.attack(enemy)
        pass
    else:
        # ... หรือย้ายกลับไปที่ตำแหน่งป้องกันของคุณ
        hero.moveXY(40, 35)
        pass
