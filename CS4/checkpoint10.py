# ปกป้องชาวบ้านจากยักษ์โอเกอร์

while True:
    # ให้รับอาร์เรย์ของศัตรู
    enemies = hero.findEnemies()
    # หากอาร์เรย์ไม่ว่างเปล่า
    if len(enemies) > 0:
        # โจมตีศัตรูตัวแรกจากอาร์เรย์ "enemies"
        hero.attack(enemies[0])
        # กลับไปที่ตำแหน่งเริ่มต้น
        hero.moveXY(40, 20)
        pass