# สิ่งนี้กำหนดฟังก์ชันที่เรียกว่า findAndAttackEnemy
def findAndAttackEnemy():
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)

# โค้ดนี้ไม่ได้เป็นส่วนหนึ่งของฟังก์ชัน
while True:
    # ตอนนี้คุณสามารถลาดตระเวนหมู่บ้านโดยใช้ findAndAttackEnemy
    hero.moveXY(35, 34)
    findAndAttackEnemy()
    
    # ตอนนี้ย้ายไปทางเข้าด้านขวา
    hero.moveXY(60, 31)
    # ใช้ findAndAttackEnemy
    findAndAttackEnemy()
