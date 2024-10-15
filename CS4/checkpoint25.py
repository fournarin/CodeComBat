# ยักษ์ตัวเล็กที่นี่สร้างความเสียหายได้มากกว่าที่คิด!
# โจมตีพวกยักษ์ด้วยพลังชีวิตน้อยที่สุดก่อน
while True:
    weakest = None
    leastHealth = 99999
    enemyIndex = 0
    enemies = hero.findEnemies()

    # ลูปศัตรูทั้งหมด
    while enemyIndex < len(enemies):
        enemy = enemies[enemyIndex]
        # หากพลังชีวิตของศัตรูน้อยกว่า leastHealth
        if enemy.health < leastHealth:
            weakest = enemy
            # ทำให้มันอ่อนแอที่สุดและตั้งค่า leastHealth กัยพลังชีวิต
            leastHealth = enemy.health
        #  อย่าลืมเพิ่ม enemyIndex 1 ตัว
        enemyIndex += 1
    if weakest:
        # โจมตียักษ์ที่อ่อนแอที่สุด
        while weakest.health > 0:
            hero.attack(weakest)
        pass