# เอาชนะโครงกระดูกและรวบรวม lightstones

while True:
    enemies = hero.findEnemies()
    enemyIndex = 0
    while enemyIndex < len(enemies):
        enemy = enemies[enemyIndex]
        # โจมตีในขณะที่ศัตรูมีพลังชีวิต
        while enemy.health > 0:
            hero.attack(enemy)
        enemyIndex += 1
    items = hero.findItems()
    itemIndex = 0
    # loop ทุกไอเทม
    while itemIndex < len(items):
        item = items[itemIndex]
        # ในขณะที่ระยะทางมากกว่า 2:        
        while hero.distanceTo(item) > 2:
            # พยายามที่จะเอาไอเทม
            hero.moveXY(item.pos.x, item.pos.y)
        # อย่าลืมเพิ่ม itemIndex
        itemIndex += 1