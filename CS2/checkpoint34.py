def cleaveOrAttack(enemy):
    # ถ้า "cleave" พร้อมก็ทำเลย ไม่อย่างนั้นก็ โจมตี
    if hero.isReady("cleave"):
        hero.cleave(enemy)
    else:
        hero.attack(enemy)
    pass

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        distance = hero.distanceTo(enemy)
        if distance < 5:
            # เรียกใช้ฟังก์ชั่น "cleaveOrAttack" ที่กำหนดไว้ข้างต้น
            cleaveOrAttack(enemy)
