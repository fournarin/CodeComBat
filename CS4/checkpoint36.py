# สำหรับระดับนี้ ฮีโร่ของคุณจะไม่ต่อสู้
# สั่งให้นักธนูของคุณพุ่งเป้าไปที่ศัตรูด้วยพลังชีวิตสูงสุด!
while True:
    friends = hero.findFriends()  # ค้นหานักธนูของคุณ
    enemies = hero.findEnemies()  # ค้นหาศัตรูทั้งหมด

    if enemies:
        # ค้นหาศัตรูที่มีพลังชีวิตสูงสุด
        strongestEnemy = enemies[0]
        for enemy in enemies:
            if enemy.health > strongestEnemy.health:
                strongestEnemy = enemy

        # สั่งให้นักธนูโจมตีศัตรูที่มีพลังชีวิตสูงสุด
        for friend in friends:
            if friend.type == "archer":  
                hero.command(friend, "attack", strongestEnemy)