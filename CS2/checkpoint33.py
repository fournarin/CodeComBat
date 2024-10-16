# ฟังก์ชั่น mayBuildTrap กำหนดสองพารามิเตอร์!
def maybeBuildTrap(x, y):
    # ใช้ x และ y เป็นพิกัดที่จะเคลื่อนไป
    hero.moveXY(x, y)
    enemy = hero.findNearestEnemy()
    if enemy:
        pass
        # ใช้ buildXY เพื่อสร้าง "fire-trap" ที่ x และ y ที่กำหนด
        hero.buildXY("fire-trap", x, y)
while True:
    # สิ่งนี้เรียก mayBuildTrap ซึ่งเป็นพิกัดของทางเข้าด้านบน
    maybeBuildTrap(43, 50)
    
    # ใช้ mayBuildTrap ที่ทางเข้าด้านซ้าย!
    maybeBuildTrap(25,34)
    # ใช้ mayBuildTrap ที่ทางเข้าด้านล่าง!
    maybeBuildTrap(43,20)
    