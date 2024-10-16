# ไปที่โอเอซิส ระวังศัตรูใหม่: ทหารยักษ์โอเกอร์!
# ขึ้นไปทางขวาโดยเพิ่มตำแหน่ง X และ Y ปัจจุบัน
x=hero.pos.x
y=hero.pos.y
while True:
    enemy = hero.findNearestEnemy();
    if enemy:
        hero.attack(enemy)
    else:
        x=x+5
        y=y+5
        hero.moveXY(x, y)


pass
    # มิฉะนั้นให้ขยับขึ้นและไปทางขวา