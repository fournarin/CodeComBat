# ฟังก์ชันนี้โจมตีศัตรูที่ใกล้ที่สุด
def findAndAttackEnemy():
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)

# กำหนดฟังก์ชันเพื่อ cleave ศัตรู (แต่เฉพาะเมื่อความสามารถพร้อม)
def findAndCleaveEnemy():
    # ค้นหาศัตรูที่ใกล้ที่สุด:
    enemy = hero.findNearestEnemy()
    # หากมีศัตรูอยู่:
    if enemy:
        # และถ้า "cleave" พร้อม:
        if hero.isReady("cleave"):
            # ถึงเวลาที่จะ cleave!
            hero.cleave(enemy)
    pass

# ใน loop หลักของคุณ ลาดตระเวน cleave และโจมตี
while True:
    # ไปยังจุดตรวจ cleave และโจมตี
    hero.moveXY(35, 34)
    findAndCleaveEnemy()
    findAndAttackEnemy()
    
    # ไปยังจุดอื่น:
    hero.moveXY(60, 31)
    # ใช้ฟังก์ชัน findAndCleaveEnemy:
    findAndCleaveEnemy()
    # ใช้ฟังก์ชัน findAndAttackEnemy:
    findAndAttackEnemy()
    
