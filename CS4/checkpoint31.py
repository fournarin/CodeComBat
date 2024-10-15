while True:
    # ไปที่เหรียญที่ใกล้ที่สุด
    coin = hero.findNearestItem()
    if coin:
        coinx = coin.pos.x
        coiny = coin.pos.y
        hero.moveXY(coinx, coiny) 

    # หากคุณมีเงินทุนสำหรับทหาร ให้เรียกออกมา
    if hero.gold >= hero.costOf("soldier"):  # ใช้ >= แทน >
        hero.summon("soldier")

    enemy = hero.findNearest(hero.findEnemies())
    if enemy:
        soldiers = hero.findFriends()
        soldierIndex = 0
        
        # ลูปทหารทั้งหมดของคุณ และสั่งให้โจมตี
        while soldierIndex < len(soldiers):  # ใช้ < แทน ==
            soldier = soldiers[soldierIndex]
            hero.command(soldier, "attack", enemy)  # สั่งให้ทหารโจมตีศัตรู
            soldierIndex += 1  # เพิ่ม soldierIndex ขึ้น 1