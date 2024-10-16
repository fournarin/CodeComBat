# เลี้ยวขวาไปยังโอเอซิส
# สร้าง "fence" ด้านบนหรือด้านล่างเมื่อคุณ
while True:
    hero.moveXY(hero.pos.x+10, hero.pos.y)
    yak = hero.findNearestEnemy()
        # ถ้า yak.pos.y มากกว่า hero.pos.y
    if yak:
        if yak.pos.y > hero.pos.y:
            hero.buildXY("fence",hero.pos.x, hero.pos.y+5)
            pass
        else:
            hero.buildXY("fence",hero.pos.x, hero.pos.y-5)
            pass