while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        pass  # แทนที่นี่ด้วยโค้ดของคุณเอง
        # หา ระยะทาง ไปยังศัตรูด้วย distanceTo
        distance = hero.distanceTo(enemy)
        # ถ้าระยะทางน้อยกว่า 5 เมตร...
        if distance < 5:
            # ...ถ้า "cleave" พร้อมแล้ว ให้ cleave!
            if hero.isReady("cleave"):
                hero.cleave(enemy)
            # ถ้าไม่ใช่ ก็แค่โจมตีไปเลย
            else:
                hero.attack(enemy)
