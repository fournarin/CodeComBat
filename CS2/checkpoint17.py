while True:
    enemy = hero.findNearestEnemy()
    distance = hero.distanceTo(enemy)
    if distance < 10:
        # โจมตีถ้ามันมาใกล้ชาวบ้านเกินไป
        hero.attack(enemy)
        pass
    #  esle อยู่ใกล้ชาวบ้าน! ใช้อย่างอื่น
    else:
        hero.moveXY(40, 37)
    