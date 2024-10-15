while True:
    coin = hero.findNearestItem()
    
    # While เหรียญมีอยู่
    while coin:
        # ไปที่ตำแหน่งของเหรียญ
        hero.moveXY(coin.pos.x, coin.pos.y)
        # กำหนดตัวแปรเหรียญใหม่ให้กับไอเทมที่ใกล้ที่สุด
        coin = hero.findNearestItem()
    
    enemy = hero.findNearestEnemy()
    
    if enemy:
        # While พลังชีวิตของศัตรูมากกว่า 0
        while enemy.health > 0:
            # โจมตีศัตรู
            hero.attack(enemy)