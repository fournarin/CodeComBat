# ค้นหาว่ายักษ์ตนนั้นมาจากไหน

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # ซ้าย:enemy.pos.x น้อยกว่า hero.pos.x
        isLeft = hero.pos.x  > enemy.pos.x
        # ด้านบน:enemy.pos.y มากกว่า hero.pos.y
        isAbove = hero.pos.y < enemy.pos.y
        # ขวา:enemy.pos.x มากกว่า hero.pos.x
        isRight = hero.pos.x  < enemy.pos.x
        # ด้านล่าง:enemy.pos.y น้อยกว่า hero.pos.y
        isBelow = hero.pos.y > enemy.pos.y
        # หากศัตรู isAbove และ isLeft:
        # buildXY() เป็น "fire-trap" ที่เครื่องหมาย X
        if isLeft and isAbove:
            hero.buildXY("fire-trap", 20, 51)
            pass
        # หากศัตรู isAbove และ isRight:
        # buildXY() เป็น "fire-trap" ที่เครื่องหมาย X
        if isRight and isAbove:
            hero.buildXY("fire-trap", 60, 51)
            pass
        # หากศัตรูอยู่ isBelow และ isLeft:
        # buildXY() เป็น "fire-trap" ที่เครื่องหมาย X
        if isLeft and isBelow:
            hero.buildXY("fire-trap", 20, 17)
            pass
        # หากศัตรู isBelow และ isRight:
        # buildXY() เป็น "fire-trap" ที่เครื่องหมาย X
        if isBelow and isRight:
            hero.buildXY("fire-trap", 60, 17)
            pass
        hero.moveXY(40, 34)
        pass
    else:
        hero.moveXY(40, 34)
        pass