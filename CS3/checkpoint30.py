# พ่อมดของเราเคลื่อนย้ายยักษ์โอเกอร์ออกจากค่ายของพวกเขาที่นี่
# ปรากฏขึ้นเพียงชั่วครู่และถูกสตั๊น
# โจมตีเฉพาะยักษ์โอเกอร์ที่อ่อนแอและอยู่ใกล้เท่านั้น

while True:
    enemy = hero.findNearestEnemy()
    distance = hero.distanceTo(enemy)
    # หาก enemy.type เป็น : "munchkin"
    # และระยะทางไปไม่เกิน 20 เมตร
    if enemy.type == "munchkin" and distance < 20:
        if hero.isReady("cleave"):
            hero.cleave(enemy)
        else:
            hero.attack(enemy)
        # ให้โจมตี