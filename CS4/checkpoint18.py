while True:
    enemies = hero.findEnemies()
    enemyIndex = 0

    # ใช้ while loop เพื่อโจมตีศัตรูทั้งหมด
    while enemyIndex < len(enemies):
        enemy = enemies[enemyIndex]

        # ตรวจสอบว่าศัตรูไม่ใช่ "sand-yak"
        if enemy.type != "sand-yak":
            # เมื่อพลังชีวิตของศัตรูมากกว่า 0 โจมตีมัน!
            while enemy.health > 0:
                hero.attack(enemy)

        # เพิ่มค่า index เพื่อตรวจสอบศัตรูตัวถัดไป
        enemyIndex += 1

    # หลังจากกำจัดศัตรูได้บางส่วน ให้ถอยกลับมาที่ศูนย์เพื่อเตรียมรับคลื่นต่อไป
    hero.moveXY(40, 34)  # ปรับตำแหน่งนี้ตามตำแหน่งศูนย์ของคุณ