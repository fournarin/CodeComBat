# ใช้ "fire-trap" เพื่อกำจัดยักษ์

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # หากศัตรูอยู่ทางด้านซ้ายของฮีโร่:
        if enemy.pos.x < hero.pos.x:
            # buildXY เป็น "fire-trap" ทางซ้าย X
            hero.buildXY("fire-trap",24, 34)
            pass
        # หากศัตรูอยู่ทางด้านขวาของฮีโร่:
        elif enemy.pos.x > hero.pos.x:
            # buildXY เป็น "fire-trap" ทางด้านขวา X
            hero.buildXY("fire-trap",55, 34)
            pass
        # หากศัตรูอยู่ต่ำกว่าฮีโร่:
        elif enemy.pos.y < hero.pos.y:
            # buildXY เป็น  "fire-trap" ที่ด้านล่าง X
            hero.buildXY("fire-trap",40, 19)
            pass
        # หากศัตรูอยู่เหนือฮีโร่:
        elif enemy.pos.y > hero.pos.y:
            # buildXY เป็น "fire-trap" บน X
            hero.buildXY("fire-trap",40, 49)
            pass
    # เคลื่อนกลับไปที่ศูนย์
    hero.moveXY(40, 34)