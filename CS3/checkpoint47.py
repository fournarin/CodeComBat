# ใช้ทักษะใหม่ของคุณเพื่อเลือกว่าจะทำอย่างไร hero.time

while True:
    # หากเป็น 10 วินาทีแรก ให้โจมตี
    if hero.time < 10:
        enemy = hero.findNearestEnemy()
        hero.attack(enemy)
        pass
    # ถ้าหากเป็น 35 วินาทีแรก ให้สะสมเหรียญ
    elif hero.time < 35:
        coin = hero.findNearestItem()
        hero.moveXY(coin.pos.x, coin.pos.y)
        pass
    # หลังจาก 35 วินาที ให้โจมตีอีกครั้ง!
    else:
        enemy = hero.findNearestEnemy()
        hero.attack(enemy)
        pass